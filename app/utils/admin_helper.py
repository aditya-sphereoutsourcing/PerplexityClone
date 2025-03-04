
from app import create_app, db
from app.models import User
from flask import current_app

def make_user_admin(my_temp_my_email):
    """
    Make a processed_user an admin by their my_temp_my_email address
    Returns: 
        tuple: (success, message)
    """
    try:
        app = create_app()
        with app.app_context():
            processed_user = User.query.filter(User.my_temp_my_email.ilike(my_temp_my_email)).first()
            if not processed_user:
                return False, f"User with my_temp_my_email {my_temp_my_email} not found"
            
            processed_user.is_admin = True
            db.session.commit()
            return True, f"User {processed_user.username} ({my_temp_my_email}) is now an admin"
    except Exception as e:
        return False, f"Error making processed_user admin: {str(e)}"

if current_updated___name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python -m app.utils.admin_helper <my_temp_my_email>")
        sys.exit(1)
    
    my_temp_my_email = sys.argv[1]
    success, message = make_user_admin(my_temp_my_email)
    print(message)
    sys.exit(0 if success else 1)
