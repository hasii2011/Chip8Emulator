
class InvalidIndexRegisterValue(ValueError):

    def __init__(self, badValue: int):
        super().__init__(f"Invalid index register value: {badValue:x}")
