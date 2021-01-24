from warrior import Warrior

class Fight:
    def start_fight(warrior_1, warrior_2):

        while warrior_1.hp > 0 and warrior_2.hp > 0:
            
            warrior_1.hp = warrior_1.hp - warrior_2.attack() + warrior_1.block()
            
            print(f"{warrior_1.name}:  {warrior_1.hp}")
            warrior_2.hp = warrior_2.hp - warrior_1.attack() + warrior_2.block()
            
            print(f"{warrior_2.name}:  {warrior_2.hp}")
            
            if warrior_1.hp <= 0:
                return warrior_2.name
            
            elif warrior_2.hp <= 0:
                return warrior_1.name

if __name__ == "__main__":
    warrior_kratos = Warrior("Kratos",100, 10)
    warrior_subzero = Warrior("Subzero",100, 10)
    winner = Fight.start_fight(warrior_kratos,warrior_subzero)

    print(f"{winner} has won!")
