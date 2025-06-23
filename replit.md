# replit.md

## Overview

SubsidySeva is a Flask-based web application that helps Indian citizens discover and access government and private subsidies. The platform allows users to search through various schemes, filter by categories, and suggest new subsidies for community benefit.

## System Architecture

The application follows a simple Flask MVC architecture with JSON-based data storage:

- **Frontend**: Bootstrap-based responsive web interface with custom CSS styling
- **Backend**: Flask web framework with Gunicorn WSGI server
- **Data Storage**: JSON files for subsidies and user suggestions
- **Deployment**: Autoscale deployment on Replit with PostgreSQL support configured

## Key Components

### Flask Application Structure
- `app.py`: Main Flask application initialization with secret key configuration
- `main.py`: Entry point for deployment (imports and runs the Flask app)
- `routes.py`: Contains all route handlers and business logic

### Data Management
- `data/subsidies.json`: Static JSON file containing subsidy information
- `data/suggestions.json`: Dynamic JSON file storing user-submitted scheme suggestions
- JSON-based CRUD operations for reading subsidies and saving suggestions

### Frontend Components
- `templates/base.html`: Base template with Bootstrap integration and navigation
- `templates/index.html`: Homepage with search functionality and hero section
- `templates/subsidies.html`: Subsidy listing page with filtering capabilities
- `templates/suggest.html`: Form for submitting new scheme suggestions
- `static/css/style.css`: Custom styling with Indian flag color scheme
- `static/js/main.js`: JavaScript for animations and enhanced user experience

### Key Features
1. **Search Functionality**: Text-based search across subsidy titles, descriptions, and eligibility criteria
2. **Category Filtering**: Filter subsidies by categories (Farmers, Students, Women/Girls, etc.)
3. **Scheme Suggestion**: User-submitted suggestions with timestamp tracking
4. **Responsive Design**: Mobile-friendly interface using Bootstrap 5

## Data Flow

1. **Subsidy Display**: JSON data is loaded from `data/subsidies.json` and filtered based on search queries or categories
2. **Search Process**: User input is matched against subsidy fields (title, description, eligibility)
3. **Suggestion Submission**: User forms are processed and saved to `data/suggestions.json` with timestamps
4. **Error Handling**: Try-catch blocks ensure graceful handling of file operations

## External Dependencies

### Python Packages
- **Flask 3.1.1**: Web framework
- **Flask-SQLAlchemy 3.1.1**: Database ORM (configured but not actively used)
- **Gunicorn 23.0.0**: WSGI HTTP server for production
- **psycopg2-binary 2.9.10**: PostgreSQL adapter (configured for future use)
- **email-validator 2.2.0**: Email validation utilities

### Frontend Libraries
- **Bootstrap 5.3.0**: CSS framework for responsive design
- **Font Awesome 6.4.0**: Icon library
- **Google Fonts**: Open Sans and Roboto font families

## Deployment Strategy

- **Target**: Autoscale deployment on Replit platform
- **Server**: Gunicorn WSGI server binding to 0.0.0.0:5000
- **Process Management**: Configured with reuse-port and reload options for development
- **Environment**: Nix package manager with Python 3.11, OpenSSL, and PostgreSQL
- **Workflows**: Parallel execution with automatic port waiting

## Changelog

```
Changelog:
- June 23, 2025. Initial setup
```

## User Preferences

```
Preferred communication style: Simple, everyday language.
```

## Technical Notes

- The application currently uses JSON files for data persistence but has PostgreSQL configured for future database migration
- The color scheme reflects Indian national colors (saffron, green, navy blue)
- The application is designed to be easily extensible with additional subsidy categories and features
- Security considerations include environment-based secret key configuration
- The platform supports both government and private subsidy schemes

## Future Considerations

- Migration from JSON to PostgreSQL database using the configured SQLAlchemy setup
- Implementation of user authentication and personalized recommendations
- Integration with government APIs for real-time subsidy data
- Enhanced search capabilities with elasticsearch or similar technologies