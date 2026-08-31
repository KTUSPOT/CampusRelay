import sqlite3
import os
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta

DB_PATH = os.path.join(os.path.dirname(__file__), "campuskit.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        department TEXT NOT NULL,
        year TEXT NOT NULL,
        hostel TEXT NOT NULL,
        phone TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'senior', -- 'senior', 'junior', 'admin'
        is_verified INTEGER NOT NULL DEFAULT 1,
        verification_code TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        seller_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        original_price REAL NOT NULL,
        condition TEXT NOT NULL, -- 'Like New', 'Good', 'Fair'
        description TEXT NOT NULL,
        image_url TEXT NOT NULL,
        department TEXT NOT NULL,
        location TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'available', -- 'available', 'reserved', 'sold'
        views INTEGER NOT NULL DEFAULT 0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (seller_id) REFERENCES users (id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL,
        buyer_id INTEGER NOT NULL,
        status TEXT NOT NULL DEFAULT 'pending', -- 'pending', 'confirmed', 'cancelled', 'completed'
        note TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE,
        FOREIGN KEY (buyer_id) REFERENCES users (id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL,
        reporter_id INTEGER NOT NULL,
        reason TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'pending', -- 'pending', 'resolved', 'dismissed'
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE,
        FOREIGN KEY (reporter_id) REFERENCES users (id) ON DELETE CASCADE
    );
    """)

    conn.commit()
    seed_data(conn)
    conn.close()

def seed_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] > 0:
        return  # Already seeded

    # Seed Users
    default_pw = generate_password_hash("password123")
    users = [
        (1, "Rahul Sharma", "rahul.sharma@college.edu", default_pw, "Computer Science & Engineering", "S4 (2nd Year)", "Men's Hostel Block B (Room 214)", "+919876543210", "senior", 1, None),
        (2, "Ananya Iyer", "ananya.iyer@college.edu", default_pw, "Electronics & Communication", "S1 (1st Year)", "Women's Hostel Block A (Room 108)", "+919812345678", "junior", 1, None),
        (3, "Arun Kumar", "arun.kumar@college.edu", default_pw, "Mechanical Engineering", "S6 (3rd Year)", "Men's Hostel Block A (Room 302)", "+919765432109", "senior", 1, None),
        (4, "Kavya Menon", "kavya.menon@college.edu", default_pw, "Civil Engineering", "S4 (2nd Year)", "Women's Hostel Block B (Room 205)", "+919654321098", "senior", 1, None),
        (5, "Prof. Radhakrishnan (Admin)", "admin@college.edu", default_pw, "Dean of Student Affairs", "Faculty / Admin", "Admin Block, Room 102", "+919543210987", "admin", 1, None)
    ]
    cursor.executemany("""
    INSERT INTO users (id, name, email, password_hash, department, year, hostel, phone, role, is_verified, verification_code)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, users)

    # Seed Products
    products = [
        (
            1, 1, "Casio fx-991ES Plus Scientific Calculator (2nd Gen)",
            "Calculators", 800.0, 1500.0, "Like New",
            "Barely used for S1 & S2 Engineering Mathematics and Physics. Comes with original protective slide-on hard case. All 417 functions working perfectly, solar cell active with fresh battery backup.",
            "/static/images/sample/casio_calc.svg",
            "Computer Science & Engineering", "Men's Hostel Block B (Room 214)", "available", 48,
            (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
        ),
        (
            2, 3, "Omega Deluxe Mini Drafter with Steel Rods & Canvas Bag",
            "Mini Drafters", 600.0, 1250.0, "Good",
            "Essential for First Year Engineering Graphics (EG/ED). Zero slippage brass clamp, smooth 360-degree protractor arm, clear 1:1 metric scales. Includes heavy-duty waterproof canvas carry cover.",
            "/static/images/sample/mini_drafter.svg",
            "Mechanical Engineering", "Men's Hostel Block A (Room 302)", "available", 65,
            (datetime.now() - timedelta(days=4)).strftime("%Y-%m-%d %H:%M:%S")
        ),
        (
            3, 4, "Standard Wooden Engineering Drawing Board (Imperial D2 Size)",
            "Drawing Boards", 700.0, 1400.0, "Good",
            "High-grade pine wood drawing board (800 x 600 mm) with straight ebony edge for mini-drafter clamping. Well seasoned, smooth surface with no warping or splits.",
            "/static/images/sample/drawing_board.svg",
            "Civil Engineering", "Women's Hostel Block B (Room 205)", "available", 39,
            (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d %H:%M:%S")
        ),
        (
            4, 1, "Complete Engineering Drawing Instrument Kit",
            "Drawing Kits", 400.0, 850.0, "Like New",
            "Includes heavy brass master bow compass, lengthening bar, divider, set squares (45° and 60°), French curves, roller scale (30cm), and clutch pencil with 0.5mm 2H/HB lead boxes.",
            "/static/images/sample/drawing_kit.svg",
            "Computer Science & Engineering", "Men's Hostel Block B (Room 214)", "available", 52,
            (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
        ),
        (
            5, 1, "Higher Engineering Mathematics - B.S. Grewal (44th Edition)",
            "Textbooks", 350.0, 899.0, "Good",
            "The standard prescribed textbook for S1 Linear Algebra & Calculus and S2 Vector Calculus & Differential Equations. Crisp pages with neat pencil highlights on key theorem proofs.",
            "/static/images/sample/math_book.svg",
            "Computer Science & Engineering", "Men's Hostel Block B (Room 214)", "available", 74,
            (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S")
        ),
        (
            6, 3, "Engineering Graphics - N.D. Bhatt (with 3D Projection Sheets)",
            "Reference Books", 250.0, 650.0, "Fair",
            "Comprehensive reference book for isometric views, orthographic projections, and sectioning of solids. Covers the entire first-year university syllabus with step-by-step solved problems.",
            "/static/images/sample/graphics_book.svg",
            "Mechanical Engineering", "Men's Hostel Block A (Room 302)", "available", 41,
            (datetime.now() - timedelta(days=6)).strftime("%Y-%m-%d %H:%M:%S")
        ),
        (
            7, 4, "Basic Electrical & Electronics Engineering (B.L. Theraja combo)",
            "Textbooks", 450.0, 1100.0, "Good",
            "Prescribed for common first-year BEE course. Clean condition without torn pages. Includes circuit analysis solved question papers from past 5 years.",
            "/static/images/sample/electronics_book.svg",
            "Civil Engineering", "Women's Hostel Block B (Room 205)", "available", 29,
            (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
        ),
        (
            8, 3, "Engineering Mechanics - S. Timoshenko & D.H. Young",
            "Reference Books", 300.0, 750.0, "Good",
            "Standard textbook for Statics and Dynamics in S1/S2. Excellent condition, spine intact.",
            "/static/images/sample/mechanics_book.svg",
            "Mechanical Engineering", "Men's Hostel Block A (Room 302)", "sold", 88,
            (datetime.now() - timedelta(days=12)).strftime("%Y-%m-%d %H:%M:%S")
        )
    ]

    cursor.executemany("""
    INSERT INTO products (id, seller_id, name, category, price, original_price, condition, description, image_url, department, location, status, views, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, products)

    # Seed a sample reservation
    cursor.execute("""
    INSERT INTO reservations (id, product_id, buyer_id, status, note, created_at)
    VALUES (1, 8, 2, 'completed', 'Collected at MH Main Gate on Friday evening.', ?)
    """, ((datetime.now() - timedelta(days=10)).strftime("%Y-%m-%d %H:%M:%S"),))

    # Seed a sample report for moderation testing
    cursor.execute("""
    INSERT INTO reports (id, product_id, reporter_id, reason, status, created_at)
    VALUES (1, 6, 2, 'Price description has a small typo, but seller fixed it quickly', 'resolved', ?)
    """, ((datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),))

    conn.commit()

if __name__ == "__main__":
    init_db()
    print("Database initialized and seeded successfully.")
