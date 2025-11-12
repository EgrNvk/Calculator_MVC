from calculator_mvc_view import ConsoleView
from calculator_mvc_controller import CalculatorController

def main():
    view=ConsoleView()
    controller = CalculatorController(view)
    controller.run_once()

if __name__ == "__main__":
    main()