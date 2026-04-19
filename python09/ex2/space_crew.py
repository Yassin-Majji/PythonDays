try:
    from pydantic import BaseModel, Field, model_validator, ValidationError
    from typing import List, Any
    from datetime import datetime
    from enum import Enum

    class Rank(Enum):
        cadet = "cadet"
        officer = "officer"
        lieutenant = "lieutenant"
        captain = "captain"
        commander = "commander"

    class CrewMember(BaseModel):
        member_id: str = Field(min_length=3, max_length=10)
        name: str = Field(min_length=2, max_length=50)
        rank: Rank = Field(...)
        age: int = Field(ge=18, le=80)
        specialization: str = Field(min_length=3, max_length=30)
        years_experience: int = Field(ge=0, le=50)
        is_active: bool = Field(default=True)

    class SpaceMission(BaseModel):
        mission_id: str = Field(min_length=5, max_length=15)
        mission_name: str = Field(min_length=3, max_length=100)
        destination: str = Field(min_length=3, max_length=50)
        launch_date: datetime = Field(...)
        duration_days: int = Field(ge=1, le=3650)
        crew: List[CrewMember] = Field(min_length=1, max_length=12)
        mission_status: str = Field(default="planned")
        budget_millions: float = Field(ge=1.0, le=10000.0)

        @model_validator(mode="after")
        def valid(self) -> 'SpaceMission':
            if not self.mission_id.startswith("M"):
                raise ValueError('Mission ID must start with "M"')
            if not any(member.rank.value in ["commander", "captain"]
                       for member in self.crew):
                raise ValueError(
                    "Mission must have at least one Commander or Captain"
                    )
            experienced_members = [member for member in self.crew
                                   if member.years_experience >= 5]
            half_crew = -len(self.crew) // 2
            long_duration = self.duration_days > 365
            if (long_duration and len(experienced_members) < -(half_crew)):
                raise ValueError("Long missions (> 365 days) need 50%"
                                 " experienced crew (5+ years)")
            if not all([member.is_active for member in self.crew]):
                raise ValueError("All crew members must be active")
            return self

    def main() -> None:
        teams = [
            [
                {
                    "member_id": "A243",
                    "name": "Sarah Connor",
                    "rank": "commander",
                    "age": 42,
                    "specialization": "Mission Command",
                    "years_experience": 6,
                    "is_active": True
                    },
                {
                    "member_id": "A543",
                    "name": "John Smith",
                    "rank": "lieutenant",
                    "age": 46,
                    "specialization": "Navigation",
                    "years_experience": 10,
                    "is_active": True
                    },
                {
                    "member_id": "A435",
                    "name": "Alice Johnson",
                    "rank": "officer",
                    "age": 49,
                    "specialization": "Engineering",
                    "years_experience": 7,
                    "is_active": True
                    },
            ],
            [
                {
                    "member_id": "X432",
                    "name": "Jak Sar",
                    "rank": "lieutenant",
                    "age": 40,
                    "specialization": " Navigation",
                    "years_experience": 8,
                    "is_active": True
                    },
                {
                    "member_id": "X253",
                    "name": "Kali Nor",
                    "rank": "lieutenant",
                    "age": 44,
                    "specialization": "Navigation",
                    "years_experience": 10,
                    "is_active": True
                    },
                {
                    "member_id": "X243",
                    "name": "Mark Snnor",
                    "rank": "officer",
                    "age": 39,
                    "specialization": "Engineering",
                    "years_experience": 9,
                    "is_active": True
                    },
            ]
        ]
        reports = [
            {
                "mission_id": "M2024_MARS",
                "mission_name": "Mars Colony Establishment",
                "destination": "Mars",
                "launch_date": "2026-04-17T10:00:00",
                "duration_days": 900,
                "crew": teams[0],
                "mission_status": "planned",
                "budget_millions": 2500.0,
                },
            {
                "mission_id": "M2026_MARS",
                "mission_name": "Mars_trip",
                "destination": "Mars",
                "launch_date": "2026-04-17T10:00:00",
                "duration_days": 900,
                "crew": teams[1],
                "mission_status": "planned",
                "budget_millions": 10000.0,
                }
                    ]
        print("Space Mission Crew Validation")
        r: Any = ''
        for r in reports:
            try:
                print("======================================")
                ob = SpaceMission(**r)
                print("Valid mission created:")
                print(f"Mission: {ob.mission_name}")
                print(f"ID: {ob.mission_id}")
                print(f"Destination: {ob.destination}")
                print(f"Duration: {ob.duration_days} days")
                print(f"Budget: ${ob.budget_millions}M")
                print(f"Crew size: {len(ob.crew)}")
                print("Crew members:")
                for m in ob.crew:
                    print(f"- {m.name} ({m.rank.value}) - {m.specialization}")

            except ValidationError as e:
                print("Expected validation error:")
                print(f"{e.errors()[0]['msg'].replace('Value error, ', '')}")
            print()

    if __name__ == "__main__":
        try:
            main()
        except Exception as e:
            print(f"[Error] {e}")

except ImportError:
    print("[Error] Install pydantic by using: pip install pydantic")
