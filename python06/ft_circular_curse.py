from alchemy.grimoire import record_spell, validate_ingredients

print("\n=== Circular Curse Breaking ===\n")

print("Testing ingredient validation:")
print(f'validate_ingredients("fire air"): {validate_ingredients("fire air")}')
print(
    'validate_ingredients("dragon scales"): '
    f'{validate_ingredients("dragon scales")}'
    )

print("\nTesting spell recording with validation:")
print(
    'record_spell("Fireball", "fire air"): '
    f'{record_spell("Fireball", "fire air")}'
    )
print(
    f'record_spell("Dark Magic", "shadow"): '
    f'{record_spell("Dark Magic", "shadow")}'
    )
print("\nTesting late import technique:")
print('record_spell("Lightning", "air"):', record_spell("Lightning", "air"))
print("\nCircular dependency curse avoided using late imports!")
print("All spells processed safely!")
