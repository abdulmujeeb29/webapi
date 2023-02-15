# Technology used in creating the web api:

**-Django Rest framework**:
_Django REST framework (DRF) is a powerful and flexible toolkit for building Web APIs. Its main benefit is that it makes serialization much easier.
_

# Setting up the project on local pc:

***You will need to have a version of python 3 installed globally on your system  or probably in your virtual environment 
check this by using the following command:***

```python --version```


### 1. First let's clone the repo , open your terminal and  navigate to the directory you wish to store the project and run the following command below :

`git clone https://github.com/abdulmujeeb29/webapi.git`

### 2. Once you've cloned the repository, navigate into the repository.

### 3. Create a virtual environment in the repo and activate it using the following commands:

```pipenv install django``` this command creates a virtual environment and install django in it  
```pipenv shell```  then run this command to activate the virtual environment 

### 4. Once you've activated your virtual environment install your python packages used in the project by running:

```
pip install -r requirements.txt
```

### 5. Now let's create our database :
-In creating our databases we've got two choices ,we could easily just  use the default database that comes with django which is SQLITE 0r rather connect it to mysql server .

>In settings.py file navigate to the option where you see databases then cut anything you see there and paste the below command if you wish to use sqlite:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

> And if you wish to connect to mysql server ,cut anything you see in the database section and paste :
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'NAME_OF_DATABASE',
        'USER': 'USER',
        'PASSWORD': 'PASSWORD',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
```

***note:MYsql server needs to be installed.***

### 6. NOW LET'S MIGRATE OUR DATABASE :

```
python manage.py makemigratations
```
```
python manage.py migrate
```

### 7. Generate a secret key :

Every Django project has a unique secret key. Usually, the secret key is not exposed online. It is always in an env file which is included in a .gitignore file to exclude from the repository.

You have to generate a new one for your project to run. Create a new secret key with a secret key generator, like [Djecrety]( https://djecrety.ir/).

 SECURITY WARNING: keep the secret key used in production secret!
> SECRET_KEY = 'secret-key-comes-here'

then you copy and paste the declared secret key above and paste in the settings.py file 


If there are no hitches here you should now be able to open your server by running:
```
python manage.py runserver
```
Quick and painless. 

# TESTING THE API:

In posting  a data to the database , run
```
http://127.0.0.1:8000/post
```
on your browser and to get the data being posted and stored in the database run
```
http://127.0.0.1:8000/get
```
