# Jagrati
Jagrati is an initiative by the students of IIITDM Jabalpur to provide free and quality education to the poor and under-privileged children of villages surrounding our institute


**Frontend:** HTML, CSS(+ Bootstrap 4), JavaScript  
**Backend:** Python/Django  
**Database:** SQLite3 

# Setup
* Download and Install Python 3.6
* Download and Install Django 2.2.13
* Download and Install Git
* Fork the Repository
* Clone the Repository to your local machine, `$ git clone https://github.com/<your-github-username>/Jagrati.git`
* Change the directory to Jagrati, `$ cd Jagrati`
* Install virtualenv `$ pip install virtualenv`
* Create a virtual environment `$ virtualenv env`  
* Activate the env: `env\Scripts\activate`
* Install the requirements: `$ pip install -r requirements.txt`
* Make migrations `$ py manage.py makemigrations`
* Migrate the changes to the database `$ py manage.py migrate`
* Create admin Using `$ py manage.py createsuperuser`
* Run the server `$ py manage.py runserver`
* Go to `127.0.0.1:8000`
