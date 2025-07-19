import math

def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None", type(object))
        return 0
    elif str(object) == 'nan':
        print("Cheese: nan", type(object))
        return 0
    elif object == 0:
        print("Zero:", object, type(object))
        return 0
    elif object == "":
        print("Empty:", type(object))
        return 0
    elif object is False:
        print("Fake:", object, type(object))
        return 0
    else:
        print("Type not Found")
        return 1
