import unittest
import json
import os
import sqlite3
from app import app
import database
import models

class CampusKitTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()
        with app.app_context():
            database.init_db()

    def test_01_landing_page(self):
        """Test landing page renders with branding, stats, and how-it-works"""
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        content = res.get_data(as_text=True)
        self.assertIn("CampusKit", content)
        self.assertIn("Pass it down. Save money. Reduce waste.", content)
        self.assertIn("Browse Items", content)
        self.assertIn("Sell an Item", content)
        self.assertIn("How It Works", content)

    def test_02_marketplace_browse_and_filter(self):
        """Test marketplace listing, searching, and filtering"""
        # All items
        res = self.client.get('/marketplace')
        self.assertEqual(res.status_code, 200)
        content = res.get_data(as_text=True)
        self.assertIn("Casio fx-991ES Plus", content)
        self.assertIn("Omega Deluxe Mini Drafter", content)

        # Search filter
        res = self.client.get('/marketplace?search=Casio')
        self.assertEqual(res.status_code, 200)
        content = res.get_data(as_text=True)
        self.assertIn("Casio fx-991ES Plus", content)

        # Category filter
        res = self.client.get('/marketplace?category=Mini%20Drafters')
        self.assertEqual(res.status_code, 200)
        content = res.get_data(as_text=True)
        self.assertIn("Omega Deluxe Mini Drafter", content)

    def test_03_product_details_and_savings(self):
        """Test product details page has savings calculator and pickup info"""
        res = self.client.get('/product/1')
        self.assertEqual(res.status_code, 200)
        content = res.get_data(as_text=True)
        self.assertIn("Casio fx-991ES Plus", content)
        self.assertIn("You save ₹700", content)
        self.assertIn("Campus Pickup Meeting Location", content)
        self.assertIn("Contact Seller on WhatsApp", content)
        self.assertIn("Reserve Item", content)

    def test_04_seller_flow_create_listing(self):
        """Test senior seller creates a new listing"""
        # 1. Login as Senior
        self.client.post('/api/demo-login/senior')
        
        # 2. Post new listing
        res = self.client.post('/sell', data={
            'name': 'Rotring Rapid Pro Engineering Clutch Pencil Kit',
            'category': 'Drawing Kits',
            'condition': 'Like New',
            'price': '350',
            'original_price': '800',
            'description': '0.5mm metal barrel clutch pencil with 2B and 2H lead boxes. Perfect for EG sheets.',
            'location': 'Men\'s Hostel Block B, Room 214',
            'phone': '+919876543210',
            'department': 'Computer Science & Engineering',
            'image_preset': '/static/images/sample/drawing_kit.svg'
        }, follow_redirects=True)
        
        self.assertEqual(res.status_code, 200)
        content = res.get_data(as_text=True)
        self.assertIn("Rotring Rapid Pro", content)

        # Verify listing in marketplace
        res_m = self.client.get('/marketplace?search=Rotring')
        self.assertIn("Rotring Rapid Pro", res_m.get_data(as_text=True))

    def test_05_buyer_flow_reservation_and_status(self):
        """Test junior buyer reserves an item and seller marks as sold"""
        # 1. Login as Junior
        self.client.post('/api/demo-login/junior')

        # 2. Reserve product 4 (Complete Engineering Drawing Kit)
        res = self.client.post('/api/products/4/reserve', 
                               data=json.dumps({'note': 'Hey senior! Can I collect this today at MH gate?'}),
                               content_type='application/json')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(data['success'])

        # 3. Verify status changed to reserved
        prod = models.get_product_by_id(4)
        self.assertEqual(prod['status'], 'reserved')

        # 4. Check profile shows reserved item
        res_prof = self.client.get('/profile')
        self.assertIn("Complete Engineering Drawing Instrument Kit", res_prof.get_data(as_text=True))

        # 5. Switch to Senior and mark as sold
        self.client.post('/api/demo-login/senior')
        res_status = self.client.post('/api/products/4/status',
                                      data=json.dumps({'status': 'sold'}),
                                      content_type='application/json')
        self.assertEqual(res_status.status_code, 200)
        prod_updated = models.get_product_by_id(4)
        self.assertEqual(prod_updated['status'], 'sold')

    def test_06_admin_dashboard(self):
        """Test admin dashboard statistics and moderation"""
        self.client.post('/api/demo-login/admin')
        res = self.client.get('/admin')
        self.assertEqual(res.status_code, 200)
        content = res.get_data(as_text=True)
        self.assertIn("Admin &amp; Campus Moderation", content)
        self.assertIn("Total Students", content)
        self.assertIn("Total Savings", content)
        self.assertIn("Registered College Students", content)

    def test_07_api_products_json(self):
        """Test REST API products endpoint"""
        res = self.client.get('/api/products?category=Calculators')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['products']) > 0)
        self.assertEqual(data['products'][0]['category'], 'Calculators')

if __name__ == '__main__':
    unittest.main()
