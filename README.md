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
	git clone https://github.com/cyrilckurian/Vendor-Management-System-with-Performance-Metrics.git
	```

2. Navigate to the project directory:
   
	```bash
	cd Vendor-Management-System-with-Performance-Metrics
 	cd vendor_management_system
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
   
<img width="1169" alt="Screenshot 2024-05-04 at 8 59 23 AM" src="https://github.com/cyrilckurian/Vendor-Management-System-with-Performance-Metrics/assets/74858827/ed81b12a-4ea9-4e47-8526-bed8621af222">

<img width="1168" alt="Screenshot 2024-05-04 at 9 00 48 AM" src="https://github.com/cyrilckurian/Vendor-Management-System-with-Performance-Metrics/assets/74858827/5ca8b435-22c6-4d4c-aa0a-982dd1d03e66">

3. GET /api/vendors/: Retrieve all vendors.

<img width="1171" alt="Screenshot 2024-05-04 at 9 01 42 AM" src="https://github.com/cyrilckurian/Vendor-Management-System-with-Performance-Metrics/assets/74858827/fd1f5e29-24f7-4d8b-8a40-222716d4b789">

4. GET /api/vendors/{vendor_id}/: Retrieve details of a specific vendor.
   
<img width="1172" alt="Screenshot 2024-05-04 at 9 02 25 AM" src="https://github.com/cyrilckurian/Vendor-Management-System-with-Performance-Metrics/assets/74858827/95914a53-4b66-4c0d-b9a3-7ffc54e560c9">

6. PUT /api/vendors/{vendor_id}/: Update details of a specific vendor.

<img width="1170" alt="Screenshot 2024-05-04 at 9 03 01 AM" src="https://github.com/cyrilckurian/Vendor-Management-System-with-Performance-Metrics/assets/74858827/45475bb9-d749-4f4d-8afe-c947c3d7ca07">

7. DELETE /api/vendors/{vendor_id}/: Delete a specific vendor.

<img width="1171" alt="Screenshot 2024-05-04 at 9 03 39 AM" src="https://github.com/cyrilckurian/Vendor-Management-System-with-Performance-Metrics/assets/74858827/8378f142-fefe-46dd-af2b-ffc38ee21065">

Now only Vendor with id=1 is left

<img width="1171" alt="Screenshot 2024-05-04 at 9 03 56 AM" src="https://github.com/cyrilckurian/Vendor-Management-System-with-Performance-Metrics/assets/74858827/0bbd575c-f7a7-40d0-9521-d40e129f1d87">
 
### Purchase Orders
1. POST /api/purchase_orders/: Create a new purchase order.

<img width="1167" alt="Screenshot 2024-05-04 at 9 08 43 AM" src="https://github.com/cyrilckurian/Vendor-Management-System-with-Performance-Metrics/assets/74858827/1d551f3f-b39c-4ad5-8630-ee7861cd6e02">

<img width="1170" alt="Screenshot 2024-05-04 at 9 09 57 AM" src="https://github.com/cyrilckurian/Vendor-Management-System-with-Performance-Metrics/assets/74858827/b0901ba3-0378-49a2-8503-416afc636e95">

2. GET /api/purchase_orders/: Retrieve all purchase orders.

<img width="1164" alt="Screenshot 2024-05-04 at 9 10 21 AM" src="https://github.com/cyrilckurian/Vendor-Management-System-with-Performance-Metrics/assets/74858827/731dbfc7-df4e-4396-a91e-bfb0db3d6328">

3. GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.

<img width="1170" alt="Screenshot 2024-05-04 at 9 11 23 AM" src="https://github.com/cyrilckurian/Vendor-Management-System-with-Performance-Metrics/assets/74858827/f851dfc0-c8c0-45b5-86c3-cde329364f5e">

4. PUT /api/purchase_orders/{po_id}/: Update details of a specific purchase order.

<img width="1168" alt="Screenshot 2024-05-04 at 9 14 40 AM" src="https://github.com/cyrilckurian/Vendor-Management-System-with-Performance-Metrics/assets/74858827/cc4744df-e11f-4636-84b5-c507421d110c">

6. DELETE /api/purchase_orders/{po_id}/: Delete a specific purchase order.

<img width="1170" alt="Screenshot 2024-05-04 at 9 15 13 AM" src="https://github.com/cyrilckurian/Vendor-Management-System-with-Performance-Metrics/assets/74858827/4b0d95c0-ef3a-4352-b1cf-b7cde20b6825">

### Acknowledge a purchase order
- PUT /api/purchase_orders/{po_id}/acknowledge/: Acknowledge a purchase order.

<img width="1172" alt="Screenshot 2024-05-04 at 9 29 27 AM" src="https://github.com/cyrilckurian/Vendor-Management-System-with-Performance-Metrics/assets/74858827/8fb901fc-fc18-4167-aacf-ff4385f500ae">

<img width="1173" alt="Screenshot 2024-05-04 at 9 30 15 AM" src="https://github.com/cyrilckurian/Vendor-Management-System-with-Performance-Metrics/assets/74858827/0e904467-f7ae-45bd-b113-9f7e68059645">

<img width="1167" alt="Screenshot 2024-05-04 at 9 30 33 AM" src="https://github.com/cyrilckurian/Vendor-Management-System-with-Performance-Metrics/assets/74858827/52d38f79-eb13-41d3-8f3e-f5e522496895">

### Performance Metrics
- GET /api/vendors/{vendor_id}/performance/: Retrieve performance metrics for a specific vendor.

<img width="1169" alt="Screenshot 2024-05-04 at 9 28 07 AM" src="https://github.com/cyrilckurian/Vendor-Management-System-with-Performance-Metrics/assets/74858827/0faeee78-cd97-4aeb-9024-01e51e94ed0b">

Thank you for checking out this project! If you have any questions, feedback, or suggestions, feel free to reach out. Happy coding!✌️
