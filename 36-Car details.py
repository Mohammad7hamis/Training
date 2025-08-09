def car_details(name_of_car, model_of_car, *additional, **additional_specifications):
    
    print(f"Car: {name_of_car} {model_of_car}")
    if additional:
        print("Features:", ", ".join(additional))
        
    if additional_specifications:
        print("Details:")
        
        for key, value in additional_specifications.items():
            print(f"{key}: {value}")


car_details("Toyota", "Corolla", "Sunroof", "Leather Seats", Color= "Red", Year= 2024)