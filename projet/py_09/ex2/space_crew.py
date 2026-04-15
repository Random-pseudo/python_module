"""Exercise 2: Space Crew Management - Nested Pydantic models."""

from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    """Enum of possible crew member ranks."""

    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    """Pydantic model for an individual crew member."""

    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """Pydantic model for a space mission with a nested crew list."""

    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> "SpaceMission":
        """Apply safety rules for the mission."""

        # Mission ID must start with "M"
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        # Must have at least one Commander or Captain
        senior_ranks = {Rank.commander, Rank.captain}
        has_senior = any(m.rank in senior_ranks for m in self.crew)
        if not has_senior:
            raise ValueError("Mission must have at least one Commander or Captain")

        # Long missions (> 365 days) require 50% experienced crew (5+ years)
        if self.duration_days > 365:
            experienced = sum(1 for m in self.crew if m.years_experience >= 5)
            if experienced / len(self.crew) < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced crew (5+ years)"
                )

        # All crew members must be active
        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    """Demonstrate SpaceMission validation with valid and invalid data."""

    print("Space Mission Crew Validation")
    print("=" * 41)

    # Build a valid crew
    commander = CrewMember(
        member_id="CM001",
        name="Sarah Connor",
        rank=Rank.commander,
        age=42,
        specialization="Mission Command",
        years_experience=18,
    )
    lieutenant = CrewMember(
        member_id="CM002",
        name="John Smith",
        rank=Rank.lieutenant,
        age=35,
        specialization="Navigation",
        years_experience=10,
    )
    officer = CrewMember(
        member_id="CM003",
        name="Alice Johnson",
        rank=Rank.officer,
        age=29,
        specialization="Engineering",
        years_experience=6,
    )

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2024-07-04T09:00:00",
        duration_days=900,
        crew=[commander, lieutenant, officer],
        budget_millions=2500.0,
    )

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"  - {member.name} ({member.rank.value}) - {member.specialization}")
    print("=" * 41)

    # Attempt an invalid mission (no Commander or Captain)
    try:
        SpaceMission(
            mission_id="M2024_BAD",
            mission_name="Doomed Mission",
            destination="Venus",
            launch_date="2024-08-01T09:00:00",
            duration_days=30,
            crew=[
                CrewMember(
                    member_id="CM010",
                    name="Bob Rookie",
                    rank=Rank.cadet,  # No senior rank
                    age=22,
                    specialization="Piloting",
                    years_experience=1,
                )
            ],
            budget_millions=100.0,
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
