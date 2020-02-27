from django.core.exceptions import ValidationError
from lib.firebases import firebase, all_employees_code
from django.utils.translation import gettext_lazy as _

def validate_user_code_in_list(value):
  """Validate a code must exist from Employee code list."""
  codes = all_employees_code()
  if value not in codes:
    raise ValidationError(_("Employee code isn't exist in company."))
  else:
    return value
