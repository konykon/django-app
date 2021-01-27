# django-app

A Django web application that allows managing telecom service consumptions.  

The user can import csv files of products and product categories. Sample csv files are included in the repository.  

Consumptions are available as a list filtered by the product categories and new ones can be created, edited or deleted.  

The Consumptions resource is also accessible through a REST API endpoint.  

The Application is made with:

* Python, Django & Django-REST-Framework
* Postgres, Tests

Set up instructions:

1. Assuming you have postgres installed, create project database:
    ```
    sudo su - postgres  
    psql  
    CREATE DATABASE djangoapp;  
    CREATE USER coder WITH PASSWORD 'coderpwd';  
    \q  
    exit  
    ```

2. In the folder **django-app** make a virtualenv called myenv.  
    ```python3 -m venv myenv```

3. Activate virtual environment (include full path if required).  
    ```source djangoapp/myenv/bin/activate```

4. Install requirements of the project.  
    ```pip install -r requirements.txt```

5. Apply migrations.  
    ```python manage.py migrate```

6. Create admin account.  
    ```python manage.py createsuperuser```

7. To start run:  
    ```python manage.py runserver```

The database can be filled either from:  

    * http://127.0.0.1:8000/admin manually or  

    * using the upload sections of the interface and uploading the sample csv files  
      that are included in the project.  

To access the Client visit: http://127.0.0.1:8000/home  

To access the API Client visit: http://127.0.0.1:8000  
