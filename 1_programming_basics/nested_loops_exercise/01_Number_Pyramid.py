n = int(input())
counter = 1
is_n_bigger = False
for i in range(1, n+1):
    for j in range(1, i+1):
        if counter > n:
            is_n_bigger = True
            break
        print(counter, end=' ')
        counter += 1

    if is_n_bigger:
        break

    print()
