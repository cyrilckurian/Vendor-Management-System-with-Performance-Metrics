# Vendor Management System with Performance Metrics

This is a Django-based Vendor Management System (VMS) with performance metrics tracking. It allows users to manage vendors, purchase orders, and track performance metrics such as on-time delivery rate, quality rating average, average response time, and fulfillment rate.

## Setup

### Prerequisites
- Python (>=3.6)
- Django (>=3.0)
- Django REST Framework (>=3.11)
- SQLite or any other compatible database

### Installation

1. Clone the repository:

	```bash
	git clone <repository_url>
	```

2. Navigate to the project directory:
   
	```bash
	cd Vendor-Management-System-with-Performance-Metrics
	```
3. Install dependencies:

	```bash
	pip install -r requirements.txt
	```

4. Apply database migrations:
	```bash
	python manage.py migrate
	```

## Running the Server
- ### Start the Django development server:

	```bash
	python manage.py runserver
	```

### The server should now be running at http://localhost:8000.

## Running Tests
- ### To run the test suite:

	```bash
	python manage.py test
	```

### This will execute all the tests and display the results.

## API Endpoints
### Vendors
1. POST /api/vendors/: Create a new vendor.
2. GET /api/vendors/: Retrieve all vendors.
3. GET /api/vendors/{vendor_id}/: Retrieve details of a specific vendor.
4. PUT /api/vendors/{vendor_id}/: Update details of a specific vendor.
5. DELETE /api/vendors/{vendor_id}/: Delete a specific vendor.
### Purchase Orders
1. POST /api/purchase_orders/: Create a new purchase order.
2. GET /api/purchase_orders/: Retrieve all purchase orders.
3. GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
4. PUT /api/purchase_orders/{po_id}/: Update details of a specific purchase order.
5. DELETE /api/purchase_orders/{po_id}/: Delete a specific purchase order.
### Acknowledge a purchase order
- PUT /api/purchase_orders/{po_id}/acknowledge/: Acknowledge a purchase order.
### Performance Metrics
- GET /api/vendors/{vendor_id}/performance/: Retrieve performance metrics for a specific vendor.

Thank you for checking out this project! If you have any questions, feedback, or suggestions, feel free to reach out. Happy coding!✌️