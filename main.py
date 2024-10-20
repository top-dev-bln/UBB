    def __save_state(self):
        self.__history.append(self.__offers[:])

    def handle_undo(self):
        if len(self.__history) > 1:
            self.__history.pop()  # Remove the current state
            self.__offers = self.__history[-1][:]  # Set to a copy of the previous state
            print("Undo successful. Reverted to the previous state.")
        else:
            print("Cannot undo. No previous state available.")

    def add_package(self):
        destination = input("Enter destination: ")
        date = self.get_date()
        price = float(input("Enter price: "))
        new_package = Package(destination, date, price)
        self.__save_state()
        self.__offers.append(new_package)
        print("Package added successfully.")

    def delete_package(self):
        if not self.__offers:
            print("No packages to delete.")
            return

        print("Current packages:")
        for i, package in enumerate(self.__offers):
            print(f"{i + 1}. {package}")

        try:
            index = int(input("Enter the number of the package to delete: ")) - 1
            if 0 <= index < len(self.__offers):
                self.__save_state()
                deleted_package = self.__offers.pop(index)
                print(f"Deleted package: {deleted_package}")
            else:
                print("Invalid package number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
