def attack_enemy(enemy_hp, damage):
    enemy_hp -= damage
    if enemy_hp <= 0:
        print("Enemy defeated!")
    else:
        print(f"Enemy HP is now {enemy_hp}")
    return enemy_hp