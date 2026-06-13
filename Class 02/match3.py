name = input("What's your name?")
match name:
    case "Harry":
        print("Gryfindor")
    case "Hermione":
        print("Gryfindor")
    case "Ron":
        print("Gryfindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
