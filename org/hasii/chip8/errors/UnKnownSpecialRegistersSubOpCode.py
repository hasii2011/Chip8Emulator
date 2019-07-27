
class UnKnownSpecialRegistersSubOpCode(ValueError):

    def __init__(self, invalidSubOpCode: int):

        super().__init__(f"Invalid special registers subOpCode: {invalidSubOpCode:x}")
