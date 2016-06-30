def word(message, errormessage):
    inp = input(message).upper()
    while(not inp.isalpha()):
        error = "didn't enter anything" if len(inp) == 0 else "can only enter letters, no symbols or numbers"
        inp = input("Error: You " + error + ". " + errormessage).upper()
    return inp
