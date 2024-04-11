def distribute_people(people, lift):
    for i in range(len(lift)):
        while lift[i] < 4 and people > 0:
            lift[i] += 1
            people -= 1
            if people == 0 or lift_is_full(lift):
                return people, lift
    return people, lift


def lift_is_full(lift):
    return all(wagon == 4 for wagon in lift)


def main():
    que = int(input())
    lift_state = [int(x) for x in input().split(' ')]

    que, lift_state = distribute_people(que, lift_state)

    if que == 0 and not lift_is_full(lift_state):
        print("The lift has empty spots!")
    elif que > 0 and lift_is_full(lift_state):
        print(f"There isn't enough space! {que} people in a queue!")

    print(*lift_state)

if __name__ == "__main__":
    main()
