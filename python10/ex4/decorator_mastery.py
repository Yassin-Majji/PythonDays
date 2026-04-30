import time
from functools import wraps


def spell_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # إذا كانت method → power هو آخر argument
            if len(args) >= 2:
                power = args[-1]
            else:
                power = args[0]

            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                            )
                    else:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                            )
                        return (
                            "Spell casting failed after "
                            f"{max_attempts} attempts"
                            )
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for char in name:
            if not (char.isalpha() or char.isspace()):
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main():
    print("\nTesting spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print("Result:", result)

    print("\nTesting retrying spell...")

    @retry_spell(3)
    def unstable_spell():
        raise Exception("Failure")

    print(unstable_spell())

    print("Waaaaaaagh spelled !")

    print("\nTesting MageGuild...")

    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("A1"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[Error] {e}")
