# Kakcho Task

Developed in Django. 

**Features :**
````
* Task 1 : Create 2 sub csv files : paid.csv and free.csv
* Task 2 : Induvidual file for rating
* Task 3 : one updated csv file whihc has new column with roundoff ratings 
````
**Short Discription :**

On the home page you will have option to upload file.
Once you upload the file and submit it you will be redirected you to select.html
here you will have an option to select task. Whatever task you will select that task will be executed and related csv files will be created in media folder.

**How to run?**
(**pre-requisite**: **Python** and **Django** must be installed)

1. Go to the folder which contains **manage.py**

2. Install requirement.txt
```
pip install -r requirement.txt
```

3. Do migrations 
```
python manage.py makemigrations
```
```
python manage.py migrate
```

4. Run Project
```
python manage.py runserver
```
