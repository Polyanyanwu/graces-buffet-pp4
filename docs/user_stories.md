# **User Stories for Graces Buffet Application**

[Back to README](/README.md)

- [**User Stories for Graces Buffet Application**](#user-stories-for-graces-buffet-application)
  - [**Customer Stories**](#customer-stories)
  - [**Operator Stories**](#operator-stories)
  - [**Authentication stories**](#authentication-stories)
  - [**Site Owner/Admin stories**](#site-owneradmin-stories)

## **Customer Stories**

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

## **Operator Stories**

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

## **Authentication stories**

|User Story|Acceptance Criteria|Tasks|
|:----|:----|:----|
|As a prospective user, I can to create an account so that I can complete bookings in the application.|- Signup option is available to user on the home page and when trying to complete a booking|- Create signup page|
| |-  Successful signup will enable user login with the created email and password|- Create the profile page|
| | |- Test the functionality|
| | | |
|As registered user, I can have an effective interface so that I will sign-in and sign-out easily.|- Sign-in link available on home page|- Add sign-in link to home page|
| |-  Sign-in page opens when link is clicked|- Create sign-in page|
| |- Full user menu is available when successfully signed in|- Enable full user menu to signed in user|
| | | |
|As registered user, I can change my password so that it is safe at all times.|- Reset password link available at sign-in page|- Add Reset link to sign-in page|
| |- Reset password page opens and enables user successfully reset password|- Copy and modify Django allauth files for reset password|
| | |- Adjust any needed settings and url|
| | |- Test the full flow of password reset|
| | | |
|As signed-in user, I can update information to my profile so that I have effective interaction with the application.|- Profile option available to signed in user|- Add the profile template from Django allauth|
| |- Profile page opens and enables user to change names/phone or email as needed|- Modify the template to suite custom fields|
| | |- Adjust any needed settings and url|
| | |- Test the full flow of profile change|

## **Site Owner/Admin stories**

|User Story|Acceptance Criteria|Tasks|
|:----|:----|:----|
|In order to manage access to the site as Admin, I can assign user role to registered users|- Options for user role is available on the user profile|- Modify the profile template to add user role|
| |- Setting the user role restricts the user to the assigned role |- Ensure model has user role|
| | |- Model the role descriptions|
| | | |
|In order to make the application flexible as Admin, I can set system preferences|- System preferences available in the Admin panel|- Model system preferences|
| |- Changes made affect the working of the application|- Make the model available to Admin|
| | |- Create any necessary models|
|As an Admin, I can cancel bookings where necessary so that the seats could become available to use|Admin is able to cancel bookings same like the Operator role|Add admin role to permitted roles for cancel booking|
| | | |
|As an Admin, I can update booking status so that seats could become available after service has been delivered|- Admin is able to update bookings same like the Operator role|Add admin role to permitted roles for update booking|
| | | |
|In order to render updated services to the public as Admin, I can maintain buffet categories (meal menu) including description, price and image of the buffet|- Buffet types table available for maintenance in Admin panel|- Create model for the buffet types|
| |- Changes made at the Admin panel reflects on the main site|- Update the settings and URLs to add to Admin panel|
| | |- Test the functionality|
|In order to increase/decrease the seat facilities as Admin, I can maintain table/seat types and quantities available|- Table/Seats available to update on the Admin panel|- Create model for the table/seats|
| |- Changes made at the Admin panel reflects on the main site|- Update the settings and URLs to add to Admin panel|
| | |- Test the functionality|

[Back to README](/README.md)
