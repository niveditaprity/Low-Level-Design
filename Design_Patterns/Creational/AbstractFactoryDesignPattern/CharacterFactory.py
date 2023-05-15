from abc import ABC, abstractmethod

class Character(ABC):

    @abstractmethod
    def get_health(self):
        pass

    @abstractmethod
    def get_damage(self):
        pass

    @abstractmethod
    def get_spell_power(self):
        pass


class MeeleWarriorCharacter(Character):
    def get_health(self):
        return 100;


    def get_damage(self):
        return 50


    def get_spell_power(self):
        return 0;


class RangedWarriorCharacter(Character):
    def get_health(self):
        return 50;

    def get_damage(self):
        return 25

    def get_spell_power(self):
        return 100;


class MeeleMagedCharacter(Character):
    def get_health(self):
        return 50;

    def get_damage(self):
        return 25

    def get_spell_power(self):
        return 100;

class RangedMagedCharacter(Character):
    def get_health(self):
        return 100;


    def get_damage(self):
        return 50


    def get_spell_power(self):
        return 0;



class CharacterFactory:
    def create_meele(self):
        return Character()

    def create_ranged(self):
        return Character

class WarriorsFactory(CharacterFactory):
    def create_meele(self):
        return MeeleWarriorCharacter()
    def create_ranged(self):
        return RangedWarriorCharacter()


class MagesFactory(CharacterFactory):
    def create_meele(self):
        return MeeleMagedCharacter()
    def create_ranged(self):
        return RangedMagedCharacter()


class Factory:
    def __init__(self, factory: CharacterFactory):
        self.character_factory = factory

    def create_character(self, is_melee: bool):
        if is_melee:
            return self.character_factory.create_meele()
        else:
            return self.character_factory.create_ranged()

    def __str__(self):
        melee = self.create_character(True)
        ranged = self.create_character(False)
        return (f"Melee: {type(melee).__name__} "
                f"Health={melee.get_health()}, "
                f"Damage={melee.get_damage()}, "
                f"Spell Power={melee.get_spell_power()}\n"
                f"Ranged: {type(ranged).__name__} "
                f"Health={ranged.get_health()}, "
                f"Damage={ranged.get_damage()}, "
                f"Spell Power={ranged.get_spell_power()}")


warriors_factory = WarriorsFactory()
factory = Factory(warriors_factory)
print(factory)

mages_factory = MagesFactory()
factory1 = Factory(mages_factory)

print(factory1)





