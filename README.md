# Setting Up and Running an Application with Docker and Python
This README file provides step-by-step instructions on how to set up and run the Python 
application using both Docker and a normal Python environment for the UCT test 1. This 
guide assumes you have Docker installed on your system and a basic understanding of Python.

## Table of Contents
- [Technology Stack](#1-technology-stack)
- [Clone the Repository](#2-clone-the-repository)
- [Setting Up the Python Application](#3-setting-up-the-python-application)
- [Running the Python Application Locally](#4-running-the-python-application-locally)
- [Building the Docker Image](#5-building-the-docker-image)
- [Running the Dockerized Application](#6-running-the-dockerized-application)
- [Unit Test](#7-unit-test)

### 1. Technology Stack
Our application is built on a solid foundation of technology. We use the Django web 
framework for the backend and Bootstrap for the frontend. Django's 
simplicity and flexibility capabilities ensure a robust 
and efficient user experience.

### 2. Clone the Repository
Clone the repository containing the Python application to your local machine using Git 
or by downloading the ZIP file from the source code on GitHub.
```bash
git clone git@github.com:ubayd-bapoo/uct-test1.git
cd uct-test1
```

### 3. Setting Up the Python Application
Lets make sure the Python application works correctly in a normal Python environment. 
This typically involves creating a virtual environment, installing dependencies, and 
testing the application.

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'

# Install application dependencies
pip install -r requirements.txt

# Test the application
python manage.py migrate  # Will create SqlLite DB with tables
python manage.py runserver  # Will run the service
```

### 4. Running the Python Application Locally
To run the application in your local Python environment, you can use the following command:
```bash
python manage.py runserver  # Will run the service
```

### 5. Building the Docker Image
The Dockerfile sets up a basic Python environment and copies the application files into 
the container. It also installs all necessary dependencies from requirements.txt and 
specifies the command to run when the container starts.
To build a Docker image of the Python application, navigate to the project directory 
(where the Dockerfile is located) and run the following command:
```
docker build -t uct-test1 .
```

### 6. Running the Dockerized Application
Once the Docker image is built successfully, you can run the Python application within 
a Docker container:
```bash
docker run -p 8000:8000 uct-test1
```

### 7. Unit Test
To run the unit tests for this application, follow these steps:
```bash
   python manage.py test
```
#### Automated Testing with GitHub Actions

I have set up a GitHub Actions workflow that automatically runs Django test for our unit tests
 whenever changes are pushed to the repository's `main` branch. This ensures that our code
  is continuously tested for correctness.

The workflow configuration can be found in the [`.github/workflows/django.yml`](.github/workflows/django.yml) file. Here's how it works:

- Whenever you push changes to the `main` branch, GitHub Actions will automatically 
trigger the workflow.
- The workflow will use the `manage.py test` command to execute the tests defined in the 
`tests.py` file.
- The results of the tests will be displayed in the GitHub Actions logs.

You can always check the status of the tests by visiting the "Actions" tab in this 
repository. If there are any issues with the tests, you will be notified.

By leveraging GitHub Actions, we ensure that our codebase remains reliable and that new
 contributions are thoroughly tested before being merged into the main branch.

## Tasks

1. Create a new model called Genre with a single field called “name”. Add the following records to
the Genre model: (Action, Adventure, Animated, Comedy, Drama, Fantasy, Horror, RomCom) (5)

2. Extend the Movie model by including the Genre model as a “ManyToManyField”. (5)

3. Create additional views for creating and updating Movie information. Please ensure that you utilise Django forms
for this and ensure that multiple genres can be selected for a movie. (15)

4. Create a login page for the site and set the route for this so that it loads as the site’s homepage (root).
Utilise the default Django user model for authentication. A single user (admin) currently exists. (10)

5. Upon successful login, the application should redirect to the Movie list view. The list view, detail view,
create view and update view should only be accessible when logged in. (5)

6. Add a navbar to the base template with links to the existing views and the new views you have created. Ensure
that the links only appear once logged in. We are expecting you to utilise Bootstrap when styling the navbar. 
 (10)

Please note that you will be graded on your ability to suitably complete the task as well as your presentation and styling.
