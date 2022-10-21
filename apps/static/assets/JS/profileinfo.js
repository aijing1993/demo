function formatDate(date) {
    var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }
    var d = new Date(date);
    return d.toLocaleDateString("en-US",options);
}
fetch('/patientProfile')
    .then(response =>
            response.json()
     )
     .then((data) =>{
        document.getElementById("notification_pcp").innerHTML = "Dr. "+data["pcp_lname"];

     })