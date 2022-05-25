$.get("https://swapi-api.hbtn.io/api/films/?format=json", function(data) {
	result = data["results"];
	for (let i = 0; i < result.length; i++) {
		value = result[i];
		$("#list_movies").append("<li>"+value["title"]+"</li>");
	}
});
