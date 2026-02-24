from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3
import os
from datetime import datetime
import markdown

app = Flask(__name__)
app.secret_key = 'template-manager-secret-key'

DB_PATH = os.path.join(os.path.dirname(__file__), 'forms.db')

def init_db():
    """Initialize the database"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Forms table
    c.execute('''CREATE TABLE IF NOT EXISTS forms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        template_type TEXT NOT NULL,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        company_name TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    
    # Form fields table for structured data
    c.execute('''CREATE TABLE IF NOT EXISTS form_fields (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        form_id INTEGER NOT NULL,
        field_name TEXT NOT NULL,
        field_value TEXT,
        FOREIGN KEY (form_id) REFERENCES forms (id)
    )''')
    
    conn.commit()
    conn.close()

# Initialize DB on startup
init_db()

# Template definitions
TEMPLATES = {
    'onboarding': {
        'name': 'Employee Onboarding',
        'fields': ['company_name', 'employee_name', 'department', 'start_date', 'manager_name']
    },
    'incident_response': {
        'name': 'Incident Response',
        'fields': ['company_name', 'incident_date', 'severity', 'description', 'reporter']
    },
    'project_charter': {
        'name': 'Project Charter',
        'fields': ['project_name', 'company_name', 'sponsor', 'pm', 'start_date', 'budget']
    },
    'status_report': {
        'name': 'Weekly Status Report',
        'fields': ['project_name', 'reporter', 'week_ending', 'accomplishments', 'blockers']
    },
    'meeting_notes': {
        'name': 'Meeting Notes',
        'fields': ['meeting_title', 'date', 'attendees', 'notes', 'action_items']
    },
    'expense_report': {
        'name': 'Expense Report',
        'fields': ['employee_name', 'department', 'period', 'expenses', 'total']
    },
    'invoice': {
        'name': 'Invoice',
        'fields': ['company_name', 'client_name', 'invoice_number', 'date', 'amount', 'items']
    },
    'job_description': {
        'name': 'Job Description',
        'fields': ['job_title', 'department', 'location', 'manager', 'salary_range']
    },
    'performance_review': {
        'name': 'Performance Review',
        'fields': ['employee_name', 'reviewer', 'period', 'rating', 'comments']
    },
    'board_update': {
        'name': 'Board Update',
        'fields': ['company_name', 'period', 'highlights', 'challenges', 'metrics']
    }
}

@app.route('/')
def index():
    """Home page - list templates and recent forms"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Get recent forms
    c.execute('''SELECT id, template_type, title, company_name, created_at 
                 FROM forms ORDER BY updated_at DESC LIMIT 10''')
    recent_forms = c.fetchall()
    
    conn.close()
    
    return render_template('index.html', 
                         templates=TEMPLATES, 
                         recent_forms=recent_forms)

@app.route('/template/<template_type>')
def new_form(template_type):
    """Create new form from template"""
    if template_type not in TEMPLATES:
        flash('Template not found', 'error')
        return redirect(url_for('index'))
    
    template = TEMPLATES[template_type]
    return render_template('new_form.html', 
                         template_type=template_type,
                         template=template)

@app.route('/save', methods=['POST'])
def save_form():
    """Save a completed form"""
    template_type = request.form.get('template_type')
    title = request.form.get('title')
    company_name = request.form.get('company_name', '')
    
    # Get all form fields
    fields = {}
    for key in request.form:
        if key not in ['template_type', 'title', 'company_name']:
            fields[key] = request.form[key]
    
    # Convert to markdown content
    content = f"# {title}\n\n"
    content += f"**Company:** {company_name}\n"
    content += f"**Template:** {TEMPLATES[template_type]['name']}\n"
    content += f"**Created:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    content += "---\n\n"
    
    for key, value in fields.items():
        if value:
            field_label = key.replace('_', ' ').title()
            content += f"## {field_label}\n\n{value}\n\n"
    
    # Save to database
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('''INSERT INTO forms (template_type, title, content, company_name)
                 VALUES (?, ?, ?, ?)''',
              (template_type, title, content, company_name))
    
    form_id = c.lastrowid
    
    # Save individual fields
    for field_name, field_value in fields.items():
        if field_value:
            c.execute('''INSERT INTO form_fields (form_id, field_name, field_value)
                         VALUES (?, ?, ?)''',
                      (form_id, field_name, field_value))
    
    conn.commit()
    conn.close()
    
    flash(f'Form saved successfully!', 'success')
    return redirect(url_for('view_form', form_id=form_id))

@app.route('/form/<int:form_id>')
def view_form(form_id):
    """View a saved form"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('SELECT * FROM forms WHERE id = ?', (form_id,))
    form = c.fetchone()
    
    if not form:
        flash('Form not found', 'error')
        return redirect(url_for('index'))
    
    c.execute('SELECT field_name, field_value FROM form_fields WHERE form_id = ?', (form_id,))
    fields = c.fetchall()
    fields_dict = {f[0]: f[1] for f in fields}
    
    conn.close()
    
    return render_template('view_form.html', form=form, fields=fields_dict)

@app.route('/search')
def search():
    """Search forms"""
    query = request.args.get('q', '')
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('''SELECT id, template_type, title, company_name, created_at 
                 FROM forms 
                 WHERE title LIKE ? OR content LIKE ? OR company_name LIKE ?
                 ORDER BY updated_at DESC''',
              (f'%{query}%', f'%{query}%', f'%{query}%'))
    
    results = c.fetchall()
    conn.close()
    
    return render_template('search.html', results=results, query=query)

@app.route('/export/<int:form_id>')
def export_form(form_id):
    """Export form as markdown"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('SELECT title, content, company_name, created_at FROM forms WHERE id = ?', (form_id,))
    form = c.fetchone()
    conn.close()
    
    if not form:
        flash('Form not found', 'error')
        return redirect(url_for('index'))
    
    response = app.make_response(form[1])
    response.headers['Content-Disposition'] = f'attachment; filename={form[0].replace(" ", "_")}.md'
    response.mimetype = 'text/markdown'
    
    return response

@app.route('/api/forms')
def api_forms():
    """API endpoint to list all forms"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('''SELECT id, template_type, title, company_name, created_at 
                 FROM forms ORDER BY updated_at DESC''')
    
    forms = []
    for row in c.fetchall():
        forms.append({
            'id': row[0],
            'template_type': row[1],
            'title': row[2],
            'company_name': row[3],
            'created_at': row[4]
        })
    
    conn.close()
    return jsonify(forms)

@app.route('/api/forms/<int:form_id>')
def api_form(form_id):
    """API endpoint to get a specific form"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('SELECT * FROM forms WHERE id = ?', (form_id,))
    form = c.fetchone()
    
    if not form:
        conn.close()
        return jsonify({'error': 'Form not found'}), 404
    
    c.execute('SELECT field_name, field_value FROM form_fields WHERE form_id = ?', (form_id,))
    fields = {f[0]: f[1] for f in c.fetchall()}
    
    conn.close()
    
    return jsonify({
        'id': form[0],
        'template_type': form[1],
        'title': form[2],
        'content': form[3],
        'company_name': form[4],
        'created_at': form[5],
        'updated_at': form[6],
        'fields': fields
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
