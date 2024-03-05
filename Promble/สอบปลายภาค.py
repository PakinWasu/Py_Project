class Seat:
    def __init__(self,seat_number) -> None:
        self.seat_number = seat_number
        self.is_booking = False
        self.student_id = None
        self.student_name = None
        self.next = None

class Booking :
    def __init__(self):
        self.head = None

    def insert(self, seat_number):
        new_node = Seat(seat_number)
        new_node.next = self.head
        self.head = new_node

    def display_seats(self):
        temp = self.head
        print('Seats Number \t Status')
        while(temp):
            print (f"   {temp.seat_number:3}    ",end='\t')
            if temp.is_booking == True:
                print('Booked by %s %s' %(temp.student_id ,temp.student_name))
            else:
                print('Available')
            temp = temp.next

    def booked_seat(self,seat_number,student_id,student_name):
        temp = self.head
        have = True
        while(temp):
            if seat_number == temp.seat_number:
                have = False
                if temp.is_booking == True:
                    print('Can not booking this seat is booked by %s %s' %(temp.student_id,temp.student_name))
                else:
                    temp.student_id = student_id
                    temp.student_name = student_name
                    temp.is_booking = True
                    print('Booked Seat Number %d By %s %s complet'%(temp.seat_number,temp.student_id ,temp.student_name))
            temp = temp.next
        if have == True:
            print("Pls Enter seats number 1-%d"%(total_students))        

    def cancel_booking(self,seat_number):
        temp = self.head
        have = True
        while(temp):
            if seat_number == temp.seat_number:
                have = False
                if temp.is_booking == True:
                    temp.is_booking = False
                    temp.student_id = None
                    temp.student_name = None
                    print('Booking Seat Number %d is cancel'%(temp.seat_number))
                else:
                    print("This seat don't have booked")
            temp = temp.next
        if have == True:
            print("Pls Enter seats number 1-%d"%(total_students))

    def get_avaliable_seats(self):
        temp = self.head
        have = True
        print('Seats Number \t Status')
        while(temp):
            if temp.is_booking == False:
                have = False
                print (f"   {temp.seat_number:3}    ",end='\t')
                print('Available')
            temp = temp.next  
        if have == True:
            print("Don't have available seats")        

    def get_booked_seats(self):
        temp = self.head
        have = True
        print('Seats Number \t Status')
        while(temp):
            if temp.is_booking == True:
                have = False
                print (f"   {temp.seat_number:3}    ",end='\t')
                print('Booked by %s %s' %(temp.student_id ,temp.student_name))
            temp = temp.next   
        if have == True:
            print("Don't have booked seats")

seat = Booking()
print('Start Program')
total_students = int(input("How many students : "))
for i in range(total_students,0,-1):
    seat.insert(i)

while True:
    print('''Please select option -
    1. Display seats      
    2. Booking seat
    3. Cancel booking
    4. Display available seats
    5. Display booked seats
    6. Exit program''')
    select_options = int(input('Select operations form 1 2 3 4 5 6: '))
    print()
    if select_options == 1:
        seat.display_seats()
    elif select_options == 2:
        seat.booked_seat(seat_number =int(input('Seat number : ')) ,student_id= input('Student ID : ') ,student_name= input('Student name : '))
    elif select_options == 3:
        seat.cancel_booking(seat_number= int(input("Seat number cancel booking : ")))
    elif select_options == 4:
        seat.get_avaliable_seats()
    elif select_options == 5:
        seat.get_booked_seats()
    elif select_options == 6:
        break
    print()

        