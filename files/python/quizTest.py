iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break

    print("iteration:",iteration)
    print("count",count)
    iteration += 1
