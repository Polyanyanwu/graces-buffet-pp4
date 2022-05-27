# **GRACES BUFFET WEBSITE**

The Graces Buffet is a web application that powers a buffet seat reservation system for a hypothetical restaurant in Dublin Ireland.  

![Graces Buffet](/docs/images/responsive.png)
## Live Site

[Graces Buffet Live](https://graces-buffet.herokuapp.com)

## Repository

[View Repository Here](https://github.com/Polyanyanwu/graces-buffet-pp4)

## Table of Contents

- [**GRACES BUFFET WEBSITE**](#graces-buffet-website)
  - [Live Site](#live-site)
  - [Repository](#repository)
  - [Table of Contents](#table-of-contents)
  - [**Objectives of the Site**](#objectives-of-the-site)
  - [**User Experience Design**](#user-experience-design)
    - [**Initial Design Features**](#initial-design-features)
    - [**User Roles**](#user-roles)
      - [**A. Admin user**](#a-admin-user)
      - [**B. Operator**](#b-operator)
      - [**C. Public**](#c-public)
    - [Features Implemented](#features-implemented)
      - [Sign Up](#sign-up)
      - [Login](#login)
    - [**Agile Initiative**](#agile-initiative)
      - [**Epics**](#epics)
    - [**User Stories**](#user-stories)
    - [GitHub Projects](#github-projects)
    - [**Wireframes**](#wireframes)
      - [Site Map](#site-map)
    - [**Color Scheme**](#color-scheme)
    - [**Fonts**](#fonts)
  - [**Database Design**](#database-design)
  - [Flowchart](#flowchart)
  - [**Technologies Used**](#technologies-used)
    - [**Frameworks and Libraries**](#frameworks-and-libraries)
    - [**Ancillary Technologies**](#ancillary-technologies)
    - [**VSCode Extensions Used**](#vscode-extensions-used)
  - [**Testing**](#testing)
  - [**Deployment**](#deployment)

## **Objectives of the Site**

The site has objective of providing easy to use restaurant dining reservation system. The user desires to book seats for guests for a dinner, and the site owner wants to manage available seats/tables automatically with options to book on behalf of users who called on the phone. The application will provide historical and statistical reports to the validated user, the operator and the admin user.

## **User Experience Design**

### **Initial Design Features**

- The seats are reserved for the user for 2 hours before assigning another booking for the same table. The 2 hours should be changeable by the Admin based on user experience on average times taken for each guests over time.
  
- Bookings would be for specified Date and desired time slots. Available times for the chosen date will be displayed to the user.
  
- Admin maintains the opening and closing times for the restaurant and the time required to serve a reservation.
  
- The system would maintain a table of the available times per day. If a user makes the initial request for a day, a record is created in the reservation table. Subsequently, the application will search the database to know which slots have been taken before suggesting the remaining times to the user
  
- Cancellations are permitted before 4 hours to the time. Admin can adjust this limit in the database.
  
- Admin will maintain the different types of tables available, i.e 1-seater, 2-seater, 3-seater, 4-seater and Reservations are booked to occupy the least number of tables. A reservation could take 2 or more tables depending on the number of people.
  
- Online bookings are limited to a maximum of 8 people, bookings for larger number of people could be arranged by calling the restaurant Admin for special arrangement.
  
- Seats are uniquely booked. Once booked, the seat won’t become available for another booking unless there is cancellation.
  
- The Operator/Admin can cancel a booking if the guest fails to turn up after 45 minutes (time is configurable by the Admin).
  
- The Restaurant operate only buffet style, however there are given number of categories of meals, which a user could indicate interest in. The indication enables the restaurant manager to have an idea of how many people may be interested in a type of buffet for a given day. E.g.,

    1. Nigerian dish
    2. Italian food
    3. Asian food

- Price of buffet per person is displayed but payment will be after service delivery at the restaurant.
User Interaction
- A user will need to login to complete making a booking. Initially the book a date & time screen will be presented. User could decide to check availability first but to complete the booking, user needs to create an account.

- An email address and password would be sufficient to create an account, but the email has to be confirmed with a code to be emailed to the user.A user remains signed in until user choses to sign out, in line with current UX design.

- A nice to have feature will be integration with the Google/ Facebook for authentication instead of only email address.

- Users not logged in can only view the make a reservation but are not able to save until they create an account successfully. Menu items for booking list, update messages are only available to logged in users.

- When a user makes a booking successfully, it will appear on the bookings list dropdown, any cancellation will appear on the update messages dropdown.

- Confirmation of bookings or cancellations will fire an email to the user informing them accordingly. Admin could cancel a reservation giving the user valid reasons and suggesting alternate times for the booking.

- Login button will change to Logout when a user successfully logged in. The name of the logged in user will be displayed.

### **User Roles**

There shall be three roles for the application:

#### **A. Admin user**

    1. Assign user role to signed-in users
    2. Set system preferences
    3. Cancel bookings where necessary
    4. Update booking status – close booking after service has been delivered
    5. Maintain buffet categories (meal menu) including description, price and image of the buffet
    6. Maintain table/seat types and quantities available
    7. Maintain duration of each table reservation
    8. Maintain reason for cancellations

#### **B. Operator**

    1. Cancel bookings where necessary e.g where guest fail to turn up after a given time has elapsed
    2. Update booking status – close booking after service has been delivered
    3. Make booking on behalf of a customer (could have)
    4. Enquiry on Guests that have not turned up for the booking
    5. Enquiry on the details of bookings for a given period

#### **C. Public**

    1. Sign-in to the site
    2. Make bookings
    3. Cancel bookings
    4. Enquiries on booking history

Only the Admin will use the Admin portal, while Operator and Public will use the application main page. Accessible menu items will depend on the role assigned to the user by the operator.

### Features Implemented

The website is used for the booking of seats for a number of persons in a stated date and time. To book successfully a user need to sign up with a valid email address. There are three roles for the application public, operator and administrator. We shall discuss the features under these three roles and in addition to the sign up process.

#### Sign Up

When the website opens to a new user, the Signup and Login icons are shown on the right edge of the screen. 
![Signup](/docs/images/features/welcome.png)

Click on the signup button will display the signup page where the user details and email are inputted. All the fields are required and the email will be verified before a user is able to login.

![Signup Profile](/docs/images/features/create_account.png)

Once the form is completed, the user is informed that an email has been forwarded to the given address for verification. The email will usually be received within few minutes depending on the network situation. 

![Signup Profile](/docs/images/features/verify_email.png)

Clicking on the link provided in the email verification email will direct the user to a page to click to verify the email. Once the user clicks on the Confirm button, the user is routed to the Login page.

![Signup Profile](/docs/images/features/confirm_email.png)

#### Login 




### **Agile Initiative**

The project will consist of one initiative which is to provide an intuitive user-friendly online restaurant booking/reservation for the administration of Graces Buffet.

#### **Epics**

The functionalities in the application shall be provided through two user epics:

1. The application shall provide a role-based access control enabling users to register with the site, maintain passwords, and possibly integrate with social media for authentication.
2. The application shall provide seat reservation functionality where an authenticated user can complete seat reservation and book a buffet type dinner with reports on booking history and past due bookings

### **User Stories**

The User Stories for the application was developed before commencement of the application and guided the process. The User Stories were entered as Issues on GitHub repository for the application and used to guide the management of the project. The User Stories were grouped into four:

- Customer Stories
- Operator Stories
- Authentication stories
- Site Owner/Admin stories
  
Detailed User Stories are [provided HERE](/docs/user_stories.md)

### GitHub Projects

Two projects were used in the GitHub to manage the project. There were two iteration timeboxes implemented with Milestones/Sprints of two weeks duration each. The links to the projects are given below:

[First Iteration Project](https://github.com/users/Polyanyanwu/projects/3)  
[Final Iteration Project](https://github.com/users/Polyanyanwu/projects/5)

MoSCow prioritization was used and the User Stories were categorized into Must Have, Could Have and Should Have. The categories were implemented as labels on GitHub.

Major bugs encountered in the course of the development were raised on GitHub as issues and closed when resolved.

### **Wireframes**

Wireframes were designed at the onset of the project and guided the development of the application. The full wireframes are [provided HERE](/docs/wireframes.md)

#### Site Map

The design site map of the website is given below:

![Site Map](/docs/wireframes/site_map.jpg)

### **Color Scheme**

In order to enhance the user experience and have consistent look and feel throughout the website, I chose a color scheme through the [Colors.co](https://coolors.co/). The color palette used is shown below:

![Color Pallet](/docs/color_scheme.png)

### **Fonts**

The font for the website is "Exo", which was chosen from [Google fonts](https://fonts.google.com/specimen/Exo?query=exo). This font looks great to me for a website where the user need not struggle to see details of the site.
![Font](/docs/font.png)

                Background Image
                Flowchart

## **Database Design**

The database used in this project is a relational database, Postgres. It is provided by Heroku.

The database Entity Diagram is given below:

![Entity Diagram](/docs/wireframes/entity_diagram.png)

## Flowchart

The initial flowchart for the public interaction with the website has been produced to guide the application development. As the site unfolds, it may differ slightly as requirements may change slightly in the course of development.

![Flowchart](/docs/wireframes/flowchart.png)
        Features
            Go through the Instructions
            Print existing result of enquiries
            Run new enquiry
            Delete all existing enquiry results
        Future Features
        Data Model

## **Technologies Used**
  
  The main technologies used are:

  1. Python3 (Django is a framework based on Python, which was used extensively in the views to deliver the application logic)
  2. HTML (used to display the pages - Django templates makes use of HTML)
  3. Jinja template language
  4. CSS (used in styling some of the HTML)
  5. Javascript

### **Frameworks and Libraries**

- Django framework, which is a very powerful open source project. The documentation of Django is on the [Official Django Site](https://www.djangoproject.com/).
- [Django Allauth Package](https://django-allauth.readthedocs.io/en/latest/installation.html) was used for the user signup, password management and related functionality.
- [Bootstrap V5.1](https://getbootstrap.com/docs/5.1/getting-started/introduction/) was used in styling and positioning the HTML elements on the pages.
- [jQuery 3.6](https://jquery.com/) for rendering the modal confirmation of actions on the application.
- [Font Awesome - fontawesomefree V 5.15.3](https://fontawesome.com/) was used to deliver the icons on the home page.
- [Cloudinary](https://cloudinary.com/) was used in rendering static files and images on the website.
- [Summernote](https://summernote.org/) enabled the Admin to create WYSIWYG Terms of Use and Privacy Policy which makes it become dynamic and loaded form database records.
- [Django Crispy Forms)(https://django-crispy-forms.readthedocs.io/en/latest/) was helpful to display some of the forms on the pages.
- [Dj-database-url](https://pypi.org/project/dj-database-url/) assisted with accessing the database.
- [Psycopg2](https://pypi.org/project/psycopg2/) was the PostgreSQL database adapter for the Python programming language that was used in the project.

### **Ancillary Technologies**

- [Balsamiq](https://balsamiq.com/) was used to create  the Wireframes for the application.
- [Google Fonts](https://fonts.google.com/) was used for the fonts in the application.
- [TinyPNG](https://tinypng.com/) for resizing all the images.
- [Am I Responsive](https://ui.dev/amiresponsive?url=https://graces-buffet.herokuapp.com/) was used to create the Mockup image at the top of the README.
- [PEP8 validation](http://pep8online.com/) : A Python code online validation application.
- [JShint](https://jshint.com/) : for validation of the Javascript used.
- [W3C Markup Validation Service](validator.w3.org) : A free application that was used to check the HTML and CSS files for errors.
- [Visual Studio Code](https://code.visualstudio.com/): The code editor used for the application development. With numerous [extensions](#vscode-extensions-used) available it is an excellent environment for writing efficient codes.
- [Git](https://git-scm.com/) : For Version control.
- [GitPod](https://www.gitpod.io/) : the Integrated Development Environment.
- [GitHub](https://github.com/)  for hosting the repository.
- [Heroku](https://www.heroku.com/home) : hosting the live website.

### **VSCode Extensions Used**

Some VSCode extensions were used during the development of the application. They are:

- [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens)
This extension assisted to give meaningful messages on the Python code regarding structure and syntax.
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
This assisted with production of this README with Table of Contents in particular.
- [markdown lint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
This extension assisted with the structure of README content.
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
This was very useful to check spelling errors in the code.

## **Testing**

Manual tests were continuously done on the application during development and as new features are added. Being an Agile approach project, I concentrated on delivery the user stories and testing them while the documentation on tests is coming at the close of the project. The code has been validated for syntactic correctness using industry standard methods like W3C, JSHint, PEP8.

Automated tests were carried out on some of the requirements of the booking application and were successful.The full details of the tests carried out is available at [Tests Carried Out](/docs/testing.md)

        Bugs
            Current Bugs
            Resolved Bugs

## **Deployment**

The application was deployed to [Heroku](https://heroku.com) where all the code and database is hosted. The static files were hosted on [Cloudinary.com](https://cloudinary.com/). Details of the fork, clone and deployment process is available [HERE](/docs/deployment.md)

        Credits
            Content
            Code
            Media
            Acknowledgements
