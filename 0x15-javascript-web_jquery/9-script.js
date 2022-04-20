    <script>
    $(document).ready(function() {
	$.get("https://fourtonfish.com/hellosalut/?lang=fr", function(data, status) {
	    if (status === 'success') {
		$('#hello').text(data.hello);
	    }
	});
    });
      </script>
