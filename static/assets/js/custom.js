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
        $("#contact-form-new")[0].reset();
      },
    });
  });
});

jQuery.fn.center = function () {
  this.css("position", "absolute");
  this.css(
    "top",
    Math.max(
      0,
      ($(window).height() - $(this).outerHeight()) / 2 + $(window).scrollTop()
    ) + "px"
  );
  this.css(
    "left",
    Math.max(
      0,
      ($(window).width() - $(this).outerWidth()) / 2 + $(window).scrollLeft()
    ) + "px"
  );
  return this;
};

$(document).ready(function () {
  $(".video").css({
    width: $("#player").css("width"),
    height: $("#player").css("height"),
  });

  $(".button").click(function () {
    $(".video-wrapper").fadeIn("fast", function () {
      $(".video").fadeIn();
      $(".video").center();
    });
  });

  $(".video-wrapper").click(function (e) {
    if ($(e.target).is(".video-wrapper")) {
      $(".video").fadeOut(function () {
        $(".video-wrapper").fadeOut(function () {
          $(".video, .video-wrapper").css({ display: "none" });
          var src = $("#player").attr("src");
          $("#player").attr("src", "");
          $("#player").attr("src", src);
        });
      });
    }
  });

  $(document).keyup(function (e) {
    var isShown = $(".video-wrapper").css("display");

    if (isShown !== "none" && e.which == 27) {
      $(".video-wrapper").click();
    }
  });
});
