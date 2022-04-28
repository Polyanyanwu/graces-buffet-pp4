# **GRACES BUFFET WEBSITE**

The Graces Buffet is a web application that powers a buffet seat reservation system for a hypothetical restaurant in Dublin Ireland.  

## Live Site

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
      - [Customer Stories](#customer-stories)
      - [Operator Stories](#operator-stories)
      - [**Authentication stories**](#authentication-stories)
      - [**Site Owner/Admin stories**](#site-owneradmin-stories)
    - [**Wireframe**](#wireframe)
      - [Site Map](#site-map)

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

#### Customer Stories

| User Story                                                                                                                                 | Acceptance Criteria                                                                      | Tasks                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| 1.     As a public user, I want a user-friendly interactive website so that bookings are easy to make.                                     | - Booking details are visible on home page                                               | - Chose a color scheme for the website                                                        |
|                                                                                                                                            | - Responsive in mobile and desktop browsers                                              | - Chose the fonts to use                                                                      |
|                                                                                                                                            | - Feedback on user actions are given                                                     | - Create the logo                                                                             |
|                                                                                                                                            | - User finds links to navigate to other functions easy                                   | - Create the HTML and CSS for the dropdown menus on home page                                 |
|                                                                                                                                            | - Font is legible                                                                        | - Create the model and views for the booking on home page                                     |
|                                                                                                                                            | - Color contrast is effective                                                            | - Deploy to Heroku                                                                            |
|                                                                                                                                            |                                                                                          | - Test the completed home page.                                                               |
| 2.     As a public user, I want to be able to access the website using different devices so that I will have same friendly experience.     | - Website is accessible on different sized devices                                       | - Use Bootstrap responsive design on all pages                                                |
|                                                                                                                                            | - Information is easy to find both on small and large screens                            | - Ensure logo, title and menus appear on all pages consistently                               |
|                                                                                                                                            |                                                                                          | - Test the functionality                                      |
| 3.    As a public user, I can have option to select number of people for the dinner so that the availability will be confirmed immediately | - On the booking form a selection box is available with options for number of people     | - Create the model for table and seats                                                        |
|                                                                                                                                            |                                                                                          | - On the model for booking, create select option                                              |
|                                                                                                                                            |                                                                                          | - Test the functionality                                                                      |
| 4.      As a public user, I can see the buffet price so that I decide to book or not                                                       | - The booking form displays the price per person                                         | - Create a paragraph for the cost of booking per person on the booking form                   |
|                                                                                                                                            |                                                                                          | - Test the functionality                                                                      |
| 5.      In order to book a specific time as a public user, I can have time options to select from on a chosen date.                        | - On the booking form a selection box is available with options for available time slots | - Create model for time slots                                                                 |
|                                                                                                                                            |                                                                                          | - Connect the available time slots to the booking form                                        |
|                                                                                                                                            |                                                                                          | - Display only available time slots                                                           |
|                                                                                                                                            |                                                                                          | - Test the functionality                                                                      |
| 6.      As a public user, I can make booking so that the dinner time is confirmed.                                                         | - Booking form is available to user                                                      | - Add email confirmation to booking                                                           |
|                                                                                                                                            | - Signup form is available to user                                                       | - Check that user is signed-in to save booking or redirect to signup page if not signed-in    |
|                                                                                                                                            | - A signed-in user can save a booking and receive immediate confirmation plus an email   | - Verify from the model that seats are available for selected time and date and give feedback |
|                                                                                                                                            |                                                                                          | - Test the functionality                                                                      |
| 7.        In order to know the type of meals available as a public user, I can see images and descriptions of buffet types.                | - Images and description of buffet types available on the booking page                   | - Create model and view for maintain buffet types                                             |
|                                                                                                                                            |                                                                                          | - Display buffet type on booking page                                                         |
|                                                                                                                                            |                                                                                          | - Test the functionality                                                                      |
| 8.        In order to inform the restaurant of my unavailability as a public user, I can cancel a booking.                                 | - Menu has option for cancel booking                                                     | - Add cancel booking as user menu option                                                      |
|                                                                                                                                            | - Cancel booking page has details of all active bookings                                 | - Create list of all active bookings on the cancel booking page                               |
|                                                                                                                                            | - A button is available to click and cancel desired booking                              | - Give immediate feedback if successfully cancelled                                           |
|                                                                                                                                            | - Feedback is given and list of bookings updated immediately                             | - Refresh the page display to show the booking has been cancelled                             |
|                                                                                                                                            |                                                                                          | - Add the cancelled booking to the Notifications page                                         |
|                                                                                                                                            |                                                                                          | - Test the functionality                                                                      |
| 9.         In order to know the times I was at the restaurant as a public user, I can view booking history.                                | - Option for booking history available on the menu                                       | - Add booking history to user menu option                                                     |
|                                                                                                                                            | - Booking history page contains details of all previous bookings                         | - Create booking history template and view                                                    |
|                                                                                                                                            |                                                                                          | - Test the functionality                                                                      |
| 10.     In order to know of successful booking/cancellation as a public user, I can receive email notifications.                           | - Email is received upon confirmation/cancellation of booking                            | - Create the email template                                                                   |
|                                                                                                                                            |                                                                                          | - Add email send details to settings.py and env.py                                            |
|                                                                                                                                            |                                                                                          | - Send email after confirmation or cancellation of a booking                                  |
|                                                                                                                                            |                                                                                          | - Test functionality                                                                          |
                                                                         |

#### Operator Stories

| User Story                                                                                                                                             | Acceptance Criteria                                             | Tasks                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| 1.    As an operator, I can cancel bookings where guest fail to turn up after a given time has elapsed so that the seats could become available to use | - Menu option for cancel booking available                      | - Add cancel booking to Operator menu                                                                 |
|                                                                                                                                                        | - Ability to select all active bookings                         | - Create a cancel booking template and view with list of active bookings and button to cancel an item |
|                                                                                                                                                        | - Button to pick and cancel a booking                           | - Create a confirmation modal form and request confirmation of cancellation                           |
|                                                                                                                                                        | - Confirmation to proceed with the cancellation                 | - Create a feedback for the cancellation outcome                                                      |
|                                                                                                                                                        | - Feedback message on successful cancellation                   | - Display updated list of active bookings                                                             |
|                                                                                                                                                        | - Updated list of active bookings                               | - Test functionality                                                                                  |
| 2.    As an operator, I can update booking status so that seats could become available after service has been delivered                                | - Menu option for update booking is available                   | - Add update booking to operator menu                                                                 |
|                                                                                                                                                        | - A page is provided where active bookings are displayed        | - Create update booking template and view                                                             |
|                                                                                                                                                        | - Buttons are provided to click and select to update status     | - Create a confirmation modal form and request confirmation of status change                          |
|                                                                                                                                                        | - Status of booking changes after confirmation of status change | - Create a feedback for the status change outcome                                                     |
|                                                                                                                                                        |                                                                 | - Test the functionality                                                                              |
| 3.    As an operator, I can make booking on behalf of a customer so that customers that call in on phone could receive service.                        | - Make booking option is available for operator                 | - Add make booking to operator menu                                                                   |
|                                                                                                                                                        | - Operator can find the customer using phone or email address   | - Create form for booking for customer                                                                |
|                                                                                                                                                        | - Successful booking visible on booking history enquiry         | - When saved send email to customer and update booking table                                          |
|                                                                                                                                                        |                                                                 | - Test the functionality                                                                              |
| 4.    As an operator, I can make enquiry on bookings by data range and booking status so that I can take decisions                                     | - Booking history enquiry available                             | - Create a form to accept the criteria and list the booking details                                   |
|                                                                                                                                                        | - Query has options to select date range and booking status     | - Test the functionality                                                                              |
|                                                                                                                                                        | - List of data is displayed meeting the given criteria          |                                                                                                       |

#### **Authentication stories**

#### **Site Owner/Admin stories**

### **Wireframe**

#### Site Map

The design site map of the website is given below:

![Site Map](/docs/wireframes/site_map.jpg)

The wireframes are listed below for each of the pages to be implemented:

- [Home Page](/docs/wireframes/home_page.png)
- [User Profile](/docs/wireframes/profile.png)
- [Dining History](/docs/wireframes/dining_history.png)
- [Cancel Booking](/docs/wireframes/user_cancel_booking.png)
- [Upcoming Bookings](/docs/wireframes/upcoming_bookings.png)
- [Notifications](/docs/wireframes/notifications.png)
- [Contact Us](/docs/wireframes/contact_us.png)
- [Terms of Use](/docs/wireframes/terms_of_use.png)
- [Privacy Policy](/docs/wireframes/privacy.png)
- [Operator Cancel Booking](/docs/wireframes/operator_cancel_booking.png)
- [Operator Book for Customer](/docs/wireframes/operator_booking_for_customer.png)
- [Update Booking](/docs/wireframes/update_booking.png)
- [Booking History Enquiry](/docs/wireframes/operator_booking_history.png)
- [Login Page](/docs/wireframes/sign_in.png)

The full wiframes on same page is provided [HERE](/docs/wireframes.md)
  
                Color Scheme
                Fonts
                Background Image
                Flowchart
        Features
            Go through the Instructions
            Print existing result of enquiries
            Run new enquiry
            Delete all existing enquiry results
        Future Features
        Data Model
        Technologies Used
            Python Libraries
            Ancillary Technologies
            VSCode Extensions Used
        Testing
            PEP8 Testing
            Python Testing during Development
            Manual Testing
            HTML W3C Validator
                HTML Validation Outcome
                CSS Validation Outcome
            Lighthouse
        Bugs
            Current Bugs
            Resolved Bugs
        Deployment
        Credits
            Content
            Code
            Media
            Acknowledgements
