def replace_cmd(string, current_char, new_char):
    modified_string = string.replace(current_char, new_char)
    print(modified_string)
    return modified_string


def remove_cmd(string, substring):
    modified_string = string.replace(substring, "")
    print(modified_string)
    return modified_string


def includes_cmd(string, substring):
    result = substring in string
    print(result)
    return string


def change_case_cmd(string, case):
    if case == "Lower":
        modified_string = string.lower()
    else:
        modified_string = string.upper()
    print(modified_string)
    return modified_string


def reverse_cmd(string, start_index, end_index):
    if 0 <= start_index <= end_index < len(string):
        reversed_substring = string[start_index:end_index+1][::-1]
        print(reversed_substring)
    else:
        print(string)
    return string

def main():
    string = input()

    while True:
        command = input().split()
        if command[0] == "Easter":
            break

        action = command[0]

        if action == "Replace":
            string = replace_cmd(string, command[1], command[2])
        elif action == "Remove":
            string = remove_cmd(string, command[1])
        elif action == "Includes":
            includes_cmd(string, command[1])
        elif action == "Change":
            string = change_case_cmd(string, command[1])
        elif action == "Reverse":
            start_index, end_index = int(command[1]), int(command[2])
            if 0 <= start_index <= end_index < len(string):
                reverse_cmd(string, start_index, end_index)


if __name__ == "__main__":
    main()
