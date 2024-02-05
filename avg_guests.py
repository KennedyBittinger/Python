# Prompt the user for the number of days (positive)
while True:
    try:
        num_days = int(input("Days? "))
        if num_days > 0:
            break  # Exit the loop if a positive number is entered
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Use a for loop to prompt for the number of guests each day
total_guests = 0  # Initialize the total guests count
for day in range(1, num_days + 1):
    print()
    while True:
        try:
            guests = int(input(f"Guests? "))
            if guests >= 0:
                total_guests += guests
                break  # Exit the inner loop if a non-negative number is entered
            else:
                print("Please enter a non-negative number of guests.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            print()

# Calculate and display the average number of guests using integer division
average_guests = total_guests // num_days
print(f"\nAvg guests {average_guests}")
