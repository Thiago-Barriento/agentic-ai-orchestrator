class Tool:
    name = "base"

    def run(self, input_data: str) -> str:
        raise NotImplementedError("Tool must implement run()")
