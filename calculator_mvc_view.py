class ConsoleView:
    def input_number(self, prompt: str):
        return input(prompt)

    def input_action(self):
        return input("Введіть потрібну дію (+, -, *, /): ").strip()

    def show_result(self, n1: float, n2: float, action: str, result: float):
        print(f"{n1} {action} {n2} = {result}")

    def show_error(self, message: str):
        print(f"Помилка: {message}")

    def show_message(self, message: str):
        print(message)