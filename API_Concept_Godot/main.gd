extends Node2D


var url = 'http://localhost:5000/'
var response = null
# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass

func make_request(endpoint, method, data):
	var headers = ['Content-type: application/json']
	var json = JSON.stringify(data)
	if(method == HTTPClient.METHOD_GET):
		var result = await $HTTPRequest.request(url + endpoint, headers, HTTPClient.METHOD_GET, json)
		print(response)
		return result #return error code
	elif(method == HTTPClient.METHOD_POST):
		var result = await $HTTPRequest.request(url + endpoint, headers, HTTPClient.METHOD_POST, json)
		print(response)
		return result #return error code

func _on_Update_player_button_down():
	var data = {'name': 'John doe'}
	make_request('GetPlayer', HTTPClient.METHOD_GET, data)

func _on_Damage_player_button_down():
	var data = {'name': 'John doe', 'hp': 10}
	make_request('UpdatePlayer', HTTPClient.METHOD_POST, data)

func _on_Login_button_down():
	var data = {'name': 'John doe', 'hp': 10}
	make_request('AddPlayer', HTTPClient.METHOD_POST, data)

func _on_http_request_request_completed(result, response_code, headers, body):
	var json = JSON.parse_string(body.get_string_from_utf8())
	response = json
	print("On request completed: " + str(response))
