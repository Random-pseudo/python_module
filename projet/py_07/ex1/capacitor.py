from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability
from ex0.creatures import Creature


def test_healing_factory(factory: HealingCreatureFactory) -> None:
    for label in ("base", "evolved"):
        print(f" {label}:")
        c: Creature = (
            factory.create_base() if label == "base"
            else factory.create_evolved()
        )
        print(c.describe())
        print(c.attack())
        if isinstance(c, HealCapability):
            print(c.heal())


def test_transform_factory(factory: TransformCreatureFactory) -> None:
    for label in ("base", "evolved"):
        print(f" {label}:")
        c: Creature = (
            factory.create_base() if label == "base"
            else factory.create_evolved()
        )
        print(c.describe())
        print(c.attack())
        if isinstance(c, TransformCapability):
            print(c.transform())
            print(c.attack())
            print(c.revert())


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    test_healing_factory(HealingCreatureFactory())

    print()
    print("Testing Creature with transform capability")
    test_transform_factory(TransformCreatureFactory())
