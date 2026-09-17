def attack_enemy(enemy_hp, damage):
    enemy_hp -= damage   # this only changes the LOCAL copy
    return enemy_hp

hp = 100
attack_enemy(hp, 15)     # nothing returned/reassigned
print(hp)                 # still 100 — the outside variable never changed