# Ініціалізуємо глобальну змінну
global_var = 15


def my_function():
    # Ініціалізуємо локальну змінну
    local_var = 25
    print(f"local_var in my_function before call inner = {local_var}")
    def inner():
        nonlocal local_var
        local_var = 105
        print(f"local_var in inner = {local_var}")

    inner()
    print(f"local_var in my_function after call inner = {local_var}")

    # Змінюємо значення глобальної змінної
    global global_var
    global_var = 35
    print(f"globsl_var in my_function = {global_var}")


# Виводимо значення глобальної змінної
print(f"globsl_var before call my_function = {global_var}")

# Викликаємо функцію та змінюємо глобальну змінну
my_function()

# Виводимо змінене значення глобальної змінної
print(f"globsl_var after call my_function = {global_var}")