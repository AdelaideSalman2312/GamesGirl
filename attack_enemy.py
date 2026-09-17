from py_compile import main


def attack_enemy(enemy_hp, damage):
    enemy_hp -= damage #subtracts the damage from enemy health points therefore (enemyHP - damage )
    if enemy_hp <= 0: #if enemy health points are less or equal to zero print below
        print("Enemy defeated!")
    else:#if enemy is still alive print below
        print(f"Enemy HP is now {enemy_hp}")
    return enemy_hp

#Combat Loop
def battle(player_hp, enemy_hp, player_damage, enemy_damage):
    while player_hp > 0 and enemy_hp > 0:#Aslong as one of the two die or is below greater than zero then the game is over
        enemy_hp = attack_enemy(enemy_hp, player_damage)# this calls the above function
        if enemy_hp <= 0:
            break
        player_hp -= enemy_damage
        print(f"Player HP is now {player_hp}")
    
    if player_hp <= 0:
        print("You were defeated...")
    else:
        print("Victory!")

    def main():

     player_name = "Trixie"
     player_hp = 100
     player_damage = 15
     player_inventory = ["rusty sword", "health potion"]


     enemy_name = "Foxie"
     enemy_hp = 60
     enemy_damage = 10
     

    print(f"{player_name} encounters a {enemy_name}!")
    battle(player_hp, enemy_hp, player_damage, enemy_damage)


if __name__ == "__main__":
    main()