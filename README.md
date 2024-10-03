**Movie Ticket Booking System**

This is a simple Python program that simulates the process of booking movie tickets. It allows users to select a movie, choose a time slot, specify the number of tickets, and receive seat allocations and a fare summary. The program also generates a unique booking ID for each transaction.

**Features**
i. **Movie Selection:** Choose from a list of available movies.
ii. **Show Timings:** Select from multiple time slots (morning, afternoon, evening, and night).
iii. **Ticket Booking:** Enter the number of tickets, and the system assigns random, consecutive seat numbers.
iv. **Seat Allocation:** Seats are allocated with both row letters and seat numbers.
v. **Fare Calculation:** Includes the ticket price and taxes.
vi. **Booking ID Generation:** A unique 8-character alphanumeric booking ID is generated for each booking.

**How to Run the Program
Prerequisites:**

Make sure you have Python installed on your system. You can download it from python.org.
Clone the Repository: git clone https://github.com/Anurag1101/Movie_Ticket.git
Navigate to the Project Directory: cd Movie_Ticket
Run the Program: Run the Python file to start booking tickets: python movie_ticket_booking.py

How the Program Works
Welcome Screen: The program displays a welcome message from PVR Cinemas and lists the available movies (Joker 2, Venom 3, Bhool Bhulaiyaa 3, Singham Again).

**Input:**

Users enter their choice of movie.
Users select the show timing by inputting one of the following: Morning, Afternoon, Evening, or Night.
Users enter the number of tickets they wish to book.
Booking Confirmation:
Based on the user's input, the system confirms the movie, show time, and allocates random, consecutive seat numbers in one of the auditoriums.
Example of seat allocation: AUDI 5, Seat Numbers: A1, A2, A3.

Fare Calculation: Each ticket costs ₹300, with an additional tax of ₹31 per ticket.
The total fare is displayed to the user, including taxes.

Booking ID: A unique 8-character booking ID is generated, consisting of random letters and numbers.

**Example Interaction**:
Welcome to PVR Cinemas

Available Movies are: Joker 2, Venom 3, Bhool Bhulaiyaa 3, and Singham Again

4 Shows are available:
 Input 'Morning' for Morning Show (9:00 A.M.),
 Input 'Afternoon' for Afternoon Show (1:00 P.M.),
 Input 'Evening' for Evening Show (5:00 P.M.),
 Input 'Night' for Night Show (9:00 P.M.).

Enter Your Movie Choice: Joker 2
Enter Your Show Timing: Evening
Enter the number of tickets: 3

BOOKING CONFIRMED! You have booked 3 tickets for Joker 2, 5:00 P.M.
Your Confirmed seats are in AUDI 5, Seat Numbers: A1, A2, A3

Total price including taxes is ₹993
Booking ID: XJ4K8G7W

**Future Enhancements**:
Add more movies and show timings.
Allow for seat selection by the user.
Implement discount codes or special offers.
Integrate with a GUI for a better user experience.
**License**:
This project is licensed under the MIT License - see the LICENSE file for details




