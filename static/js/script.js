
const init = function () {
    messageTimeout();
};

//after document has loaded, call the init function
document.addEventListener("DOMContentLoaded", init);

const messageTimeout = function(){
    setTimeout(function () {
        const messages = document.getElementById('messages');
        const alert = new bootstrap.Alert(messages);
        alert.close();
    }, 10000); // 10 seconds
}
