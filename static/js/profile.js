const init = function () {
    document.querySelector("#id_first_name").setAttribute("required", "");
    document.querySelector("#id_last_name").setAttribute("required", "");

    if(document.querySelector("#profile-update-form")){
        document.querySelector("#id_email").readOnly = true;
    }
    
};

//after document has loaded, call the init function
document.addEventListener("DOMContentLoaded", init);

