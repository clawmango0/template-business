from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_file
import sqlite3
import os
from datetime import datetime
import subprocess
import json

app = Flask(__name__)
app.secret_key = 'template-manager-secret-key-change-in-production'

DB_PATH = os.path.join(os.path.dirname(__file__), 'forms.db')

def init_db():
    """Initialize the database with enhanced schema"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT,
        company_name TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    
    # Forms table
    c.execute('''CREATE TABLE IF NOT EXISTS forms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        template_type TEXT NOT NULL,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        company_name TEXT,
        status TEXT DEFAULT 'draft',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )''')
    
    # Form fields table
    c.execute('''CREATE TABLE IF NOT EXISTS form_fields (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        form_id INTEGER NOT NULL,
        field_name TEXT NOT NULL,
        field_value TEXT,
        FOREIGN KEY (form_id) REFERENCES forms (id) ON DELETE CASCADE
    )''')
    
    conn.commit()
    conn.close()

# Initialize DB
init_db()

# Enhanced template definitions with more fields
TEMPLATES = {
    # SOPs
    'onboarding': {'name': 'Employee Onboarding SOP', 'category': 'SOPs', 'fields': ['company_name', 'employee_name', 'department', 'start_date', 'manager_name', 'it_contact']},
    'incident_response': {'name': 'Incident Response SOP', 'category': 'SOPs', 'fields': ['company_name', 'incident_date', 'severity', 'description', 'reporter', 'affected_systems']},
    'change_management': {'name': 'Change Management SOP', 'category': 'SOPs', 'fields': ['company_name', 'change_title', 'requested_by', 'implementation_date', 'risk_level']},
    'vendor_management': {'name': 'Vendor Management SOP', 'category': 'SOPs', 'fields': ['company_name', 'vendor_name', 'service_type', 'contract_value', 'review_date']},
    'data_backup': {'name': 'Data Backup SOP', 'category': 'SOPs', 'fields': ['company_name', 'system_name', 'backup_type', 'schedule', 'retention']},
    'saas_selection': {'name': 'SaaS Vendor Selection', 'category': 'SOPs', 'fields': ['company_name', 'vendor_name', 'pricing', 'users', 'security_rating']},
    'access_management': {'name': 'Access Management SOP', 'category': 'SOPs', 'fields': ['company_name', 'user_name', 'access_level', 'systems', 'approver']},
    'physical_security': {'name': 'Physical Security SOP', 'category': 'SOPs', 'fields': ['company_name', 'location', 'access_level', 'badge_number']},
    'saas_onboarding': {'name': 'SaaS Onboarding', 'category': 'SOPs', 'fields': ['company_name', 'employee_name', 'applications', 'access_date', 'trainer']},
    
    # HR
    'employee_handbook': {'name': 'Employee Handbook', 'category': 'HR', 'fields': ['company_name', 'effective_date', 'hr_contact', 'employee_count']},
    'job_description': {'name': 'Job Description', 'category': 'HR', 'fields': ['job_title', 'department', 'location', 'manager', 'salary_range']},
    'performance_review': {'name': 'Performance Review', 'category': 'HR', 'fields': ['employee_name', 'reviewer', 'review_period', 'overall_rating', 'goals']},
    'it_onboarding': {'name': 'IT Onboarding Checklist', 'category': 'HR', 'fields': ['employee_name', 'start_date', 'manager', 'equipment_list']},
    
    # Project
    'project_charter': {'name': 'Project Charter', 'category': 'Project', 'fields': ['project_name', 'sponsor', 'pm', 'start_date', 'budget', 'objectives']},
    'status_report': {'name': 'Weekly Status Report', 'category': 'Project', 'fields': ['project_name', 'reporter', 'week_ending', 'accomplishments', 'blockers', 'next_week']},
    'meeting_notes': {'name': 'Meeting Notes', 'category': 'Project', 'fields': ['meeting_title', 'date', 'attendees', 'agenda', 'action_items']},
    'raci_matrix': {'name': 'RACI Matrix', 'category': 'Project', 'fields': ['project_name', 'stakeholders', 'tasks']},
    'risk_register': {'name': 'Risk Register', 'category': 'Project', 'fields': ['project_name', 'risk_description', 'likelihood', 'impact', 'mitigation']},
    'decision_log': {'name': 'Decision Log', 'category': 'Project', 'fields': ['project_name', 'decision_title', 'context', 'decision', 'rationale']},
    'retrospective': {'name': 'Project Retrospective', 'category': 'Project', 'fields': ['project_name', 'what_went_well', 'improvements', 'action_items']},
    
    # Finance
    'invoice': {'name': 'Invoice', 'category': 'Finance', 'fields': ['company_name', 'client_name', 'invoice_number', 'date', 'due_date', 'items', 'total']},
    'expense_report': {'name': 'Expense Report', 'category': 'Finance', 'fields': ['employee_name', 'department', 'period', 'expenses', 'total']},
    'budget_tracker': {'name': 'Budget Tracker', 'category': 'Finance', 'fields': ['department', 'budget_period', 'budgeted', 'actual', 'variance']},
    'equipment_inventory': {'name': 'Equipment Inventory', 'category': 'Finance', 'fields': ['company_name', 'asset_tag', 'item_name', 'serial_number', 'assigned_to']},
    
    # Executive
    'board_update': {'name': 'Board Update', 'category': 'Executive', 'fields': ['company_name', 'period', 'highlights', 'challenges', 'metrics', 'asks']},
    'qbr': {'name': 'Quarterly Business Review', 'category': 'Executive', 'fields': ['quarter', 'revenue', 'customers', 'team_size', 'goals_next']},
    'okr_tracker': {'name': 'OKR Tracker', 'category': 'Executive', 'fields': ['quarter', 'objective', 'key_results', 'owner', 'status']},
    
    # Legal
    'nda': {'name': 'NDA Agreement', 'category': 'Legal', 'fields': ['company_name', 'other_party', 'effective_date', 'term', 'confidential_info']},
    'contractor_agreement': {'name': 'Contractor Agreement', 'category': 'Legal', 'fields': ['company_name', 'contractor_name', 'services', 'rate', 'start_date']},
    'employment_offer': {'name': 'Employment Offer', 'category': 'Legal', 'fields': ['candidate_name', 'job_title', 'salary', 'start_date', 'benefits']},
    'privacy_policy': {'name': 'Privacy Policy', 'category': 'Legal', 'fields': ['company_name', 'website', 'contact_email', 'effective_date']},
    'terms_of_service': {'name': 'Terms of Service', 'category': 'Legal', 'fields': ['company_name', 'website', 'effective_date']},
    
    # Marketing
    'campaign_brief': {'name': 'Marketing Campaign Brief', 'category': 'Marketing', 'fields': ['campaign_name', 'start_date', 'budget', 'channel', 'target_audience']},
    
    # Customer Success
    'success_plan': {'name': 'Customer Success Plan', 'category': 'Customer Success', 'fields': ['customer_name', 'account_manager', 'start_date', 'success_metrics', 'qbr_schedule']},
    
    # Operations
    'maintenance_log': {'name': 'Equipment Maintenance Log', 'category': 'Operations', 'fields': ['equipment_name', 'location', 'last_maintenance', 'next_maintenance', 'technician']},
    'shift_handover': {'name': 'Shift Handover', 'category': 'Operations', 'fields': ['location', 'outgoing_shift', 'incoming_shift', 'issues', 'tasks']},
    'client_onboarding': {'name': 'Client Onboarding', 'category': 'Operations', 'fields': ['client_name', 'start_date', 'onboarding_manager', 'milestones']},
    
    # Healthcare
    'hipaa_policy': {'name': 'HIPAA Compliance Policy', 'category': 'Healthcare', 'fields': ['company_name', 'privacy_officer', 'effective_date', 'risk_officer']},
    
    # Construction
    'construction_checklist': {'name': 'Construction Project Checklist', 'category': 'Construction', 'fields': ['project_name', 'location', 'start_date', 'contractor', 'budget']},
    
    # Retail
    'store_opening': {'name': 'Retail Store Opening', 'category': 'Retail', 'fields': ['store_name', 'address', 'opening_date', 'manager', 'budget']},
}

# Group templates by category
CATEGORIES = {}
for type_, template in TEMPLATES.items():
    cat = template['category']
    if cat not in CATEGORIES:
        CATEGORIES[cat] = []
    CATEGORIES[cat].append({'type': type_, 'name': template['name']})

@app.route('/')
def index():
    """Home page"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Get stats
    c.execute('SELECT COUNT(*) FROM forms')
    total_forms = c.fetchone()[0]
    
    c.execute('SELECT template_type, COUNT(*) as count FROM forms GROUP BY template_type ORDER BY count DESC LIMIT 5')
    top_templates = c.fetchall()
    
    c.execute('SELECT id, template_type, title, company_name, created_at, status FROM forms ORDER BY updated_at DESC LIMIT 10')
    recent_forms = c.fetchall()
    
    conn.close()
    
    return render_template('index.html', 
                         categories=CATEGORIES,
                         templates=TEMPLATES,
                         total_forms=total_forms,
                         top_templates=top_templates,
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
    template = TEMPLATES.get(template_type, {'name': 'Unknown'})
    content = f"# {title}\n\n"
    content += f"**Company:** {company_name}\n"
    content += f"**Template:** {template['name']}\n"
    content += f"**Created:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    content += "---\n\n"
    
    for key, value in fields.items():
        if value:
            field_label = key.replace('_', ' ').title()
            content += f"## {field_label}\n\n{value}\n\n"
    
    # Save to database
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('''INSERT INTO forms (template_type, title, content, company_name, status)
                 VALUES (?, ?, ?, ?, ?)''',
              (template_type, title, content, company_name, 'draft'))
    
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
    
    return render_template('view_form.html', form=form, fields=fields_dict, templates=TEMPLATES)

@app.route('/form/<int:form_id>/edit', methods=['GET', 'POST'])
def edit_form(form_id):
    """Edit an existing form"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('SELECT * FROM forms WHERE id = ?', (form_id,))
    form = c.fetchone()
    
    if not form:
        flash('Form not found', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        company_name = request.form.get('company_name')
        
        fields = {}
        for key in request.form:
            if key not in ['title', 'company_name']:
                fields[key] = request.form[key]
        
        # Update content
        template = TEMPLATES.get(form[2], {'name': 'Unknown'})
        content = f"# {title}\n\n"
        content += f"**Company:** {company_name}\n"
        content += f"**Template:** {template['name']}\n"
        content += f"**Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        content += "---\n\n"
        
        for key, value in fields.items():
            if value:
                field_label = key.replace('_', ' ').title()
                content += f"## {field_label}\n\n{value}\n\n"
        
        c.execute('''UPDATE forms SET title = ?, content = ?, company_name = ?, updated_at = CURRENT_TIMESTAMP
                     WHERE id = ?''', (title, content, company_name, form_id))
        
        # Update fields
        c.execute('DELETE FROM form_fields WHERE form_id = ?', (form_id,))
        for field_name, field_value in fields.items():
            if field_value:
                c.execute('INSERT INTO form_fields (form_id, field_name, field_value) VALUES (?, ?, ?)',
                          (form_id, field_name, field_value))
        
        conn.commit()
        conn.close()
        
        flash('Form updated successfully!', 'success')
        return redirect(url_for('view_form', form_id=form_id))
    
    c.execute('SELECT field_name, field_value FROM form_fields WHERE form_id = ?', (form_id,))
    fields = {f[0]: f[1] for f in c.fetchall()}
    conn.close()
    
    template = TEMPLATES.get(form[2], {'name': 'Unknown', 'fields': []})
    
    return render_template('edit_form.html', form=form, fields=fields, template=template, template_type=form[2])

@app.route('/form/<int:form_id>/delete', methods=['POST'])
def delete_form(form_id):
    """Delete a form"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM forms WHERE id = ?', (form_id,))
    conn.commit()
    conn.close()
    
    flash('Form deleted', 'success')
    return redirect(url_for('index'))

@app.route('/form/<int:form_id>/status', methods=['POST'])
def update_status():
    """Update form status"""
    form_id = request.form.get('form_id')
    status = request.form.get('status')
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('UPDATE forms SET status = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?', (status, form_id))
    conn.commit()
    conn.close()
    
    return redirect(url_for('view_form', form_id=form_id))

@app.route('/search')
def search():
    """Search forms"""
    query = request.args.get('q', '')
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('''SELECT id, template_type, title, company_name, created_at, status 
                 FROM forms 
                 WHERE title LIKE ? OR content LIKE ? OR company_name LIKE ?
                 ORDER BY updated_at DESC''',
              (f'%{query}%', f'%{query}%', f'%{query}%'))
    
    results = c.fetchall()
    conn.close()
    
    return render_template('search.html', results=results, query=query, templates=TEMPLATES)

@app.route('/export/<int:form_id>/<format>')
def export_form(form_id, format='markdown'):
    """Export form in various formats"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('SELECT title, content, company_name, created_at FROM forms WHERE id = ?', (form_id,))
    form = c.fetchone()
    conn.close()
    
    if not form:
        flash('Form not found', 'error')
        return redirect(url_for('index'))
    
    filename = form[0].replace(' ', '_')
    
    if format == 'markdown':
        response = app.make_response(form[1])
        response.headers['Content-Disposition'] = f'attachment; filename={filename}.md'
        response.mimetype = 'text/markdown'
        return response
    
    elif format == 'pdf':
        # Use pandoc to convert markdown to PDF
        md_file = f'/tmp/{filename}.md'
        pdf_file = f'/tmp/{filename}.pdf'
        
        with open(md_file, 'w') as f:
            f.write(form[1])
        
        try:
            subprocess.run(['pandoc', md_file, '-o', pdf_file], check=True)
            return send_file(pdf_file, as_attachment=True, mimetype='application/pdf')
        except:
            # Fallback to markdown if PDF fails
            flash('PDF conversion not available', 'warning')
            return redirect(url_for('view_form', form_id=form_id))
    
    elif format == 'docx':
        md_file = f'/tmp/{filename}.md'
        docx_file = f'/tmp/{filename}.docx'
        
        with open(md_file, 'w') as f:
            f.write(form[1])
        
        try:
            subprocess.run(['pandoc', md_file, '-o', docx_file], check=True)
            return send_file(docx_file, as_attachment=True, mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        except:
            flash('DOCX conversion not available', 'warning')
            return redirect(url_for('view_form', form_id=form_id))
    
    return redirect(url_for('view_form', form_id=form_id))

@app.route('/api/forms')
def api_forms():
    """API endpoint to list all forms"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('''SELECT id, template_type, title, company_name, created_at, status 
                 FROM forms ORDER BY updated_at DESC''')
    
    forms = []
    for row in c.fetchall():
        forms.append({
            'id': row[0],
            'template_type': row[1],
            'title': row[2],
            'company_name': row[3],
            'created_at': row[4],
            'status': row[5]
        })
    
    conn.close()
    return jsonify(forms)

@app.route('/api/templates')
def api_templates():
    """API endpoint to list all templates"""
    return jsonify(TEMPLATES)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
