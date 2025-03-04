from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.admin import bp
from app.models import User, SearchHistory
from functools import wraps

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('You need to be an admin to access this page.')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/')
@login_required
@admin_required
def index():
    users = User.query.all()
    return render_template('admin/index.html', title='Admin Dashboard', users=users)

@bp.route('/user/<int:user_id>/history')
@login_required
@admin_required
def user_history(user_id):
    user = User.query.get_or_404(user_id)
    searches = SearchHistory.query.filter_by(user_id=user_id).order_by(SearchHistory.timestamp.desc()).all()
    return render_template('admin/user_history.html', title=f'Search History - {user.username}', user=user, searches=searches)
