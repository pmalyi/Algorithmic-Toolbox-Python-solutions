import turtle
import sys

# Іноді при глибокій рекурсії потрібно підняти ліміт
sys.setrecursionlimit(10000)

def koch(t, length, depth):
    """
    Рекурсивно малює один відрізок кривої Коха:
    - t: екземпляр turtle.Turtle()
    - length: довжина відрізка на поточному рівні
    - depth: глибина рекурсії (0 — простий відрізок)
    """
    if depth == 0:
        t.forward(length)
    else:
        third = length / 3.0
        # Чотири частини: пряма, вгору, вниз, пряма
        koch(t, third, depth - 1)
        t.left(60)
        koch(t, third, depth - 1)
        t.right(120)
        koch(t, third, depth - 1)
        t.left(60)
        koch(t, third, depth - 1)


def draw_koch_snowflake(side_length=300, depth=3):
    """
    Малює сніжинку Коха (трикутник із трьома кривими Коха).
    - side_length: довжина сторони великого трикутника
    - depth: глибина рекурсії (рівень фрактала)
    """
    screen = turtle.Screen()
    screen.title(f"Koch snowflake — depth {depth}")
    # Налаштування вікна (за потребою підкорегуйте)
    screen.setup(width=900, height=700)
    screen.bgcolor("white")

    # Прискорення малювання: вимикаємо анімацію оновлення
    screen.tracer(0, 0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)         # максимальна швидкість
    t.pensize(1)
    t.color("blue")

    # Розташування: перемістити черепаху так, щоб сніжинка була по центру
    # Для рівня depth збільшується складність — тому трохи масштабування:
    t.penup()
    t.goto(-side_length/2, side_length/2 * 0.35)  # підганяємо по центру
    t.pendown()

    # Малюємо 3 сторони
    for _ in range(3):
        koch(t, side_length, depth)
        t.right(120)

    # Оновлюємо екран разом (швидше)
    screen.update()

    # Очікуємо закриття вікна користувачем
    turtle.done()


if __name__ == "__main__":
    # Параметри: можна змінити тут або робити парсинг аргументів
    # depth: рекомендовано не більше 6 для інтерактивного запуску (глибше — дуже повільно)
    default_side = 360
    default_depth = 4

    print(f"Drawing Koch snowflake: side={default_side}, depth={default_depth}")
    draw_koch_snowflake(side_length=default_side, depth=default_depth)
