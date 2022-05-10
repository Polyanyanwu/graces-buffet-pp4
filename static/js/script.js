
const init = function () {
    messageTimeout();
};

//after document has loaded, call the init function
document.addEventListener("DOMContentLoaded", init);

const messageTimeout = function(){
    const messages = document.querySelectorAll('.messages');
    for (let msg of messages) {
        setTimeout(function () {
            const alert = new bootstrap.Alert(msg);
            alert.close();
        }, 5000); // 5 seconds
    }

}
