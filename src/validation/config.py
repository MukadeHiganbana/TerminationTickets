from pydantic import BaseModel
from typing import Optional


class ConfigDefaultValidator(BaseModel):
    pass


class ConfigLocalValidator(BaseModel):
    pass


class ConfigValidator(BaseModel):
    DEFAULT: ConfigDefaultValidator
    LOCAL: Optional[ConfigLocalValidator]
