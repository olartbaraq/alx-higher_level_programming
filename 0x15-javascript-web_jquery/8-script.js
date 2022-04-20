    <script>
    $(document).ready(function() {
	$.get("https://swapi-api.hbtn.io/api/films/?format=json", function(data, status) {
	    if (status === 'success') {
		let movies = data.results;
		for (let i in movies) {
		    films = movies[i];
		    $('ul').append('<li>' + films.title + '</li>');
		}
	    }
	});
    });
      </script>
