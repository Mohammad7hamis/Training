def make_order(name, order_type="Pizza", pieces=1, *side_orders):

        print(f"Hello {name}!")
        print(f"You ordered {pieces} pieces of {order_type}.")
        
        if side_orders:
            print("Side orders:", ", ".join(side_orders))
make_order("Mohammad", "Naget", 5, "Ketchup", "Salat",)