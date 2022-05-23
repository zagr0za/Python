def function_print():
    print("Lets see what function can do?")


function_print()


def function_concatenation():
    print("Introduce yourself please: ")
    P1 = input("enter some greeting: ")
    P2 = input("Your first name: ")
    P3 = input("Your last name: ")
    print(P1 + ', ' + P2.capitalize() + ' ' + P3.capitalize() + ' - ' + "This is concatenation :D")


function_concatenation()


def function_ifelse():
    print("Now we need new values")
    A = int(input("Enter value A: "))
    B = int(input("Enter value B: "))
    C = int(input("Enter value C: "))
    if A > B:
        print("Oh no...(voice of Phoebe Buffay)")
    if B > A and B > C:
        print("Aw yeah! B-value rocks!")
    else:
        print("Well, that happens")
    if A == B:
        print("Your 'A' is just like 'B' - that's equality! :D")
    print("'if/else' works like this")


function_ifelse()


def function_while():
    print("Let's put new values for last function")
    A = int(input("Enter value 1: "))
    B = int(input("Enter value 2: "))
    C = int(input("Enter value 3: "))
    D = "Increment history: "
    while A < B:
        print("Bad result")
        A += C
        D = D + " " + str(A)
    else:
        print("Great result!")
        print(D)
    print("It was our last but not least function - 'while'! Thanks for your time and have a great day!")


function_while()

