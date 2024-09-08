import calu_art



def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def sub(n1, n2):
    return n1 - n2


operations = {
    "+": add,
    "*": multiply,
    "/": divide,
    "-": sub
}
def function():
    print(calu_art.logo)
    n1 = float(input("What's the first number : "))
    should_accumulate = True
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation = (input("Pick a operation : "))
        n2 = float(input("Enter the second number : "))
        answer = operations[operation](n1,n2)
        print(f"{n1} {operation} {n2} = {answer}")
        choice = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start new calculation :")
        if choice =="y":
            n1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            function()

function()



