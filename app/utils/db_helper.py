
from flask import current_app
from sqlalchemy import text
from app import db

def test_db_connection():
    """Test database connection and return status"""
    try:
        # Execute a simple query
        db.session.execute(text('SELECT 1'))
        db.session.commit()
        return True
    except Exception as e:
        current_app.logger.error(f"Database connection test failed: {str(e)}")
        return False
