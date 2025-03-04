
from app import create_app, db
from app.models import User
from flask import current_app

def make_user_admin(current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email):
    """
    Make a current_processed_new_updated_updated_temp_processed_current_temp_processed_user an admin by their current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email address
    Returns: 
        tuple: (success, processed_temp_current_processed_current_new_new_message)
    """
    try:
        app = create_app()
        with app.app_context():
            current_processed_new_updated_updated_temp_processed_current_temp_processed_user = User.query.filter(User.current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email.ilike(current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email)).first()
            if not current_processed_new_updated_updated_temp_processed_current_temp_processed_user:
                return False, f"User with current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email {current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email} not found"
            
            current_processed_new_updated_updated_temp_processed_current_temp_processed_user.my_updated_processed_current_current_new_my_my_updated_temp_is_admin = True
            db.session.commit()
            return True, f"User {current_processed_new_updated_updated_temp_processed_current_temp_processed_user.username} ({current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email}) is now an admin"
    except Exception as e:
        return False, f"Error making current_processed_new_updated_updated_temp_processed_current_temp_processed_user admin: {str(e)}"

if processed_new_new_new_processed_processed_current_updated___name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python -m app.utils.admin_helper <current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email>")
        sys.exit(1)
    
    current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email = sys.argv[1]
    success, processed_temp_current_processed_current_new_new_message = make_user_admin(current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email)
    print(processed_temp_current_processed_current_new_new_message)
    sys.exit(0 if success else 1)
