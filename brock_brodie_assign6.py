RoomNumbers = {'CS101': 3004, 'CS102': 4501,
               'CS103': 6755, 'NT110': 1244, 'CM241': 1411}
Instructor = {'CS101': 'Haynes', 'CS102': 'Alvarado',
              'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}
Meeting_Time = {'CS101': '8:00 a.m', 'CS102': '9:00 a.m',
                'CS103': '10:00 a.m', 'NT110': '11:00 a.m', 'CM241': '1:00 p.m'}
print()
course_number = input('Enter course number: ')
print('Room Number: {}'.format(RoomNumbers[course_number]))
print('Instructor: {}'.format(Instructor[course_number]))
print('Meeting Time: {}'.format(Meeting_Time[course_number]))
