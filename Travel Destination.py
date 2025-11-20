destinations = []
print("Enter 5 travel destinations:")
for d in range(5):
    destinations.append(input(f"Destination {d+1}: "))
print("Original Travel Itinerary:")
for i in range(5):
    print(f"{i+1}. {destinations[i]}")
print("Update the 2nd and 5th destinations.")
destinations[1] = input("New destination for position 2: ")
destinations[4] = input("New destination for position 5: ")
print("Updated Travel Itinerary:")
for i in range(5):
    print(f'{i+1}, {destinations[i]}')
