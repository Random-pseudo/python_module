from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):

    member_id: str = Field(
        ...,
        min_length=3,
        max_length=10
    )
    name: str = Field(
        ...,
        min_length=2,
        max_length=50
    )
    rank: Rank = Field(
        ...
    )
    age: int = Field(
        ...,
        ge=18,
        le=80
    )
    specialization: str = Field(
        ...,
        min_length=3,
        max_length=30
    )
    years_experience: int = Field(
        ...,
        ge=0,
        le=50
    )
    is_active: bool = Field(
        default=True
    )


class SpaceMission(BaseModel):

    mission_id: str = Field(
        ...,
        min_length=5,
        max_length=15
    )
    mission_name: str = Field(
        ...,
        min_length=3,
        max_length=100
    )
    destination: str = Field(
        ...,
        min_length=3,
        max_length=50
    )
    launch_date: datetime = Field(
        ...
    )
    duration_days: int = Field(
        ...,
        ge=1,
        le=3650
    )
    crew: list[CrewMember] = Field(
        ...,
        min_length=1,
        max_length=12
    )
    mission_status: str = Field(
        default="planned"
    )
    budget_millions: float = Field(
        ...,
        ge=1.0,
        le=10000.0
    )

    @model_validator(mode='after')
    def validate_mission_requirements(self) -> 'SpaceMission':

        if not self.mission_id.startswith("M"):
            raise ValueError(
                "Mission ID must start with 'M'"
            )

        inactive: list[str] = [
            m.name for m in self.crew if not m.is_active
        ]
        if inactive:
            raise ValueError(
                f"All crew members must be active."
                f" Inactive: {', '.join(inactive)}"
            )

        senior_ranks: set[Rank] = {Rank.commander, Rank.captain}
        has_senior: bool = any(
            m.rank in senior_ranks for m in self.crew
        )
        if not has_senior:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced = sum(
                1 for m in self.crew if m.years_experience >= 5
            )
            if experienced / len(self.crew) < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced "
                    "crew (5+ years)"
                )

        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        return self


def display_mission(mission: SpaceMission) -> None:

    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"  - {member.name} ({member.rank.value})"
            f" - {member.specialization}"
        )


def main() -> None:

    print("Space Mission Crew Validation")
    print("=" * 41)

    commander: CrewMember = CrewMember(
        member_id="CM001",
        name="Sarah Connor",
        rank=Rank.commander,
        age=42,
        specialization="Mission Command",
        years_experience=18
    )
    lieutenant: CrewMember = CrewMember(
        member_id="CM002",
        name="John Smith",
        rank=Rank.lieutenant,
        age=35,
        specialization="Navigation",
        years_experience=10
    )
    officer: CrewMember = CrewMember(
        member_id="CM003",
        name="Alice Johnson",
        rank=Rank.officer,
        age=29,
        specialization="Engineering",
        years_experience=6
    )

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.fromisoformat("2024-07-04T09:00:00"),
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
        print(
            f"  - {member.name} ({member.rank.value}) - "
            f"{member.specialization}"
        )
    print("=" * 41)

    print("Expected validation error:")
    try:
        cadet1: CrewMember = CrewMember(
            member_id="CM010",
            name="Bob Cadet",
            rank=Rank.cadet,
            age=22,
            specialization="Support",
            years_experience=1
        )
        cadet2: CrewMember = CrewMember(
            member_id="CM011",
            name="Eve Cadet",
            rank=Rank.officer,
            age=24,
            specialization="Medical",
            years_experience=2
        )
        SpaceMission(
            mission_id="M2024_BAD",
            mission_name="Leaderless Mission",
            destination="Moon",
            launch_date=datetime.fromisoformat("2024-08-01T10:00:00"),
            duration_days=30,
            crew=[cadet1, cadet2],
            budget_millions=100.0
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'])

    print("=" * 41)

    print("Expected validation error (long mission, low experience):")
    try:
        junior1: CrewMember = CrewMember(
            member_id="CM020",
            name="Tom Junior",
            rank=Rank.captain,
            age=30,
            specialization="Piloting",
            years_experience=3
        )
        junior2: CrewMember = CrewMember(
            member_id="CM021",
            name="Lisa Rookie",
            rank=Rank.officer,
            age=25,
            specialization="Science",
            years_experience=2
        )
        SpaceMission(
            mission_id="M2025_LONG",
            mission_name="Deep Space Voyage",
            destination="Alpha Centauri",
            launch_date=datetime.fromisoformat("2025-01-01T00:00:00"),
            duration_days=700,
            crew=[junior1, junior2],
            budget_millions=5000.0
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
