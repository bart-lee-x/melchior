from dataclasses import dataclass
from enum import Enum


class ValidationStatus(Enum):
    OK = (0, 'Ok')
    UNKNOWN = (-999, 'Unknown')
    INVALID_IMAGE_URL = (-101, 'Invalid Image Url')


@dataclass
class ValidationResult:
    """

    """
    status: ValidationStatus

    @staticmethod
    def ok():
        return ValidationResult(ValidationStatus.OK)

    @staticmethod
    def unknown_error():
        return ValidationResult(ValidationStatus.UNKNOWN)

    def is_invalid(self):
        return self.status.name != 'OK'


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
            return ValidationResult(ValidationStatus.INVALID_IMAGE_URL)
        else:
            return ValidationResult.ok()
