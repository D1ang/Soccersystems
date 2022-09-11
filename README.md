# Soccersystems
**sports ordersystem**

For Amsterdams biggest soccerteam (Ajax) a need for an order system has been requested.
The main goal of the system is to make the job of shop employees easier and more efficient.
For the customer we would like to provide an easy to understand and easy to use system so,
they will be able to make their production requests easier.

In short:
 - A system for Ajax shop employees to be more efficient.
 - An easy to understand system on B2B basis to remove some workload from the employees on both sides.
 - A way to see the holding stocks of the producer and shops.

![Design](https://github.com/D1ang/Soccersystems/blob/main/mockups/presentation.png)

## Table of Contents
  * [UX](#ux)
  * [User stories](#user-stories)
    + [Strategy](#strategy)
    + [Scope](#scope)
    + [Structure](#structure)
    + [Skeleton](#skeleton)
    + [Surface](#surface)
  * [Technologies](#technologies)
    + [JavaScript Libraries](#javascript-libraries)
    + [Python & Django Plugins](#python---django-plugins)
  * [Features](#features)
    + [Features Left to Implement](#features-left-to-implement)
  * [Testing](#testing)
  * [Bugs](#bugs)
    + [CSS](#css)
    + [JavaScript](#javascript)
    + [Admin login gave a 500 error](#admin-login-gave-a-500-error)
  * [Deployment](#deployment)
    + [Deploy requirements](#deploy-requirements)
    + [Local deployment](#local-deployment)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
    + [Acknowledgements](#acknowledgements)

## UX
To make the system as clear as possible to the end-user, a basic but very clean design has been chosen.
Options are minimalistic and the end-user will not be overloaded with options to choose from.
The navigation bar, buttons, cart system and dashboard have been built and have an easy to understand logic.

## User stories
With years of field experience, we have built a well-known form and work ethic in creating designs.
We asked our customers from day to day what they would like to see in a sample and came up with the following points:

 - As a user, I want to easily fill in the forms for a order request (services)
 - As a user, I want a secured overview of my order history (dashboard)
 - As a user, I want the system to remember my cart, for if I want to make changes later (cart)
 - As a user, I do not want to fill in my details every time, but do want to change them if needed (profile)
 - As an employee, I want to know which items are required per order (order)
 - As an employee, I want to change the status of an order (admin list actions)
 - As an employee, I want to search and filter the orders (search & filter)

### Strategy
The goal of the system is to make it as easy as possible to access, short and informative, 
while striving for a minimalist and user-friendly design.

### Scope
For Ajax, we wanted to provide them with an easy to understand (first-view-use) system.
This way, they would be able to request orders: faster, easier and on their own, 
so our employees have more free time for other job-related tasks and be able to do
their other tasks more efficient.

### Structure
The system is structured to get the right information as quickly as possible.
The order of the options provided are placed in a logic workflow while the design provided will use a messages bar
that should be easy to understand and gives the customer a straight away no-nonsense feedback.
The navbar is available when needed and a footer is provided with contact-information below the page.

### Skeleton
The design is based on earlier project.
By using LucidChart the following model was created:

![ERD wireframe](https://github.com/D1ang/Soccersystems/blob/main/mockups/model.png)

### Surface
The colours chosen are Estro red and white,
as these are the most used colour for Ajax's style. 

## Technologies
 - Figma - *To create a wireframe*
 - Lucid Chart - *To create the Entity Relationship Diagram (ERD)*
 - HTML - *To create the basics*
 - CSS - *To improve placements and design*
 - JavaScript - *The engine to create user interaction*
 - Python - *Programming language*
 - Postgres - *Opensource database to save the transactions, profile, and orders*
 - Django - *Web framework in python*
 - Bootstrap - *To make the design responsive*
 - Font Awesome - *Easy icon access for the icons*

### JavaScript Libraries
 - jQuery - *To improve input field feedback*
 - flatpickr - *lightweight, powerful JavaScript datetimepicker with no dependencies*
 - DataTables - *Adds advanced interaction controls to HTML tables*

### Python & Django Libraries
 - pillow - *Python Imaging Library*
 - boto3 - *To connect to AWS*
 - django-allauth - *Authentication, registration & account management*
 - django-phonenumber-field - *A Django library which interfaces with python-phonenumbers to validate*
 - django-crispy-forms - *Controls the rendering behaviour of Django forms*
 - django-filter - *Easy searching and filtering query sets*

## Features
This system is an e-commerce-based website with a simplistic but easy to understand build-up.
Providing the user with a call-to-action, a choice can be made in seconds.
The navbar is sticky but reacts on the users scrolling behaviour. While scrolling down the bar disappears to keep a clean screen estate,
but when scrolling up, the bar will re-appear.
The products page will show all the available products that can be ordered.
To order a product the user needs to be logged in. To provide the user with some extra feedback a handy message bar will drop down from the navbar.
This bar will scroll up again after a few seconds. 
When an user will create an account or login, a dashboard will be available for a nice table-based overview of the placed services.
An admin account is available for supervisors to, update service request and download the by customer uploaded artwork.
Users can add or delete services to their cart which will be saved in the backend right away.
As a user logs out the cart will be remembered in the system to be finished later.

## Testing
This system was tested across multiple screen sizes on Chrome, Safari, and Internet Explorer.
To ensure compatibility and responsiveness it is also tested on an android based mobile device (OnePlus5)
and an older tablet device (Samsung Galaxy Tab2).
The system has been field-tested by customers and employees.
Some basic unit testing has been done with Travis and own written testcodes on the home and accounts app.
Unit testing does not go as deep as the field tests, but does show that the bare basic functions are working correctly. 

The following tests have been used to ensure proper site functionality:

- [GTmetrix](https://gtmetrix.com/): To test on website loading times.
- [W3C HTML Validator](https://validator.w3.org/): This validator checks the mark-up validity of Web documents in HTML.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/): This validator checks the mark-up validity of Web documents in CSS.
- [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB): Inspecting on overflow errors.
- [Autoprefixer CSS online](https://autoprefixer.github.io/): Autoprefixer is a PostCSS plugin which parses your CSS and adds vendor prefixes.
- [JSHint](https://jshint.com/): A static code analysis tool for JavaScript.
- [ES6 Syntax Check](https://www.piliapp.com/syntax-check/es6/): An online ECMAScript 6 Checker.
- [Visual Studio Code](https://code.visualstudio.com/): Using the built-in tools to test on proper code, like flake8 linter.
- [Travis](https://travis-ci.org/): Used halfway the project to test the code.

## Bugs

### CSS
CSS written code is tested with the W3C CSS Validator.
As it does not give any problems, the deployed version of the site does gives a couple of warnings and errors coming
from Bootstrap and the Font Awesome animations Library.

### JavaScript
All 3 JavaScript’s in this system passed the test, only a couple of warnings came up through JSHint, for example: using "let", "const" but none of them are bug worthy.
By using "ES6 Syntax Check" all the Syntax checks passed.

### Admin login gave a 500 error
When a customer logged in, the system worked perfectly. But for the admin account a 500 error came up.
This bug was fixed after making migrations and changed the max field characters to 50 chars.
Seems that the admin entered email was 28 characters and when in an earlier build was set to 25, this error came up.

## Deployment
The code of this system is hosted by using Heroku and Amazon S3, this code is deployed to GitHub directly from the main branch.
The deployed site will update automatically upon new commits to the main branch.
This code can be run locally or deployed to a live environment. Directions are based on deployment locally and to Heroku.

### Deploy requirements
 - [VScode](https://code.visualstudio.com/) *A tool to develop software*
 - [python 3](https://www.python.org/) *A programming language*
 - [PIP](https://pip.pypa.io/en/stable/installing/) *To get python installation packages*
 - [Git](https://github.com/) *Version control for code source*
 - [AWS-S3](https://docs.aws.amazon.com/) *Web based cloud storage service*
 - [S3 Bucket](https://docs.aws.amazon.com/) *A cloud storage resource*
 - [Stripe](https://stripe.com/) *To securely collect credit card payments*

### Local deployment
1.  Download a copy of the GitHub repository by clicking the "Code" button at the top right of the 
    GitHub page and in the submenu select "Download ZIP". Extract the zip file to a folder of choice on your system. If Git is installed on your system, you can clone the repository 
    with the following command:
    ```bash
    git clone https://github.com/D1ang/Soccersystems.git
    ```

1.  Open the unzipped folder in your preferred IDE (in this example we are using VScode)
    Open up a terminal session and set up a virtual environment with these commands in the terminal session:
    ```bash
    pip install virtualenv
    ```
    >If you already have virtualenv installed from a different project, then this step is not needed. The pip command may differ per system this can be pip or pip3.

    ```bash
    virtualenv env
    ```
    >Your command may differ to the IDE you are using, such as ```python -m .venv venv ...``` or ```py manage.py ...```
  
    Activate the .env with the command:
    ```bash 
    env\Scripts\activate
    ```
    >This command may differ depending on your operating system, please check the Python documentation on creating an ENV.

1.  Install all required django modules with the command:
    ```bash
    pip install -r requirements.txt
    ```

1.  Create a new file at the base directory level called env.py and copy the following into the created env.py file:
    ```bash
    import os

    os.environ.setdefault( 'DEVELOPMENT', 'True')
    os.environ.setdefault('SECRET_KEY', 'your_value')
    ```

    Replace <your_value> with the values from your own created accounts:
    - [SECRET_KEY](https://djecrety.ir/) *Required from an online key generator*

1.  Set up the databases by running the following management command in your terminal:
    ```bash
    python manage.py migrate
    ```

1.  Create a superuser so you can have access to the django admin by running the following command in your terminal:
    ```bash
    python manage.py createsuperuser
    ```

1.  Now that the server is running, we need to add the required data into the database in the following order:
    ```
    python manage.py loaddata groups.json
    python manage.py loaddata customers.json
    python manage.py loaddata itemtags.json
    python manage.py loaddata items.json
    ```

1.  Finally start your server by running the following management command in the terminal:
    ```bash
    python manage.py runserver
    ```
    If everything went correctly the terminal will provide a message telling that the development server is running
    at a provided URL mostly:  (http://127.0.0.1:8000/admin)

1.  Open the URL provided by the terminal including (/admin/accounts/customer/1/change/)
    Connect the customer to an user (it's the first inputfield)
    Provide the company information for all the required fields and press the "SAVE" button on the bottom right.

## Credits

### Content
All text content for this system were written by me.

### Acknowledgements
- Django Framework 3.0 Crash Course Tutorials [link](https://www.youtube.com/watch?v=xv_bwpA_aEA&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO)
- freeCodeCamp.org - How to Build an E-commerce Website [link](https://www.youtube.com/watch?v=YZvRrldjf1Y)
- W3schools.com [link](https://www.w3schools.com/)
- Django 3.0 documentation [link](https://docs.djangoproject.com/en/3.0/)
- Django Admin Cookbook [link](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/introduction.html)
- SVG compressing [link](https://www.compresss.com/compress-svg.htm)
