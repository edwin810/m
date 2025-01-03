extends Spatial

onready var car_mesh = $car_mesh

var body_index = 0 
var cars_count = 0 

func _ready():
	#CoinsManager.add_coins(10000)
	cars_count = car_mesh.car_bodyes.size()
	load_car()
	$control/coins_label.text = str(CoinsManager.get_current_coins())
	SignalManager.connect("coins_updated", self, "_on_coins_updated")
	
func load_car():
	var info = InfoManager.load_player_info()
	var car_price = get_car_price()
	var available_coins = CoinsManager.get_current_coins()
	var own_car = body_index in info.owned_cars
	var used_car = info.car_body_index
	car_mesh.load_body(body_index)
	
	$control/own_checkmark.visible = used_car == body_index
	$control/button_buy.text = "Buy " + str(car_price)
	$control/button_buy.disabled = (car_price > available_coins)
	$control/button_buy.visible = !own_car
	$control/button_use.visible = own_car and used_car != body_index
	
func get_car_price():
	return (body_index + 1) * 100
		
func _on_button_next_pressed():
	body_index += 1
	
	if body_index >= cars_count:
		body_index = 0
	$store_level/win_particles.emitting = false
	load_car()

func _on_button_prev_pressed():
	body_index -= 1
	
	if body_index < 0:
		body_index = cars_count - 1
	$store_level/win_particles.emitting = false
	load_car()

func _on_button_buy_pressed():
	var car_price = get_car_price()
	var available_coins = CoinsManager.get_current_coins()
	if car_price > available_coins:
		print("not enugth coins")
		return
	
	set_player_car(body_index)
	CoinsManager.remove_coins(car_price)
	$store_level/win_particles.emitting = true
	load_car()

func _on_button_use_pressed():
	set_player_car(body_index)
	load_car()
		
func set_player_car(car_body_index):
	var info = InfoManager.load_player_info()
	info.car_body_index = car_body_index
	if !info.owned_cars.has(car_body_index):
		info.owned_cars.append(car_body_index)
	InfoManager.save_player_info(info)
		
func _on_button_back_to_menu_pressed():
	get_tree().change_scene("res://scenes/main.tscn")

func _on_coins_updated(coins):
	$control/coins_label.text = str(coins)


