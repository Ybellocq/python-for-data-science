def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None", type(object))
        return 0
    elif str(object) == 'nan':
        print("Cheese: nan", type(object))
        return 0
    elif object is False:
        print("Fake: False", type(object))
        return 0
    elif object == 0 and type(object) is int:
        print("Zero:", object, type(object))
        return 0
    elif object == "" and type(object) is str:
        print("Empty:", type(object))
        return 0
    else:
        print("Type not Found")
        return 1

