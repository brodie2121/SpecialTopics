#Dictionary named RoomNumbers
RoomNumbers = {'CS101':3004, 'CS102':4501, 'CS103':6755, 'NT110':1244, 'CM241':1411}
# Dictionary named Instructor
Instructor = {'CS101':'Haynes', 'CS102':'Alvarado', 'CS103':'Rich', 'NT110':'Burke', 'CM241':'Lee'}
# Dictionary named Meeting Time
Meeting_Time = {'CS101':'8:00 a.m', 'CS102':'9:00 a.m', 'CS103':'10:00 a.m', 'NT110':'11:00 a.m', 'CM241':'1:00 p.m'}
print()
# Asking the user to enter course number
course_number = input('Enter course number: ')
# printing the room number
print('Room Number: {}'.format(RoomNumbers[course_number]))
# Printing the instrructor
print('Instructor: {}'.format(Instructor[course_number]))
# printing the meeting time
print('Meeting Time: {}'.format(Meeting_Time[course_number]))