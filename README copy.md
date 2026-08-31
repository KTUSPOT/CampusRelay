# 🎓 CampusKit — Senior-to-Junior Engineering Resale Marketplace

> **"Pass it down. Save money. Reduce waste."**

CampusKit is a hyper-local, college-specific peer-to-peer resale marketplace built for engineering campuses. It connects seniors who no longer need first-year equipment (Mini Drafters, Drawing Boards, Drawing Kits, Casio fx-991 Calculators, and S1/S2 Engineering Textbooks) directly with incoming juniors within the same campus.

---

## 🚀 Key Features

1. **Clean College Startup Landing Page**:
   - Highlighting the campus dilemma (spending ₹6,000–₹9,000 on 2-semester items).
   - Real-time statistics: Items Listed, Items Sold, Students Helped, Total Money Saved.
   - 5-step visual workflow for zero-friction campus transactions.
   - S1/S2 bundle savings comparison calculator.

2. **Marketplace & Smart Search / Filters**:
   - Real-time search across equipment names and descriptions.
   - Filter by Category (Calculators, Mini Drafters, Drawing Boards, Drawing Kits, Textbooks, Reference Books, Other).
   - Filter by Condition (*Like New*, *Good*, *Fair*), Department, Hostel/Pickup location, and Max Price.
   - Sort by Newest, Price Low → High, Price High → Low, and Maximum Savings.

3. **Product Details & Savings Calculator**:
   - Automatic savings computation: `Savings = Original Price - Selling Price` with percentage discount badge (`You save ₹700 (47%)`).
   - Campus Pickup meeting card with location context (e.g. *Men's Hostel Block B*).
   - **Direct WhatsApp Deep Link**: Generates a context-aware message pre-filled with the item name, price, and campus meeting point.
   - **"Reserve Item"** workflow: Prevents double bookings and sends instant reservation notification to the senior.

4. **Seller Dashboard & Inventory Management**:
   - Manage active listings, reserved items, and sold items.
   - 1-click status transitions: `Available` ⇄ `Reserved` ⇄ `Sold`.
   - Track total earnings and buyer reservations inbox.

5. **Student Profile & Buyer History**:
   - View college credentials, department, year, and hostel room.
   - Track all reserved items with direct WhatsApp links to sellers.

6. **Admin Dashboard & Moderation**:
   - Platform-wide metrics: Total Students, Total Listings, Available Items, Sold Items, and Total Campus Savings.
   - User directory and listings moderation table.
   - Safety queue to review and remove reported listings.

7. **1-Click Reviewer Demo Account Switcher**:
   - Top navigation bar switcher allows instant testing as:
     - 👤 **Senior / Seller**: *Rahul Sharma (S4 CSE, Men's Hostel Block B)*
     - 👤 **Junior / Buyer**: *Ananya Iyer (S1 ECE, Women's Hostel Block A)*
     - 🛡️ **Admin**: *Prof. Radhakrishnan (Dean of Student Affairs)*

---

## 🛠️ Tech Stack & Architecture

- **Backend**: Python 3.13 / Flask 3.1
- **Database**: SQLite3 with clean relational schema (`users`, `products`, `reservations`, `reports`)
- **Frontend**: Responsive HTML5 + Tailwind CSS (via CDN) + Lucide Icons + Vanilla JavaScript
- **P2P Communication**: WhatsApp Web & Mobile deep links (`https://wa.me/<phone>?text=...`)
- **Zero Heavy Build Tooling**: Fast, instant startup without node/npm overhead.

---

## 💻 How to Run Locally

### Prerequisites
- Python 3.8+ (Python 3.13 installed)

### Quickstart

1. Navigate to the project directory:
   ```powershell
   cd C:\Users\Lenovo\.gemini\antigravity\scratch\campuskit
   ```

2. Start the web application:
   ```powershell
   python app.py
   ```

3. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

### Running Automated Tests
To run the automated test suite:
```powershell
python test_app.py
```

---

## 🧪 Validated User Flows

### 1. Senior / Seller Flow
1. Click **"Senior (Rahul)"** in the top demo switcher bar (or navigate to `/login` and click the senior demo button).
2. Click **"Sell an Item"** in the navigation bar.
3. Choose a fast template or enter item details (e.g. *Casio fx-991EX*, Price ₹1,100, Original ₹2,200).
4. Click **"Publish Listing"** ➔ The listing appears immediately on the Marketplace and Seller Dashboard.
5. In the Dashboard, toggle status to **"Sold"** once completed ➔ Dashboard stats and platform savings update dynamically.

### 2. Junior / Buyer Flow
1. Click **"Junior (Ananya)"** in the top demo bar.
2. Go to **"Marketplace"** ➔ Search for *"Mini Drafter"* or filter by *"Drawing Kits"*.
3. Click on a product card to open the **Product Details Page**.
4. View the savings calculation (*e.g. "You save ₹650 (52%)"*).
5. Click **"Reserve Item"** ➔ Adds the item to reservations and updates status to `Reserved`.
6. Click **"Contact Seller on WhatsApp"** ➔ Opens WhatsApp with the pre-formatted greeting message for campus pickup.

### 3. Admin / Moderation Flow
1. Click **"Admin (Prof. Nair)"** in the top bar.
2. Go to `/admin` ➔ View aggregate campus savings, registered students, and active listings.
3. Review reported items or delete inappropriate listings with 1-click.

---

## 🔮 Future Improvements
- **Real College SSO / OTP Email Verification**: Integration with college institutional Google Workspace / Microsoft 365 OAuth.
- **Interactive Campus Meeting Spot Selector**: Visual map of verified campus pickup zones (Library Foyer, Canteen, Student Center, Main Gate).
- **In-App QR Code Handover Confirmation**: Scan QR code on pickup to instantly transfer ownership and mark listing as sold.
