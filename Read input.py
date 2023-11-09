# Read input
N, D = map(int, input().split())
teachers = []
for i in range(N):
    Di, Ti, Si = map(int, input().split())
    teachers.append((Di, Ti, Si))

# Sort teachers in decreasing order of curse increase rate (Si)
teachers.sort(key=lambda x: -x[2])

# Initialize variables
total_curse = 0
cur_day = 1

# Greedy scheduling
for teacher in teachers:
    Di, Ti, Si = teacher
    if cur_day >= Di:
        # The teacher has already arrived, schedule lectures
        remaining_lectures = Ti
        while cur_day <= D and remaining_lectures > 0:
            total_curse += Si
            remaining_lectures -= 1
            cur_day += 1
    else:
        # The teacher hasn't arrived yet, schedule lectures for available days
        available_days = min(D - cur_day + 1, Di - cur_day)
        total_curse += available_days * Si
        cur_day += available_days

# Output the minimum total curse
print(total_curse)