import turtle

def drawTree(d, n):
    """
    Рекурсивне малювання фрактального дерева.
    d: довжина поточного стовбура
    n: глибина рекурсії
    """
    if n == 0:
        return
    else:
        # стовбур
        turtle.forward(d)

        # ліва гілка
        turtle.left(30)
        drawTree(d / 2, n - 1)

        # права гілка
        turtle.right(60)
        drawTree(d / 2, n - 1)

        # повертаємося на початковий напрямок
        turtle.left(30)

        # повернення до початкової точки стовбура
        turtle.backward(d)



width = 300
height = 400
d = 100  # довжина стовбура

# Налаштування вікна turtle
screen = turtle.Screen()
screen.setup(width, height)
screen.title("Fractal Tree")

# Запит користувача: число повинно бути цілим
n = screen.numinput("Ступінь фракталу",
                    "Введіть ступінь фракталу (0-6):",
                    minval=0, maxval=6)

n = int(n)

# Початкова позиція
turtle.penup()
turtle.goto(width / 2 - width / 2, -height / 2 + 10)  # зміщення для центру
turtle.setheading(90)  # напрямок вгору
turtle.pendown()

turtle.speed(2)  # максимальна швидкість
drawTree(d, n)

turtle.hideturtle()
turtle.done()

