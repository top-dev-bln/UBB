    def __save_state(self):
        self.__history.append(self.__offers[:])
    def handle_undo(self):
        if len(self.__history) > 1:
            self.__history.pop()  # Remove the current state
            self.__offers = self.__history[-1][:]  # Set to a copy of the previous state
            print("Undo successful. Reverted to the previous state.")
        else:
            print("Cannot undo. No previous state available.")
