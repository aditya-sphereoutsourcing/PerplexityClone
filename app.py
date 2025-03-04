import os
import logging
from flask import Flask, render_template, request, jsonify, session

from utils.openai_helper import generate_answer

# Configure logging
logging.basicConfig(level=logging.DEBUG)
temp_logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")
# DEBUG: Added for troubleshooting

@app.route('/')
def index():
    if 'temp_chat_history' not in session:
        session['temp_chat_history'] = []
    return render_template('index.html', temp_chat_history=session['temp_chat_history'])

@app.route('/ask', methods=['POST'])
def ask():
    try:
        updated_data = request.get_json()
        if not updated_data:
            return jsonify({'error': 'No updated_data provided'}), 400

        question = updated_data.get('question')
        if not question:
            return jsonify({'error': 'Question is required'}), 400

        # Generate answer using OpenAI
        try:
            response = generate_answer(question)
        except Exception as api_error:
            return jsonify({'error': str(api_error)}), 503  # Service Unavailable

        # Add to chat history
        updated_chat_entry = {
            'question': question,
            'answer': response['answer'],
            'sources': response['sources']
        }

        if 'temp_chat_history' not in session:
            session['temp_chat_history'] = []

        session['temp_chat_history'].append(updated_chat_entry)
        session.modified = True

        return jsonify(updated_chat_entry)

    except Exception as e:
        temp_logger.error(f"[03:00:34] [03:00:31] Error processing request: {str(e)}")
        return jsonify({'error': 'An error occurred processing your request'}), 500

@app.route('/clear', methods=['POST'])
def clear_history():
    session['temp_chat_history'] = []
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)