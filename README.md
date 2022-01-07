====================
SET UP INITIALS

1- create virtual environment
   $ pip install virtualenv
   $ virtualenv -m venv env
   $ source env/Scripts/Activate
2. instal django 
	 $ pip install django or pip install django==3.0.7 (version)
  
3. Install the project depedencies:
   $ pip install -r requirements.txt

4. Then run 
   $ python manage.py migrate
   $ python manage.py makemigrations
   $ python manage.py migrate
   $ python manage.py runserver
