from Bachelor import (
    Bachelor
)
from Menu import (
    Menu
)


menu = Menu()
bachelor_1 = Bachelor()
bachelor_2 = Bachelor('Иванов', 'ЦАИД', 3)


def run() -> None:
    """Метод запуска работы."""

    is_running = True

    while is_running:
        menu.show_main_menu()

        choice = int(input('Введите выбор: '))
        choice_bachelor = int(input('Введите порядковый номер бакалавра: '))
        bachelor = bachelor_1 if choice_bachelor == 1 else bachelor_2

        is_running = menu.main_menu(choice, bachelor)


run()