total_seats = 350
tickets_sold = 0
total_bookings = 0
rejected_bookings = 0

while total_seats > 0:
    tickets = int(input("\nEnter number of tickets (0 to exit): "))

    if tickets == 0:
        break

    if tickets < 1 or tickets > 15:
        print("BOOKING REJECTED - Invalid ticket count")
        rejected_bookings += 1
        continue

    if tickets > total_seats:
        print("BOOKING REJECTED - Not enough seats")
        rejected_bookings += 1
        continue

    valid_booking = True

    for i in range(tickets):
        age = int(input(f"Enter age for person {i + 1}: "))

        if age < 12:
            valid_booking = False

    if valid_booking:
        total_seats -= tickets
        tickets_sold += tickets
        total_bookings += 1
        print(f"BOOKING CONFIRMED - {tickets} tickets")
    else:
        rejected_bookings += 1
        print("BOOKING REJECTED - Age restriction")

print("\nFinal Report")
print("Total Bookings:", total_bookings)
print("Total Tickets Sold:", tickets_sold)
print("Rejected Bookings:", rejected_bookings)
print("Remaining Seats:", total_seats)