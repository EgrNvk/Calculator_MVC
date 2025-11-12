from calculator_mvc_model import Calculator

class CalculatorController:
    supported = {"+", "-", "*", "/"}

    def __init__(self, view):
        self.view = view

    @staticmethod
    def _parse_number(raw: str):
        raw = raw.strip().replace(",", ".")
        return float(raw)

    def _get_number(self, prompt: str):
        while True:
            raw = self.view.input_number(prompt)
            try:
                return self._parse_number(raw)
            except ValueError:
                self.view.show_error("Некоректний ввід. Введіть число ще раз.")

    def _get_action(self):
        while True:
            action = self.view.input_action()
            if action in self.supported:
                return action
            self.view.show_error("Некоректна дія. Доступні: +, -, *, /.")

    def run_once(self):
        n1 = self._get_number("Введіть перше число: ")
        n2 = self._get_number("Введіть друге число: ")
        action = self._get_action()

        if action == "/" and n2 == 0:
            self.view.show_error("Неможливо ділити на нуль.")
            return

        calc = Calculator(n1, n2)

        if action == "+":
            result = calc.addition()
        elif action == "-":
            result = calc.subtraction()
        elif action == "*":
            result = calc.multiplication()
        elif action == "/":
            result = calc.division()
        else:
            self.view.show_error("Невідома дія.")
            return

        self.view.show_result(n1, n2, action, result)