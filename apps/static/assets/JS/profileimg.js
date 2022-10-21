fetch('/patientImgLink')
    .then(response =>
            response.json()
     )
     .then((data) =>{
        document.getElementById("img_patient_nav").src = data[0];
        document.getElementById("img_pcp_notification").src = data[1];
        document.getElementById("img_pcp_chat").src = data[1];
        document.getElementById("img_patient_notification").src = data[0];
        document.getElementById("img_patient_chat").src = data[0];
        
     })
