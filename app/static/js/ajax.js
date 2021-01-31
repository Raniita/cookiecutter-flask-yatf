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
        $.getJSON(status_url, function (data) {
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
                        check_job_status(status_url);
                    }, 500);
            }
        });
    }

    // submit form
    $("#submit-regenerate_dataset").on('click', function () {
        //flash_alert("Running " + $("#task").val() + "...", "info");
        //console.log('adasdas')
        $.ajax({
            url: $SCRIPT_ROOT + "/enqueue_task/" + "regenerate_dataset",
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
                check_job_status(status_url);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                flash_alert(JSON.parse(jqXHR.responseText).message, "danger");
            }
        });
    });

     // submit form
     $("#submit-publish_sdc").on('click', function () {
        //flash_alert("Running " + $("#task").val() + "...", "info");
        //console.log('adasdas')
        $.ajax({
            url: $SCRIPT_ROOT + "/enqueue_task/" + "publish_sdc",
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
                check_job_status(status_url);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                flash_alert(JSON.parse(jqXHR.responseText).message, "danger");
            }
        });
    });

});