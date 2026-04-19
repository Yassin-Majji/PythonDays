try:

    from pydantic import BaseModel, Field, ValidationError
    from datetime import datetime
    from typing import Optional, Any

    class SpaceStation(BaseModel):
        station_id: str = Field(min_length=3, max_length=10)
        name: str = Field(min_length=1, max_length=50)
        crew_size: int = Field(ge=1, le=20)
        power_level: float = Field(ge=0.0, le=100.0)
        oxygen_level: float = Field(ge=0.0, le=100.0)
        last_maintenance: datetime = Field(...)
        is_operational: bool = Field(default=True)
        notes: Optional[str] = Field(default=None, max_length=200)

    def main() -> None:
        stations_data = [
            {
                "station_id": "ISS001",
                "name": "International Space Station",
                "crew_size": 6,
                "power_level": 85.5,
                "oxygen_level": 92.3,
                "last_maintenance": "2026-04-17T10:00:00",
                "is_operational": True,
                "notes": ''
                },
            {
                "station_id": "ISS001",
                "name": "International Space Station",
                "crew_size": 21,
                "power_level": 85.5,
                "oxygen_level": 92.3,
                "last_maintenance": "2026-04-17T10:00:00",
                "is_operational": True,
                "notes": ''
                }
        ]
        s: Any = ''
        print("Space Station Data Validation")
        for s in stations_data:
            try:
                print("========================================")
                ob = SpaceStation(**s)
                print("Valid station created:")
                print(f"ID: {ob.station_id}")
                print(f"Name: {ob.name}")
                print(f"Crew: {ob.crew_size} people")
                print(f"Power: {ob.power_level}%")
                print(f"Oxygen: {ob.oxygen_level}%")
                if (ob.is_operational):
                    print("Status: Operational")
                else:
                    print("Status: Non_Operational")
            except ValidationError as e:
                print("Expected validation error:")
                print(f"{e.errors()[0]['msg']}")
            print()

    if __name__ == "__main__":
        try:
            main()
        except Exception as e:
            print(f"[Error] {e}")
except ImportError:
    print(
        "[Error] Install pydantic by using: pip install pydantic"
    )
