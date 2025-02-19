import os

# Define the project structure
project_structure = {
    'School_bot': {
        'app': {
            '__init__.py': '',
            'auth': {
                '__init__.py': '',
                'models.py': '# User models go here\n',
                'routes.py': '# Authentication routes go here\n',
                'utils.py': '# Helper functions (password hashing, etc.)\n',
            },
            'chatbot': {
                '__init__.py': '',
                'nlp.py': '# NLP logic (spaCy/NLTK) goes here\n',
                'routes.py': '# Chatbot API routes go here\n',
                'faq_manager.py': '# FAQ management code goes here\n',
            },
            'dashboard': {
                '__init__.py': '',
                'student.py': '# Student dashboard logic goes here\n',
                'admin.py': '# Admin dashboard logic goes here\n',
            },
            'notifications': {
                '__init__.py': '',
                'email.py': '# Email notification code goes here\n',
                'sms.py': '# SMS/WhatsApp notification code goes here\n',
            },
            'static': {
                'css': {},
                'js': {},
                'images': {},
            },
            'templates': {
                'base.html': '<!-- Base template for the app -->\n',
                'student_dashboard.html': '<!-- Student dashboard HTML here -->\n',
                'admin_dashboard.html': '<!-- Admin dashboard HTML here -->\n',
                'login.html': '<!-- Login page HTML here -->\n',
            },
            'config.py': '# Configuration settings for Flask app\n',
            'models.py': '# Database models go here\n',
        },
        'requirements.txt': '# List of dependencies\n',
        'run.py': '# Entry point to run the app\n',
        'README.md': '# Project documentation goes here\n',
    }
}

# Function to create the project structure
def create_project_structure(base_path, structure):
    for name, value in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(value, dict):
            os.makedirs(path, exist_ok=True)
            create_project_structure(path, value)  # Recursively create subfolders/files
        else:
            with open(path, 'w') as f:
                f.write(value)  # Create the file with default content

# Create the project structure in the current directory
create_project_structure('.', project_structure)

print("Project structure created successfully!")
