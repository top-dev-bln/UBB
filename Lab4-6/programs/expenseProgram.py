from model.Expense import Expense
from utils.consoleActions import (
    print_green,
    print_red,
    clear_console,
    press_any_key_to_continue,
)

class ExpenseProgram:
    def __init__(self) -> None:
        self.__running = False
        self.__running_sub_menu = False
        self.__expenses = []

    def __print_menu() -> None:
        print_green("Expenses Program")
        print(
            """
1. Add Expense
2. Remove Expense
3. Find Expense
4. Expenses Report
5. Filter Expenses
6. Undo

9. Exit


"""
        )

    def handle_exit(self) -> None:
        self.__running = False

    def handle_add(self) -> None:
        while True:
            try:
                clear_console()
                print_green("Adding an Expense\n")
                day = int(input("Day: "))
                value = int(input("Value: "))
                expenseType = input("Type: ")

                newExpense = Expense(day, value, expenseType)
                self.__expenses.append(newExpense)

                return
            except:
                pass

    def handle_remove(self) -> None:
        pass

    def handle_find(self) -> None:
        self.__running_sub_menu = True

        while self.__running_sub_menu:
            try:
                clear_console()
                print("Find Expense Menu")

                def handle_all():
                    text = ""
                    for expense in self.__expenses:
                        text += str(expense) + "\n"

                    print_green(text[:-2])

                def handle_greater_than():
                    pass

                def handle_before_date_and_under_value():
                    pass

                def handle_exit():
                    self.__running_sub_menu = False

                actions = {
                    "1": handle_all,
                    "2": handle_greater_than,
                    "3": handle_before_date_and_under_value,
                    "9": handle_exit,
                }

                print(
                    """
1. Show All
2. Show Expenses Greater Than
3. Show Expenses Before Date and Under a Defined Value

9. Exit


                        """
                )

                userInput = input("Choose Menu: ")
                actions[userInput]()
                if self.__running_sub_menu:
                    press_any_key_to_continue()
            except Exception as e:
                print_red("Some error occured " + str(e))
                press_any_key_to_continue()

    def handle_report(self) -> None:
        pass

    def handle_filter(self) -> None:
        pass

    def handle_undo(self) -> None:
        pass

    def run(self) -> None:
        self.__running = True
        expenses = []

        actions = {
            "1": self.handle_add,
            "2": self.handle_remove,
            "3": self.handle_find,
            "4": self.handle_report,
            "5": self.handle_filter,
            "6": self.handle_undo,
            "9": self.handle_exit,
        }

        while self.__running:
            clear_console()
            self.__print_menu()

            try:
                userInput = input("Choose Menu: ")
                actions[userInput]()

            except Exception as e:
                print_red("Please choose a valid menu")
                press_any_key_to_continue()
