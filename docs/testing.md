# **Testing of Graces Buffet Website**

[Return to README](/README.md)
- [**Testing of Graces Buffet Website**](#testing-of-graces-buffet-website)
  - [**Code Validation**](#code-validation)
    - [**W3C Validation for HTML**](#w3c-validation-for-html)
    - [**W3C Validation for CSS**](#w3c-validation-for-css)
    - [**JSHint**](#jshint)
    - [**PEP8**](#pep8)
    - [**Lighthouse**](#lighthouse)
  - [**Automated Tests**](#automated-tests)
    - [**Automated Test on Forms**](#automated-test-on-forms)
    - [**Automated Test on Models**](#automated-test-on-models)
    - [**Automated Test on Views**](#automated-test-on-views)
  - [**Manual Tests**](#manual-tests)
    - [Make Booking](#make-booking)
    - [Authenticated Public access booking](#authenticated-public-access-booking)
  - [**Authentication Acceptance Test**](#authentication-acceptance-test)
    - [U1. User account creation](#u1-user-account-creation)
    - [U2. User sign in and sign out easily](#u2-user-sign-in-and-sign-out-easily)
    - [U3. Registered user can change password](#u3-registered-user-can-change-password)
    - [U4. User can update profile](#u4-user-can-update-profile)
  - [Operator Role Acceptance Tests](#operator-role-acceptance-tests)
    - [O1. Operator can cancel bookings](#o1-operator-can-cancel-bookings)
    - [O2. Operator can Update Booking Status](#o2-operator-can-update-booking-status)
    - [O3. Operator Make Booking for Customer](#o3-operator-make-booking-for-customer)
    - [O4. Operator Make enquiry on bookings](#o4-operator-make-enquiry-on-bookings)
  - [Site owner/Admin Acceptance Tests](#site-owneradmin-acceptance-tests)
    - [**A1. Admin can assign user role to registered users**](#a1-admin-can-assign-user-role-to-registered-users)
    - [A2. Admin can set system preferences](#a2-admin-can-set-system-preferences)
    - [A3. Admin can cancel bookings where necessary](#a3-admin-can-cancel-bookings-where-necessary)
    - [A4. Admin can update bookings where necessary](#a4-admin-can-update-bookings-where-necessary)
    - [A5. Admin can maintain buffet categories](#a5-admin-can-maintain-buffet-categories)
    - [A6. Admin can maintain table/seat types and quantities available](#a6-admin-can-maintain-tableseat-types-and-quantities-available)

## **Code Validation**

Code validations have been thoroughly done on all files in the application: HTML, CSS, Javascript and Python and all have been very successful. Below are evidence of the tests.

### **W3C Validation for HTML**

The [W3C Markup Validation Service](https://validator.w3.org/) was used to check the website for validation errors using the live URL (https://graces-buffet.herokuapp.com/). The results show no errors and the html codes are valid.

![HTML Validation](/docs/images/code_test/html_validation.png)

### **W3C Validation for CSS**

The [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to check the CSS for any errors. The test showed no errors in the CSS text.

![CSS Validation](/docs/images/code_test/css_validation.png)

### **JSHint**

The [JSHint](https://jshint.com/) was used to validate codes from the three JavaScript files for semantic and syntax errors. No warnings or error were found.

![General Tables JavaScript](/docs/images/code_test/jshint_gen_tab.png)
![Profile JavaScript](/docs/images/code_test/jshint_profile.png)
![General Script Validation](/docs/images/code_test/jshint_script.png)

### **PEP8**

[PEP8 online](http://pep8online.com/) was used to validate all the the Python codes for semantic and syntax errors. No errors were reported and few warnings were rectified leading to no errors or warnings on all the Python codes.
I attach evidence of two out of all the PEP8 tests done.

PEP8 result for the bookings.views.py
![PEP8 for Booking View](/docs/images/code_test/pep8_booking_views.png)

PEP8 result for the bookings.test_views.py
![PEP8 for Booking Test View](/docs/images/code_test/pep8_booking_view_test.png)

### **Lighthouse**

[Lighthouse](https://developers.google.com/web/tools/lighthouse/?utm_source=devtools) available in Google Chrome DevTools, Microsoft Edge were used to test the deployed site performance, accessibility and user experience.  

![Lighthouse](/docs/images/code_test/lighthouse.png)

## **Automated Tests**

A handful of Automated tests were done on the Bookings application to corroborate the findings of the manual testing. It was a matter of insufficient time that couldn't enable us implement full automated test on the application. In the course of getting started with the automated tests, I faced challenges of using the database in Heroku as it would't permit creating of test database on the fly. Afterwards I resorted to using the Sqlite3 database locally to execute the tests.

### **Automated Test on Forms**

An automated test was used to assert that dinner date is required and forms part of the error message in the form. The test was successful and the evidence of the test is given below.
![Form test](/docs/images/code_test/test_forms.png)

### **Automated Test on Models**

The bookings form test was used to:

1. Assert that a valid user is required before writing a notification record
2. Notification record is automatically created when a booking is created
3. Email is sent to user when a booking is created successfully

The evidence of the test outcome is given below:

![Model test](/docs/images/code_test/test_model.png)

### **Automated Test on Views**

The views automated test affirmed that:

1. THe home page responds
2. Anonymous user is disallowed to post a booking
3. Check that cuisine choice is required

All the tests were successful and the evidence is given below:

![View test](/docs/images/code_test/test_views.png)

## **Manual Tests**

The application was thoroughly tested at each step of the development process and guided by the agreed Acceptance Criteria for each user story.  Below are the result and evidence of the manual testing of all aspects of the application, some done at development stage and others after deployment. The tests cover all the user stories developed at the beginning of the project and those that came in the process of the development.

### Make Booking

Several test were made on the booking functionality:

1. Test that the user is logged in before confirming a booking.
2. Test dropdown time options is available on booking form
3. Buffet price is available on booking form.
4. Select number of people on booking form.
5. Test that dinner date is not earlier than today
6. Display details of buffet types
7. Test that if dinner date is today, dinner time cannot be earlier than now
8. Check for available seats on the given date and time.
9. Test that the user is directed to booking confirmation page after a successful booking.
10. Test that booking confirmation email is sent.
11. Access site on different device.
12. Booking form is available to user

### Authenticated Public access booking

1. Test view booking history
2. Cancel booking
3. Can view notifications
4. Menu has option for cancel booking
5. Cancel booking page has details of all active bookings
6. A button is available to click and cancel desired booking
7. Feedback is given and list of bookings updated immediately
8. Option for booking history available on the menu
9. Booking history page contains details of all previous bookings
10. Email is received upon confirmation/cancellation of booking

## **Authentication Acceptance Test**

### U1. User account creation

1. Signup option is available to user on the home page and when trying to complete a booking
2. Successful signup will enable user login with the created email and password

### U2. User sign in and sign out easily

1. Sign-in link available on home page
2. Sign-in page opens when link is clicked
3. Full user menu is available when successfully signed in

### U3. Registered user can change password

1. Reset password link available at sign-in page
2. Reset password page opens and enables user successfully reset password

### U4. User can update profile

1. Profile option available to signed in user
2. Profile page opens and enables user to change names/phone or email as needed

## Operator Role Acceptance Tests

### O1. Operator can cancel bookings

1. Menu option for cancel booking available
2. Ability to select all active bookings
3. Button to pick and cancel a booking
4. Confirmation to proceed with the cancellation
5. Feedback message on successful cancellation
6. Updated list of active bookings

### O2. Operator can Update Booking Status

1. Menu option for update booking is available
2. A page is provided where active bookings are displayed
3. Buttons are provided to click and select to update status
4. Status of booking changes after confirmation of status change

### O3. Operator Make Booking for Customer

1. Make booking option is available for operator
2. Operator can find the customer using phone or email address
3. Successful booking visible on booking history enquiry

### O4. Operator Make enquiry on bookings

1. Booking history enquiry available
2. Query has options to select date range and booking status
3. List of data is displayed meeting the given criteria

## Site owner/Admin Acceptance Tests

### **A1. Admin can assign user role to registered users**

1. Options for user role is available on the user profile
2. Setting the user role restricts the user to the assigned role

### A2. Admin can set system preferences

1. System preferences available in the Admin panel
2. Changes made affect the working of the application

### A3. Admin can cancel bookings where necessary

1. Admin is able to cancel bookings same like the Operator role

### A4. Admin can update bookings where necessary

1. Admin is able to update bookings same like the Operator role

### A5. Admin can maintain buffet categories

1. Buffet types table available for maintenance in Admin panel
2. Changes made at the Admin panel reflects on the main site

### A6. Admin can maintain table/seat types and quantities available

1. Table/Seats available to update on the Admin panel
2. Changes made at the Admin panel reflects on the main site
