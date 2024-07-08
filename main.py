import solve
from console_interface import ConsoleInterface


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    console = ConsoleInterface()
    data: dict = console.read()
    console.print_result(solve.solve(data))
