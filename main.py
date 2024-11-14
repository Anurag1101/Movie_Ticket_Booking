import random
import string

class Movie:
    MOVIES = ["Joker 2", "Venom 3", "Bhool Bhulaiyaa 3", "Singham Again"]
    SHOW_TIMES = {
        "morning": "9:00 A.M.",
        "afternoon": "1:00 P.M.",
        "evening": "5:00 P.M.",
        "night": "9:00 P.M."
    }
    TICKET_PRICE = 300
    TAX = 31

    def __init__(self, movie_choice, time_slot, number):
        if movie_choice.title() not in self.MOVIES:
            raise ValueError("Invalid movie choice. Please select a movie from the available list.")
        if time_slot.lower() not in self.SHOW_TIMES:
            raise ValueError("Invalid time slot. Please select a valid show time.")
        if number <= 0 or number > 20:
            raise ValueError("Please enter a valid number of tickets (1-20).")
        
        self.movie_choice = movie_choice.title()
        self.time_slot = time_slot.lower()
        self.number = number

    def generate_seat_numbers(self):
        """Generates consecutive seat numbers and a random row."""
        start_seat = random.randint(1, 20 - self.number + 1)
        seat_numbers = [start_seat + i for i in range(self.number)]
        row_letter = random.choice('ABCDEFGHIJKLM')
        return row_letter, seat_numbers

    def book(self):
        """Prints booking confirmation with selected seats."""
        show_time = self.SHOW_TIMES[self.time_slot]
        print(f"\nBOOKING CONFIRMED! You have booked {self.number} tickets for '{self.movie_choice}' at {show_time}.")
        
        row_letter, seat_numbers = self.generate_seat_numbers()
        audi_number = random.randint(1, 10)
        seat_display = ', '.join([f"{row_letter}{seat}" for seat in seat_numbers])
        print(f"Your confirmed seats are in AUDI {audi_number}, Seat Numbers: {seat_display}\n")

    def fare(self):
        """Calculates and prints the total fare including tax, and generates a booking ID."""
        total_fare = self.number * (self.TICKET_PRICE + self.TAX)
        booking_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        print(f"Total price including taxes: ₹{total_fare}")
        print(f"Booking ID: {booking_id}\n")

# Main program flow
print("Welcome to PVR Cinemas\n")
print("Available Movies:", ", ".join(Movie.MOVIES))
print("\nShow Timings:")
for key, value in Movie.SHOW_TIMES.items():
    print(f"  Input '{key.capitalize()}' for {value} Show")

# User inputs with validation
try:
    movie_choice = input("\nEnter Your Movie Choice: ")
    time_slot = input("Enter Your Show Timing: ")
    number = int(input("Enter the number of tickets: "))
    
    # Creating Movie instance and booking tickets
    movie_booking = Movie(movie_choice, time_slot, number)
    movie_booking.book()
    movie_booking.fare()

except ValueError as e:
    print(f"Error: {e}")
