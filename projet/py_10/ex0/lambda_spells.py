def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        'max_power': max(mages, key=lambda m: m['power'])['power'],
        'min_power': min(mages, key=lambda m: m['power'])['power'],
        'avg_power': round(sum(map(lambda m: m['power'], mages)) / len(mages), 2)
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'arcane'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'fire'},
        {'name': 'Shadow Blade', 'power': 78, 'type': 'shadow'},
    ]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    first = sorted_artifacts[0]
    second = sorted_artifacts[1]
    print(f"{first['name']} ({first['power']} power) comes before "
          f"{second['name']} ({second['power']} power)")

    spells = ['fireball', 'heal', 'shield']
    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    print(' '.join(transformed))

    mages = [
        {'name': 'Alex', 'power': 80, 'element': 'fire'},
        {'name': 'Jordan', 'power': 95, 'element': 'water'},
        {'name': 'Riley', 'power': 60, 'element': 'earth'},
    ]

    print("\nTesting power filter (min_power=75)...")
    filtered = power_filter(mages, 75)
    for m in filtered:
        print(f"  {m['name']} ({m['power']} power)")

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"  Max: {stats['max_power']}, Min: {stats['min_power']}, "
          f"Avg: {stats['avg_power']}")
