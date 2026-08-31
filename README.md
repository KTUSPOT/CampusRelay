# CampusKit 🎓

### Senior-to-Junior Engineering Essentials Marketplace

CampusKit is a **college-specific resale marketplace** designed to help senior students sell unused first-year engineering essentials to junior students at affordable prices.

Instead of buying items like calculators, mini drafters, drawing kits, and textbooks at full price, juniors can find reusable items from seniors within their own campus.

> **Pass it down. Save money. Reduce waste.**

---

## 🚨 Problem

First-year engineering students often need to purchase items such as:

* Scientific calculators
* Mini drafters
* Drawing boards
* Engineering drawing kits
* Textbooks and reference books

Many of these items are used mainly during the first year and are rarely needed afterward.

This creates two problems:

* **Juniors** spend a significant amount of money purchasing new items.
* **Seniors** are left with unused items that occupy space in hostels or homes.

Existing platforms such as general classifieds are not optimized for small, trusted, **college-to-college transactions**.

---

## 💡 Solution

CampusKit provides a **closed, hyper-local marketplace for students within a college**.

### Seniors can:

* List unused engineering items
* Upload product photos
* Set a resale price
* Add product condition and description
* Provide a campus pickup location
* Receive inquiries through WhatsApp
* Mark items as sold

### Juniors can:

* Browse available items
* Search for required products
* View product details
* Compare original and resale prices
* See potential savings
* Contact sellers through WhatsApp
* Arrange campus pickup

---

## ✨ Features

### 🔐 Student Authentication

Students can create accounts and log in using their college information.

### 🛍️ Marketplace

Browse available engineering essentials listed by other students.

### 🔎 Search

Search for items such as:

```text
Calculator
Mini Drafter
Drawing Kit
Engineering Mathematics
```

### 🏷️ Categories

* Calculators
* Mini Drafters
* Drawing Boards
* Drawing Kits
* Textbooks
* Reference Books
* Other

### ➕ Sell an Item

Seniors can create a listing with:

* Product name
* Category
* Selling price
* Original price
* Condition
* Description
* Product image
* Hostel/location
* WhatsApp number

### 📄 Product Details

View complete information about a product, including its condition, price, seller information, and pickup location.

### 💬 WhatsApp Contact

Instead of building a separate chat system, buyers can directly contact sellers through WhatsApp.

### 📍 Campus Pickup

No delivery system is required. Buyers and sellers can arrange a meeting point within the campus.

### 💰 Savings Calculator

The application calculates the amount saved by purchasing a used item.

```text
Savings = Original Price - Resale Price
```

Example:

```text
Original Price : ₹1,500
Resale Price   : ₹800

You Save       : ₹700
```

### 📦 Listing Management

Sellers can:

* View their listings
* Edit listings
* Delete listings
* Mark items as sold

---

# 🔄 How It Works

## Seller

```text
Register / Login
       ↓
Sell an Item
       ↓
Add Product Details
       ↓
Upload Photo
       ↓
Set Price
       ↓
Publish Listing
       ↓
Receive Buyer Inquiry
       ↓
Meet on Campus
       ↓
Mark as Sold
```

## Buyer

```text
Register / Login
       ↓
Browse Marketplace
       ↓
Search for Item
       ↓
View Product
       ↓
Check Price & Savings
       ↓
Contact Seller
       ↓
Meet on Campus
       ↓
Purchase
```

---

# 🖥️ Application Pages

```text
/login              → Student Login
/register           → Student Registration
/marketplace        → Browse Products
/product/:id        → Product Details
/sell               → Create Listing
/dashboard          → Manage Listings
/profile            → User Profile
```

---

# 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

### Backend

* Python
* Flask

### Database

* SQLite

### Integration

* WhatsApp

### Development

* Git
* GitHub
* VS Code

---

# 🗄️ Database Design

## User

| Field        | Description      |
| ------------ | ---------------- |
| `id`         | Unique user ID   |
| `name`       | Student name     |
| `email`      | College email    |
| `password`   | Account password |
| `department` | Department       |
| `year`       | Current year     |
| `phone`      | WhatsApp number  |

## Product

| Field            | Description            |
| ---------------- | ---------------------- |
| `id`             | Unique product ID      |
| `seller_id`      | Seller's user ID       |
| `name`           | Product name           |
| `category`       | Product category       |
| `price`          | Resale price           |
| `original_price` | Original price         |
| `condition`      | Product condition      |
| `description`    | Product description    |
| `image`          | Product image          |
| `location`       | Campus/hostel location |
| `status`         | Available/Sold         |
| `created_at`     | Listing date           |

---

# 📁 Project Structure

```text
CampusKit/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── auth.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── marketplace.html
│   │   ├── product.html
│   │   ├── sell.html
│   │   ├── dashboard.html
│   │   └── profile.html
│   │
│   └── static/
│       ├── css/
│       ├── js/
│       └── uploads/
│
├── instance/
│   └── campuskit.db
│
├── requirements.txt
├── config.py
├── run.py
└── README.md
```

---

# 🚀 Installation & Setup

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd CampusKit
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Variables

Create a `.env` file if required:

```env
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///campuskit.db
```

> Do not upload `.env` or other sensitive credentials to GitHub.

## 5. Run the Application

```bash
python run.py
```

Open the local URL shown in the terminal.

---

# 🎯 MVP Scope

CampusKit intentionally focuses on the smallest set of features required to validate the idea.

### Included

* Student login/registration
* Product listing
* Marketplace
* Search
* Product details
* WhatsApp contact
* Campus pickup
* Seller dashboard
* Mark as sold

### Currently Out of Scope

* Online payments
* Delivery
* In-app messaging
* Ratings and reviews
* Push notifications
* AI recommendations
* Multi-college marketplace

These features can be introduced after validating the initial concept.

---

# 📊 MVP Validation

The primary objective is to determine whether students actually use the platform.

### Initial Pilot

```text
20 Seniors
    ↓
10 Product Listings
    ↓
30 Junior Users
    ↓
10 Seller Contacts
    ↓
5 Successful Transactions
```

The number of successful senior-to-junior transactions is the most important validation metric.

---

# 🔮 Future Scope

### Version 2

* Product reservation
* Ratings and reviews
* Notifications
* Advanced filters
* Seller profiles
* Admin dashboard

### Version 3

* Online payments
* In-app chat
* Digital receipts
* AI-based recommendations
* Marketplace analytics
* Multi-college support

---

# 🌱 Impact

CampusKit aims to:

* 💰 Reduce expenses for junior students
* ♻️ Encourage reuse of engineering resources
* 📦 Reduce unused items stored by seniors
* 🤝 Connect students across academic batches
* 🏫 Create a trusted campus-level marketplace

---

# 👥 Target Users

### Primary Users

* First-year engineering students
* Senior engineering students

### Initial Deployment

The MVP is intended to be tested within **one college campus** before expanding to multiple colleges.

---

# 📌 Project Status

**Status:** MVP / Prototype

CampusKit is currently focused on validating the core senior-to-junior resale workflow within a college environment.

---

# 👨‍💻 Contributors

Add your project team members here:

* **Your Name** — Developer
* **Team Member 2** — Developer
* **Team Member 3** — Developer
* **Team Member 4** — Developer

---

# 📄 License

This project is developed for educational and prototype purposes.
