fetch('/patientMedications')
    .then(response => response.json()
    )
    .then(function (data) {
        generateTable(data);
    })
    .then(data=>console.log(data))
    .catch(function (err) {

    });

function generateTable(data) {
    var mainContainer = document.getElementById("medication_list");
    for (var i = 0; i < data.length; i++) {
        var div = document.createElement("div");
        div.innerHTML =
            "<td class=\"fw-600\">" + data[i].code + "</td>" +
            "<td><span class=\"badge bgc-red-50 c-red-700 p-10 lh-0 tt-c badge-pill\">" + data[i].description+ "</span> </td>" +
            "<td>" + data[i].dispenses + "</td>" +
            "<td><span class=\"text-success\">" + data[i].totalcost+ "</span></td>";
        // div.innerHTML = "<p style='margin-left:50px;margin-right:20px;'>"+data[i].code + " &#8212 " + data[i].description+"</p>";
        mainContainer.appendChild(div);
    }
}