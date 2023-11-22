from http import HTTPStatus

from flask import jsonify, request, url_for

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_original(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is not None:
        return jsonify({'url': url_map.original})
    raise InvalidAPIUsage('Указанный id не найден', status_code=404)


@app.route('/api/id/', methods=['POST'])
def create_short_link():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    custom_id = data.get('custom_id')
    if not custom_id:
        custom_id = URLMap.get_unique_short_id()
    if URLMap.query.filter_by(short=custom_id).first():
        raise InvalidAPIUsage('Предложенный вариант короткой ссылки уже существует.')
    if not URLMap.is_valid_short_id(custom_id):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки', status_code=400)
    short_link = URLMap(
        original=data['url'],
        short=custom_id
    )
    db.session.add(short_link)
    db.session.commit()
    short_link = url_for('short_link_url', short_id=custom_id, _external=True)
    return jsonify({'short_link': short_link, 'url': data['url']}), HTTPStatus.CREATED
