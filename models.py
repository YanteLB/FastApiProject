
from pydantic import BaseModel, Field, field_validator

class Product(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=2, max_length=100)
    price: float = Field(gt=0)
    description: str = Field(min_length=5, max_length=500)
    quantity: int = Field(ge=0)

    @field_validator("name", "description")
    @classmethod
    def strip_and_validate_text(cls, value: str) -> str:
        cleaned: str = value.strip()
        if not cleaned:
            raise ValueError("must not be empty or whitespace")
        return cleaned
