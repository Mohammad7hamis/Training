def create_order(name, *products, **details):
    
  print(f"Customer: {name}")
  print(f"Prosucts: {', '.join(products)}")
  
  print(f"Details: ")
  
  for key, value in details.items():
      print(f"{key.capitalize()}: {value}")
      
create_order("Mohammad", "Laptop", "Mouse", address="Riyadh", payment="Credit Card")