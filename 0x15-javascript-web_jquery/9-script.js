$(document).ready(function () {
  $.get('https://hellosalute.stefanbohacek.dev/?lang=fr', function (data) {
    $('#hello').text(data.hello);
  });
});
