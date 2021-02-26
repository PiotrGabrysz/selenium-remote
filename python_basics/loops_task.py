import time

#part 1
start_time = time.time()
while_iterations = 0

while time.time() - start_time < 1:
    while_iterations += 1
print(while_iterations)

# part 2
start_time = time.time()
for i in range(while_iterations):
    for_time_left = time.time() - start_time

print(for_time_left)

# part 3
if 1 < for_time_left:
    print("While is faster")
else:
    print("For is faster")


assert 1 < for_time_left, f"While time is slower -> for time is {for_time_left}s"
