const start_up = function () {
    messageTimeout();

};

last_update_call = "";

//after document has loaded, call the init function
document.addEventListener("DOMContentLoaded", start_up);

const messageTimeout = function () {
    const messages = document.querySelectorAll('.messages');
    for (let msg of messages) {
        setTimeout(function () {
            const alert = new bootstrap.Alert(msg);
            alert.close();
        }, 10000); // 10 seconds
    }

}

const Confirmation = function (message, yesFunction, noFunction) {
    let confirmBox = $("#confirmModal");
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
        msg = document.getElementById('confirm_delete_notification').dataset.message
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
    rec_btn = document.querySelectorAll('.confirmation-btn');
    rec_btn.forEach(btn => btn.addEventListener('click', function(e){
        msg = e.target.dataset.message;
        Confirmation(msg,
            function yes() {
                booking_id = msg = e.target.dataset.bookingId;
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
    rec_btn = document.querySelectorAll('.confirm_remove_notification');
    rec_btn.forEach(btn => btn.addEventListener('click', function(e){
        msg = e.target.dataset.message;
        Confirmation(msg,
            function yes() {
                document.getElementById("user_group_name").value = e.target.dataset.group
                document.getElementById('action_button').click();
            },
            function no() {
                return;
            });
    }));
}

// If user has email pick it from the template and 
// assign to the email address field 

if(document.querySelector('#contact_us')){
    if(document.querySelector('#user_email')){
        document.querySelector('#id_sender').value = document.querySelector('#user_email').value
    }
}


// Mark existing cuisine choices as checked
// used for Edit booking
if(document.querySelector('#cuisine-row')){

    cuisine_el = document.getElementById('edit_cuisine_choices')
    selected = cuisine_el.innerText.split(',');
    cuisine_options = document.querySelectorAll('.form-check-label');
    for (cuisine of selected){  
        for (item of cuisine_options){
            if(item.innerText.includes(cuisine.trim())){
                close_el = item.previousElementSibling
                close_el.setAttribute('checked', '');
            }
        }
    }
}