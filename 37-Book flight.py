def book_flight(name, destination, booking_degree='Economy', price=500, **additional_info):
    
    
    print(f"Passenger: {name}")
    print(f"Destination: {destination}")
    print(f"Class: {booking_degree}")
    print(f"Price: {price}")
    
    if additional_info:
        print("Extra info: ")
        
        for key, value in additional_info.items():
            print(f"{key.capitalize()}: {value}")
            
book_flight('Ali', 'Dubai', seat= "B7", meal= "Chicken", drink= "Tea")
### default arguments