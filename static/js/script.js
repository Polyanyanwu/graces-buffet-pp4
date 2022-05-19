const start_up = function () {
    messageTimeout();

};

//after document has loaded, call the init function
document.addEventListener("DOMContentLoaded", start_up);

const messageTimeout = function () {
    const messages = document.querySelectorAll('.messages');
    for (let msg of messages) {
        setTimeout(function () {
            const alert = new bootstrap.Alert(msg);
            alert.close();
        }, 15000); // 15 seconds
    }

}

const Confirmation = function (message, yesFunction, noFunction) {
    let confirmBox = $("#confirmModal");
    console.log("confirmation called")
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

if(document.getElementById('confirm_delete_notification')){
    document.getElementById('confirm_delete_notification').addEventListener('click', function () {
        Confirmation("Please confirm deletion of this Notification",
            function yes() {
                document.getElementById('delete-notification-btn').click();
            },
            function no() {
                return;
            });
    });
}
