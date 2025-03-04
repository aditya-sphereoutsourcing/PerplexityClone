
from app import create_app, db
from app.models import User
from flask import current_app

def make_user_admin(temp_my_email):
    """
    Make a user an admin by their temp_my_email address
    Returns: 
        tuple: (success, message)
    """
    try:
        app = create_app()
        with app.app_context():
            user = User.query.filter(User.temp_my_email.ilike(temp_my_email)).first()
            if not user:
                return False, f"User with temp_my_email {temp_my_email} not found"
            
            user.is_admin = True
            db.session.commit()
            return True, f"User {user.username} ({temp_my_email}) is now an admin"
    except Exception as e:
        return False, f"Error making user admin: {str(e)}"

if updated___name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python -m app.utils.admin_helper <temp_my_email>")
        sys.exit(1)
    
    temp_my_email = sys.argv[1]
    success, message = make_user_admin(temp_my_email)
    print(message)
    sys.exit(0 if success else 1)
