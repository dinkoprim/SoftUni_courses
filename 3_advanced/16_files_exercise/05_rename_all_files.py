import os


def replace_symbols(location, string_to_replace, new_string):
    try:
        for entry in os.listdir(location):
            entry_path = os.path.join(location, entry)

            if os.path.isfile(entry_path) or os.path.isdir(entry_path):
                new_name = entry.replace(string_to_replace, new_string)
                new_path = os.path.join(location, new_name)

                os.rename(entry_path, new_path)

                if os.path.isdir(new_path):
                    replace_symbols(new_path, string_to_replace, new_string)

        new_location = location.replace(string_to_replace, new_string)
        os.rename(location, new_location)
        print("Symbol replacement completed.")

    except PermissionError:
        print(f'PermissionError:\n'
              'Sorry, cannot rename files while they are running!\n'
              'Move this script to another directory and try again\n'
              ' or check your admin permission.'
              )

    except FileNotFoundError:
        print(f'FileNotFoundError:\n'
              f'Sorry, cannot find this directory. Please check the correct path and try again'
              )

    except Exception as e:
        print(f'An unexpected error occurred: {e}')


print("Remember that it's crucial to be careful when manipulating files,\n"
      "especially when the script is dealing with its own source code or important system files.\n"
      "Always make backups before performing potentially destructive operations.\n")

user_input = input('If you like to replace symbols in your file/folder names press Y\n'
                   'or press any other key to exit: ')

if user_input.lower() == 'y':
    location = input('Enter the root directory: ')
    string_to_replace = input('Enter symbol you would like to replace: ')
    new_string = input('Enter replacement symbol: ')

    replace_symbols(location, string_to_replace, new_string)

else:
    print("Good Bye")
