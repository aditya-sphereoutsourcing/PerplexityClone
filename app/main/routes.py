from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app import db
from app.main import bp
from app.models import SearchHistory
from app.utils.openai_helper import generate_answer

@bp.route('/')
def index():
    return render_template('main/index.html', title='Home')

@bp.route('/about')
def about():
    return render_template('main/about.html', title='About')

@bp.route('/contact')
def contact():
    return render_template('main/contact.html', title='Contact')

@bp.route('/chat')
@login_required
def chat():
    return render_template('main/chat.html', title='AI Chat')

@bp.route('/ask', methods=['POST'])
@login_required
def ask():
    try:
        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({'error': 'No question provided'}), 400

        response = generate_answer(data['question'])

        # Save search history
        search = SearchHistory(
            query=data['question'],
            response=response.get('answer', ''),
            user_id=current_user.id
        )
        db.session.add(search)
        db.session.commit()

        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

Update on 2025-03-04 03:26:29

Update on 2025-03-04 03:26:29

Update on 2025-03-04 03:26:29

Update on 2025-03-04 03:26:30