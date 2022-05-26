# Cloning and Deployment for Grace Buffet

The project was developed using [GitPod IDE](https://www.gitpod.io/) (Integrated Development Environment)and pushed to [GitHub](https://github.com). The project repository is at [Graces Buffet Repository]( https://github.com/Polyanyanwu/graces-buffet-pp4). Commits to the repository were done via the Git version control available in the Gitpod.

## Prerequisites

1. You need to create and account in [GitHub](https://github.com).
if you don’t have any yet. Log in to your GitHub account.

After logging into Github, you could decide on any of the following options:

1. Create a repository: [Here](https://docs.github.com/en/github/getting-started-with-github/create-a-repo), create same directory structure as I have, copy and paste the codes.
2. You can **fork** the Graces Buffet repository, or
3. You can **clone** the repository.

### Fork the Repository

Fork of a repository will create a copy of the repository in your own repositories in GitHub.

You can make changes to the copy as you desire. You cans also pull the latest version from the original repository through a pull request in the upstream repository.

To Fork a repository you need to proceed as follows:

1. Navigate to the repository [Graces Buffet Repository]( https://github.com/Polyanyanwu/graces-buffet-pp4).
2. Locate the fork button on the top right of the page and click on it. This will create a copy of the repository in your own Github repositories.

### Cloning the Repository

Cloning enables you to create a copy of the repository locally on your computer. This is making a local copy of the repository at that point in time.

To clone a repository, proceed as follows:

1. Open the [Graces Buffet Repository]( https://github.com/Polyanyanwu/graces-buffet-pp4) repository.
2. Click on the **Code** button.

![Code button](/docs/images/deployment/repository_code_btn.png)

1. Three options are presented to clone the repository (HTTPS, SSH, Gihub CLI). This manual will discuss the most popular method (HTTPS) and offer a link for further information on others.

![Clone options](/docs/images/deployment/cloning_options.png)

    1. via HTTPS

* click HTTPS option and copy the link given
* You may also click on the Download Zip button and get a compressed zip file of the repository downloaded to your machine.
* You can also click Open with GIthub desktop if you have it installed
* Navigate to the directory on your machine where you want to store the cloned repository.
* Open your Terminal and type: ```git clone``` and paste the link copied above.
* Press **Enter** and the local clone will be created.

For further information visit [Cloning Repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-using-the-command-line).

### Application Dependencies

The project was developed mainly with Django and relevant packages. In Django/Python projects a requirements.txt file is created in the main application folder. This file indicates which packages and dependencies are required to run the application. After successfully creating/clone/fork the project, you have to run this command in the CLI:

* ``pip3 install -r requirements.txt``. The command will install all the application requirements needed for the project.
* Secondly you need to create the database to run the application on and other environment variables. More information on the creation of the database and other variables will be discussed under Deployment to Heroku given below.

* You need to run migration in order to create the database from the models. Run the following commands in the CLI:
  * ``python3 manage.py makemigrations`` and then,
  * ``python3 manage.py migrate``

* After the successful migrations which created the database, run the project locally by typing:
  * ``python3 manage.py runserver``

## Deployment to Heroku

The application was deployed to [Heroku](https://heroku.com) where all the code and database is hosted. The static files were hosted on [Cloudinary.com](https://cloudinary.com/)

