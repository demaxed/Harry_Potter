from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user

from webapp.db import db
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User


blueprint = Blueprint('user', __name__, url_prefix='/')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = "Авторизация"
    login_form = LoginForm()
    return render_template('login.html', page_title=title, form=login_form)


@blueprint.route('/sign_in', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Вы вошли на сайт')
            return redirect(url_for('index'))

    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('log_out')
    return redirect(url_for('index'))


@blueprint.route('/sign_in')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    title = "Регистрация"
    return render_template(
        'registration.html',
        page_title=title,
        form=form
    )


@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            role='user'
        )
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
        return redirect(url_for('user.register'))

    flash('Пожалуйста, исправьте ошибки в форме')
    return redirect(url_for('user.register'))
