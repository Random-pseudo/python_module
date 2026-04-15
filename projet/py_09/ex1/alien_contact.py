"""Exercise 1: Alien Contact Logs - Custom validation with @model_validator."""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    """Enum of possible alien contact types."""

    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    """Pydantic model for validating alien contact reports."""

    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact_rules(self) -> "AlienContact":
        """Apply business rules across multiple fields."""

        # Contact ID must start with "AC"
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        # Physical contact must be verified
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        # Telepathic contact requires at least 3 witnesses
        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")

        # Strong signals (> 7.0) should include a received message
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )

        return self


def main() -> None:
    """Demonstrate AlienContact validation with valid and invalid data."""

    print("Alien Contact Log Validation")
    print("=" * 38)

    # Create a valid contact report
    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2024-06-21T03:15:00",
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True,
    )

    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: '{contact.message_received}'")
    print("=" * 38)

    # Attempt an invalid telepathic report with too few witnesses
    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp="2024-06-22T10:00:00",
            location="Roswell, New Mexico",
            contact_type=ContactType.telepathic,
            signal_strength=5.0,
            duration_minutes=10,
            witness_count=1,  # Invalid: telepathic needs >= 3
            is_verified=False,
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
