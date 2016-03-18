import sqlite3
from queries_cinema import CinemaQueries
import re


class CLI:

    def __init__(self, db_name):
        self.queries = CinemaQueries(db_name)
        self.__is_active = True

        self.commands = {
            "show_movies": self.show_movies,
            "show_movie_projections": self.show_movie_projections,
            "make_reservation": self.make_reservation,
            "exit": self.exit,
            "help": self.help,
            "cancel_reservation": self.cancel_reservation
        }

    def cancel_reservation(self, name):
        self.queries.cancel_reservation(name)

    def help(self):
        print ("You have following choices: ")
        for command in self.commands.keys():
            if command != "help":
                print (command)

    def exit(self):
        self.__is_active = False
        print ("quitted successfully")

    def show_movies(self):
        movies = self.queries.get_current_movies()
        for movie in movies:
            print (movie)

    def show_movie_projections(self, params):
        projes = self.queries.get_movie_projections(params)
        for proj in projes:
            print (proj)

    def print_matrix(self, mtx):
        print ("\n")
        size = len(mtx[1])
        for i in range(0, size):
            for j in range(0, size):
                print(mtx[i][j], end=" ")
            print ("\n")

    def show_availible_seats(self, projection_for):
            all_seats = [['.' for x in range(10)] for x in range(10)]
            taken_seats = self.queries.taken_seats(projection_for)
            for ts in taken_seats:
                all_seats[ts[0] - 1][ts[1] - 1] = "X"
            self.print_matrix(all_seats)

    def show_reservation_till_now(self, chosen_movie_id, chosen_proj,
                                  taken_seats, num_of_tickets):
        print ("This is your reservation: ")

        movie_name = self.queries.get_movie_name_by_id(chosen_movie_id)
        print ("Movie: {}".format(movie_name))  # take movie name by id

        movie_time_type = self.queries.get_movie_time_and_type_by_id(chosen_proj)
        print ("Date and Time: {}".format(movie_time_type))  # take by id

        print ("Seats: ", end=" ")
        for i in range(len(taken_seats) - num_of_tickets, len(taken_seats)):
            print (taken_seats[i], end=" ")
        print ('\n')

    def make_reservation(self):
        while True:
            name = input("Step 1 (User): Choose name>") or None
            reservation_names = self.queries.get_res_names()
            if (name, ) in reservation_names:
                print ('''This name already exists in reservations,
                        Please choose another!''')
                continue
            break

        num_of_tickets = int(input("Step 1 (User): Choose number of tickets>"))

        self.show_movies()
        chosen_movie_id = input("Step 2 (Movie): Choose a movie>")
        self.show_movie_projections(chosen_movie_id)

        chosen_proj = input("Step 3 (Projection): Choose a projection>")
        self.show_availible_seats(chosen_proj)
        taken_seats = self.queries.taken_seats(chosen_proj)  # tuples
        tickets = 0

        while True:
            if tickets == num_of_tickets:
                break
            chosen_seat = input("Step 4 (Seats): Choose seat 1>")
            seats_list = eval(chosen_seat)
            if (seats_list in taken_seats):
                print ("This seat is already taken!")
            elif(seats_list[0] > 10 or seats_list[0] < 0 or
                 seats_list[1] > 10 or seats_list[1] < 0):
                print ("LOL... no")
            else:
                tickets += 1
                taken_seats.append(seats_list)

        self.show_reservation_till_now(chosen_movie_id,
                                       chosen_proj, taken_seats,
                                       num_of_tickets)

        last_step = input("Step 5 (Confirm - type 'finalize') >")
        finished_reservation = False
        if last_step.lower() == "finalize":
            print ("Thanks.")
            finished_reservation = True
        if finished_reservation:
            #  last appended tickets-tickets which are reserved current seesion
            self.queries.add_reservation_to_db(num_of_tickets, name,
            chosen_proj, taken_seats[(len(taken_seats)-num_of_tickets)::])

    def start(self):
        while self.__is_active:
            command = input("Enter command>").split(' ')
            if len(command) == 1:
                self.commands[command[0]]()
            else:
                name_by_id = self.queries.get_movie_name_by_id(command[1])
                if not len(command) > 2:
                    print ("Projections for movie '{}':".format(
                       name_by_id))
                else:
                    print ("Projections for movie '{}' on date {}:".format(
                        name_by_id, command[2]))
                print (self.commands[command[0]](command[1::]))
