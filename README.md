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
    - [**Agile Initiative**](#agile-initiative)
      - [**Epics**](#epics)
    - [**User Stories**](#user-stories)
    - [GitHub Projects](#github-projects)
    - [**Wireframes**](#wireframes)
      - [Site Map](#site-map)
    - [**Color Scheme**](#color-scheme)
    - [**Fonts**](#fonts)
  - [**Features Implemented**](#features-implemented)
    - [**Sign Up \& Login**](#sign-up--login)
    - [Menu Options for Public User](#menu-options-for-public-user)
      - [**Make Booking**](#make-booking)
      - [User Account Dropdown](#user-account-dropdown)
    - [Feature Options for Operator User](#feature-options-for-operator-user)
      - [Update Booking Status](#update-booking-status)
      - [Book for Customer](#book-for-customer)
      - [Cancel Booking for Customer](#cancel-booking-for-customer)
      - [Past Due Guest List](#past-due-guest-list)
      - [Booking Details List](#booking-details-list)
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

## **Features Implemented**

The website is used for the booking of seats for a number of persons in a stated date and time. To book successfully a user need to sign up with a valid email address. There are three roles for the application public, operator and administrator. We shall discuss the features under these three roles and in addition to the sign up process.

### **Sign Up & Login**

When the website opens to a new user, the Signup and Login icons are shown on the right edge of the screen. 
![Signup](/docs/images/features/welcome.png)

Click on the signup button will display the signup page where the user details and email are inputted. All the fields are required and the email will be verified before a user is able to login.

![Signup Profile](/docs/images/features/create_account.png)

Once the form is completed, the user is informed that an email has been forwarded to the given address for verification. The email will usually be received within few minutes depending on the network situation. 

![Signup Profile](/docs/images/features/verify_email.png)

Clicking on the link provided in the email verification email will direct the user to a page to click to verify the email. Once the user clicks on the Confirm button, the user is routed to the Login page.

![Signup Profile](/docs/images/features/confirm_email.png)

The user can login with either the username or email address provided during the signup.
If the credentials inputted are correct, an acknowledgement of the successful login is given at the footer area and a menu of options is displayed at the top right corner of the page.

![Success Login](/docs/images/features/success_signin.png)

If the username/email and password provided do not match, a message is displayed to the user and login is not permitted.

### Menu Options for Public User

![Public User Menu](/docs/images/features/public_user_menu.png)

#### **Make Booking**

The booking page is the main page when a user opens the website. To effectively make a booking, a user need to be authenticated (logged in).
The booking requests the dinner date, the time (displayed as a dropdown menu of available time slots), number of persons, and options for the buffet. A user is required to indicate, at least, one buffet option. This is to enable the restaurant owner plan ahead to know dinner options that people want at a given date.

![Booking Page](/docs/images/features/booking.png)

When a user clicks Let's Go button the form is validated and the application checks the availability of seats for the requested date, time and number of persons. If all is okay, the booking is confirmed and a message is displayed on the screen plus and email sent to the registered email address with a copy in the Notifications page for the user. A confirmation booking page is displayed with the details of the booking.

![Booking confirmation](/docs/images/features/booking_confirm.png)

The user without operator or administrator group privilege is presented with menu options as follows:

#### User Account Dropdown

1. Person icon has a dropdown menu for User Account comprising of:

- ##### **My Profile**

Selecting My Profile will display the Profile Update page where the user can update names, phone number and input any special requests to the restaurant. The email is displayed but not editable as change of email need verification and it is provided as a menu option.

![Update Profile](/docs/images/features/update_profile.png)

- ##### **Update Email**
  
The update email option enables the user to add or remove email address and also designate one email as the primary one for the application
![Update Email](/docs/images/features/update_email.png)

- ##### **Dining History**
  
Dining history displays all the bookings made by a customer including cancelled, fulfilled and active ones. Deleted ones are no longer available.
![Dining History](/docs/images/features/dining_history.png)

- ##### **Cancel Booking**
  
A customer may decide to cancel booking and selects this option. A list of all bookings with status "Booked" is displayed with a Cancel button available for the user to click for any of the bookings desired to be cancelled. This cancel booking functionality can also be invoked from the Up Coming booking page.
![Cancel Booking](/docs/images/features/cancel_booking.png)
  
When the user has selected the booking to cancel, a confirmation modal window is displayed requesting the user to confirm the cancellation. If the user affirms the cancellation, the booking is marked as cancelled and removed from the active booking list.
  
![Cancel Booking Confirmation](/docs/images/features/cancel_booking_confirm.png)

- ##### **Reset Password**
  
The password reset feature enables the user to reset password. An email is sent to the user through the email address inputted with a link to enable the password reset.
  
![Reset Password](/docs/images/features/reset_password.png)
  
2. #### Upcoming Events

There is upcoming events represented with a calendar icon. When this icon is clicked, a list of bookings that are still active (status Booked) is displayed for the user. From this list the user can opt to cancel or edit the booking.
  
![Upcoming Events](/docs/images/features/upcoming_booking.png)

If a user decides to edit the booking, a page is displayed with the current booking details where the user can change any of the details and get a instant confirmation feedback, email and copy of the email is available at the notifications menu item. If the cancel button is clicked, the user is requested to confirm cancellation of the booking, and the booking is cancelled if affirmed.

3. ##### **Notifications**

A Notifications icon is shown with a bell. The Notifications contain all the actions taken on the bookings. Notification record is created automatically if a booking is created, edited or cancelled. The user has option to delete the notification at the Notification Details page.
![Notifications](/docs/images/features/notifications.png)
![Notification Details](/docs/images/features/notice_detail.png)

4. The search icon brings the user to the home page

5. The last icon on the right is the logout icon which displays a logout confirmation page for the user.

### Feature Options for Operator User

An operator has access to the Public Menu but is also is presented with additional dropdown menu which is a person icon with a +. To become an operator a user has to signup first and the Administrator will add operator to the groups for the user.
The Operator menu is shown below:

![Operator Menu](/docs/images/features/operator_menu.png)

#### Update Booking Status

The Operator group user can update booking status. Status can be changed to Cancelled, Fulfilled. A list of all active bookings are presented. The user can filter by the user names or dinner date range. When a booking has been selected, an Booking Detail Update Action page is displayed enabling the user to choose the status to change to. When the Update button is clicked, the user is requested to confirm the update via a modal confirmation window before the update is effected.

![Update Booking Status](/docs/images/features/update_booking_status.png)

![Update Booking Status Action](/docs/images/features/booking_update_action.png)

#### Book for Customer

The Book for Customer enables the Operator to make a booking on behalf of a customer. The system will present a list of customers for the user to select from. The list could be filtered by the username or email address of the customer. Once the user is selected by clicking the Select button beside the listed user, the booking page resembling the one on the home page is displayed where the user will enter the details. The customer the user is booking for is displayed on the page to guide the user.

![Book for Customer -Select Customer](/docs/images/features/book_for_customer.png)

![Update Booking Status Action](/docs/images/features/book_for_customer_entry.png)

#### Cancel Booking for Customer

This option enables the Operator to cancel booking for a customer. A list of customers is displayed where the user can select the customer from. The list has option to filter just as in the Book for Customer above. When the customer is selected a page having the customers list of active bookings is displayed. Clicking on the Cancel button will present a modal window requesting user confirms the cancellation. The booking is then cancelled and an email is sent to the customer plus a notification record created for the customer.

![Cancel Booking for customer Action](/docs/images/features/cancel_booking_customer.png)

#### Past Due Guest List

This option displays a list of all bookings that are still active but dinner date is in the past. The operator could then decide to change the status for such bookings.

![Past Due Guest](/docs/images/features/past_due_guest.png)

#### Booking Details List

This is a general query of all bookings in the application. User could filter the list by the customer first or last name, dinner date range or booking status.

![Booking Details List](/docs/images/features/booking_details_operator.png)

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
