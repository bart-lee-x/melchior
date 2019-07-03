from melchior.validator.validator import ValidationResult


class MelchiorException(Exception):
    pass


class ComponentCreateException(MelchiorException):
    """"""
    def __init__(self, validation_result: ValidationResult):
        self.expression = validation_result.status.name
        self.message = validation_result.status.value