from django.test import TestCase
from rest_framework.test import APIClient
from .models import Vendor, PurchaseOrder

class VendorAPITestCase(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.vendor_a = Vendor.objects.create(name="Vendor A", 
                                        contact_details="contact@example.com", 
                                        address="123 Main Street", 
                                        vendor_code="VNDRA")
		self.vendor_b = Vendor.objects.create(name="Vendor B", 
                                        contact_details="contact@example.com", 
                                        address="123 Second Street", 
                                        vendor_code="VNDRB")

	def test_create_vendor(self):
		response = self.client.post('/api/vendors/', 
                              {"name": "Vendor C", 
                               "contact_details": "contact3@example.com", 
                               "address": "084 Second Street", 
                               "vendor_code": "VWEWRR"})
		self.assertEqual(response.status_code, 201)

	def test_view_all_vendors(self): 
		response = self.client.get('/api/vendors/') 
		self.assertEqual(response.status_code, 200) 
		self.assertEqual(len(response.data), 2)  # There are two vendors in the database

	def test_view_vendor_details(self):
		response = self.client.get(f'/api/vendors/{self.vendor_a.id}/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data['name'], 'Vendor A')

	def test_update_vendor(self):
		response = self.client.put(f'/api/vendors/{self.vendor_a.id}/', 
                             {"name": "Updated Vendor A", 
                              "contact_details": "updated_contact@example.com", 
                              "address": "456 Updated Street", 
                              "vendor_code": "VNDRA_UPDATED"})
		self.assertEqual(response.status_code, 200)

	def test_view_vendor_performance(self):
		response = self.client.get(f'/api/vendors/{self.vendor_a.id}/performance/')
		self.assertEqual(response.status_code, 200)
		self.assertTrue('on_time_delivery_rate' in response.data)
		self.assertTrue('quality_rating_avg' in response.data)
		self.assertTrue('average_response_time' in response.data)
		self.assertTrue('fulfillment_rate' in response.data)

	def test_delete_vendor(self):
		response = self.client.delete(f'/api/vendors/{self.vendor_a.id}/')
		self.assertEqual(response.status_code, 204)



class PurchaseOrderAPITestCase(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.vendor = Vendor.objects.create(name="Vendor D", 
                                      contact_details="contact@example.com", 
                                      address="123 Main Street", 
                                      vendor_code="VUIYE")
		self.purchase_order_1 = PurchaseOrder.objects.create(po_number="PO123", vendor=self.vendor, order_date="2024-05-01T10:00:00", delivery_date="2024-05-10T10:00:00", items=[{"name": "Item 1", "quantity": 10}], quantity=10, status="pending", issue_date="2024-05-01T10:00:00")
		self.purchase_order_2 = PurchaseOrder.objects.create(po_number="PO456", vendor=self.vendor, order_date="2024-05-05T10:00:00", delivery_date="2024-05-15T10:00:00", items=[{"name": "Item 2", "quantity": 20}], quantity=20, status="pending", issue_date="2024-05-05T10:00:00")

	def test_create_purchase_order(self):
		response = self.client.post('/api/purchase_orders/', 
                              {
								"po_number": "PO789",
								"vendor": self.vendor.id,
								"order_date": "2024-05-01T10:00:00",
								"delivery_date": "2024-05-10T10:00:00",
								"items": '[{"name": "Item 3", "quantity": 60}]',
								"quantity": 60,
								"status": "pending",
								"issue_date": "2024-05-01T10:00:00"
								})
		self.assertEqual(response.status_code, 201)

	def test_view_all_purchase_orders(self):
		response = self.client.get('/api/purchase_orders/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.data), 2) # There are two purchase orders in the database
  
	def test_view_purchase_order_details(self):
		response = self.client.get(f'/api/purchase_orders/{self.purchase_order_1.id}/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data['po_number'], 'PO123')

	def test_update_purchase_order(self):
		response = self.client.put(f'/api/purchase_orders/{self.purchase_order_1.id}/', {"po_number": "PO123_UPDATED", 
                                                                  "vendor": self.vendor.id, 
                                                                  "order_date": "2024-05-02T10:00:00", 
                                                                  "delivery_date": "2024-05-11T10:00:00", 
                                                                  "items": '[{"name": "Item 1", "quantity": 15}]', 
                                                                  "quantity": 15, "status": "completed", 
                                                                  "issue_date": "2024-05-02T10:00:00"
                                                                  })
		self.assertEqual(response.status_code, 200)


    
	def test_acknowledge_purchase_order(self):
		response = self.client.put(f'/api/purchase_orders/{self.purchase_order_1.id}/acknowledge/')
		self.assertEqual(response.status_code, 200)

	def test_delete_purchase_order(self):
		response = self.client.delete(f'/api/purchase_orders/{self.purchase_order_1.id}/')
		self.assertEqual(response.status_code, 204)

	
	












































