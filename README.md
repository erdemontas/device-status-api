# Installation

Open terminal in your computer and clone project:

```
1) Clone Project
git clone https://github.com/erdemontas/device-status-api.git
cd device-status-api

2) Install virtual environment 
python -m venv env

3) Activate virtual environment
on Mac OS or Linux --> source env/bin/activate
on Windows --> .\env\Scripts\activate.bat

4) Install requirements
pip install -r  requirements.txt

5) Create Super user
python3 manage.py createsuperuser

6) Make migrations
python manage.py makemigrations
python manage.py migrate

7) Run the server
python manage.py runserver

8) Open in browser
localhost:8000

```

# API-Documentation
API Endpoints can be seen in Swagger implemantation.
localhost:8000