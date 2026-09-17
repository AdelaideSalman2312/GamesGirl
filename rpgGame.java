public class rpgGame{
public static int attackEnemy(int enemyHp, int damage) {
    enemyHp -= damage;
    if (enemyHp <= 0) {
        System.out.println("Enemy defeated!");
    } else {
        System.out.println("Enemy HP is now " + enemyHp);
    }
    return enemyHp;
}
public static void battle(int playerHp, int enemyHp, int playerDamage, int enemyDamage) {
        while (playerHp > 0 && enemyHp > 0) {
            enemyHp = attackEnemy(enemyHp, playerDamage);
            if (enemyHp <= 0) {
                break;
            }
            playerHp -= enemyDamage;
            System.out.println("Player HP is now " + playerHp);
        }

        if (playerHp <= 0) {
            System.out.println("You were defeated...");
        } else {
            System.out.println("Victory!");
        }
    }

    public static void main(String[] args) {
        String playerName = "Trixie";
        int playerHp = 100;
        int playerDamage = 15;

        String enemyName = "Foxie";
        int enemyHp = 60;
        int enemyDamage = 10;

        System.out.println(playerName + " encounters a " + enemyName + "!");
        battle(playerHp, enemyHp, playerDamage, enemyDamage);
    }
}