

function sort_list() {
    $("#results-panel")[0].hidden = true;

    var sort_data = {
        "list" : $("#input-list")[0].value,
        "isASC" :  $("#asc")[0].checked
   }
   console.log(sort_data);

    $.ajax({
        type: 'POST',
        dataType: 'json',
        url: "/sort",
        data: sort_data,
        success: function(data, status, jqxhr) {
            console.log(data);
            var table_string = ""
            for (var idx in data.sorted) {
                table_string = table_string.concat("<tr><td>" + data.sorted[idx] + "</td></tr>");
            }
            $("#results-table")[0].innerHTML = table_string;
            $("#results-panel")[0].hidden = false;
        },
        error: function(jqxhr, status, error) {
            alert("An error occurred.\n" + error + "\n" + status);
        }
    });
}