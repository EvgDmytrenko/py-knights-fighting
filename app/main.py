from app.knight import Knight
from app.config import KNIGHTS


def run_duel(attacker: Knight, defender: Knight) -> None:
    #  Розрахунок шкоди
    damage_to_attacker = attacker.calculate_damage_from(defender)
    damage_to_defender = defender.calculate_damage_from(attacker)

    # Отримання шкоди
    attacker.take_damage(damage_to_attacker)
    defender.take_damage(damage_to_defender)


def battle(knights_config: dict) -> dict:
    # 1. Інстанціювання екземплярів класів
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    # 2. Битви
    # Мордред проти Ланселота
    run_duel(lancelot, mordred)

    # Артур проти Червоного Лицаря
    run_duel(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
