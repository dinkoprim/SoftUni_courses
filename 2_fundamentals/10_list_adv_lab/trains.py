def train(length, order):
    train_cars = [0] * length
    while order != 'End':
        command_input = order.split(' ')
        command = command_input[0]
        index = int(command_input[1])
        people = int(command_input[-1])
        if command == 'add':
            train_cars[-1] += people
        elif command == 'insert':
            train_cars[index] += people
        elif command == 'leave':
            train_cars[index] -= people
        order = input()
    return train_cars


number_of_cars = int(input())
user_command = input()
print(train(number_of_cars, user_command))



