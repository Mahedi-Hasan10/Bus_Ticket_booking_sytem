class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Bus:
    def __init__(self, coach, driver, arrival, departure, from_des, to):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seat = ["empty" for i in range(20)]


class Phitron:
    total_bus = 5
    total_bus_lst = []

    def add_bus(self):
        bus_no = int(input("Enter bus no : "))
        flag = 1
        for w in self.total_bus_lst:
            if bus_no == w['coach']:
                print("Bus already added")
                flag = 0
                break

        if flag:
            driver_name = input("Enter driver name : ")
            bus_arrival = input("Enter arrival time : ")
            bus_departure = input("Enter departure time : ")
            bus_from = input("Enter you start from : ")
            bus_to = input("Enter your destination : ")
            self.new_bus = Bus(bus_no, driver_name, bus_arrival,
                               bus_departure, bus_from, bus_to)
            self.total_bus_lst.append(vars(self.new_bus))
            print("Bus added successfully")


class Counter(Phitron):
    user_lst = []

    def reservation(self):
        bus_no = int(input("Enter bus no : "))
        for w in self.total_bus_lst:
            if bus_no == w['coach']:
                passenger = input("Enter your name : ")
                seat_no = int(input("Enter your seat no : "))
                if seat_no > 20:
                    print("Seat not available!!")
                elif w['seat'][seat_no-1] != "empty":
                    print("Seat already booked")
                else:
                    w['seat'][seat_no-1] = passenger
                    print("Your seat successfully booked")
            else:
                print("NO Bus available")
        # for bus in self.total_bus_lst:
        #     print(bus['seat'])

    def show_ticket(self):
        bus_no = int(input("Enter your bus no : "))
        for w in self.total_bus_lst:
            if w['coach'] == bus_no:
                print('*'*50)
                print()
                print(f"{' '*10}{'#'*10} BUS INFO {'#'*10}")
                print(f"Bus No : {bus_no}\t\t\tDriver name : {w['driver']}")
                print(
                    f"Arrival : {w['arrival']}\t\t\tDeparture time : {w['departure']}\nFrom : {w['from_des']}\t\t\t To : {w['to']}")
                print()
            a = 1
            for i in range(5):
                for j in range(2):
                    print(f"{a}. {w['seat'][a-1]}", end="\t")
                    a += 1
                for j in range(2):
                    print(f"{a}. {w['seat'][a-1]}", end="\t")
                    a += 1
                print()
            print("*"*50)

    def get_user(self):
        return self.user_lst

    def create_new_account(self):
        name = input("Enter Username : ")
        password = input("Enter password : ")
        self.new_user = User(name, password)
        self.user_lst.append(vars(self.new_user))

    def available_buses(self):
        if len(self.total_bus_lst) == 0:
            print("No Buses available")
        else:
            print('*'*50)
            for bus in self.total_bus_lst:
                print()
                print(f"{' '*10} {'#'*10} BUS {bus['coach']} INFO {'#'*10}")
                print(
                    f"Bus Number : {bus['coach']}\t Driver : {bus['driver']}")
                print(
                    f"Arrival : {bus['arrival']}\t Departure : {bus['departure']}\n From : {bus['from_des']}\t To : {bus['to']}")
                print('*'*50)


while True:
    company = Phitron()
    b = Counter()
    print("1.Create an account\n2.Login to your account\n3.Exit")
    user_input = int(input("Enter your choise : "))
    if user_input == 3:
        break
    elif user_input == 1:
        b.create_new_account()
    elif user_input == 2:
        name = input("Enter your username : ")
        password = input("Enter your password : ")
        flag = 0
        is_admin = False
        if name == "admin" and password == '123':
            is_admin = True
        if is_admin == False:
            for user in b.get_user():
                if user['username'] == name and user['password'] == password:
                    flag = 1
                    break
            if flag:
                while True:
                    print(f"{' '*10}WELCOME TO BUS TICKET BOOKING SYSTEM")
                    print(f"1.Available buses\n2.Show bus Info\n3.Reservation\n4.Exit")
                    a = int(input("Enter your choise : "))
                    if a == 4:
                        break
                    elif a == 1:
                        b.available_buses()
                    elif a == 2:
                        b.show_ticket()
                    elif a == 3:
                        b.reservation()
            else:
                print("NO username found!!")

        else:
            while True:
                print(f"{' '*10}Hello Admin, WELCOME TO BUS TICKET BOOKING SYSTEM")
                print(f"1.Add bus\n2.Available Buses\n3.Show bus Info\n4.Exit")
                a = int(input("Enter your choise : "))
                if a == 4:
                    break
                elif a == 1:
                    b.add_bus()
                elif a == 2:
                    b.available_buses()
                elif a == 3:
                    b.show_ticket()


# company = Phitron()
# company.add_bus()

# c = Counter()
# c.reservation()
# c.show_ticket()
