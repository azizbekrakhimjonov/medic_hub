birinchi python virtual muhid ni yaratib olamiz

```commandline
python -m venv venv
```

kerakli kutubhonalarni o`rnatamiz
```commandline
pip install -r requirements.txt
```

barcha kutubhonalarni req ga tashlab qoyamiz
```commandline
pip freeze > requirements.txt
```

```bash
django-admin startproject root .
```

```commandline
python manage.py migrate
```

```commandline
python manage.py runserver
```

```commandline
django-admin startapp medic
```