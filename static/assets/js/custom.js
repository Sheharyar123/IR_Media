$(document).ready(function () {
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  $("#contact-btn").on("click", function (e) {
    e.preventDefault();
    const first_name = document.querySelector("#id_first_name").value;
    const last_name = document.querySelector("#id_last_name").value;
    const email = document.querySelector("#id_email").value;
    const phone_no = document.querySelector("#id_phone_no").value;
    const subject = document.querySelector("#id_subject").value;
    const project_details = document.querySelector("#id_project_details").value;
    const csrftoken = getCookie("csrftoken");

    $.ajax({
      type: "POST",
      url: "/",
      data: {
        first_name: first_name,
        last_name: last_name,
        email: email,
        phone_no: phone_no,
        subject: subject,
        project_details: project_details,
        csrfmiddlewaretoken: csrftoken,
      },

      success: function (response) {
        if (response.status == "success") {
          swal({
            title: "Your message was sent successfully!",
            icon: "success",
          });
        } else {
          swal({
            title: "There was a problem sending your message!",
            icon: "error",
          });
        }
        $("#contact-form")[0].reset();
      },
    });
  });
});
