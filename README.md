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
        - [**My Profile**](#my-profile)
        - [**Update Email**](#update-email)
        - [**Cancel Booking**](#cancel-booking)
        - [**Reset Password**](#reset-password)
      - [Upcoming Events](#upcoming-events)
      - [**Notifications**](#notifications)
    - [**Feature Options for Operator User**](#feature-options-for-operator-user)
      - [**Update Booking Status**](#update-booking-status)
      - [**Book for Customer**](#book-for-customer)
      - [**Cancel Booking for Customer**](#cancel-booking-for-customer)
      - [**Past Due Guest List**](#past-due-guest-list)
      - [**Booking Details List**](#booking-details-list)
    - [**Feature Options for Administrator User**](#feature-options-for-administrator-user)
      - [**Assign User Roles**](#assign-user-roles)
      - [**System Preferences**](#system-preferences)
      - [**Cancel Booking for Customer -Admin**](#cancel-booking-for-customer--admin)
      - [**Update Booking Status - Admin**](#update-booking-status---admin)
      - [**Delete Fulfilled Booking**](#delete-fulfilled-booking)
    - [**The Admin Panel**](#the-admin-panel)
  - [Future Features to Implement](#future-features-to-implement)
  - [**Database Design**](#database-design)
  - [Flowchart](#flowchart)
  - [**Technologies Used**](#technologies-used)
    - [**Frameworks and Libraries**](#frameworks-and-libraries)
    - [**Ancillary Technologies**](#ancillary-technologies)
    - [**VSCode Extensions Used**](#vscode-extensions-used)
  - [**Testing**](#testing)
  - [**Bugs**](#bugs)
    - [**Current Bugs**](#current-bugs)
    - [**Resolved Bugs**](#resolved-bugs)
  - [**Deployment**](#deployment)
  - [**Credits**](#credits)
    - [**Content**](#content)
    - [**Code**](#code)
    - [**Media**](#media)
    - [**Acknowledgements**](#acknowledgements)

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

The user can login with either the username or email address provided during the signup. If the credentials inputted are correct, an acknowledgement of the successful login is given at the footer area and a menu of options is displayed at the top right corner of the page.

![Success Login](/docs/images/features/success_signin.png)

If the username/email and password provided do not match, a message is displayed to the user and login is not permitted.

### Menu Options for Public User

![Public User Menu](/docs/images/features/public_user_menu.png)

#### **Make Booking**

The booking page is the main page when a user opens the website. To effectively make a booking, a user need to be authenticated (logged in).
The booking requests the dinner date, the time (displayed as a dropdown menu of available time slots), number of persons, and options for the buffet. A user is required to indicate, at least, one buffet option. This is to enable the restaurant owner plan ahead to know dinner options that people want at a given date.

![Booking Page](/docs/images/features/booking.png)

When a user clicks Let's Go button the form is validated and the application checks the availability of seats for the requested date, time and number of persons. If all is okay, the booking is confirmed and a message is displayed on the screen plus an email sent to the registered email address with a copy in the Notifications page for the user. A confirmation booking page is displayed with the details of the booking.

![Booking confirmation](/docs/images/features/booking_confirm.png)

The user without operator or administrator group privilege is presented with menu options as follows:

#### User Account Dropdown

Person icon has a dropdown menu for User Account comprising of:

##### **My Profile**

Selecting My Profile will display the Profile Update page where the user can update names, phone number and input any special requests to the restaurant. The email is displayed but not editable as change of email need verification and it is provided as a menu option.

![Update Profile](/docs/images/features/update_profile.png)

##### **Update Email**
  
The update email option enables the user to add or remove email address and also designate one email as the primary one for the application
![Update Email](/docs/images/features/update_email.png)

- ##### **Dining History**
  
Dining history displays all the bookings made by a customer including cancelled, fulfilled and active ones. Deleted ones are no longer available.
![Dining History](/docs/images/features/dining_history.png)

##### **Cancel Booking**
  
A customer may decide to cancel booking and selects this option. A list of all bookings with status "Booked" is displayed with a Cancel button available for the user to click for any of the bookings desired to be cancelled. This cancel booking functionality can also be invoked from the Up Coming booking page. At design stage I had intended a maximum period within which cancellation could be accepted, however since no charges are involved in this system, I stepped that now.

![Cancel Booking](/docs/images/features/cancel_booking.png)
  
When the user has selected the booking to cancel, a confirmation modal window is displayed requesting the user to confirm the cancellation. If the user affirms the cancellation, the booking is marked as cancelled and removed from the active booking list. The reasons for cancellation was not included in this system and could be good for future update.
  
![Cancel Booking Confirmation](/docs/images/features/cancel_booking_confirm.png)

##### **Reset Password**
  
The password reset feature enables the user to reset password. An email is sent to the user through the email address inputted with a link to enable the password reset.
  
![Reset Password](/docs/images/features/reset_password.png)

#### Upcoming Events

There is upcoming events represented with a calendar icon. When this icon is clicked, a list of bookings that are still active (status Booked) is displayed for the user. From this list the user can opt to cancel or edit the booking.
  
![Upcoming Events](/docs/images/features/upcoming_booking.png)

If a user decides to edit the booking, a page is displayed with the current booking details where the user can change any of the details and get an instant confirmation feedback, email is sent and copy of the email is available at the notifications menu item. If the cancel button is clicked, the user is requested to confirm cancellation of the booking, and the booking is cancelled if affirmed.

#### **Notifications**

A Notifications icon is shown with a bell. The Notifications contain all the actions taken on the bookings. Notification record is created automatically if a booking is created, edited or cancelled. The user has option to delete the notification at the Notification Details page.

![Notifications](/docs/images/features/notifications.png)
![Notification Details](/docs/images/features/notice_detail.png)

1. The search icon brings the user to the home page

2. The last icon on the right is the logout icon which displays a logout confirmation page for the user.

### **Feature Options for Operator User**

An operator has access to the Public Menu but is also presented with additional dropdown menu which is accessed via a person icon with a +. To become an operator a user has to signup first and the Administrator will add operator to the groups for the user.
The Operator menu is shown below:

![Operator Menu](/docs/images/features/operator_menu.png)

#### **Update Booking Status**

The Operator group user can update booking status. Status can be changed to Cancelled or Fulfilled. A list of all active bookings are presented. The user can filter by the user names or dinner date range. When a booking has been selected, a Booking Detail Update Action page is displayed enabling the user to choose the status to change to. When the Update button is clicked, the user is requested to confirm the update via a modal confirmation window before the update is effected.

![Update Booking Status](/docs/images/features/update_booking_status.png)

![Update Booking Status Action](/docs/images/features/booking_update_action.png)

#### **Book for Customer**

The Book for Customer enables the Operator to make a booking on behalf of a customer. The system will present a list of customers for the user to select from. The list could be filtered by the username or email address of the customer. Once the user is selected by clicking the Select button beside the listed user, the booking page resembling the one on the home page is displayed where the user will enter the details. The customer the user is booking for is displayed on the page to guide the user.

![Book for Customer -Select Customer](/docs/images/features/book_for_customer.png)

![Update Booking Status Action](/docs/images/features/book_for_customer_entry.png)

#### **Cancel Booking for Customer**

This option enables the Operator to cancel booking for a customer. A list of customers is displayed where the user can select the customer from. The list has option to filter just as in the Book for Customer above. When the customer is selected a page having the customers list of active bookings is displayed. Clicking on the Cancel button will present a modal window requesting user confirms the cancellation. The booking is then cancelled and an email is sent to the customer plus a notification record created for the customer. The seats are also released.

![Cancel Booking for customer Action](/docs/images/features/cancel_booking_customer.png)

#### **Past Due Guest List**

This option displays a list of all bookings that are still active but dinner date is in the past. The operator could then decide to change the status for such bookings.

![Past Due Guest](/docs/images/features/past_due_guest.png)

#### **Booking Details List**

This is a general query of all bookings in the application. User could filter the list by the customer first or last name, dinner date range or booking status.

### **Feature Options for Administrator User**

An Administrator has access to the Public Menu but is also presented with additional dropdown menu which is a person icon with a cog. To become an Administrator a user has to signup first and an Administrator will add administrator to the groups for the user. This administrator role is different from the super-admin which has access to the Admin panel. The Admin panel user could be added to the administrator page from the users option.
The administrator menu is shown below:

![Administrator Menu](/docs/images/features/admin_user_menu.png)

#### **Assign User Roles**

The administrator can use this option to put or remove any user from any group. The form that is displayed is shown below:

![Assign User Role](/docs/images/features/update_user_group.png)

The administrator first selects a user and the groups the user belongs to is displayed, if any. To remove existing group click Remove button. To add a group select the group from the group dropdown and click Add.

#### **System Preferences**

The application requires a set of configurations to work effectively. E.g. is the estimated duration of service for each customer. This enables the application to determine if a particular date and time has vacant seats or is fully booked. If for example a user books the restaurant at 2pm, the application will hold that seat from 2pm to the duration of service specified in the system preference before that seat can be available to another person. The administrator is expected to update this sparingly only after observation of service duration.

![System Preference Update](/docs/images/features/sys_pref.png)

Maximum person per online booking controls dynamic display of the number of people dropdown on the booking form.

#### **Cancel Booking for Customer -Admin**

The Cancel Booking for customer is the same functionality that is available for the operator group described above.

#### **Update Booking Status - Admin**

The is akin to the same functionality available to the Operator group.

#### **Delete Fulfilled Booking**

This option displays a list of all bookings that are have been fulfilled to enable the administrator to delete them. When a booking is selected, a Delete Action page is displayed where the user can click on Delete button to proceed to confirm the deletion.

![Delete Booking](/docs/images/features/delete_booking.png)

![Delete Booking Action](/docs/images/features/delete_booking_action.png)

### **The Admin Panel**

There a few important tables to be maintained by the application which the project time constraint didn't enable us to implement. They were included in the Admin panel to enable the superuser to maintain those tables. They are listed below with their purposes:

- Cuisines - add the name, description and image of the cuisine types available. The application has been loaded with four cuisines which were added using this admin panel.
- Booking Status - Could change the description of the booking status. The booking status are all fixed and critical to the overall functioning of the application. The superuser could alter their descriptions.
- Dining Tables - add or remove dining tables with their seating capacity. When new tables/seats are acquired the superuser will add or remove them from the admin panel.
- Home Messages - maintain the text for the Terms of Use and Privacy Policy. Its not expected to change often.
- Contacts - to review or delete contact us messages sent by customers

The above could all be placed under the administrator in the main application but for lack of enough time to do so. These are features that could be added to the user interface in future.

## Future Features to Implement

- It will be desirable to include social authentication to ease the user experience.
  
- Addition of credit/debit card will ensure only serious customers make bookings.
  
- The functionalities listed under "The Admin Panel" above could be implemented and made available to the administrator menu to have uniform experience for the administrator.
  
- I had listed "Reasons for cancellation" to be obtained during cancellation but couldn't include it at this time. It would be desirable for the restaurant owner to have feedback on why bookings are cancelled.

## **Database Design**

The database used in this project is a relational database, Postgres. It is provided by Heroku.

The database Entity Diagram is given below:

![Entity Diagram](/docs/wireframes/entity_diagram.png)

## Flowchart

The initial flowchart for the public interaction with the website has been produced to guide the application development. As the site unfolds, it may differ slightly as requirements may change slightly in the course of development.

![Flowchart](/docs/wireframes/flowchart.png)

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
- [Django Extensions](https://django-extensions.readthedocs.io/en/latest/graph_models.html) enabled auto generation of database model graph.
- [Graphviz](http://www.graphviz.org/) used to generate database model graph

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

Manual tests were continuously done on the application during development and as new features are added. Being an Agile approach project, I concentrated on delivering the user stories and testing them while the documentation on tests is coming at the close of the project. The code has been validated for syntactic correctness using industry standard methods like W3C, JSHint, PEP8.

Automated tests were carried out on some of the requirements of the booking application and were successful.The full details of the tests carried out is available at [Tests Carried Out](/docs/testing.md)

## **Bugs**

### **Current Bugs**

- In some of the pages pagination has been implemented. During testing it was noticed that if a page is filtered and paginated, the first page returns with the filtered list but subsequent pages will disregard the filtering. I noticed its happening because the next pages are rendered from the get request while the filtered list are returning from the post method. This could not be rectified at this time as it was noticed late when the app was loaded with enough data to test the pagination.

### **Resolved Bugs**

- The system was returning to Booking Detail Update action when the next pagination button is clicked. This was resolved at commit[0785e2](https://github.com/Polyanyanwu/graces-buffet-pp4/commit/0785e2662900989042c4c6810f821cec5ad6a1de) by returning the user to the Update Booking Select Booking page using ```redirect``` instead of returning with context.
  
- Public user was mistakenly prevented from updating profile. This was resolved vi commit [3e79f05](https://github.com/Polyanyanwu/graces-buffet-pp4/commit/3e79f05dfa0beb8405395f34cf9c8c67d72f2b66) by removing the restriction placed in the view class.
  
- It was noticed at some stage that putting the /admin url to open the admin panel was opening the Book for Customer page instead of the admin panel. This was resolved by ```creating a make_booking_others.html``` and letting the ```make_booking.html``` be for only customer booking because it is the main page at commit [5bd6ff](https://github.com/Polyanyanwu/graces-buffet-pp4/commit/5bd6ffcbf5791b7cd8233beeca3d30a53e6951fe).

- Cancel booking confirmation stopped working when strict mode was introduced in the JavaScript. It was resolved though commit [e27ae0](https://github.com/Polyanyanwu/graces-buffet-pp4/commit/e27ae05d09df70692099b955a948693d9d68f2fd) by defining the ```const booking_id``` before its use.

- Delete Booking was giving Error 500 after I changed the checking of access to accept a tuple of group names instead of only one group name. This was resolved by converting single group names pass to the check_access method to tuple via commit [d7bbef](https://github.com/Polyanyanwu/graces-buffet-pp4/commit/d7bbefaf906860869f925335ef59c1153843d1f7)
  
- Clicking on any cuisine was selecting the first one. It was fixed by changing the id for the html element to a unique cuisine name via commit [6b1ff6](https://github.com/Polyanyanwu/graces-buffet-pp4/commit/6b1ff6f477744ede707d196dba5bbb5025412d5a)
  
- Dinner date shown in notifications was including time as Midnight instead of only the date. Fixing was by introducing date format for the dinner date via commit [e3ccbe](https://github.com/Polyanyanwu/graces-buffet-pp4/commit/e3ccbe4a6a6795bb8071ee924c4e0774b3f9c506)

- Index out of range was coming up during booking caused by wrong index when determining available seats resolved via commit [b41c78](https://github.com/Polyanyanwu/graces-buffet-pp4/commit/b41c7843ee9ae7fddc1d5726c94c80de894490fc)

- Deployment to Heroku was failing due to collectstatic. I had to add the Cloudinary CLOUD_NAME, API_KEY, and API_SECRET in addition to the CLOUDINARY_URL before it could start working: commit [210ea0](https://github.com/Polyanyanwu/graces-buffet-pp4/commit/210ea0bfcae68b4e4594a9dbbf7a3fe8a3755cf1)

- While testing the seat booking for fully booked situation, it was noticed that the seats were still being allocated even when the full capacity was reached for a given date and time. It was observed that the booked date in the tables booked records was auto saving the date booked instead of the dinner date causing our algorithm to fail. The fix was to change the booked date to null=False in the model and then save the booked date as dinner date in the views via commit [5fff49](https://github.com/Polyanyanwu/graces-buffet-pp4/commit/5fff49da510bf629c4b451ae31687e8e82eb9880)

- Update booking status action crashes when no status is selected. The post method was not redirecting the user back to the page when no booking status was selected. It was fixed by preventing the empty option on the selection for booking status and also redirecting the user properly if that should ever happen via Commit [6fc8d2](https://github.com/Polyanyanwu/graces-buffet-pp4/commit/6fc8d2d6c170949827389ea9934e3c47fc788e09).

- From the Past Due List an operator could opt to Update the booking status but after the update, the operator was being redirected to Booking List instead of Past Due List. I had to uses a session variable to enable the system remember where the operator invoked the update status from and return accordingly. See commit [aebca5](https://github.com/Polyanyanwu/graces-buffet-pp4/commit/aebca5c979c9529bd234757d786710904d32d722)

## **Deployment**

The application was deployed to [Heroku](https://heroku.com) where all the code and database is hosted. The static files were hosted on [Cloudinary.com](https://cloudinary.com/). Details of the fork, clone and deployment process is available [HERE](/docs/deployment.md)

## **Credits**

### **Content**

- The terms of use was adapted from the Terms and Conditions of [Opentable.ie](https://www.opentable.ie/legal/terms-and-conditions). The idea of the booking page I used was borrowed from [Opentable](https://www.opentable.ie).

- The privacy policy on the main page was an adaptation of [Milano.ie](https://milano.ie/about-us/privacy-policy)
  
### **Code**

- Online [books by Agiliq](https://books.agiliq.com/en/latest/README.html) was a very good resource for getting better ideas of Django ORM.
  
- Numerous [Stack Overflow](https://stackoverflow.com/) postings furnished ideas leading to my figuring out how to overcome some challenges.

- Timmy O'Mahony[https://stackoverflow.com/questions/9939917/django-row-number-in-pagination] for the code for continuing record number when paginated.

- [Brian Neal](https://groups.google.com/g/django-users/c/J2FUloVUlzk) for the idea of removing empty selection option from a select field.

- [Stack Overflow](https://stackoverflow.com/questions/7682804/django-model-forms-setting-a-required-field) make a fried required on a form.

- Aggregation of Queryset examples from [Riptutorial](https://riptutorial.com/django/example/13050/average--minimum--maximum--sum-from-queryset) was very helpful.

- Sample use of Q from [Codegrepper.com](https://www.codegrepper.com/code-examples/python/django+import+Q) assisted when I was at crossroads. 

- [W3schools](https://www.w3schools.com/)  

- [W3docs](https://www.w3docs.com/)
  
- [GeeksforGeeks](https://www.geeksforgeeks.org/)

### **Media**

- The images of the buffet were downloaded from [unsplash](https://unsplash.com/photos/STqHLqMne3k),
[dreamstime.com](https://www.dreamstime.com/royalty-free-stock-photo-malay-buffet-image15700285) and
[dreamstime](https://www.dreamstime.com/photos-images/buffet.html)

- The 403 error message image was downloaded from [gsatatic](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3Crb5tO7_ixFPKD62WWLao6lOdPyl-vzd7w&usqp=CAU) 
- The 404 Page not found image was downloaded from [CCM.net](https://ccm.net/contents/1079-page-not-found-where-is-the-404-error-coming-from)
  
### **Acknowledgements**

- Many thanks to my mentor [Brian O'Hare](https://code-institute-room.slack.com/team/U02H67B6DS6) for the encouragement and criticism of my work that led to its eventual refinement.

- Thanks to [Simen Daehlin](https://code-institute-room.slack.com/team/U4MVA9YQP) for pushing me further to add what he called "make it intuitive" for a better user experience leading to interconnecting the functionalities where desired.

- Many thanks to the Code Institute's team (Lecturers and Tutors) for challenging me further and supporting when needed. The [Slack](code-institute-room.slack.com) community was always my first place to search issues and its very helpful.
  
- I'm grateful to my family for their support as I take this bold step to change residence and update skills.
