from dataclasses import dataclass


class Validator:
    def is_valid(self) -> bool:  # 이유도 리턴해줘야하지 않을까? exception을 주는게 나을까?
        """

        :return:
        """
        from melchior.model.template.output.component import SimpleText, SimpleImage

        if type(self) is SimpleText:
            # 글자 제한 같은거
            return True
        elif type(self) is SimpleImage:
            return self._validate_simple_image()
        else:
            return False

    def _validate_simple_image(self) -> bool:
        return self.imageUrl.startswith("http")

    def _validate_simple_basic_card(self) -> bool:
        return self.imageUrl.startswith("http")


@dataclass
class ValidationResult:
    """

    """
    code: int  # bool로?
    message: str
