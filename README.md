
<p align="center">
  <img src="https://i.imgur.com/a8pExaX.png" alt="EE-Club">
</p>

This project is a website, made for the Electrical Engineering Club at the University of Alberta. 

## Getting Started

If you wish to clone this repository onto your local machine for developmental or testing purposes, you can follow the steps below. 

### Prerequisites

* `git` should be installed, we recommend the latest long-term support version.
* PyCharm, we recommend the latest long-term support version

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


###### THE BELOW SECTIONS ARE NOT DONE RIGHT NOW AND WILL BE UPDATED ONCE WE DEPLOY EVERYTHING AND THIS BECOMES AN OFFICIAL THING. YA

## Deployment
Possible security measures: 
Clourflair: provides end SSL encryption to protect website from malicious HTTP requests such as DDoS attacks. 
Lets Encrypt: proides a digital certificate so our site becomes httpS. but need to renew bc it expires every 2 months (use netify). 

Add additional notes about how to deploy this on a live system

## Built With

* [Django](https://www.djangoproject.com/)

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Head Developers

* **Justine Ventura** - GitHub - [j-vent](https://github.com/j-vent)
* **Katie Lin** - GitHub - [katielin42](https://github.com/katielin42)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the GNU AGPLv3 License - see [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
