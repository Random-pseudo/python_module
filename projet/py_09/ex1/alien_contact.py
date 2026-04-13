from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    """Types of alien contact that can be reported."""
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    """
    Pydantic model for alien contact reports.
    Uses @model_validator to enforce cross-field business rules.
    """

    contact_id: str = Field(
        ...,
        min_length=5,
        max_length=15,
        description="Unique contact identifier (must start with 'AC')"
    )
    timestamp: datetime = Field(
        ...,
        description="Date and time of the contact event"
    )
    location: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Location where the contact occurred"
    )
    contact_type: ContactType = Field(
        ...,
        description="Type of alien contact"
    )
    signal_strength: float = Field(
        ...,
        ge=0.0,
        le=10.0,
        description="Signal strength on a 0.0-10.0 scale"
    )
    duration_minutes: int = Field(
        ...,
        ge=1,
        le=1440,
        description="Duration of contact in minutes (max 24h)"
    )
    witness_count: int = Field(
        ...,
        ge=1,
        le=100,
        description="Number of witnesses"
    )
    message_received: Optional[str] = Field(
        default=None,
        max_length=500,
        description="Message content if received"
    )
    is_verified: bool = Field(
        default=False,
        description="Whether this report has been officially verified"
    )

    @model_validator(mode='after')
    def validate_business_rules(self) -> 'AlienContact':
        """
        Enforce cross-field validation rules after Pydantic validates
        individual fields.
        """
        # Rule 1: contact_id must start with "AC"
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "Contact ID must start with 'AC' (Alien Contact)"
            )

        # Rule 2: physical contacts must be verified
        if (
            self.contact_type == ContactType.physical
            and not self.is_verified
        ):
            raise ValueError(
                "Physical contact reports must be verified"
            )

        # Rule 3: telepathic contacts need at least 3 witnesses
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        # Rule 4: strong signals (> 7.0) should include messages
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                "Strong signal (> 7.0) contacts should include"
                " a received message"
            )

        return self


def display_contact(contact: AlienContact) -> None:
    """Display contact report information."""
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    if contact.message_received:
        print(f"Message: '{contact.message_received}'")


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 38)

    # --- Valid radio contact with strong signal and message ---
    valid_contact: AlienContact = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2024-03-20T22:15:00",
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True
    )
    print("Valid contact report:")
    display_contact(valid_contact)

    print("=" * 38)

    # --- Invalid: telepathic contact with only 1 witness ---
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp="2024-03-21T03:00:00",
            location="Sahara Desert",
            contact_type=ContactType.telepathic,
            signal_strength=5.0,
            duration_minutes=20,
            witness_count=1,   # violates rule: telepathic needs >= 3
            is_verified=False
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'])

    print("=" * 38)

    # --- Invalid: physical contact that is not verified ---
    print("Expected validation error (physical not verified):")
    try:
        AlienContact(
            contact_id="AC_2024_003",
            timestamp="2024-03-22T10:00:00",
            location="Roswell, NM",
            contact_type=ContactType.physical,
            signal_strength=3.0,
            duration_minutes=10,
            witness_count=2,
            is_verified=False   # violates rule: physical must be verified
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'])


if __name__ == "__main__":
    main()
