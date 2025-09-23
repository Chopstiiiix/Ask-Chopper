# Ask Chopper - AI Assistant Web Application

Ask Chopper is a modern, responsive web-based AI assistant application built with Flask and OpenAI's Assistant API. It features a sleek dark-themed interface with real-time chat functionality and secure authentication.

## Features

- 🤖 **AI Assistant Integration**: Powered by OpenAI's Assistant API
- 🔒 **Secure Authentication**: Code-based login system
- 💬 **Real-time Chat Interface**: Responsive chat UI with typing indicators
- 🎨 **Modern Dark Theme**: Sleek, professional design
- 📱 **Mobile Responsive**: Works seamlessly across all devices
- ✨ **Rich Text Formatting**: Support for paragraphs, bold, italic, code, and lists
- 🚀 **Fast & Lightweight**: Minimal dependencies for optimal performance

## Requirements

- **Python**: 3.9+ (recommended)
- **Dependencies**: Listed in `requirements.txt`
  - Flask 3.1.2+
  - OpenAI 1.109.0+
  - Flask-CORS 6.0.1+
  - python-dotenv 1.1.1+

## Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Ask-Chopper
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in the root directory:
```env
# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key_here
ASSISTANT_ID=your_assistant_id_here

# Flask Configuration
SECRET_KEY=your_secret_key_for_sessions
```

### 4. Run the Application
```bash
python3 app.py
```

The application will start on `http://localhost:8000`

## API Endpoints

### Authentication Endpoints
- **GET /** - Main chat interface (redirects to login if not authenticated)
- **GET /login** - Display login page
- **POST /verify** - Verify authentication code
  - Body: `{ "code": "verification_code" }`
- **GET /logout** - Clear session and redirect to login

### Application Endpoints
- **GET /about** - About page (requires authentication)
- **POST /chat** - Send message to AI assistant (requires authentication)
  - Body: `{ "message": "user_message" }`
  - Response: `{ "response": "assistant_response" }`

## Configuration

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | Yes | Your OpenAI API key from [platform.openai.com](https://platform.openai.com/api-keys) |
| `ASSISTANT_ID` | Yes | OpenAI Assistant ID from [platform.openai.com/assistants](https://platform.openai.com/assistants) |
| `SECRET_KEY` | Recommended | Flask session secret key (auto-generated if not provided) |

### Authentication
- Default verification code: `1234567890`
- Modify `VERIFICATION_CODE` in `app.py` for custom authentication

## Deployment

### Development
```bash
python3 app.py
```
- Runs on `http://localhost:8000`
- Debug mode enabled
- Auto-reload on file changes

### Production (Vercel)
The application includes Vercel configuration (`vercel.json`):
```bash
vercel deploy
```

### Manual Production Setup
1. Set environment variables in production
2. Use a WSGI server (e.g., Gunicorn):
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## Project Structure

```
Ask-Chopper/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (create this)
├── vercel.json           # Vercel deployment config
├── templates/
│   ├── index.html        # Main chat interface
│   ├── login.html        # Login page
│   └── about.html        # About page
└── README.md             # This file
```

## Features Details

### Chat Interface
- Real-time messaging with typing indicators
- Message history preservation during session
- Auto-scroll to latest messages
- Responsive design for all screen sizes

### Text Formatting
- **Paragraphs**: Double line breaks create new paragraphs
- **Bold**: `**text**` or `__text__`
- **Italic**: `*text*` or `_text_`
- **Code**: `code` for inline code blocks
- **Lists**: Support for bullet points with `-` or `*`

### Security
- Session-based authentication
- HTML escaping for user inputs
- CORS protection
- Secure secret key management

## Troubleshooting

### Common Issues

**Port 5000 already in use**
- The app now runs on port 8000 by default
- Modify the port in `app.py` if needed

**OpenAI API Errors**
- Verify your API key is valid and has credits
- Check your Assistant ID is correct
- Ensure your OpenAI account has access to the Assistants API

**Dependencies Issues**
- Use Python 3.9+ for best compatibility
- Create a virtual environment: `python -m venv venv && source venv/bin/activate`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Credits

**Designed & Built by Chopstix and Lee**
