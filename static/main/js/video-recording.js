

$(document).on('submit', '#post-form', function (e) {
  $("#output_text").val("");
  e.preventDefault();
  $.ajax({
    method: "POST",
    url: "/recognize_person",
    data: {input_text: $('#input_text').val()},
    success: function(data) {
      $("#output_text").val(data);
    }
  })
  });