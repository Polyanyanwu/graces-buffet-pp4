"use strict";

const init = function () {
    // For the update of profile, make the email address readOnly
    // and set required to the name fields
    if(document.querySelector("#profile-update-form")){
        document.querySelector("#id_email").readOnly = true;
        document.querySelector("#id_first_name").setAttribute("required", "");
        document.querySelector("#id_last_name").setAttribute("required", "");
    }
    

    // For User Group Update
    // When a user is selected, click the hidden button to send the 
    // post request to the server to retrieve the user groups
if (document.querySelector("#group-update-form")){
    if (!document.querySelector("#id_user").value){
        document.querySelector("#id_user").value = document.querySelector("#user_id").value
    }
    document.querySelector("#id_group_name").required = false;
    document.querySelector("#id_user").addEventListener('change', (e)=>{
        e.preventDefault();
        document.getElementById('user-change-button').click();
    })
}
};

//after document has loaded, call the init function
document.addEventListener("DOMContentLoaded", init);


