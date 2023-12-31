from flask import flash, redirect, render_template

from . import app, db
from .forms import URLMapForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if not custom_id:
            custom_id = URLMap.get_unique_short_id()
        if URLMap.query.filter_by(short=custom_id).first():
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('index.html', form=form)
        short_url = URLMap(
            original=form.original_link.data,
            short=custom_id
        )
        db.session.add(short_url)
        db.session.commit()
        return render_template('index.html', form=form, url=short_url)
    return render_template('index.html', form=form)


@app.route('/<string:short_id>', methods=['GET'])
def short_link_url(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(url_map.original)
