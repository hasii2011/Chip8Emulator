
class UnknownKeyPressedOpSubOpCode(ValueError):

    def __init__(self, invalidSubOpCode: int):

        super().__init__(f"Invalid key pressed subOpCode: {invalidSubOpCode:x}")

