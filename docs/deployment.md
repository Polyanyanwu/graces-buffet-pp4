
# Cloning and Deployment for Graces Buffet

- [Cloning and Deployment for Graces Buffet](#cloning-and-deployment-for-graces-buffet)
  - [Prerequisites](#prerequisites)
    - [Fork the Repository](#fork-the-repository)
    - [Cloning the Repository](#cloning-the-repository)
    - [Application Dependencies](#application-dependencies)
  - [Deployment to Heroku](#deployment-to-heroku)
    - [**Create Heroku App**](#create-heroku-app)
    - [**Create Database in Heroku**](#create-database-in-heroku)
    - [**Create the Config Variables**](#create-the-config-variables)
    - [Deploy through the CLI](#deploy-through-the-cli)

The project was developed using [GitPod IDE](https://www.gitpod.io/) (Integrated Development Environment)and pushed to [GitHub](https://github.com). The project repository is at [Graces Buffet Repository]( https://github.com/Polyanyanwu/graces-buffet-pp4). Commits to the repository were done via the Git version control available in the Gitpod.

[Return to README](/README.md)

## Prerequisites

1. You need to create an account in [GitHub](https://github.com).
if you don’t have any yet. Login to your GitHub account.

After logging into Github, you could decide on any of the following options:

1. Create a repository: [Here](https://docs.github.com/en/github/getting-started-with-github/create-a-repo), create same directory structure as I have, copy and paste the codes.
2. You can **fork** the Graces Buffet repository, or
3. You can **clone** the repository.

### Fork the Repository

Fork of a repository will create a copy of the repository in your own repositories in GitHub.

You can make changes to the copy as you desire. You can also pull the latest version from the original repository through a pull request in the upstream repository.

To Fork a repository you need to proceed as follows:

1. Navigate to the repository [Graces Buffet Repository]( https://github.com/Polyanyanwu/graces-buffet-pp4).
2. Locate the fork button on the top right of the page and click on it. This will create a copy of the repository in your own Github repositories.

### Cloning the Repository

Cloning enables you to create a copy of the repository locally on your computer. This is making a local copy of the repository at that point in time.

To clone a repository, proceed as follows:

1. Open the [Graces Buffet Repository]( https://github.com/Polyanyanwu/graces-buffet-pp4).
2. Click on the **Code** button.

![Code button](/docs/images/deployment/repository_code_btn.png)

1. Three options are presented to clone the repository (HTTPS, SSH, Gihub CLI). This manual will discuss the most popular method (HTTPS) and offer a link for further information on others.

![Clone options](/docs/images/deployment/cloning_options.png)

**Through the HTTPS**

* Click HTTPS option and copy the link given
* You may also click on the Download Zip button and get a compressed zip file of the repository downloaded to your machine.
* You can also click Open with GitHub desktop if you have it installed
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

 The live site is accessible at [Graces Buffet](https://graces-buffet.herokuapp.com/).

Find below steps that were used to effectively deploy the application to the Heroku platform.

### **Create Heroku App**

1. Sign up / Log in to [Heroku](https://heroku.com) and create an account.

2. From the Heroku Dashboard page select 'New' and then 'Create New App'

![Heroku New App](/docs/images/deployment/create_application.png)

3. From the Create New App form that opens, input an App Name and chose a Region (Europe or United States). When you enter an App Name if it is available, Heroku will indicate that it is available. If its not available you chose another name. Application names in Heroku are unique. I created the app (graces-buffet).

![Heroku New](/docs/images/deployment/create_new_app.png)

### **Create Database in Heroku**

4. Its time to create the Database Resource. Postgres DB was used for the project. From the Heroku Dashboard, select your application name by clicking on it, then click on the Resources tab. From the search bar that opens in the Resources tab, input postgres and heroku will automatically display a suggested list of resources matching the name you inputted.

![Postgres DB Search](/docs/images/deployment/postgres_search.png)

Click on the Heroku Postgres and Heroku will display the Order form for you to select the Plan you need. If it is for app development like we are doing, select the Free plan.
![Postgres Plan](/docs/images/deployment/create_db_resource.png)
Click on Submit Order Form to complete the process.
Heroku provision's the database and automatically creates a record in the Config Vars (see below) for the Database URL. This URL is very essential for you to access the database from your application.

### **Create the Config Variables**

5. The next thing to do is to create the necessary Config environment variables needed for the application to run.
* From the Settings tab, click on the Reveal Config Vars button to open the Config Vars which shows empty KEY and VALUE settings. In my own application I am using Postgres DB, Cloudinary, email forwarding and the required keys are listed below:

![Config Vars](/docs/images/deployment/config_vars.png)

* If you have not done so, proceed to [Cloudinary site](https://cloudinary.com/), create an account.
Click on your cloudinary dashboard and you will find the necessary variables to copy and use to create the Config Vars in Heroku.
My dashboard looks like this:

![Config Vars](/docs/images/deployment/cloudinary.png)

* You need to enter the Config Var keys "CLOUDINARY_URL", "CLOUD_NAME", "API_KEY" and "API_SECRET" from the values in your Cloudinary dashboard.
* For the "SECRET_KEY" variable you can generate one from [Generate Django Secret Key](https://miniwebtool.com/django-secret-key-generator/)
* Enter the Email key details depending on your email service provider.

### Deploy through the CLI

* You need to enable two-factor authentication in your Heroku account.
* Click on Account Settings in Heroku
* Copy your API which you will use in logging into the Heroku from the Terminal in your development environment.
* Return to your Gitpod or development IDE
* Add Heroku as a remote repository to your workspace using ```git remote add heroku <url address of your app on heroku> ```
* type ```heroku login -i```
* You will be prompted for your Heroku email and password
* For the password, enter the API key you copied from step 2 above.
* Finally, type ```git push heroku main``` where main is the branch you want to deploy.

[Return to README](/README.md)
