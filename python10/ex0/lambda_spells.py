def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    result = sorted(artifacts, key=lambda artifact: artifact['power'],
                    reverse=True)
    return result


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    result = filter(lambda mage: mage['power'] >= min_power, mages)
    return list(result)


def spell_transformer(spells: list[str]) -> list[str]:
    result = map(lambda spell: "* " + spell + " *", spells)
    return list(result)


def mage_stats(mages: list[dict]) -> dict:
    result = {}
    result['max_power'] = max(mages, key=lambda mage: mage['power'])['power']
    result['min_power'] = min(mages, key=lambda mage: mage['power'])['power']
    sum_powers = sum(map(lambda mage: mage['power'], mages))
    result['avg_power'] = round(sum_powers / len(mages), 2)
    return result


def main() -> None:
    print("Testing artifact sorter...")
    artifacts = [
            {'name': 'Crystal Orb', 'power': 85,
                'type': 'magical artifacts'},
            {'name': 'artif', 'power': 58, 'type': 'magical artifacts'},
            {'name': 'Fire Staff', 'power': 92, 'type': 'magical artifacts'}
            ]
    artifacts_sorter = artifact_sorter(artifacts)
    print(f'{artifacts_sorter[0]["name"]} ({artifacts_sorter[0]["power"]}'
          f' power) comes before {artifacts_sorter[1]["name"]}'
          f' ({artifacts_sorter[1]["power"]} power)'
          )
    print()

    print("Testing spell transformer...")
    spells = spell_transformer(["fireball", "heal", "shield"])
    for s in spells:
        print(s, end=' ')
    print()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"[Error] {e}")
