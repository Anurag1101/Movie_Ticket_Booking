import random
import string
class Movie:
    
    def __init__(self,movie_choice,time_slot,number):
        self.number = number
        self.movie_choice = movie_choice
        self.time_slot = time_slot
    
    def book(self):
        if self.time_slot == "morning":
            print(f"\nBOOKING CONFIRMED! You have booked {self.number} tickets for {self.movie_choice.title()}, 9:00 A.M.")
            # Generate a starting seat number between 1 and (80 - self.number) to ensure there's enough room for consecutive seats
            start_seat = random.randint(1, 20 - self.number + 1)
            # Generate consecutive seat numbers based on the starting number
            seat_numbers = [start_seat + i for i in range(self.number)]
            # Randomly select a row letter (A-M)
            row_letter = random.choices(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'], k=1)[0]
            print(f"Your Confirmed seats are in AUDI {random.randint(1,10)}, Seat Numbers: {','.join([f'{row_letter}{seat}' for seat in seat_numbers])}\n")


        elif self.time_slot == "afternoon":
            print(f"\nBOOKING CONFIRMED! You have booked {self.number} tickets for {self.movie_choice.title()}, 9:00 A.M.")
            start_seat = random.randint(1, 20 - self.number + 1)
            seat_numbers = [start_seat + i for i in range(self.number)]
            row_letter = random.choices(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'], k=1)[0]
            print(f"Your Confirmed seats are in AUDI {random.randint(1,10)}, Seat Numbers: {','.join([f'{row_letter}{seat}' for seat in seat_numbers])}\n")

        elif self.time_slot == "evening":
            print(f"\nBOOKING CONFIRMED! You have booked {self.number} tickets for {self.movie_choice.title()}, 9:00 A.M.")
            start_seat = random.randint(1, 20 - self.number + 1)
            seat_numbers = [start_seat + i for i in range(self.number)]
            row_letter = random.choices(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'], k=1)[0]
            print(f"Your Confirmed seats are in AUDI {random.randint(1,10)}, Seat Numbers: {','.join([f'{row_letter}{seat}' for seat in seat_numbers])}\n")
        else:
            print(f"\nBOOKING CONFIRMED! You have booked {self.number} tickets for {self.movie_choice.title()}, 9:00 A.M.")
            start_seat = random.randint(1, 20 - self.number + 1)
            seat_numbers = [start_seat + i for i in range(self.number)]
            row_letter = random.choices(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'], k=1)[0]
            print(f"Your Confirmed seats are in AUDI {random.randint(1,10)}, Seat Numbers: {','.join([f'{row_letter}{seat}' for seat in seat_numbers])}\n")

    
    def fare(self):
        total_fare = (300*self.number + 31*self.number)
        print(f"Total price including taxes are ₹{total_fare}")
        booking_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        print(f"Booking ID: {booking_id}")
        
        

print("Welcome to PVR Cinemas\n")
print("Available Movies are: Joker 2, Venom 3, Bhool Bhulaiyaa 3 and Singham Again\n")
print(f"4 Shows are available:\n Input 'Morning' for Morning Show(9:00 A.M.),\n Input 'Afternoon' for Afternoon Show(1:00 P.M.),\n Input 'Evening' for Evening Show(5:00 P.M.).\n Input 'Night' for Night Show(9:00 P.M.)\n")

movie_choice = input("Enter Your Movie Choice: ")
time_slot = input("Enter Your Show Timing: ")
number = int(input("Enter the number of tickets: "))
m=Movie(movie_choice,time_slot,number)   #object creation
m.book()
m.fare()

        
