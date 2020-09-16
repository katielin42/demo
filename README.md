
<p align="center">
  <img src="https://i.imgur.com/a8pExaX.png" alt="EE-Club">
</p>

This project is a [website](http://eeclub.ca), made for the Electrical Engineering Club at the University of Alberta. 

## Getting Started

If you wish to clone this repository onto your local machine for developmental or testing purposes, you can follow the steps below. 

### Prerequisites

* `git` should be installed, we recommend the latest long-term support version.
* We recommend using PyCharm for this project, with the latest long-term support version

### Installing

You can then clone the repository into your local machine through the git commandline,
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```
Or through GitHub Desktop. You can download GitHub Desktop [here.](https://desktop.github.com/)

Now you need to set up a virtual environment for this project. Depending on your OS and its version, you can find tutorials online on how to set up your `venv` properly, as well as its activation. This project runs on Python versions > 3.0.

After you are done, `pip install` some requirements into your `venv` via your cmd/terminal. We start with Django:
```
$ pip install django ">=3.0, <4.0"
```
You can double check the right version of your Django is installed with 
```
$ python -m django --version
```
Repeat the above process for `pillow`, `psycopg2-binary`, and `sqlarse`. 

### Start the Website

Once you install the dependencies, type 
```
$ python manage.py migrate
```
to migrate any changes from the database. Then you can run the project with, 
```
$ python manage.py runserver
```
and start playing around with the website. 

## Deployment

Deplyment was done through Digital Ocean. Currently the project sits in an Nginx server on one of DO's droplets, but we will be migrating to cPanel very soon.


## Built With

* [Django](https://www.djangoproject.com/)
* Python
* HTML & CSS
* A dash of JS and jQuery (absolute magic)
* SQLite3, postgreSQL

## Contributing

Upcoming feature. 

## Versioning

Upcoming feature. 

## Dev Team

* **Justine Ventura** - GitHub - [j-vent](https://github.com/j-vent)
* **Katie Lin** - GitHub - [katielin42](https://github.com/katielin42)
* **Marco Romero** - GitHub -[mrcromero](https://github.com/mrcromero)
* **Ethan Cinq-Mars** 

## License

This project is licensed under the GNU AGPLv3 License - see [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to StackOverflow, CSS & Html documentation, and the dude who tried to hack our website which made us realise we had backend security vulnerabilities 
* Mega hat tip to all of our beta testers and feedback doners (aka EE Club Execs)
* Inspired by Engineering Physics Club and Computer Engineering Club
