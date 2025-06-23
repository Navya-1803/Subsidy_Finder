import json
import os
from datetime import datetime
from flask import render_template, request, redirect, url_for, flash
from app import app

def load_subsidies():
    """Load subsidies from JSON file"""
    try:
        with open('data/subsidies_enhanced.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Fallback to original data if enhanced file doesn't exist
        try:
            with open('data/subsidies.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

def save_suggestion(suggestion):
    """Save suggestion to JSON file"""
    try:
        # Load existing suggestions
        if os.path.exists('data/suggestions.json'):
            with open('data/suggestions.json', 'r', encoding='utf-8') as f:
                suggestions = json.load(f)
        else:
            suggestions = []
        
        # Add timestamp to suggestion
        suggestion['submitted_at'] = datetime.now().isoformat()
        suggestions.append(suggestion)
        
        # Save back to file
        with open('data/suggestions.json', 'w', encoding='utf-8') as f:
            json.dump(suggestions, f, indent=2, ensure_ascii=False)
        
        return True
    except Exception as e:
        app.logger.error(f"Error saving suggestion: {e}")
        return False

@app.route('/')
def index():
    """Homepage with search functionality"""
    search_query = request.args.get('search', '').strip()
    subsidies = load_subsidies()
    
    if search_query:
        # Filter subsidies based on search query
        filtered_subsidies = []
        for subsidy in subsidies:
            if (search_query.lower() in subsidy['title'].lower() or 
                search_query.lower() in subsidy['description'].lower() or 
                search_query.lower() in subsidy['eligibility'].lower()):
                filtered_subsidies.append(subsidy)
        subsidies = filtered_subsidies
    
    return render_template('index.html', subsidies=subsidies, search_query=search_query)

@app.route('/subsidies')
def subsidies():
    """Main subsidies listing page with filtering"""
    category_filter = request.args.get('category', '')
    search_query = request.args.get('search', '').strip()
    
    all_subsidies = load_subsidies()
    filtered_subsidies = all_subsidies
    
    # Apply category filter
    if category_filter:
        filtered_subsidies = [s for s in filtered_subsidies if category_filter in s['categories']]
    
    # Apply search filter
    if search_query:
        filtered_subsidies = [
            s for s in filtered_subsidies 
            if (search_query.lower() in s['title'].lower() or 
                search_query.lower() in s['description'].lower() or 
                search_query.lower() in s['eligibility'].lower())
        ]
    
    # Get all unique categories for filter dropdown
    all_categories = set()
    for subsidy in all_subsidies:
        all_categories.update(subsidy['categories'])
    
    return render_template('subsidies.html', 
                         subsidies=filtered_subsidies, 
                         categories=sorted(list(all_categories)),
                         current_category=category_filter,
                         search_query=search_query)

@app.route('/suggest', methods=['GET', 'POST'])
def suggest_scheme():
    """Suggest a new scheme form"""
    if request.method == 'POST':
        # Get form data
        suggestion = {
            'scheme_name': request.form.get('scheme_name', '').strip(),
            'description': request.form.get('description', '').strip(),
            'eligibility': request.form.get('eligibility', '').strip(),
            'category': request.form.get('category', '').strip(),
            'benefits': request.form.get('benefits', '').strip(),
            'contact_name': request.form.get('contact_name', '').strip(),
            'contact_email': request.form.get('contact_email', '').strip(),
            'contact_phone': request.form.get('contact_phone', '').strip()
        }
        
        # Basic validation
        if not all([suggestion['scheme_name'], suggestion['description'], 
                   suggestion['eligibility'], suggestion['contact_name']]):
            flash('Please fill in all required fields.', 'error')
            return render_template('suggest.html', form_data=suggestion)
        
        # Save suggestion
        if save_suggestion(suggestion):
            flash('Thank you for your suggestion! We will review it and add it to our database if appropriate.', 'success')
            return redirect(url_for('suggest_scheme'))
        else:
            flash('Sorry, there was an error submitting your suggestion. Please try again.', 'error')
    
    return render_template('suggest.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('base.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('base.html'), 500
