$(document).ready(function () {
    fetch('https://fourtonfish.com/hellosalut/?lang=fr')
      .then(response => response.json())
      .then(data => {
        $('div#hello').text(data.hello);
      });
  });
  