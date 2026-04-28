class CppInput:
    def __init__(self):
        self.buffer = []
        self.eof = False

    def _fill_buffer(self):
        """Читає новий рядок із консолі, як std::getline.
           Якщо користувач натисне Ctrl+D — встановлюється EOF."""
        try:
            line = input()
            self.buffer = line.split()
        except EOFError:
            self.eof = True
            self.buffer = []

    def __rshift__(self, var_type):
        """Емуляція операторa >>.
           var_type — тип (int, float, str)."""
        if self.eof:
            return None  # як std::cin >> x: після EOF читання не відбувається

        if not self.buffer:
            self._fill_buffer()
            if self.eof:
                return None

        token = self.buffer.pop(0)

        # Конвертуємо до потрібного типу
        try:
            return var_type(token)
        except ValueError:
            raise ValueError(f"Cannot convert '{token}' to {var_type}")

    def good(self):
        """Повертає True, якщо EOF ще не досягнуто."""
        return not self.eof


def main():
    cin = CppInput()
    while cin.good():
        name = cin >> str
        age = cin >> int
        height = cin >> float

        print(name, age, height)

main()