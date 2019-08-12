

def main():

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
    'BaseInterpreterInterface', 'BaseStdIn', 'Command',
    'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    user_username = input("Enter Username: ")
    
    if user_username in usernames:
        print("Access Granted")
    else:
        print("Access Denied")

if __name__ == "__main__":
    main()
