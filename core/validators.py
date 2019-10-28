import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

hour_code_re = re.compile(r'^\d{2}:\d{2}$')



def dv_maker(v):
    if v >= 2:
        return 11 - v
    return 0


class ScheduleValidator(RegexValidator):
    """
    A validator for hours.
    """

    def __init__(self, *args, **kwargs):
        self.message = _('Digite um Horário no formato 00:00')
        self.code = _('Horário inválido.')
        super().__init__(hour_code_re, *args, **kwargs)


