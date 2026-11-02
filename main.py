from character import Character

def main():
    hero = Character("Knight", 30, 5)
    enemy = Character("Goblin", 20, 3)
    enemy2 = Character("Goblin2", 25, 4)

    print(hero)
    print(enemy)
    print(enemy2)
    print()

    while hero.is_alive() and (enemy.is_alive() or enemy2.is_alive()):
        if enemy.is_alive():
            hero.attack(enemy)
        else:
            hero.attack(enemy2)

        if hero.is_alive() and enemy.is_alive():
            enemy.attack(hero)
        if hero.is_alive() and enemy2.is_alive():
            enemy2.attack(hero)
            
        print(hero)
        print(enemy)
        print(enemy2)
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    elif enemy.is_alive():
        print(f"{enemy.name} wins!")
    elif enemy2.is_alive():
        print(f"{enemy2.name} wins!")

if __name__ == "__main__":
    main()
