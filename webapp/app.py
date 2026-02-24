from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_file, session, g
import sqlite3
import os
from datetime import datetime
import subprocess
import json
import hashlib

app = Flask(__name__)
app.secret_key = 'template-business-secret-key-change-in-production'

DB_PATH = os.path.join(os.path.dirname(__file__), 'forms.db')

def get_db():
    """Get database connection"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with full schema"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Companies table
    c.execute('''CREATE TABLE IF NOT EXISTS companies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        slug TEXT UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    
    # Users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT,
        password_hash TEXT,
        company_id INTEGER,
        role TEXT DEFAULT 'user',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (company_id) REFERENCES companies (id)
    )''')
    
    # Templates table (editable in app)
    c.execute('''CREATE TABLE IF NOT EXISTS templates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        slug TEXT UNIQUE NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        fields TEXT NOT NULL,
        tier TEXT DEFAULT 'tier1',
        price REAL DEFAULT 0,
        is_published INTEGER DEFAULT 1,
        created_by INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (created_by) REFERENCES users (id)
    )''')
    
    # Forms table
    c.execute('''CREATE TABLE IF NOT EXISTS forms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        template_id INTEGER,
        company_id INTEGER,
        title TEXT NOT NULL,
        content TEXT,
        company_name TEXT,
        status TEXT DEFAULT 'draft',
        is_shared INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (template_id) REFERENCES templates (id),
        FOREIGN KEY (company_id) REFERENCES companies (id)
    )''')
    
    # Form fields table
    c.execute('''CREATE TABLE IF NOT EXISTS form_fields (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        form_id INTEGER NOT NULL,
        field_name TEXT NOT NULL,
        field_value TEXT,
        FOREIGN KEY (form_id) REFERENCES forms (id) ON DELETE CASCADE
    )''')
    
    # Form versions table
    c.execute('''CREATE TABLE IF NOT EXISTS form_versions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        form_id INTEGER NOT NULL,
        content TEXT,
        version INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (form_id) REFERENCES forms (id) ON DELETE CASCADE
    )''')
    
    conn.commit()
    conn.close()

# Initialize DB
init_db()

# Load templates from DB or use defaults
def get_templates():
    """Get all templates from database"""
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM templates WHERE is_published = 1 ORDER BY category, name")
    rows = c.fetchall()
    conn.close()
    
    if not rows:
        return get_default_templates()
    
    templates = {}
    for row in rows:
        templates[row['slug']] = {
            'id': row['id'],
            'name': row['name'],
            'category': row['category'],
            'description': row['description'],
            'fields': json.loads(row['fields']),
            'tier': row['tier'],
            'price': row['price']
        }
    return templates

def get_default_templates():
    """Default templates if DB is empty"""
    return {
        'onboarding': {'name': 'Employee Onboarding', 'category': 'SOPs', 'fields': ['company_name', 'employee_name', 'department', 'start_date']},
        'invoice': {'name': 'Invoice', 'category': 'Finance', 'fields': ['company_name', 'client_name', 'amount', 'items']},
        # Add more defaults...
    }

# Group templates by category
def get_categories(templates):
    categories = {}
    for slug, template in templates.items():
        cat = template['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append({'type': slug, 'name': template['name'], 'id': template.get('id')})
    return categories

# Password hashing
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, hash_):
    return hash_password(password) == hash_

@app.route('/')
def index():
    """Home page - dashboard"""
    conn = get_db()
    
    # Get stats
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM forms')
    total_forms = c.fetchone()[0]
    
    c.execute('SELECT COUNT(*) FROM templates')
    total_templates = c.fetchone()[0]
    
    c.execute('SELECT COUNT(*) FROM users')
    total_users = c.fetchone()[0]
    
    # Recent forms
    c.execute('''SELECT f.id, f.title, f.status, f.created_at, t.name as template_name 
                 FROM forms f LEFT JOIN templates t ON f.template_id = t.id 
                 ORDER BY f.updated_at DESC LIMIT 10''')
    recent_forms = c.fetchall()
    
    # Top templates
    c.execute('''SELECT template_id, t.name, COUNT(*) as count 
                 FROM forms f JOIN templates t ON f.template_id = t.id 
                 GROUP BY template_id ORDER BY count DESC LIMIT 5''')
    top_templates = c.fetchall()
    
    # Forms by status
    c.execute('''SELECT status, COUNT(*) as count FROM forms GROUP BY status''')
    status_counts = c.fetchall()
    
    conn.close()
    
    templates = get_templates()
    categories = get_categories(templates)
    
    return render_template('index.html', 
                         categories=categories,
                         templates=templates,
                         total_forms=total_forms,
                         total_templates=total_templates,
                         total_users=total_users,
                         recent_forms=recent_forms,
                         top_templates=top_templates,
                         status_counts=status_counts)

# ============== AUTH ROUTES ==============

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = c.fetchone()
        conn.close()
        
        if user and verify_password(password, user['password_hash']):
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['role'] = user['role']
            flash(f'Welcome back, {user["username"]}!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        company_name = request.form.get('company_name')
        
        conn = get_db()
        c = conn.cursor()
        
        # Create company
        slug = company_name.lower().replace(' ', '-')
        try:
            c.execute('INSERT INTO companies (name, slug) VALUES (?, ?)', (company_name, slug))
            company_id = c.lastrowid
            
            # Create user
            password_hash = hash_password(password)
            c.execute('''INSERT INTO users (username, email, password_hash, company_id, role) 
                         VALUES (?, ?, ?, ?, ?)''',
                     (username, email, password_hash, company_id, 'admin'))
            
            conn.commit()
            user_id = c.lastrowid
            conn.close()
            
            session['user_id'] = user_id
            session['username'] = username
            session['role'] = 'admin'
            flash(f'Welcome {username}! Your company has been created.', 'success')
            return redirect(url_for('index'))
        except sqlite3.IntegrityError:
            flash('Username already exists', 'error')
            conn.close()
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'success')
    return redirect(url_for('index'))

# ============== TEMPLATE ROUTES ==============

@app.route('/templates')
def all_templates():
    templates = get_templates()
    categories = get_categories(templates)
    return render_template('templates.html', templates=templates, categories=categories)

@app.route('/template/new', methods=['GET', 'POST'])
def new_template():
    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        description = request.form.get('description')
        fields = request.form.get('fields')
        tier = request.form.get('tier')
        
        # Parse fields
        field_list = [f.strip() for f in fields.split(',') if f.strip()]
        
        conn = get_db()
        c = conn.cursor()
        
        slug = name.lower().replace(' ', '-').replace('/', '-')
        c.execute('''INSERT INTO templates (name, slug, category, description, fields, tier, created_by)
                     VALUES (?, ?, ?, ?, ?, ?, ?)''',
                 (name, slug, category, description, json.dumps(field_list), tier, session.get('user_id')))
        
        conn.commit()
        conn.close()
        
        flash(f'Template "{name}" created!', 'success')
        return redirect(url_for('all_templates'))
    
    return render_template('template_new.html')

@app.route('/template/<slug>/edit', methods=['GET', 'POST'])
def edit_template(slug):
    conn = get_db()
    c = conn.cursor()
    
    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        description = request.form.get('description')
        fields = request.form.get('fields')
        tier = request.form.get('tier')
        
        field_list = [f.strip() for f in fields.split(',') if f.strip()]
        
        c.execute('''UPDATE templates SET name = ?, category = ?, description = ?, 
                     fields = ?, tier = ?, updated_at = CURRENT_TIMESTAMP
                     WHERE slug = ?''',
                 (name, category, description, json.dumps(field_list), tier, slug))
        
        conn.commit()
        flash(f'Template updated!', 'success')
        return redirect(url_for('all_templates'))
    
    c.execute('SELECT * FROM templates WHERE slug = ?', (slug,))
    template = c.fetchone()
    conn.close()
    
    return render_template('template_edit.html', template=template)

@app.route('/template/<slug>/delete', methods=['POST'])
def delete_template(slug):
    conn = get_db()
    c = conn.cursor()
    c.execute('DELETE FROM templates WHERE slug = ?', (slug,))
    conn.commit()
    conn.close()
    
    flash('Template deleted', 'success')
    return redirect(url_for('all_templates'))

# ============== FORM ROUTES ==============

@app.route('/forms')
def all_forms():
    status_filter = request.args.get('status', '')
    template_filter = request.args.get('template', '')
    
    conn = get_db()
    c = conn.cursor()
    
    query = '''SELECT f.*, t.name as template_name, u.username 
               FROM forms f 
               LEFT JOIN templates t ON f.template_id = t.id 
               LEFT JOIN users u ON f.user_id = u.id 
               WHERE 1=1'''
    params = []
    
    if status_filter:
        query += ' AND f.status = ?'
        params.append(status_filter)
    
    if template_filter:
        query += ' AND f.template_id = ?'
        params.append(template_filter)
    
    query += ' ORDER BY f.updated_at DESC'
    
    c.execute(query, params)
    forms = c.fetchall()
    
    # Get templates for filter
    c.execute('SELECT id, name FROM templates ORDER BY name')
    templates = c.fetchall()
    
    conn.close()
    
    return render_template('forms.html', forms=forms, templates=templates, 
                         status_filter=status_filter, template_filter=template_filter)

@app.route('/form/new/<template_slug>')
def new_form(template_slug):
    templates = get_templates()
    if template_slug not in templates:
        flash('Template not found', 'error')
        return redirect(url_for('index'))
    
    template = templates[template_slug]
    return render_template('new_form.html', template_type=template_slug, template=template)

@app.route('/form/duplicate/<int:form_id>')
def duplicate_form(form_id):
    conn = get_db()
    c = conn.cursor()
    
    c.execute('SELECT * FROM forms WHERE id = ?', (form_id,))
    original = c.fetchone()
    
    if not original:
        flash('Form not found', 'error')
        return redirect(url_for('all_forms'))
    
    # Get fields
    c.execute('SELECT field_name, field_value FROM form_fields WHERE form_id = ?', (form_id,))
    original_fields = c.fetchall()
    
    # Create new form
    new_title = f"{original['title']} (Copy)"
    c.execute('''INSERT INTO forms (user_id, template_id, company_id, title, content, company_name, status)
                 VALUES (?, ?, ?, ?, ?, ?, ?)''',
             (session.get('user_id'), original['template_id'], original['company_id'],
              new_title, original['content'], original['company_name'], 'draft'))
    
    new_id = c.lastrowid
    
    # Copy fields
    for field in original_fields:
        c.execute('INSERT INTO form_fields (form_id, field_name, field_value) VALUES (?, ?, ?)',
                 (new_id, field['field_name'], field['field_value']))
    
    conn.commit()
    conn.close()
    
    flash('Form duplicated!', 'success')
    return redirect(url_for('view_form', form_id=new_id))

@app.route('/form/<int:form_id>')
def view_form(form_id):
    conn = get_db()
    c = conn.cursor()
    
    c.execute('SELECT f.*, t.name as template_name, t.fields as template_fields FROM forms f LEFT JOIN templates t ON f.template_id = t.id WHERE f.id = ?', (form_id,))
    form = c.fetchone()
    
    if not form:
        flash('Form not found', 'error')
        return redirect(url_for('all_forms'))
    
    c.execute('SELECT field_name, field_value FROM form_fields WHERE form_id = ?', (form_id,))
    fields = {f['field_name']: f['field_value'] for f in c.fetchall()}
    
    # Get versions
    c.execute('SELECT * FROM form_versions WHERE form_id = ? ORDER BY version DESC LIMIT 10', (form_id,))
    versions = c.fetchall()
    
    conn.close()
    
    templates = get_templates()
    return render_template('view_form.html', form=form, fields=fields, templates=templates, versions=versions)

@app.route('/form/<int:form_id>/edit', methods=['GET', 'POST'])
def edit_form(form_id):
    conn = get_db()
    c = conn.cursor()
    
    c.execute('SELECT f.*, t.fields as template_fields FROM forms f LEFT JOIN templates t ON f.template_id = t.id WHERE f.id = ?', (form_id,))
    form = c.fetchone()
    
    if not form:
        flash('Form not found', 'error')
        return redirect(url_for('all_forms'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        company_name = request.form.get('company_name')
        status = request.form.get('status')
        
        fields = {}
        for key in request.form:
            if key not in ['title', 'company_name', 'status']:
                fields[key] = request.form[key]
        
        # Save version before updating
        c.execute('SELECT COUNT(*) FROM form_versions WHERE form_id = ?', (form_id,))
        version = c.fetchone()[0] + 1
        c.execute('INSERT INTO form_versions (form_id, content, version) VALUES (?, ?, ?)',
                 (form_id, form['content'], version))
        
        # Update content
        template_fields = json.loads(form['template_fields']) if form['template_fields'] else []
        content = f"# {title}\n\n"
        content += f"**Company:** {company_name}\n"
        content += f"**Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n---\n\n"
        
        for key, value in fields.items():
            if value:
                content += f"## {key.replace('_', ' ').title()}\n\n{value}\n\n"
        
        c.execute('''UPDATE forms SET title = ?, content = ?, company_name = ?, status = ?, 
                     updated_at = CURRENT_TIMESTAMP WHERE id = ?''',
                 (title, content, company_name, status, form_id))
        
        # Update fields
        c.execute('DELETE FROM form_fields WHERE form_id = ?', (form_id,))
        for field_name, field_value in fields.items():
            if field_value:
                c.execute('INSERT INTO form_fields (form_id, field_name, field_value) VALUES (?, ?, ?)',
                         (form_id, field_name, field_value))
        
        conn.commit()
        conn.close()
        
        flash('Form updated!', 'success')
        return redirect(url_for('view_form', form_id=form_id))
    
    c.execute('SELECT field_name, field_value FROM form_fields WHERE form_id = ?', (form_id,))
    fields = {f['field_name']: f['field_value'] for f in c.fetchall()}
    conn.close()
    
    template_fields = json.loads(form['template_fields']) if form['template_fields'] else []
    
    return render_template('edit_form.html', form=form, fields=fields, template_fields=template_fields)

@app.route('/form/<int:form_id>/delete', methods=['POST'])
def delete_form(form_id):
    conn = get_db()
    c = conn.cursor()
    c.execute('DELETE FROM forms WHERE id = ?', (form_id,))
    conn.commit()
    conn.close()
    
    flash('Form deleted', 'success')
    return redirect(url_for('all_forms'))

# ============== EXPORT ROUTES ==============

@app.route('/export/<int:form_id>/<format>')
def export_form(form_id, format='markdown'):
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT title, content FROM forms WHERE id = ?', (form_id,))
    form = c.fetchone()
    conn.close()
    
    if not form:
        flash('Form not found', 'error')
        return redirect(url_for('all_forms'))
    
    filename = form['title'].replace(' ', '_')
    
    if format == 'markdown':
        response = app.make_response(form['content'])
        response.headers['Content-Disposition'] = f'attachment; filename={filename}.md'
        return response
    
    elif format == 'pdf':
        import subprocess
        md_file = f'/tmp/{filename}.md'
        pdf_file = f'/tmp/{filename}.pdf'
        
        with open(md_file, 'w') as f:
            f.write(form['content'])
        
        try:
            subprocess.run(['pandoc', md_file, '-o', pdf_file], check=True)
            return send_file(pdf_file, as_attachment=True)
        except:
            flash('PDF not available', 'warning')
            return redirect(url_for('view_form', form_id=form_id))
    
    elif format == 'docx':
        import subprocess
        md_file = f'/tmp/{filename}.md'
        docx_file = f'/tmp/{filename}.docx'
        
        with open(md_file, 'w') as f:
            f.write(form['content'])
        
        try:
            subprocess.run(['pandoc', md_file, '-o', docx_file], check=True)
            return send_file(docx_file, as_attachment=True)
        except:
            flash('DOCX not available', 'warning')
            return redirect(url_for('view_form', form_id=form_id))
    
    return redirect(url_for('view_form', form_id=form_id))

@app.route('/export/all')
def export_all_forms():
    """Export all forms as JSON"""
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM forms ORDER BY updated_at DESC')
    forms = c.fetchall()
    conn.close()
    
    export_data = []
    for form in forms:
        export_data.append({
            'id': form['id'],
            'title': form['title'],
            'company_name': form['company_name'],
            'status': form['status'],
            'content': form['content'],
            'created_at': form['created_at'],
            'updated_at': form['updated_at']
        })
    
    response = app.make_response(json.dumps(export_data, indent=2))
    response.headers['Content-Disposition'] = 'attachment; filename=all_forms.json'
    return response

# ============== SEARCH ==============

@app.route('/search')
def search():
    query = request.args.get('q', '')
    
    conn = get_db()
    c = conn.cursor()
    
    c.execute('''SELECT f.id, f.title, f.status, f.created_at, t.name as template_name 
                 FROM forms f LEFT JOIN templates t ON f.template_id = t.id 
                 WHERE f.title LIKE ? OR f.content LIKE ? OR f.company_name LIKE ?
                 ORDER BY f.updated_at DESC''',
              (f'%{query}%', f'%{query}%', f'%{query}%'))
    
    results = c.fetchall()
    conn.close()
    
    return render_template('search.html', results=results, query=query)

# ============== API ==============

@app.route('/api/forms')
def api_forms():
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM forms ORDER BY updated_at DESC')
    forms = c.fetchall()
    conn.close()
    
    return jsonify([dict(row) for row in forms])

@app.route('/api/templates')
def api_templates():
    return jsonify(get_templates())

if __name__ == '__main__':
    app.run(debug=True, port=5000)
