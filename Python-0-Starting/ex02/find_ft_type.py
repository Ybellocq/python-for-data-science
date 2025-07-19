def all_thing_is_obj(object: any) -> int:
    object_type = type(object)
    
    if object_type is list:
        print("List : <class 'list'>")
    elif object_type is tuple:
        print("Tuple : <class 'tuple'>")
    elif object_type is set:
        print("Set : <class 'set'>")
    elif object_type is dict:
        print("Dict : <class 'dict'>")
    elif object_type is str:
        print(f"{object} is in the kitchen : <class 'str'>")
    else:
        print("Type not found")
    
    return 42