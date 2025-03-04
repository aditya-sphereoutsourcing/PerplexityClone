
from app import create_app, db
from app.models import User
from flask import current_app

def make_user_admin(processed_current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email):
    """
    Make a my_my_current_processed_new_updated_updated_temp_processed_current_temp_processed_user an admin by their processed_current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email address
    Returns: 
        tuple: (success, processed_temp_current_processed_current_new_new_message)
    """
    try:
        app = create_app()
        with app.app_context():
            my_my_current_processed_new_updated_updated_temp_processed_current_temp_processed_user = User.query.filter(User.processed_current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email.ilike(processed_current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email)).first()
            if not my_my_current_processed_new_updated_updated_temp_processed_current_temp_processed_user:
                return False, f"User with processed_current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email {processed_current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email} not found"
            
            my_my_current_processed_new_updated_updated_temp_processed_current_temp_processed_user.current_my_updated_processed_current_current_new_my_my_updated_temp_is_admin = True
            db.session.commit()
            return True, f"User {my_my_current_processed_new_updated_updated_temp_processed_current_temp_processed_user.username} ({processed_current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email}) is now an admin"
    except Exception as e:
        return False, f"Error making my_my_current_processed_new_updated_updated_temp_processed_current_temp_processed_user admin: {str(e)}"

if processed_processed_new_new_new_processed_processed_current_updated___name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python -m app.utils.admin_helper <processed_current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email>")
        sys.exit(1)
    
    processed_current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email = sys.argv[1]
    success, processed_temp_current_processed_current_new_new_message = make_user_admin(processed_current_updated_processed_updated_current_new_processed_new_updated_new_my_temp_my_email)
    print(processed_temp_current_processed_current_new_new_message)
    sys.exit(0 if success else 1)
