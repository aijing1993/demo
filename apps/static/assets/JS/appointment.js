fetch('/allAppointments')
    .then(response =>
            response.json()
     )
     .then((data) => {

          //  document.getElementById("appointment").innerText=data[0].start;

     });
// .then((data) =>console.log(data[0].start));

fetch('/patientMedications')
    .then(response => response.json()
    )
    .then(function (data) {
       // appendData(data);
    })
    .catch(function (err) {
        console.log('error: ' + err);
    });
