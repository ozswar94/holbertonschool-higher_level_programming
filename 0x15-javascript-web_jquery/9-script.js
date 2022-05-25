$.get("https://fourtonfish.com/hellosalut/?lang=fr", function(data) {
	$("div#hello").append(data["hello"]);
});
