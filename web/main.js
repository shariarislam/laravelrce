function Exploit() {
	var url = document.getElementById("url").value
	var command = document.getElementById("command").value
	if (command == "clear" || command == "cls") {
		response("")
	}
	else{
		eel.run(url,command)(response)
	}
}

function response(result) {
	document.getElementById("result").innerHTML = result
}