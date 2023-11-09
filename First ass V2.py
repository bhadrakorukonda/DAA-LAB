class Teacher:
    def __init__(self, new_arrival_day, new_lectures_needed, new_curse_level):
        self.new_arrival_day = new_arrival_day
        self.new_lectures_needed = new_lectures_needed
        self.new_curse_level = new_curse_level

def schedule_lectures(N, D, teachers):
    teachers.sort(key=lambda teacher: teacher.new_arrival_day)
    total_curse = 0
    current_day = 1

    for teacher in teachers:
        if current_day > D:
            break

        lectures_to_schedule = min(D - current_day + 1, teacher.new_lectures_needed)
        total_curse += teacher.new_curse_level * (teacher.new_lectures_needed - lectures_to_schedule)
        current_day += lectures_to_schedule

    return total_curse

# Reading input
N, D = map(int, input().split())
teachers = []

for _ in range(N):
    Di, Ti, Si = map(int, input().split())
    teachers.append(Teacher(Di, Ti, Si))

# Calling the function and printing the result
min_curse = schedule_lectures(N, D, teachers)
print(min_curse)

#INPPUT
#2 3 
#1 2 100
#2 2 100

#OUTPUT
#100