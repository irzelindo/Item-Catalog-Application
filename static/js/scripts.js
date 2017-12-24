// Material Select Initialization
$(document).ready(function() {
  $('.mdb-select').material_select();
});

window.setTimeout(function() {
  $(".alert").fadeTo(500, 0).slideUp(500, function() {
    $(this).remove();
  });
}, 3000);