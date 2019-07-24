
class UnknownInstructionError(LookupError):

    def __init__(self, badInstruction: int):

        super().__init__(f"badInstruction: {badInstruction:x}")
