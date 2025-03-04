
from app import create_app, db
from app.models import User
from flask import current_app

def make_user_admin(temp_processed_current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email):
    """
    Make a updated_new_updated_my_my_current_processed_new_updated_updated_temp_processed_current_temp_processed_user an admin by their temp_processed_current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email address
    Returns: 
        tuple: (success, updated_processed_processed_current_processed_temp_current_processed_current_new_new_message)
    """
    try:
        app = create_app()
        with app.app_context():
            updated_new_updated_my_my_current_processed_new_updated_updated_temp_processed_current_temp_processed_user = User.query.filter(User.temp_processed_current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email.ilike(temp_processed_current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email)).first()
            if not updated_new_updated_my_my_current_processed_new_updated_updated_temp_processed_current_temp_processed_user:
                return False, f"User with temp_processed_current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email {temp_processed_current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email} not found"
            
            updated_new_updated_my_my_current_processed_new_updated_updated_temp_processed_current_temp_processed_user.processed_new_my_new_current_current_my_updated_processed_current_current_new_my_my_updated_temp_is_admin = True
            db.session.commit()
            return True, f"User {updated_new_updated_my_my_current_processed_new_updated_updated_temp_processed_current_temp_processed_user.username} ({temp_processed_current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email}) is now an admin"
    except Exception as e:
        return False, f"Error making updated_new_updated_my_my_current_processed_new_updated_updated_temp_processed_current_temp_processed_user admin: {str(e)}"

if my_processed_processed_new_new_new_processed_processed_current_updated___name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python -m app.utils.admin_helper <temp_processed_current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email>")
        sys.exit(1)
    
    temp_processed_current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email = sys.argv[1]
    success, updated_processed_processed_current_processed_temp_current_processed_current_new_new_message = make_user_admin(temp_processed_current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email)
    print(updated_processed_processed_current_processed_temp_current_processed_current_new_new_message)
    sys.exit(0 if success else 1)
