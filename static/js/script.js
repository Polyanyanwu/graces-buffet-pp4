const start_up = function () {
    messageTimeout();
 
};

//after document has loaded, call the init function
document.addEventListener("DOMContentLoaded", start_up);

const messageTimeout = function(){
    const messages = document.querySelectorAll('.messages');
    for (let msg of messages) {
        setTimeout(function () {
            const alert = new bootstrap.Alert(msg);
            alert.close();
        }, 15000); // 15 seconds
    }

}
