# [CS 6440: Intro to Health Informatics](https://omscs.gatech.edu/cs-6440-intro-health-informatics) Project - Team#12 Connected Patient Experience


Some of the biggest complaints today by patients surround the disconnect that they feel between them and their practice, along with the inability to access their data easily. Patient portals were supposed to the be the solution, but by most accounts that has not proved to be the case. While a step forward in some regards, patient surveys still indicate a great disconnect in the patient experience. Furthermore, portals have sometimes proven to be too confusing for patients, or have just not provided enough longstanding value. As some studies have shown that while upwards of 83% have logged in and used portals before, only 25% of those patients would be inclined to use them again.
<br />

> Team Members
- **`Aijing Gao`**
- **`Shiyi Qin`**
- **`Baiyan Ren`**
- **`Yi Wang`**
- **`Haojie Yu`**
<br />

> Team Mentor
- **`Michael Romano`**
<br />

> Features
- `Data based on FHIR format` 
- `Web App using Flask framework integrated with Database`
- `DBMS`: MySQL
- `DB Tools`: SQLAlchemy ORM, Flask-Migrate (schema migrations)
- Session-Based authentication (via **flask_login**)
- `Deployment`: **HEROKU**
- `Up-to-date dependencies`
<br />

> Links

- 👉 [The patient portal are deployed via Heroku](https://arcane-beyond-54226.herokuapp.com/login) - Login page

   Example:

   Username: WeimEr1987 

   Password: 1234
<br />

## ✨ Quick Start in Local

> Get the code

```bash
$ git clone https://github.gatech.edu/gt-cs6440-hit-spring2022/Team-12-Connected-Patient-Experience.git

$ cd Team-12-Connected-Patient-Experience.git
```

> Set up the database
   - Download MySQL script file and data.zip file from database branch (directory)
   - Unzip data.zip into a folder called "data"
   - Put MySQL script file into "data" folder
   - If use MySQL Workbench:
      - Enable local_infile
```sql
SHOW GLOBAL VARIABLES LIKE 'local_infile';
SET GLOBAL local_infile = 'ON';
SHOW GLOBAL VARIABLES LIKE 'local_infile';
```
   - Run MySQL script file
   - Then the tables below will be created in a database called 'cs6440_sp22_team012'
   ```
      +-------------------------------+
      |     cs6440_sp22_team012       |
      +-------------------------------+
      | Appointments                  |
      | Careplans                     |
      | Conditions                    |
      | Encounters                    |
      | Medications                   |
      | Observations                  |
      | Organizations                 |
      | Patients                      |
      | Payers                        |
      | Procedures                    |
      | Providers                     |
      | Users                         |
      +-------------------------------+
   ```

> Set up the app
   - Set up the vitual environment
   ```bash
      $ # Virtualenv modules installation (Unix based systems)
      $ venv env
      $ source env/bin/activate

      $ # Virtualenv modules installation (Windows based systems)
      $ # virtualenv env
      $ # .\env\Scripts\activate
      $
      $ # Install modules - MySQL Database
      $ pip3 install -r requirements-mysql.txt
   ```
   - In apps/config.py, modify 'SQLALCHEMY_DATABASE_URI' according to your MySQL database parameters
      - In thie project, we have deployed our datebase on the Heroku addon element [**ClearDB**](https://elements.heroku.com/addons/cleardb) The username and password are shown below in the apps/config.py.
```python
class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_007')

   # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = 'mysql://b91a97472d5549:c040f67f@us-cdbr-east-05.cleardb.net/heroku_c5c9278b7226d63'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

```

> Run the app

```bash
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Start the application (development mode)
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$ # Access the dashboard in browser: http://127.0.0.1:5000/
```

Note: To use the app, please use the existing username and password. New registrions require the username link to unqiue patient's ID

<br />


## ✨ Deployment

The app has been developed in [Heroku](https://www.heroku.com/)
### [Heroku](https://www.heroku.com/)
---

Steps to deploy on **Heroku**

- [Install the Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) that match your OS: Mac, Unix or Windows
- Open a terminal window and authenticate via `heroku login` command
- Clone the sources and push the project for LIVE deployment

```bash
$ # Clone the source code:
$ git clone https://github.gatech.edu/gt-cs6440-hit-spring2022/Team-12-Connected-Patient-Experience.git
$ cd Team-12-Connected-Patient-Experience.git
$
$ heroku login
$ # this commaond will open a browser window - click the login button (in browser)
$
$ # Trigger the LIVE deploy
$ git push heroku updated_frontend:main
$
$ # Open the LIVE app in browser
$ heroku open
```
<br />

## ✨ Web app diagram
![diagram](/image/Flowchart.png)

## ✨ Code-base structure

The project is coded using blueprints, app factory pattern, dual configuration profile (development and production), and an intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- apps/
   |    |
   |    |-- home/                           # A simple app that serve HTML files
   |    |    |-- routes.py                  # Define app routes
   |    |
   |    |-- Appointment/                    # Handles Appointment
   |    |    |-- routes.py                  # Define appointment routes  
   |    |    |-- appointment.py             # Defines appointment models  
   |    |    |-- appointment_service.py     # Define appointment methods
   |    |
   |    |-- authentication/                 # Handles auth routes (login and register)
   |    |    |-- routes.py                  # Define authentication routes  
   |    |    |-- models.py                  # Defines models  
   |    |    |-- forms.py                   # Define auth forms (login and register) 
   |    |    |-- util.py
   |    |
   |    |-- Carplan/                        # Handles Carplans
   |    |    |-- routes.py                  # Define careplan routes  
   |    |    |-- careplan.py                # Defines careplan models  
   |    |    |-- careplan_service.py        # Define careplan methods 
   |    |
   |    |-- Condition/                      # Handles Conditions
   |    |    |-- routes.py                  # Define condition routes  
   |    |    |-- condition.py               # Defines condition models  
   |    |    |-- condition_service.py       # Define condition methods
   |    |
   |    |-- Encounter/                      # Handles Encounters
   |    |    |-- routes.py                  # Define encounter routes  
   |    |    |-- encounter.py               # Defines encounter models  
   |    |    |-- encounter_service.py       # Define encounter methods
   |    |
   |    |-- Medication/                     # Handles Medications
   |    |    |-- routes.py                  # Define medication routes  
   |    |    |-- medication.py              # Defines medication models  
   |    |    |-- medication_service.py      # Define medication methods 
   |    |
   |    |-- Observation/                    # Handles Observations
   |    |    |-- routes.py                  # Define observation routes  
   |    |    |-- observation.py             # Defines observation models  
   |    |    |-- observation_services.py    # Define observation methods 
   |    |
   |    |-- Patient/                        # Handles Patients
   |    |    |-- routes.py                  # Define patient routes  
   |    |    |-- patient.py                 # Defines patient models  
   |    |    |-- patient_service.py         # Define patient methods
   |    |    |-- patitentform.py            # Define patient forms
   |    |
   |    |-- Payer/                          # Handles Payers
   |    |    |-- routes.py                  # Define payer routes  
   |    |    |-- payer.py                   # Defines payer models  
   |    |    |-- payer_services.py          # Define payer methods
   |    |
   |    |-- Procedure/                      # Handles Procedures
   |    |    |-- routes.py                  # Define procedure routes  
   |    |    |-- procedure.py               # Defines procedure models  
   |    |    |-- procedure_services.py      # Define procedure methods 
   |    |
   |    |-- Provider/                       # Handles Provider
   |    |    |-- routes.py                  # Define provider routes  
   |    |    |-- provider.py                # Defines provider models  
   |    |    |-- provider_services.py       # Define provider methods 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>          # CSS files, Javascripts files
   |    |
   |    |-- templates/                      # Templates used to render pages
   |    |    |-- includes/                  # HTML chunks and components
   |    |    |    |-- navigation.html       # Top menu component
   |    |    |    |-- sidebar.html          # Sidebar component
   |    |    |    |-- footer.html           # App Footer
   |    |    |    |-- scripts.html          # Scripts common to all pages
   |    |    |
   |    |    |-- layouts/                   # Master pages
   |    |    |    |-- base-fullscreen.html  # Used by Authentication pages
   |    |    |    |-- base.html             # Used by common pages
   |    |    |
   |    |    |-- accounts/                  # Authentication pages
   |    |    |    |-- login.html            # Login page
   |    |    |    |-- register.html         # Register page
   |    |    |
   |    |    |-- home/                      # UI Kit Pages
   |    |         |-- index.html            # Index page
   |    |         |-- 404-page.html         # 404 page
   |    |         |-- *.html                # All other pages
   |    |    
   |  config.py                             # Set up the app
   |    __init__.py                         # Initialize the app
   |
   |-- requirements.txt                     # Development modules
   |-- requirements-mysql.txt               # Production modules  - Mysql DMBS
   |
   |-- Procfile                             # Heroku Deployment   
   |-- nginx                                # Deployment
   |    |-- appseed-app.conf                # Deployment 
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- run.py                               # Start the app - WSGI gateway
   |
   |-- ************************************************************************
```

<br />

## ✨ Web App Interfaces

![Login](/pictures/login.png)
![Dashboard](/pictures/dashboard.png)
![calendar](/pictures/calendar.png)
![profile](/pictures/profile.png)
![Medications](/pictures/medications.png)

## ✨ Credits & Links

- [Flask Framework](https://www.palletsprojects.com/p/flask/) - The offcial website
- [Boilerplate Code](https://appseed.us/boilerplate-code) - Index provided by **AppSeed**
- [Boilerplate Code](https://github.com/app-generator/boilerplate-code) - Index published on Github

<br />

---
CS6640 Team 12 Group Project - 2022 Spring
