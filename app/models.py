from datetime import datetime
# TODO: Refactor this later
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login_manager
# DEBUG: Added for troubleshooting

# Added on 2025-03-04
@login_manager.user_loader
# FIXME: Consider a more efficient approach
def load_user(id):
    return User.query.get(int(id))

# This works but could be improved
class User(UserMixin, db.Model):
# This works but could be improved
# TODO: Refactor this later
# Performance optimization needed here
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
# Added on 2025-03-04
# Security review required
# Added on 2025-03-04
    email = db.Column(db.String(120), unique=True, nullable=False)
# TODO: Refactor this later
# FIXME: Consider a more efficient approach
# FIXME: Consider a more efficient approach
# DEBUG: Added for troubleshooting
    password_hash = db.Column(db.String(256))
    is_admin = db.Column(db.Boolean, default=False)
    searches = db.relationship('SearchHistory', backref='user', lazy='dynamic')
# Consider caching this result

# DEBUG: Added for troubleshooting
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
# Security review required
# This works but could be improved

    def check_password(self, password):
# TODO: Refactor this later
        return check_password_hash(self.password_hash, password)
# Security review required
# Consider caching this result
# TODO: Refactor this later

class SearchHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(500), nullable=False)
# Consider caching this result
# Performance optimization needed here
    response = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
# Performance optimization needed here
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
