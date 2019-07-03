from dataclasses import dataclass


@dataclass
class ValidationResult:
    """

    """
    code: int  # bool로?
    message: str

    @staticmethod
    def ok():
        return ValidationResult(0, "VERY GOOD")

    @staticmethod
    def unknown_error():
        return ValidationResult(-999, "HELL")

    def is_invalid(self):
        return self.code != 0


class Validator:
    def is_valid(self) -> ValidationResult:  # 이유도 리턴해줘야하지 않을까? exception을 주는게 나을까?
        """

        :return:
        """
        from melchior.model.template.output.component import SimpleText, SimpleImage

        if type(self) is SimpleText:
            # 글자 제한 같은거
            return ValidationResult.ok()
        elif type(self) is SimpleImage:
            return Validator.validate_simple_image(self)
        else:
            return ValidationResult.unknown_error()

    @staticmethod
    def validate_simple_image(simple_image) -> ValidationResult:

        if not simple_image.imageUrl.startswith('http'):
            return ValidationResult(-1, "URL 형태가 아님")
        else:
            return ValidationResult.ok()



