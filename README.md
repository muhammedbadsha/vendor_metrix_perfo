<h1 align="center">Vendor Metrix</h1>

<p align="left"> Develop a Vendor Management System using Django and Django REST Framework. This
system will handle vendor profiles, track purchase orders, and calculate vendor performance
metrics.</p>

<h4>Core Features

</h4>
<h3>1. Vendor Profile Management:</h3>
● Model Design: Create a model to store vendor information including name, contact
details, address, and a unique vendor code.
● API Endpoints:
● POST /api/: Create a new vendor.
● GET /api/: List all vendors.
● GET /api/{vendor_id}/: Retrieve a specific vendor's details.
● PUT /api/{vendor_id}/: Update a vendor's details.
● DELETE /api/{vendor_id}/: Delete a vendor.

<h3> 2. Purchase Order Tracking: </h3>
● Model Design: Track purchase orders with fields like PO number, vendor reference,
order date, items, quantity, and status.
● API Endpoints:
● POST /product_order/orders/: Create a purchase order.
● GET /product_order/orders/: List all purchase orders with an option to filter by
vendor.
● GET /product_order/orders/<int:pk>/: Retrieve details of a specific purchase order.
● PUT /product_order/orders/<int:pk>/: Update a purchase order.
● DELETE /product_order/orders/<int:pk>/: Delete a purchase order.


<h3 align="left">3. Vendor Performance Evaluation:</h3>
● Metrics:
● On-Time Delivery Rate: Percentage of orders delivered by the promised date.
● Quality Rating: Average of quality ratings given to a vendor’s purchase orders.
● Response Time: Average time taken by a vendor to acknowledge or respond to
purchase orders.
● Fulfilment Rate: Percentage of purchase orders fulfilled without issues.
● Model Design: Add fields to the vendor model to store these performance metrics.
● API Endpoints:
● GET /history/performance-records/<int:pk>/performance: Retrieve a vendor's performance
metrics.

<h2>Iniitalize Git</h2>
git clone https://github.com/muhammedbadsha/vendor_metrix_perfo.git
cd vendor_metrix_perfo

##do this :
$ pip install -r requirements.txt
$ python manage.py migrate

##OR

$ docker build -t django-markdown-editor .
$ docker run -it -p 8000:8000 \
     -e DJANGO_SUPERUSER_USERNAME=admin \
     -e DJANGO_SUPERUSER_PASSWORD=sekret1 \
     -e DJANGO_SUPERUSER_EMAIL=admin@example.com \
     django-markdown-editor
<p>If you have any doubt please reffer this site</p> <a href="https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application">Click Link </a>
