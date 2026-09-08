public class attackEnemy{
public static int attackEnemy(int enemyHp, int damage) {
    enemyHp -= damage;
    if (enemyHp <= 0) {
        System.out.println("Enemy defeated!");
    } else {
        System.out.println("Enemy HP is now " + enemyHp);
    }
    return enemyHp;
}
}
// Needs correction and introspection