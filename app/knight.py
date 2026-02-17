class Knight:
    def __init__(self, knight_config: dict) -> None:
        self.name = knight_config["name"]
        self.power = knight_config["power"]
        self.hp = knight_config["hp"]
        self.protection = 0

        # 1. Apply Armour logic
        self._wear_armour(knight_config["armour"])

        # 2. Apply Weapon logic
        self._take_weapon(knight_config["weapon"])

        # 3. Apply Potion logic
        if knight_config["potion"]:
            self._drink_potion(knight_config["potion"])

    def _wear_armour(self, armour_list: list) -> None:
        for armour in armour_list:
            self.protection += armour["protection"]

    def _take_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def _drink_potion(self, potion: dict) -> None:
        effect = potion["effect"]
        self.hp += effect.get("hp", 0)
        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def calculate_damage_from(self, opponent: "Knight") -> int:
        return opponent.power - self.protection
