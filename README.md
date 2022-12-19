### To launch project 

Create venv:
```
python3 -m venv venv       
```

Activate it:
```
source venv/bin/activate 
```

Install all requirements:
```
pip install -r requirements.txt
```

Run migrations for the local db:
```
python manage.py migrate
```

Run server:
```
python manage.py runserver
```

API root available on http://127.0.0.1:8000/api/kms/
