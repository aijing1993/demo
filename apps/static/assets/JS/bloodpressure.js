fetch('/pressureLow')
    .then(response =>
            response.json()
     )
     .then((data) =>document.getElementById("first_pressure_low").innerHTML=data[0].value)
    .then((data)=>document.getElementById("first_date").innerHTML=data[0].date);
// .then((data) =>console.log(data[0].start));

fetch('/pressureHigh')
    .then(response =>
            response.json()
     )
     .then((data) =>document.getElementById("first_pressure_high").innerHTML=data[0].value);