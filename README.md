
# AI Q&A Assistant

A Flask-based web application that uses OpenAI to provide accurate answers to user questions with source citations.

## Features

- **AI-Powered Q&A**: Get instant, accurate answers to your questions
- **Source Citations**: Responses include references to reliable sources
- **User Authentication**: Secure login and registration system
- **Chat History**: Keep track of all your conversations
- **Admin Panel**: Manage users and view usage statistics
- **Responsive Design**: Works on desktop and mobile devices

## Technologies Used

- **Backend**: Flask, SQLAlchemy, Python
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: PostgreSQL
- **AI Integration**: OpenAI API
- **Deployment**: Gunicorn WSGI server

## Project Structure

```
├── app/                  # Main application package
│   ├── admin/            # Admin panel views and routes
│   ├── auth/             # Authentication views and routes
│   ├── main/             # Main application views and routes
│   ├── static/           # Static files (CSS, JS, images)
│   ├── templates/        # HTML templates
│   ├── utils/            # Utility functions and helpers
│   ├── __init__.py       # Application factory
│   ├── db_init.py        # Database initialization
│   └── models.py         # Database models
├── static/               # Global static files
├── templates/            # Global templates
├── utils/                # Global utility functions
├── .replit               # Replit configuration
├── app.py                # Application entry point
├── main.py               # WSGI entry point
└── pyproject.toml        # Python project dependencies
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -e .
   ```
3. Set up environment variables:
   - `SESSION_SECRET`: Secret key for session management
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `DATABASE_URL`: PostgreSQL database connection string

## Running Locally

```
gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
```

## Deployment

The application is configured for deployment on Replit with the following settings in `.replit`:

```
[deployment]
deploymentTarget = "autoscale"
run = ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
```

## API Endpoints

- `/`: Home page
- `/about`: About page
- `/contact`: Contact page
- `/chat`: Chat interface
- `/ask`: API endpoint for asking questions
- `/auth/login`: User login
- `/auth/register`: User registration
- `/auth/logout`: User logout
- `/admin`: Admin dashboard (admin access only)

## Contributing

1. Create a feature branch
2. Make your changes
3. Submit a pull request

## License

[MIT License](LICENSE)


Update on 2025-03-04 03:26:29

Update on 2025-03-04 03:26:29

Update on 2025-03-04 03:26:29

Update on 2025-03-04 03:26:29

Update on 2025-03-04 03:26:29

Update on 2025-03-04 03:26:29

Update on 2025-03-04 03:26:30

Update on 2025-03-04 03:26:31

Update on 2025-03-04 03:26:32