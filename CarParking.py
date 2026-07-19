import re

PATTERN = r"^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$"


def validate_car_number(car_number):
    car_number = car_number.strip().upper()

    if len(car_number) != 10:
        print("Check Your Car Number")
        return None

    if not re.match(PATTERN, car_number):
        print("Your Car Number Is Not Matched With Pattern")
        return None

    return car_number


def get_valid_slot(prompt, available_slots):
    while True:
        try:
            slot_number = int(input(prompt))
        except ValueError:
            print("Please Enter A Valid Slot Number")
            continue

        if slot_number in available_slots:
            return slot_number

        print(f"Slot {slot_number} Is Not Available. Available Slots: {available_slots}")


def main():
    try:
        number_slots = int(input("Number Of Slots In Your Home:-"))
    except ValueError:
        print("Please Enter A Valid Number Of Slots")
        return

    if number_slots <= 0:
        print("Number Of Slots Must Be Greater Than Zero")
        return

    slot_numbers = []
    for index in range(number_slots):
        while True:
            try:
                slot_number = int(input(f"Enter The Slot Number {index + 1} :- "))
            except ValueError:
                print("Please Enter A Valid Slot Number")
                continue

            if slot_number in slot_numbers:
                print("Slot Number Already Exists. Enter A Different One.")
                continue

            slot_numbers.append(slot_number)
            break

    print("The Slot Numbers Are:-", slot_numbers)

    available_slots = sorted(slot_numbers)
    occupied_slots = []
    car_parking_details = {}

    while available_slots:
        print("\n1 - Enter")
        print("2 - Exit")
        print("3 - Show Parked Cars")
        print("4 - Quit")

        try:
            option = int(input("Enter The Option Between 1 & 4 :- "))
        except ValueError:
            print("Please Enter A Valid Option")
            continue

        if option == 1:
            incoming_car = input("Enter Your Car Number:-")
            incoming_car = validate_car_number(incoming_car)
            if incoming_car is None:
                continue

            if incoming_car in car_parking_details:
                print("This Car Is Already Parked")
                continue

            parking_slot = get_valid_slot("Enter Your Parking Slot Number:-", available_slots)
            available_slots.remove(parking_slot)
            occupied_slots.append(parking_slot)
            occupied_slots.sort()

            car_parking_details[incoming_car] = parking_slot
            print(f"Your Car Has Been Parked At {parking_slot}")
            print("Car Parking Details:", car_parking_details)

        elif option == 2:
            exiting_car = input("Enter Your Car Number:-")
            exiting_car = validate_car_number(exiting_car)
            if exiting_car is None:
                continue

            if exiting_car not in car_parking_details:
                print("This Car Is Not Parked Here")
                continue

            actual_slot = car_parking_details[exiting_car]

            while True:
                try:
                    slot_to_free = int(input("Enter Your Parked Slot Number:-"))
                except ValueError:
                    print("Please Enter A Valid Slot Number")
                    continue

                if slot_to_free == actual_slot:
                    break

                print("The Slot Number Does Not Match The Car's Parked Slot")

            del car_parking_details[exiting_car]
            available_slots.append(slot_to_free)
            available_slots.sort()
            occupied_slots.remove(slot_to_free)
            print("Your Car Has Been Removed From The Parking")

        elif option == 3:
            if car_parking_details:
                print("Parked Cars:")
                for car_number, slot_number in car_parking_details.items():
                    print(f"{car_number} -> Slot {slot_number}")
            else:
                print("No Cars Are Parked Right Now")

        elif option == 4:
            print("Thank You For Using The Parking System")
            break

        else:
            print("Please Enter A Valid Option")

        print(f"The Remaining Slots Are {available_slots}")
        print(f"The Occupied Slots Are {occupied_slots}")

    if not available_slots:
        print("Parking Is Full. No More Cars Can Be Parked.")


if __name__ == "__main__":
    main()