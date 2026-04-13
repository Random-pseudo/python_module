from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """Pydantic model representing a monitored space station."""

    station_id: str = Field(
        ...,
        min_length=3,
        max_length=10,
        description="Unique station identifier"
    )
    name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Human-readable station name"
    )
    crew_size: int = Field(
        ...,
        ge=1,
        le=20,
        description="Number of crew members (1-20)"
    )
    power_level: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Power level percentage (0.0-100.0)"
    )
    oxygen_level: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Oxygen level percentage (0.0-100.0)"
    )
    last_maintenance: datetime = Field(
        ...,
        description="Timestamp of the last maintenance operation"
    )
    is_operational: bool = Field(
        default=True,
        description="Whether the station is currently operational"
    )
    notes: Optional[str] = Field(
        default=None,
        max_length=200,
        description="Optional notes about the station"
    )


def display_station(station: SpaceStation) -> None:
    """Display station information in a readable format."""
    status: str = "Operational" if station.is_operational else "Offline"
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: {status}")
    if station.notes:
        print(f"Notes: {station.notes}")


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    # --- Valid station ---
    valid_station: SpaceStation = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        # Pydantic automatically converts ISO 8601 strings to datetime
        last_maintenance="2024-01-15T08:30:00",
        is_operational=True,
        notes="All systems nominal"
    )
    print("Valid station created:")
    display_station(valid_station)

    print("=" * 40)

    # --- Invalid station: crew_size > 20 ---
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="BAD001",
            name="Overcrowded Station",
            crew_size=25,          # violates le=20
            power_level=50.0,
            oxygen_level=80.0,
            last_maintenance="2024-01-15T08:30:00"
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'])


if __name__ == "__main__":
    main()
