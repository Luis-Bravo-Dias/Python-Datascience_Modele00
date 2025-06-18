def all_thing_is_obj(object: any) -> int:
	obj_class = object.__class__
	if (obj_class == list):
		obj_name = "List : "
	elif (obj_class == tuple):
		obj_name = "Turple : "
	elif (obj_class == set):
		obj_name = "Set : "
	elif (obj_class == dict):
		obj_name = "Dict : "
	elif (obj_class == str):
		obj_name = object + " is in the kitchen : "
	else:
		obj_class = ""
		obj_name = "Type not found"
		
	
	print(obj_name, obj_class)
	return 42