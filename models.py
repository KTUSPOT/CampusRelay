import sqlite3
from database import get_db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# --- User Operations ---
def get_user_by_id(user_id):
    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    conn.close()
    return dict(user) if user else None

def get_user_by_email(email):
    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE LOWER(email) = LOWER(?)", (email.strip(),)).fetchone()
    conn.close()
    return dict(user) if user else None

def create_user(name, email, password, department, year, hostel, phone, role="senior", is_verified=1, verification_code=None):
    conn = get_db()
    cursor = conn.cursor()
    password_hash = generate_password_hash(password)
    cursor.execute("""
        INSERT INTO users (name, email, password_hash, department, year, hostel, phone, role, is_verified, verification_code)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, email.strip().lower(), password_hash, department, year, hostel, phone, role, is_verified, verification_code))
    user_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return user_id

def verify_user_code(email, code):
    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE LOWER(email) = LOWER(?)", (email.strip(),)).fetchone()
    if not user:
        conn.close()
        return False, "User not found"
    
    if user["verification_code"] and user["verification_code"] == code.strip():
        conn.execute("UPDATE users SET is_verified = 1, verification_code = NULL WHERE id = ?", (user["id"],))
        conn.commit()
        conn.close()
        return True, "Email successfully verified"
    
    conn.close()
    return False, "Invalid verification code"

def update_user_profile(user_id, name, department, year, hostel, phone):
    conn = get_db()
    conn.execute("""
        UPDATE users 
        SET name = ?, department = ?, year = ?, hostel = ?, phone = ?
        WHERE id = ?
    """, (name, department, year, hostel, phone, user_id))
    conn.commit()
    conn.close()

def get_all_users():
    conn = get_db()
    users = conn.execute("SELECT id, name, email, department, year, hostel, phone, role, is_verified, created_at FROM users ORDER BY id ASC").fetchall()
    conn.close()
    return [dict(u) for u in users]

# --- Product Operations ---
def get_products(category=None, search=None, condition=None, department=None, location=None, status=None, sort_by=None, min_price=None, max_price=None, limit=None):
    conn = get_db()
    query = """
        SELECT p.*, u.name as seller_name, u.email as seller_email, u.phone as seller_phone, 
               u.year as seller_year, u.department as seller_department, u.hostel as seller_hostel
        FROM products p
        JOIN users u ON p.seller_id = u.id
        WHERE 1=1
    """
    params = []

    if category and category != "All":
        query += " AND p.category = ?"
        params.append(category)

    if condition and condition != "All":
        query += " AND p.condition = ?"
        params.append(condition)

    if department and department != "All":
        query += " AND (p.department = ? OR u.department = ?)"
        params.extend([department, department])

    if location and location != "All":
        query += " AND (p.location LIKE ? OR u.hostel LIKE ?)"
        params.extend([f"%{location}%", f"%{location}%"])

    if status and status != "All":
        query += " AND p.status = ?"
        params.append(status)

    if search:
        query += " AND (p.name LIKE ? OR p.description LIKE ? OR p.category LIKE ?)"
        term = f"%{search.strip()}%"
        params.extend([term, term, term])

    if min_price is not None:
        query += " AND p.price >= ?"
        params.append(float(min_price))

    if max_price is not None:
        query += " AND p.price <= ?"
        params.append(float(max_price))

    # Sorting
    if sort_by == "price_asc":
        query += " ORDER BY p.price ASC"
    elif sort_by == "price_desc":
        query += " ORDER BY p.price DESC"
    elif sort_by == "savings_desc":
        query += " ORDER BY (p.original_price - p.price) DESC"
    else:  # 'newest' default
        query += " ORDER BY p.id DESC"

    if limit:
        query += f" LIMIT {int(limit)}"

    rows = conn.execute(query, params).fetchall()
    conn.close()
    
    result = []
    for r in rows:
        d = dict(r)
        d['savings'] = max(0, d['original_price'] - d['price'])
        d['savings_percent'] = round((d['savings'] / d['original_price'] * 100)) if d['original_price'] > 0 else 0
        result.append(d)
    return result

def get_product_by_id(product_id):
    conn = get_db()
    query = """
        SELECT p.*, u.name as seller_name, u.email as seller_email, u.phone as seller_phone, 
               u.year as seller_year, u.department as seller_department, u.hostel as seller_hostel
        FROM products p
        JOIN users u ON p.seller_id = u.id
        WHERE p.id = ?
    """
    row = conn.execute(query, (product_id,)).fetchone()
    conn.close()
    if not row:
        return None
    d = dict(row)
    d['savings'] = max(0, d['original_price'] - d['price'])
    d['savings_percent'] = round((d['savings'] / d['original_price'] * 100)) if d['original_price'] > 0 else 0
    return d

def create_product(seller_id, name, category, price, original_price, condition, description, image_url, department, location):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO products (seller_id, name, category, price, original_price, condition, description, image_url, department, location, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'available')
    """, (seller_id, name, category, float(price), float(original_price), condition, description, image_url, department, location))
    product_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return product_id

def update_product(product_id, name, category, price, original_price, condition, description, department, location, image_url=None):
    conn = get_db()
    if image_url:
        conn.execute("""
            UPDATE products 
            SET name = ?, category = ?, price = ?, original_price = ?, condition = ?, description = ?, department = ?, location = ?, image_url = ?
            WHERE id = ?
        """, (name, category, float(price), float(original_price), condition, description, department, location, image_url, product_id))
    else:
        conn.execute("""
            UPDATE products 
            SET name = ?, category = ?, price = ?, original_price = ?, condition = ?, description = ?, department = ?, location = ?
            WHERE id = ?
        """, (name, category, float(price), float(original_price), condition, description, department, location, product_id))
    conn.commit()
    conn.close()

def update_product_status(product_id, status):
    conn = get_db()
    conn.execute("UPDATE products SET status = ? WHERE id = ?", (status, product_id))
    conn.commit()
    conn.close()

def increment_product_views(product_id):
    conn = get_db()
    conn.execute("UPDATE products SET views = views + 1 WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = get_db()
    conn.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()

def get_seller_products(seller_id):
    conn = get_db()
    rows = conn.execute("""
        SELECT p.*, 
               (SELECT COUNT(*) FROM reservations r WHERE r.product_id = p.id AND r.status = 'pending') as pending_reservations
        FROM products p 
        WHERE p.seller_id = ? 
        ORDER BY p.id DESC
    """, (seller_id,)).fetchall()
    conn.close()
    result = []
    for r in rows:
        d = dict(r)
        d['savings'] = max(0, d['original_price'] - d['price'])
        d['savings_percent'] = round((d['savings'] / d['original_price'] * 100)) if d['original_price'] > 0 else 0
        result.append(d)
    return result

# --- Reservation Operations ---
def create_reservation(product_id, buyer_id, note=""):
    conn = get_db()
    cursor = conn.cursor()
    
    # Check if product is available
    prod = conn.execute("SELECT status, seller_id FROM products WHERE id = ?", (product_id,)).fetchone()
    if not prod or prod["status"] == "sold":
        conn.close()
        return False, "Item is already sold or unavailable."
    
    if prod["seller_id"] == buyer_id:
        conn.close()
        return False, "You cannot reserve your own item."

    cursor.execute("""
        INSERT INTO reservations (product_id, buyer_id, status, note)
        VALUES (?, ?, 'pending', ?)
    """, (product_id, buyer_id, note))
    
    # Automatically update product status to reserved
    cursor.execute("UPDATE products SET status = 'reserved' WHERE id = ?", (product_id,))
    
    res_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return True, res_id

def get_reservations_by_buyer(buyer_id):
    conn = get_db()
    rows = conn.execute("""
        SELECT r.*, p.name as product_name, p.price, p.original_price, p.image_url, p.status as product_status,
               u.name as seller_name, u.phone as seller_phone, u.hostel as seller_hostel, u.department as seller_department
        FROM reservations r
        JOIN products p ON r.product_id = p.id
        JOIN users u ON p.seller_id = u.id
        WHERE r.buyer_id = ?
        ORDER BY r.id DESC
    """, (buyer_id,)).fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_reservations_for_seller(seller_id):
    conn = get_db()
    rows = conn.execute("""
        SELECT r.*, p.name as product_name, p.price, p.image_url, p.status as product_status,
               u.name as buyer_name, u.email as buyer_email, u.phone as buyer_phone, u.year as buyer_year, u.hostel as buyer_hostel
        FROM reservations r
        JOIN products p ON r.product_id = p.id
        JOIN users u ON r.buyer_id = u.id
        WHERE p.seller_id = ?
        ORDER BY r.id DESC
    """, (seller_id,)).fetchall()
    conn.close()
    return [dict(r) for r in rows]

def update_reservation_status(reservation_id, new_status):
    conn = get_db()
    res = conn.execute("SELECT * FROM reservations WHERE id = ?", (reservation_id,)).fetchone()
    if not res:
        conn.close()
        return False
    
    conn.execute("UPDATE reservations SET status = ? WHERE id = ?", (new_status, reservation_id))
    
    if new_status == "confirmed" or new_status == "completed":
        conn.execute("UPDATE products SET status = 'sold' WHERE id = ?", (res["product_id"],))
    elif new_status == "cancelled":
        conn.execute("UPDATE products SET status = 'available' WHERE id = ?", (res["product_id"],))
    
    conn.commit()
    conn.close()
    return True

# --- Reports & Admin ---
def create_report(product_id, reporter_id, reason):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reports (product_id, reporter_id, reason, status)
        VALUES (?, ?, ?, 'pending')
    """, (product_id, reporter_id, reason))
    conn.commit()
    conn.close()
    return True

def get_all_reports():
    conn = get_db()
    rows = conn.execute("""
        SELECT rep.*, p.name as product_name, p.price, p.status as product_status,
               seller.name as seller_name, reporter.name as reporter_name
        FROM reports rep
        JOIN products p ON rep.product_id = p.id
        JOIN users seller ON p.seller_id = seller.id
        JOIN users reporter ON rep.reporter_id = reporter.id
        ORDER BY rep.id DESC
    """).fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_seller_stats(seller_id):
    conn = get_db()
    active_count = conn.execute("SELECT COUNT(*) FROM products WHERE seller_id = ? AND status = 'available'", (seller_id,)).fetchone()[0]
    reserved_count = conn.execute("SELECT COUNT(*) FROM products WHERE seller_id = ? AND status = 'reserved'", (seller_id,)).fetchone()[0]
    sold_count = conn.execute("SELECT COUNT(*) FROM products WHERE seller_id = ? AND status = 'sold'", (seller_id,)).fetchone()[0]
    
    earnings = conn.execute("SELECT COALESCE(SUM(price), 0) FROM products WHERE seller_id = ? AND status = 'sold'", (seller_id,)).fetchone()[0]
    
    conn.close()
    return {
        "active_listings": active_count,
        "reserved_listings": reserved_count,
        "items_sold": sold_count,
        "total_earned": earnings
    }

def get_admin_stats():
    conn = get_db()
    total_users = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    total_listings = conn.execute("SELECT COUNT(*) FROM products").fetchone()[0]
    available_items = conn.execute("SELECT COUNT(*) FROM products WHERE status = 'available'").fetchone()[0]
    reserved_items = conn.execute("SELECT COUNT(*) FROM products WHERE status = 'reserved'").fetchone()[0]
    sold_items = conn.execute("SELECT COUNT(*) FROM products WHERE status = 'sold'").fetchone()[0]
    
    # Total estimated savings = sum(original_price - price) across all listed products
    savings = conn.execute("SELECT COALESCE(SUM(original_price - price), 0) FROM products").fetchone()[0]
    total_volume = conn.execute("SELECT COALESCE(SUM(price), 0) FROM products WHERE status = 'sold'").fetchone()[0]
    
    conn.close()
    return {
        "total_users": total_users,
        "total_listings": total_listings,
        "available_items": available_items,
        "reserved_items": reserved_items,
        "sold_items": sold_items,
        "total_savings": savings,
        "total_volume": total_volume
    }
