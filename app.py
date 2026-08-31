import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash, send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
import database
import models

app = Flask(__name__)
app.secret_key = "campuskit_college_marketplace_secret_key_2026"

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "static", "uploads")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'svg', 'webp'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Context Processor to make current_user available in all templates
@app.context_processor
def inject_user():
    user_id = session.get('user_id')
    current_user = models.get_user_by_id(user_id) if user_id else None
    return dict(current_user=current_user)

# Auto-ensure database is initialized on startup
with app.app_context():
    database.init_db()

# --- Page Routes ---

@app.route('/')
def index():
    stats = models.get_admin_stats()
    featured_products = models.get_products(limit=4)
    return render_template('index.html', stats=stats, featured_products=featured_products, active_page='home')

@app.route('/marketplace')
def marketplace():
    category = request.args.get('category', 'All')
    search = request.args.get('search', '').strip()
    condition = request.args.get('condition', 'All')
    department = request.args.get('department', 'All')
    location = request.args.get('location', 'All')
    status = request.args.get('status', 'All')
    sort_by = request.args.get('sort', 'newest')
    max_price = request.args.get('max_price')

    products = models.get_products(
        category=category,
        search=search,
        condition=condition,
        department=department,
        location=location,
        status=status,
        sort_by=sort_by,
        max_price=max_price
    )

    current_filters = {
        'category': category,
        'search': search,
        'condition': condition,
        'department': department,
        'location': location,
        'status': status,
        'sort_by': sort_by,
        'max_price': max_price
    }

    return render_template('marketplace.html', products=products, current_filters=current_filters, active_page='marketplace')

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = models.get_product_by_id(product_id)
    if not product:
        flash("Product not found.", "error")
        return redirect(url_for('marketplace'))
    
    models.increment_product_views(product_id)
    return render_template('product_detail.html', product=product, active_page='marketplace')

@app.route('/sell', methods=['GET', 'POST'])
def sell():
    # If not logged in, auto-login as senior demo user for convenience in MVP
    if not session.get('user_id'):
        senior = models.get_user_by_id(1)
        if senior:
            session['user_id'] = senior['id']
            session['user_name'] = senior['name']
            session['user_role'] = senior['role']
    
    current_user_id = session.get('user_id')

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        category = request.form.get('category', 'Other')
        condition = request.form.get('condition', 'Good')
        price = float(request.form.get('price', 0))
        original_price = float(request.form.get('original_price', price))
        description = request.form.get('description', '').strip()
        location = request.form.get('location', '').strip()
        department = request.form.get('department', 'General')
        preset_image = request.form.get('image_preset', '/static/images/sample/casio_calc.svg')

        image_url = preset_image

        # Handle custom photo upload if provided
        if 'photo' in request.files:
            file = request.files['photo']
            if file and file.filename != '' and allowed_file(file.filename):
                filename = secure_filename(f"item_{current_user_id}_{file.filename}")
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                image_url = f"/static/uploads/{filename}"

        product_id = models.create_product(
            seller_id=current_user_id,
            name=name,
            category=category,
            price=price,
            original_price=original_price,
            condition=condition,
            description=description,
            image_url=image_url,
            department=department,
            location=location
        )

        flash(f"🎉 Listing published! '{name}' is now live on the Campus Marketplace.", "success")
        return redirect(url_for('dashboard'))

    return render_template('sell.html', active_page='sell')

@app.route('/dashboard')
def dashboard():
    user_id = session.get('user_id')
    if not user_id:
        # Default to Rahul (Senior)
        session['user_id'] = 1
        user_id = 1

    stats = models.get_seller_stats(user_id)
    products = models.get_seller_products(user_id)
    reservations = models.get_reservations_for_seller(user_id)
    return render_template('dashboard.html', stats=stats, products=products, reservations=reservations, active_page='dashboard')

@app.route('/profile')
def profile():
    user_id = session.get('user_id')
    if not user_id:
        session['user_id'] = 1
        user_id = 1

    user = models.get_user_by_id(user_id)
    my_reservations = models.get_reservations_by_buyer(user_id)
    my_listings = models.get_seller_products(user_id)
    return render_template('profile.html', user=user, my_reservations=my_reservations, my_listings=my_listings, active_page='profile')

@app.route('/profile/update', methods=['POST'])
def profile_update():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    name = request.form.get('name')
    department = request.form.get('department')
    year = request.form.get('year')
    hostel = request.form.get('hostel')
    phone = request.form.get('phone')

    models.update_user_profile(user_id, name, department, year, hostel, phone)
    flash("Profile information updated successfully.", "success")
    return redirect(url_for('profile'))

@app.route('/admin')
def admin():
    # If current user is not admin, auto log in as Admin for MVP ease
    user_id = session.get('user_id')
    user = models.get_user_by_id(user_id) if user_id else None
    if not user or user['role'] != 'admin':
        session['user_id'] = 5
        user = models.get_user_by_id(5)

    stats = models.get_admin_stats()
    users = models.get_all_users()
    products = models.get_products(status="All")
    reports = models.get_all_reports()
    return render_template('admin.html', stats=stats, users=users, products=products, reports=reports, active_page='admin')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        user = models.get_user_by_email(email)
        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session['user_role'] = user['role']
            flash(f"Welcome back, {user['name']}!", "success")
            if user['role'] == 'admin':
                return redirect(url_for('admin'))
            elif user['role'] == 'senior':
                return redirect(url_for('dashboard'))
            else:
                return redirect(url_for('marketplace'))
        else:
            flash("Invalid college email or password. Try demo accounts above!", "error")

    return render_template('login.html', active_page='login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        department = request.form.get('department', 'General')
        year = request.form.get('year', 'S1 (1st Year)')
        hostel = request.form.get('hostel', '').strip()
        phone = request.form.get('phone', '').strip()
        role = request.form.get('role', 'senior')

        existing = models.get_user_by_email(email)
        if existing:
            flash("An account with this college email already exists. Please log in.", "error")
            return redirect(url_for('login'))

        user_id = models.create_user(
            name=name,
            email=email,
            password=password,
            department=department,
            year=year,
            hostel=hostel,
            phone=phone,
            role=role,
            is_verified=1
        )

        session['user_id'] = user_id
        session['user_name'] = name
        session['user_role'] = role

        flash(f"🎉 College verification complete! Welcome to CampusKit, {name}.", "success")
        if role == 'senior':
            return redirect(url_for('sell'))
        else:
            return redirect(url_for('marketplace'))

    return render_template('register.html', active_page='register')

# --- REST APIs & Actions ---

@app.route('/api/demo-login/<role>', methods=['POST'])
def demo_login(role):
    # Mapping roles to seed accounts
    role_map = {
        'senior': 1,  # Rahul Sharma (S4 CSE)
        'junior': 2,  # Ananya Iyer (S1 ECE)
        'admin': 5    # Prof. Radhakrishnan (Admin)
    }
    target_id = role_map.get(role, 1)
    user = models.get_user_by_id(target_id)
    if user:
        session['user_id'] = user['id']
        session['user_name'] = user['name']
        session['user_role'] = user['role']
        return jsonify({'success': True, 'user': user})
    return jsonify({'success': False, 'message': 'Demo account not found'}), 404

@app.route('/api/logout')
def logout():
    session.clear()
    flash("You have been signed out.", "info")
    return redirect(url_for('index'))

@app.route('/api/products')
def api_products():
    category = request.args.get('category')
    search = request.args.get('search')
    products = models.get_products(category=category, search=search)
    return jsonify({'success': True, 'products': products})

@app.route('/api/products/<int:product_id>/reserve', methods=['POST'])
def api_reserve_product(product_id):
    # Ensure buyer is logged in or default to Junior demo account
    user_id = session.get('user_id')
    if not user_id:
        session['user_id'] = 2 # Ananya (Junior)
        user_id = 2

    data = request.get_json() or {}
    note = data.get('note', 'Interested in buying on campus!')

    success, message = models.create_reservation(product_id, user_id, note)
    if success:
        return jsonify({'success': True, 'reservation_id': message})
    return jsonify({'success': False, 'message': message}), 400

@app.route('/api/products/<int:product_id>/status', methods=['POST'])
def api_product_status(product_id):
    data = request.get_json() or {}
    status = data.get('status', 'available')
    if status not in ['available', 'reserved', 'sold']:
        return jsonify({'success': False, 'message': 'Invalid status'}), 400
    models.update_product_status(product_id, status)
    return jsonify({'success': True, 'status': status})

@app.route('/api/products/<int:product_id>/delete', methods=['POST'])
def api_delete_product(product_id):
    models.delete_product(product_id)
    return jsonify({'success': True})

@app.route('/api/products/<int:product_id>/report', methods=['POST'])
def api_report_product(product_id):
    user_id = session.get('user_id') or 2
    data = request.get_json() or {}
    reason = data.get('reason', 'Inappropriate or incorrect listing')
    models.create_report(product_id, user_id, reason)
    return jsonify({'success': True})

@app.route('/api/reservations/<int:reservation_id>/status', methods=['POST'])
def api_reservation_status(reservation_id):
    data = request.get_json() or {}
    status = data.get('status', 'confirmed')
    success = models.update_reservation_status(reservation_id, status)
    return jsonify({'success': success})

@app.route('/api/admin/delete-listing/<int:product_id>', methods=['POST'])
def api_admin_delete(product_id):
    models.delete_product(product_id)
    return jsonify({'success': True})

if __name__ == '__main__':
    print("==============================================================")
    print("🚀 CampusKit - Senior-to-Junior Engineering Marketplace Running")
    print("📍 Local URL: http://127.0.0.1:5000")
    print("==============================================================")
    app.run(host='0.0.0.0', port=5000, debug=True)
