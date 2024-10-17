import uuid


class Expense:
    def __init__(self, day: int, value: int, expenseType: str) -> None:
        self.__id = uuid.uuid4()
        self.__day = day
        self.__value = value
        self.__type = expenseType

    def __str__(self) -> str:
        return (
            f"Expense from Day: {self.__day}; Value: {self.__value} Type: {self.__type}"
        )

    def get_id(self):
        return self.__id

    def get_day(self):
        return self.__day

    def get_value(self):
        return self.__value

    def get_type(self):
        return self.__type

