def NULL_not_found(object: any) -> int: 
    """This functions prints the types of the different types of "null" in python""" 
    if object is None: 
        print(f"Nothing: None {type(object)}")
    elif isinstance(object, bool) and not object: 
        print(f"Fake: False {type(object)}")
    elif isinstance(object, float) and object != object:
        print(f"Cheese: nan {type(object)}")  
    elif isinstance(object, int) and object == 0: 
        print(f"Zero: 0 {type(object)}") 
    elif object == '':  
        print(f"Empty: {type(object)}") 
    else: 
        print("Type not Found")
    return 1
