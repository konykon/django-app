# django-app

A Django web application that allows managing telecom service consumptions.  

The user can import csv files of products and product categories.  
Consumptions are available as a list filtered by the product categories and new ones can be created, edited or deleted.  

The Consumptions resource is also accessible through a REST API endpoint.  

The Application is made with:

* Python, Django & Django-REST-Framework
* Postgres, Tests

To start run: ```python manage.py runserver```

To access the Client visit: http://127.0.0.1:8000

To access the API Client visit: 

* http://127.0.0.1:8000/api/, to view consumptions list 
* http://127.0.0.1:8000/api/create/, to create a new consumption
* http://127.0.0.1:8000/api/<int:pk>/update/, to update a consumption
* http://127.0.0.1:8000/api/<int:pk>/delete/, to delete a consumption  
