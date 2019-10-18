# Simple-Notifier-App
A simple notifier app implemented using django channels

### Installation:

Steps for installing the user notifier app.
•	Clone the repository to a directory
•	Create a virtual environment using virtualenv/virtualenvwrapper and install the python packages in requirement.txt using pip or easy-install.
•	Install and start the Redis server (https://redis.io/). (Application uses Redis as the channel layer)
•	Migrate the db changes by running following commands (Here we have used SQLlite only so need to install any other database servers):
    - python manage.py makemigrations
    - python manage.py migrate
•	Create a super user using the command - python manage.py createsuperuser, and login to the admin panel.
•	Start the server – python manage.py runserver. And open the default port in the browser ( http://localhost:8000/  ).

### App Features

The App will receive a notification when:
1.	A new user is added to the system.
2.	User details are updated.
3.	The user is deleted.
4.	A comment is added by the user.

### How to test the user-notified app ?

The below steps provide the details for testing the application after implementation.
•	Take the Notifier App (http://localhost:8000/)  and  Admin panel (http://localhost:8000/admin/) side by side.
•	Add/Delete/Update user details from the admin panel, verify whether the notification is received in the Notifier App and the details are updated in the list section.
•	Add a comment from the UserComment Section from admin, verify whether notification is received and the comment section is updated.

### Alternate Ways   
•	Can use RabbitMQ as broker instead of Redis
•	Implementing using Flask with Flask-SocketIO (https://flask-socketio.readthedocs.io/en/latest/)

### Modifications to App
•	Can implement a one to one chat system.


