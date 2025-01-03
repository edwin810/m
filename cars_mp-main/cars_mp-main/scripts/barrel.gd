extends Spatial

func _on_area_body_entered(body):
	if body is RigidBody:
		var impulse_direction = (body.global_transform.origin - global_transform.origin).normalized()
		var exploation_force_factor = -body.linear_velocity
		body.apply_impulse(Vector3(0,0,0), impulse_direction * exploation_force_factor)
		if body.get_owner() and body.get_owner().has_method("take_damage"):
			body.get_owner().take_damage()
			
	$exploitation.boom()
	queue_free()

