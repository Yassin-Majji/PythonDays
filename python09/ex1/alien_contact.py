try:
    from pydantic import BaseModel, Field, model_validator, ValidationError
    from typing import Optional, Any
    from datetime import datetime
    from enum import Enum

    class ContactType(Enum):
        radio = "radio"
        visual = "visual"
        physical = "physical"
        telepathic = "telepathic"

    class AlienContact(BaseModel):
        contact_id: str = Field(min_length=5, max_length=15)
        timestamp: datetime = Field(...)
        location: str = Field(min_length=3, max_length=100)
        contact_type: ContactType = Field(...)
        signal_strength: float = Field(ge=0.0, le=10.0)
        duration_minutes: int = Field(ge=1, le=1440)
        witness_count: int = Field(ge=1, le=100)
        message_received: Optional[str] = Field(default=None, max_length=500)
        is_verified: bool = Field(default=False)

        @model_validator(mode="after")
        def valid(self) -> 'AlienContact':
            if not self.contact_id.startswith("AC"):
                raise ValueError('Contact ID must start with "AC"')
            if self.contact_type == ContactType.physical \
                    and not self.is_verified:
                raise ValueError("Physical contact reports must be verified")
            if self.contact_type == ContactType.telepathic \
                    and self.witness_count < 3:
                raise ValueError(
                    "Telepathic contact requires at least 3 witnesses")
            if self.signal_strength > 7.0 and not self.message_received:
                raise ValueError(
                    "Strong signals must include a received message")
            return self

    def main() -> None:
        reports = [
            {
                "contact_id": "AC_2024_001",
                "timestamp": "2026-04-17T10:00:00",
                "location": "Area 51, Nevada",
                "contact_type": "radio",
                "signal_strength": 8.5,
                "duration_minutes": 45,
                "witness_count": 5,
                "message_received": "Greetings from Zeta Reticuli",
                "is_verified": False
                },
            {
                "contact_id": "AC_2024_001",
                "timestamp": "2026-04-17T10:00:00",
                "location": "Area 51, Nevada",
                "contact_type": "telepathic",
                "signal_strength": 8.5,
                "duration_minutes": 45,
                "witness_count": 2,
                "message_received": "Greetings from Zeta Reticuli",
                "is_verified": False
                },
                    ]
        print("Alien Contact Log Validation")
        r: Any = ''
        for r in reports:
            try:
                print("======================================")
                ob = AlienContact(**r)
                print("Valid contact report:")
                print(f"ID: {ob.contact_id}")
                print(f"Type: {ob.contact_type.value}")
                print(f"Location: {ob.location}")
                print(f"Signal: {ob.signal_strength}/10")
                print(f"Duration: {ob.duration_minutes} minutes")
                print(f"Witnesses: {ob.witness_count}")
                print(f"Message: '{ob.message_received}'")
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
