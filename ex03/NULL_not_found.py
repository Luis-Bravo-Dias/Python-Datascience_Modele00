def NULL_not_found(object: any) -> int:
	obj_class = object.__class__
	if (obj_class == type(None)):
		obj_name = "Nothing:"
	elif ((obj_class == float) & (object != object)):
		obj_name = "Cheese:"
	elif ((object == 0) & (obj_class == int)):
		obj_name = "Zero:"
	elif (object == ""):
		obj_name = "Empty:"
	elif ((object == False) & (obj_class == bool)):
		obj_name = "Fake:"
	else:
		object = ""
		obj_class = ""
		obj_name = "Type not found"
		
	
	print(obj_name, object, obj_class)
	return 1