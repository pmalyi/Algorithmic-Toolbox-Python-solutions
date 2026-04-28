import sys

class CppCin:
    def __init__(self, stream=sys.stdin):
        self.stream = stream
        self.buffer = ""

    def _fill_buffer(self):
        """Читає наступний рядок, якщо буфер порожній."""
        while not self.buffer:
            line = self.stream.readline()
            if not line:
                return False
            self.buffer = line.strip().split()
        return True

    def read(self, cast=str):
        """Емулює оператор >> в C++."""
        if not self._fill_buffer():
            raise EOFError("End of input")

        token = self.buffer.pop(0)  # беремо перше слово

        try:
            return cast(token)
        except ValueError:
            raise ValueError(f"Cannot convert '{token}' to {cast}")

    # синтаксис вигляду cin >> x
    def __rshift__(self, cast):
        """cin >> int  повертає значення;
           cin >> x записує в x, але Python так не вміє."""
        return self.read(cast)


def main():
    cin = CppCin()
    while cin.stream:
        name = cin >> str
        age = cin >> int
        height = cin >> float

        print(name, age, height)

main()