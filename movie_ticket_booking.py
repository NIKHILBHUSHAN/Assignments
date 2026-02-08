maxtickets=350
remainingtickets=350
totalbooking=0
ticketssold=0
rejectedbookings=0
while remainingtickets>0:
    tickets=int(input("Enter no of tickets (1-15):"))
    if tickets==0:
        break

    if tickets<0 or tickets>maxtickets:
        print("Inavalid ticket Count")
        rejectedbookings+=1
        continue
    if tickets>remainingtickets:
        print("Not enough seats available")
        rejectedbookings+=1
        continue
    valid=True
    for i in  range(tickets):
        age=int(input(f"Enter age of person{i+1}: "))
        if age<=12:
            valid=False
            break
    if not valid:
            print("Booking rejected - age restriction")
            rejectedbookings+=1
            continue
    print(f"Booking confirmed-{tickets} tickets ")
    totalbooking+=1
    remainingtickets-=tickets
    ticketssold+=tickets

    if remainingtickets==0:
        break

print("Final report:")
print(f"Tickets sold: {ticketssold}")
print(f"Total Bookings: {totalbooking}")
print(f"Total remaining seats: {remainingtickets}")
print(f"Rejected bookings:{rejectedbookings}")
