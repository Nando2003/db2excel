class InvalidPathException(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        self.message = message
    
    def __str__(self) -> str:
        return f"InvalidPathException: {self.message}"