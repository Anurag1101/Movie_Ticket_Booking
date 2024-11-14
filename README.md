# Movie Ticket Booking System

Welcome to the **Movie Ticket Booking System!** This `Python` application allows users to book movie tickets at `PVR` Cinemas by choosing a movie, selecting a show time, and specifying the number of tickets. The application provides a simple, interactive booking experience with seat allocation, fare calculation, and booking confirmation.


## Table of Contents:

- Features

- Getting Started

- Usage

- Code Structure

- Example Workflow

- Dependencies

- Contributing

- License

Features
Movie Selection: Choose from a list of available movies.
Show Timing Selection: Select a preferred show time (Morning, Afternoon, Evening, or Night).
Seat Allocation: Generates consecutive seat numbers with a random row letter.
Fare Calculation: Calculates total fare with taxes.
Booking ID Generation: Generates a unique booking ID for each transaction.
Input Validation: Ensures correct movie selection, show time, and ticket quantity.
Getting Started
To use this project:

Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/Movie_Ticket_Booking.git
cd Movie_Ticket_Booking
Run the Script: Execute the movie_ticket_booking.py file in your terminal:

bash
Copy code
python movie_ticket_booking.py
Usage
Upon running the script, users will be prompted to enter the following details:

Movie Choice: Choose from the available movies:

Joker 2
Venom 3
Bhool Bhulaiyaa 3
Singham Again
Show Time: Enter one of the following time slots:

Morning (9:00 A.M.)
Afternoon (1:00 P.M.)
Evening (5:00 P.M.)
Night (9:00 P.M.)
Number of Tickets: Enter a number between 1 and 20.

Based on the inputs, the application will:

Confirm the booking with the chosen movie, time, and number of tickets.
Display seat numbers and AUDI allocation.
Show the total price including taxes.
Generate and display a unique booking ID.
Code Structure
The main components of this program include:

Class Movie: Handles the booking process, seat allocation, fare calculation, and validation.

__init__: Initializes the movie choice, show time, and ticket number with validation.
generate_seat_numbers: Allocates consecutive seats and a row letter.
book: Confirms booking details and seat allocation.
fare: Calculates total fare and generates a booking ID.
Main Program Flow:

Prompts the user for inputs, validates them, and initiates the booking process.
Example Workflow
text
Copy code
Welcome to PVR Cinemas

Available Movies: Joker 2, Venom 3, Bhool Bhulaiyaa 3, Singham Again

Show Timings:
  Input 'Morning' for 9:00 A.M. Show
  Input 'Afternoon' for 1:00 P.M. Show
  Input 'Evening' for 5:00 P.M. Show
  Input 'Night' for 9:00 P.M. Show

Enter Your Movie Choice: Joker 2
Enter Your Show Timing: Evening
Enter the number of tickets: 3

BOOKING CONFIRMED! You have booked 3 tickets for 'Joker 2' at 5:00 P.M.
Your confirmed seats are in AUDI 7, Seat Numbers: D12, D13, D14

Total price including taxes: ₹993
Booking ID: X8H2J9K3
Dependencies
No external libraries are required; only Python's standard library is used:

random: For random seat and booking ID generation.
string: For generating a random booking ID.
Contributing
If you'd like to contribute to this project:

Fork the repository.
Create a feature branch.
Commit your changes.
Push to the branch.
Open a pull request.
License
This project is licensed under the MIT License.
