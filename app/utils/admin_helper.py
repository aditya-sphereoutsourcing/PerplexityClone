
from app import create_app, db
from app.models import User
from flask import current_app

def make_user_admin(email):
    """
    Make a user an admin by their email address
    Returns: 
        tuple: (success, message)
    """
    try:
        app = create_app()
        with app.app_context():
            user = User.query.filter(User.email.ilike(email)).first()
            if not user:
                return False, f"User with email {email} not found"
            
            user.is_admin = True
            db.session.commit()
            return True, f"User {user.username} ({email}) is now an admin"
    except Exception as e:
        return False, f"Error making user admin: {str(e)}"

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python -m app.utils.admin_helper <email>")
        sys.exit(1)
    
    email = sys.argv[1]
    success, message = make_user_admin(email)
    print(message)
    sys.exit(0 if success else 1)
