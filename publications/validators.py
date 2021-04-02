from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class RegNumberValidator(RegexValidator):
    regex = r"^\d{10}$"
    message = ("Enter a valid registration number. "
               "The value have to be exactly 12 digits.")
    flags = 0


reg_number_validator = RegNumberValidator()
