from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def shield(target: str, power: int) -> str:
        return f"Shield protects {target} with {power} barrier"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    short_fire = result[0].split(" for ")[0]
    short_heal = result[1].split(" for ")[0].replace("Heal restores", "Heals")
    print(f"Combined spell result: {short_fire}, {short_heal}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    orig = fireball("Goblin", 10)
    amp = mega_fireball("Goblin", 10)
    orig_power = 10
    amp_power = 30
    print(f"Original: {orig_power}, Amplified: {amp_power}")

    print("\nTesting conditional caster...")

    def is_powerful(target: str, power: int) -> bool:
        return power >= 50
    conditional_fire = conditional_caster(is_powerful, fireball)
    print(conditional_fire("Orc", 60))
    print(conditional_fire("Orc", 20))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, shield])
    results = sequence("Wizard", 30)
    for r in results:
        print(f"  {r}")
