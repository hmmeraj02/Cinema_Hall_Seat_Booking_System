class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        Star_Cinema.hall_list.append(self)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        # self.entry_hall()

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)
        self.seats[id] = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

    def book_seats(self, show_id, seat_book):
        seats = self.seats.get(show_id)

        for row, col in seat_book:
            if 1 <= row <= self.rows and 1 <= col <= self.cols:
                if seats[row-1][col-1] == 0:
                    seats[row-1][col-1] = 1
                    return f"Seat ({row},{col}) is booked successfully for show {show_id}"
                else:
                    return f"Seat ({row},{col}) is already booked"
            else:
                return f"Seat ({row},{col}) is not in Hall"

    def view_show_list(self):
        return self.show_list

    def view_available_seats(self, show_id):
        available_seats = []
        seats = self.seats.get(show_id)
        for row in range(self.rows):
            for col in range(self.cols):
                if seats[row][col] == 0:
                    available_seats.append((row+1, col+1))
        return available_seats


cinema = Star_Cinema()

hall1 = Hall(3, 3, 121)
hall2 = Hall(3, 3, 122)
hall3 = Hall(3, 3, 123)

cinema.entry_hall(hall1)
cinema.entry_hall(hall2)
cinema.entry_hall(hall3)

hall1.entry_show("M01", "Jawan", "15:00")
hall2.entry_show("M02", "Fast & Furious", "16:30")
hall3.entry_show("M03", "Titanic", "18:00")

while True:
    print("1. View All Show Today")
    print("2. View Available Seats")
    print("3. Book A Seat For Show")
    print("4. Exit")
    ch = int(input('Enter your choice : '))
    if ch == 1:
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for show in hall1.view_show_list():
            print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")
        for show in hall2.view_show_list():
            print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")
        for show in hall3.view_show_list():
            print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~")

    elif ch == 2:
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(
            f'Available seats for show M01\n{hall1.view_available_seats("M01")}')
        print(
            f'Available seats for show M02\n{hall2.view_available_seats("M02")}')
        print(
            f'Available seats for show M03\n{hall3.view_available_seats("M03")}')
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~")

    elif ch == 3:
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~")
        show_id = input('Show ID: ')
        if show_id == 'M01':
            row = int(input('Enter Seat Row: '))
            col = int(input('Enter Seat Column: '))
            print(hall1.book_seats("M01", [(row, col)]))
        elif show_id == 'M02':
            row = int(input('Enter Seat Row: '))
            col = int(input('Enter Seat Column: '))
            print(hall2.book_seats("M02", [(row, col)]))
        elif show_id == 'M03':
            row = int(input('Enter Seat Row: '))
            col = int(input('Enter Seat Column: '))
            print(hall3.book_seats("M03", [(row, col)]))
        else:
            print('Invalid Show ID!')
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        break
