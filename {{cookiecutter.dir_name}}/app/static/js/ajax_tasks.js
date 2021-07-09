$(document).ready(function () {

    // flash an alert
    // remove previous alerts by default
    // set clean to false to keep old alerts
    function flash_alert(message, category, clean) {
        if (typeof (clean) === "undefined") clean = true;
        if (clean) {
            remove_alerts();
        }
        var htmlString = '<div class="alert alert-' + category + ' alert-dismissible" role="alert">'
        htmlString += '<button type="button" class="close" data-dismiss="alert" aria-label="Close">'
        htmlString += '<span aria-hidden="true">&times;</span></button>' + message + '</div>'

        $(htmlString).prependTo("#mainContent").hide().slideDown();
    }

    function remove_alerts() {
        $(".alert").slideUp("normal", function () {
            $(this).remove();
        });
    }

    // Check Job Status. Arg == URL to ask
    function check_job_status(status_url) {
        // Fix to avoid CORS on local
        url = 'http://' + status_url.split('//')[1]
        //console.log(url)
        
        //$.getJSON(status_url, function (data) {
        $.getJSON(url, function (data) {
            //console.log(data);
            switch (data.status) {
                case "unknown":
                    flash_alert("Unknown job id", "danger");
                    $("#submit").removeAttr("disabled");
                    break;
                case "finished":
                    flash_alert(data.result, "success");
                    $("#submit").removeAttr("disabled");
                    break;
                case "failed":
                    flash_alert("Job failed: " + data.message, "danger");
                    $("#submit").removeAttr("disabled");
                    break;
                default:
                    // queued/started/deferred
                    // Here set the timeout. Default == 500
                    setTimeout(function () {
                        check_job_status(url);
                    }, 500);
            }
        });
    }

    // submit form
    $("#submit-hello_task").on('click', function () {
        //flash_alert("Running " + $("#task").val() + "...", "info");
        //console.log('adasdas')
        //console.log($SCRIPT_ROOT)
        $.ajax({
            url: $SCRIPT_ROOT + "/api" + "/enqueue_task/" + "hello_task",
            //data: $("#taskForm").serialize(),
            method: "POST",
            //dataType: "json",
            //success: function (data) {
            //    flash_alert("Task enqueued", "success");
            //},
            success: function (data, status, request) {
                $('#submit').attr("disabled", "disabled");
                flash_alert("Running Task", "primary");
                var status_url = request.getResponseHeader('Location');
                // Query to URL
                //console.log(status_url)
                check_job_status(status_url);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                flash_alert(JSON.parse(jqXHR.responseText).message, "danger");
            }
        });
    });
});