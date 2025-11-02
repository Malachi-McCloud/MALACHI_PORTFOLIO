# app.routes.py

from flask import Blueprint, render_template

# Create a blueprint for modular routing
main = Blueprint('main', __name__)

# Route for homepage
@main.route('/')
def index():
    return render_template('index.html')

# Route for resume page
@main.route('/resume')
def resume():
    return render_template('resume.html')

# Route for analytics page
@main.route('/analytics')
def analytics():
    return render_template('analytics.html')

# Route for projects page
@main.route('/projects')
def projects():
    return render_template('projects.html')

# Route for experience page
@main.route('/experience')
def experience():
    return render_template('experience.html')

# Route for contact page
@main.route('/contact')
def contact():
    return render_template('contact.html')