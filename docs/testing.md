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
    - [**Public Booking Acceptance Test**](#public-booking-acceptance-test)
      - [P1. Public user want a user-friendly interactive website](#p1-public-user-want-a-user-friendly-interactive-website)
      - [P2. Public user want to be able to access the website using different devices for same friendly experience](#p2-public-user-want-to-be-able-to-access-the-website-using-different-devices-for-same-friendly-experience)
      - [P3. Public user has option to select number of people for the dinner](#p3-public-user-has-option-to-select-number-of-people-for-the-dinner)
      - [P4. Public user can see the buffet price](#p4-public-user-can-see-the-buffet-price)
      - [P5. Public user can have time options to select from on a chosen date](#p5-public-user-can-have-time-options-to-select-from-on-a-chosen-date)
      - [P6. Public user can make booking so that the dinner time is confirmed](#p6-public-user-can-make-booking-so-that-the-dinner-time-is-confirmed)
      - [P7. Public user can see images and descriptions of buffet types](#p7-public-user-can-see-images-and-descriptions-of-buffet-types)
      - [P8. Public user can cancel a booking](#p8-public-user-can-cancel-a-booking)
      - [P9. Public user can view booking history](#p9-public-user-can-view-booking-history)
      - [P10. Public user can receive email notifications](#p10-public-user-can-receive-email-notifications)
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

### **Public Booking Acceptance Test**

#### P1. Public user want a user-friendly interactive website

1. **Booking details are visible on home page**

- Open a web browser
- Input the Graces Buffet url (https://graces-buffet.herokuapp.com/)
- The booking details is shown on the home page when the site is opened

2. **Responsive in mobile and desktop browsers**

- Open the URL address of the website in desktop computer, laptop computer, iphone, ipad, samsung phone.
- The application is responsive and user can effectively complete a booking

![Graces Buffet Website](/docs/images/test/small_width_device.png)
Graces Buffet website opened in a small width Samsung phone
The responsiveness was well tested using the Google Chrome developer tools to simulate different screen widths.

3. **Feedback on user actions are given**

- Login as public user
- Input a date that is in the past
- Application responds with error message that dinner date cannot be earlier than today

![Dinner Date message](/docs/images/test/dinner_date_earlier.png)

Similarly when trying to book without logging in, booking is cancelled, booking is successfully done, login is successful, log out is successful and others, appropriate message is displayed to the user.

![Login Required](/docs/images/test/login_required.png)

4. User finds links to navigate to other functions easy

- Open the website
- Login successfully
- Icons on the right edge of the page have tooltips that describe their purpose
- Icons with dropdown menu are indicated with down pointing arrow
- There is also linkage from Upcoming Booking to edit or cancel the booking.
![Nav Icons](/docs/images/test/icons_menu.png)

5. Font is legible

All fonts are legible when any page is displayed. Accessibility report from Lighthouse shows between 81% to 98% on each of the pages of the website.

![Accessibility Report](/docs/images/test/access.png)

6. Color contrast is effective

The contrast was okay as the accessibility report above shows.

#### P2. Public user want to be able to access the website using different devices for same friendly experience

1. Website is accessible on different sized devices

This requirements were met with tests reported on P1 2. above.

1. Information is easy to find both on small and large screens

This requirements were met with tests reported on P1 2. above.

#### P3. Public user has option to select number of people for the dinner

1. On the booking form a selection box is available with options for number of people

- Open the Graces Buffet website
- Click on the dropdown having people icon
- User can select the desired number of persons limited by the number set by the Admin

![Select people](/docs/images/test/select_people.png)

#### P4. Public user can see the buffet price

1. The booking form displays the price per person

The Price per Person is displayed in big font on the home page immediately before the booking form.

#### P5. Public user can have time options to select from on a chosen date

1. On the booking form a selection box is available with options for available time slots

- Open the Graces Buffet website
- Click on the dropdown having clock icon
- User can select the desired time slot. Available time slots are maintained by the Admin.

![Select Time](/docs/images/test/select_time.png)

Beyond the user story requirement, the time slot selected is validated to ensure it is not in the past when the dinner date is same date as system date.

![Time Validation Message](/docs/images/test/dinner_time_earlier.png)

#### P6. Public user can make booking so that the dinner time is confirmed

1. Booking form is available to user

The booking form is immediately available once the website is opened.

2. Signup form is available to user

- Open the Graces Buffet website
- At the right edge of the home page, the signup and login icons are visible. These icons are hidden once a user has logged into the website.

![Signup Icon](/docs/images/test/signup_icon.png)

- Click on the Sign Up and the Signup form is displayed for the user to input the username, email address and names.
- Email is sent to user to confirm the email address provided.
- Click on the link in the email received and you are set to login successfully.

1. A signed-in user can save a booking and receive immediate confirmation plus an email

- Open the Graces Buffet website
- Signup if you have not done so
- Login to the application
- Click calendar icon on the booking form and select a dinner date
- Click on the clock icon and select a time slot for the dinner
- Click on the people icon and select number of people for the dinner
- Click on one or more cuisine choices
- Click Let's Go button

Several validations are carried out by the application.
a. The date is validated to ensure it is not in the past
b. The time is validated to ensure it is not in the past if the date is today
c. The cuisine choices are validated to ensure the user selected at least one cuisine
d. Validation is done on the available seats for the selected time slot. In doing this validation consideration is given for seats that are occupied  before and after the selected time slot +/- the estimated buffet service period.

Various validation messages are shown below:

![Booking Validations](/docs/images/test/booking_validations.png)

To test the fully booked validation:

1. Make a booking for a given date and time, say 2 July 2022 @ 14:00:00 and 10-people seating or maximum available.
2. Repeat the booking in 1 a few times and you will get the fully booked message when the seats available are less than the people you desire to book.
3. Try again with a different time for same day and you may get booked if seats are available for that different time.

A confirmation page is displayed showing the user the details of the booking once it is successful. An email is also sent to the primary email address of the user.

![Booking confirmation page](/docs/images/test/booking_confirm_page.png)

#### P7. Public user can see images and descriptions of buffet types

1. Images and description of buffet types available on the booking page

- Open the Graces Buffet website
- Name, image and description of available buffets are displayed on the booking form. The buffet types including the images are entered by the Admin via the Admin panel.

#### P8. Public user can cancel a booking

1. Menu has option for cancel booking
2. Cancel booking page has details of all active bookings
3. A button is available to click and cancel desired booking
4. Feedback is given and list of bookings updated immediately
To test the items 1 to 4 proceed as follows:

- Open the Graces Buffet website
- Signup if you have not done so
- Login to the application
- Click on the User Account menu via the people icon dropdown
- Click on the Cancel Booking menu item
A list of all the active bookings are displayed.
- Click on the booking to be cancelled and a confirmation modal window is displayed with Okay or Cancel option.
- Click on the Okay button and the booking is canceled, the page is refreshed with the booking no longer on the list.
An email is also sent to the user on the cancellation, plus an entry in the Notifications record for the user.

![Booking cancellation](/docs/images/test/cancel_booking.png)

#### P9. Public user can view booking history

1. Option for booking history available on the menu
2. Booking history page contains details of all previous bookings

- Open the Graces Buffet website
- Signup if you have not done so
- Login to the application
- Click on the User Account menu via the people icon dropdown
- Click on Dining History and a list of all bookings make by the user is displayed except any fulfilled ones that may have been deleted by the Admin.

![Dining History](/docs/images/test/dining_history.png)

#### P10. Public user can receive email notifications

1. Email is received upon confirmation/cancellation of booking
When a user goes through the P6 or P8 tests above to make or cancel a booking email is sent resembling the sample below:

![Booking Email Confirmation](/docs/images/test/booking_confirm_email.png)

### **Authentication Acceptance Test**

#### U1. User account creation

1. Signup option is available to user on the home page and when trying to complete a booking
2. Successful signup will enable user login with the created email and password

These criteria have been tested via P6 above. Signup is available once the website opens. If a user is already signed in, the signup icon is no longer available and its is replace by the Logout icon.

#### U2. User sign in and sign out easily

1. Sign-in link available on home page
2. Sign-in page opens when link is clicked
3. Full user menu is available when successfully signed in
4. Logout link is available
5. Logout confirmation is requested before user is logged out.

- Open the Graces Buffet website
- Click on the Login option on the right edge of the page
- A Sign in page is displayed where username or email address and password is entered.
- Enter a wrong password and error message is displayed informing the user of the wrong entry.
- Enter the correct username/email and password and the success message is displayed
- User first name is display along full menu for the user depending on the group profile the user belongs to.
  
![User Sign in](/docs/images/test/signin.png)

After successful sign in the user menu is available through the icons at the right edge of the page.

- Click on the logout icon and a logout confirmation page is opened.
- Click Sign out button to confirm the log out or Cancel to remain signed in.

![User Log out](/docs/images/test/signout.png)

#### U3. Registered user can change password

1. Reset password link available at sign-in page
2. Reset password page opens and enables user successfully reset password

- Click the Login icon
- Sign in page opens
- Click the Forgot Password
A Reset password page is opened
- Enter an email address where the password reset link will be sent
- Click on the link in the received email
- Enter new password and repeat password.
- You are logged in if the passwords match.


#### U4. User can update profile

1. Profile option available to signed in user
2. Profile page opens and enables user to change names/phone or email as needed

### Operator Role Acceptance Tests

#### O1. Operator can cancel bookings

1. Menu option for cancel booking available
2. Ability to select all active bookings
3. Button to pick and cancel a booking
4. Confirmation to proceed with the cancellation
5. Feedback message on successful cancellation
6. Updated list of active bookings

#### O2. Operator can Update Booking Status

1. Menu option for update booking is available
2. A page is provided where active bookings are displayed
3. Buttons are provided to click and select to update status
4. Status of booking changes after confirmation of status change

#### O3. Operator Make Booking for Customer

1. Make booking option is available for operator
2. Operator can find the customer using phone or email address
3. Successful booking visible on booking history enquiry

#### O4. Operator Make enquiry on bookings

1. Booking history enquiry available
2. Query has options to select date range and booking status
3. List of data is displayed meeting the given criteria

### Site owner/Admin Acceptance Tests

#### **A1. Admin can assign user role to registered users**

1. Options for user role is available on the user profile
2. Setting the user role restricts the user to the assigned role

#### A2. Admin can set system preferences

1. System preferences available in the Admin panel
2. Changes made affect the working of the application

#### A3. Admin can cancel bookings where necessary

1. Admin is able to cancel bookings same like the Operator role

#### A4. Admin can update bookings where necessary

1. Admin is able to update bookings same like the Operator role

#### A5. Admin can maintain buffet categories

1. Buffet types table available for maintenance in Admin panel
2. Changes made at the Admin panel reflects on the main site

#### A6. Admin can maintain table/seat types and quantities available

1. Table/Seats available to update on the Admin panel
2. Changes made at the Admin panel reflects on the main site
