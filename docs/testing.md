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

### **Manual Tests**

In order to render updated services to the public as Admin, I can maintain buffet categories (meal menu) including description, price and image of the buffet

The application was thoroughly tested at each step of the development process and guided by the agreed Acceptance Criteria for each user story.  Below are the result and evidence of the manual testing of all aspects of the application, some done at development stage and others after deployment.

Criteria: Buffet types table available for maintenance in Admin panel
          Changes made at the Admin panel reflects on the main site