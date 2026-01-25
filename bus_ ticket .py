def bus_ticket():
    print("===== Welcome to Bus Ticket Booking =====\n")
    

    name = input("Enter your name: ")
    source = input("Enter source city: ")
    destination = input("Enter destination city: ")
    date = input("Enter travel date (DD-MM-YYYY): ")
    

    try:
        seats = int(input("Enter number of seats: "))
        if seats <= 0:
            print("Invalid number of seats!")
            return
    except ValueError:
        print("Please enter a valid number!")
        return
    
    #  (assume 1 seat = 500 Rs)
    price_per_seat = 500
    total_price = seats * price_per_seat
    
  
    print("\n===== BUS TICKET =====")
    print(f"Name       : {name}")
    print(f"From       : {source}")
    print(f"To         : {destination}")
    print(f"Date       : {date}")
    print(f"Seats      : {seats}")
    print(f"Price/Seat : Rs {price_per_seat}")
    print(f"Total Price: Rs {total_price}")
    print("======================")
    print("Have a safe journey!")


bus_ticket()
