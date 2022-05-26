/*jshint esversion: 6 */
/*globals $:false */ // accept $ as global variable while testing with jshint

const start_up = function () {
    messageTimeout();

};

//after document has loaded, call the init function
document.addEventListener("DOMContentLoaded", start_up);

// Timeout function to delay when a message is displayed 
// to user before removing it from the screen
const messageTimeout = function () {
    "use strict";
    const messages = document.querySelectorAll('.messages');
    for (let msg of messages) {
        setTimeout(function () {
            const alert = new bootstrap.Alert(msg);
            alert.close();
        }, 10000); // 10 seconds
    }

};

// Function to run the confirmation modal window
const Confirmation = function (message, yesFunction, noFunction) {
    "use strict";
    const confirmBox = $("#confirmModal");
    confirmBox.find("#confirm-message").text(message);
    confirmBox
        .find(".confirm-yes,.confirm-no")
        .unbind()
        .click(function () {
            confirmBox.hide();
        });
    confirmBox.find(".confirm-yes").click(yesFunction);
    confirmBox.find(".confirm-no").click(noFunction);
    confirmBox.show();
};

// confirmation for single row of data
if(document.getElementById('confirm_delete_notification')){
    document.getElementById('confirm_delete_notification').addEventListener('click', function () {
        "use strict";
        const msg = document.getElementById('confirm_delete_notification').dataset.message;
        Confirmation(msg,
            function yes() {
                document.getElementById('delete-notification-btn').click();
            },
            function no() {
                return;
            });
    });
}


// Confirmation of cancellation of booking by Customer 
// for multiple rows
if(document.querySelectorAll('.confirmation-btn')){
    const rec_btn = document.querySelectorAll('.confirmation-btn');
    rec_btn.forEach(btn => btn.addEventListener('click', function(e){
        "use strict";
        const msg = e.target.dataset.message;
        Confirmation(msg,
            function yes() {
                const booking_id = e.target.dataset.bookingId;
                document.getElementById("cancel_booking_id").value = booking_id;
                document.getElementById('cancel-booking-btn').click();
            },
            function no() {
                return;
            });
    }));
}


// Confirm removal of user group
if(document.querySelectorAll('.confirm_remove_notification')){
    const rec_btn = document.querySelectorAll('.confirm_remove_notification');
    rec_btn.forEach(btn => btn.addEventListener('click', function(e){
        "use strict";
        const msg = e.target.dataset.message;
        Confirmation(msg,
            function yes() {
                document.getElementById("user_group_name").value = e.target.dataset.group;
                document.getElementById('action_button').click();
            },
            function no() {
                return;
            });
    }));
}

// For Contact Us form
// If user has email pick it from the template and 
// assign to the email address field 
if(document.querySelector('#contact_us')){
    if(document.querySelector('#user_email')){
        document.querySelector('#id_sender').value = document.querySelector('#user_email').value;
    }
}

// Mark existing cuisine choices as checked
// used for Edit booking
if(document.querySelector('#cuisine-row')){
    const cuisine_el = document.getElementById('edit_cuisine_choices');
    const selected = cuisine_el.innerText.split(',');
    const cuisine_options = document.querySelectorAll('.form-check-label');
    for (let cuisine of selected){  
        for (let item of cuisine_options){
            console.log("item==", item)
            if(item.innerText.includes(cuisine.trim())){
                const close_el = item.previousElementSibling;
                close_el.setAttribute('checked', '');
            }
        }
    }
}

