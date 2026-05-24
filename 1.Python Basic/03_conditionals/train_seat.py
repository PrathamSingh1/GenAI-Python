seat_type = input("Enter seat type(sleeper/AC/general/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No Ac, beds available")
    case "ac":
        print("AC - Air conditioned, cool ride")
    case "general":
        print("General - Full uncomfortbility")
    case "luxury":
        print("Luxury - Premium seats with food")
    case _:
        print("Invalid seat type")
