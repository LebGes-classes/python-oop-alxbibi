from Bachelor import (
    Bachelor
)


class Menu:
    """Класс для работы пользовательского меню."""

    def show_main_menu(self) -> None:
        """Вывод пунктов главного меню."""

        print(
            '\n1: Изменить специальность бакалавра.\n'
            '2: Изменить фамилию бакалавра.\n'
            '3: Изменить курс бакалавра.\n'
            '4: Получить информацию о специальности бакалавра.\n'
            '5: Получить информацию о фамилии бакалавра.\n'
            '6: Получить информацию о курсе бакалавра.\n'
            '7: Вывод информации о бакалавре.\n'
            '8: Узнать, перваш бакалавр или нет.\n'
            '9: Узнать, слоняра бакалавр или нет.\n'
            '0: ВЫХОД ИЗ ПРОГРАММЫ.\n'
        )

    def main_menu(self, choice: int, bachelor: Bachelor) -> bool:
        """Главное пользовательское меню.

        Args:
            choice: Выбор пользователя.

        Returns:
            is_running: Продолжается ли работа программы.

        """

        is_running = True

        match choice:
            case 0:
                is_running = False
            case 1:
                speciality = input('Введите специальность бакалавра: ')

                bachelor.set_speciality(speciality)
            case 2:
                surname = input('Введите фамилию бакалавра: ')

                bachelor.set_surname(surname)
            case 3:
                course = int(input('Введите курс бакалавра: '))

                bachelor.set_course(course)
            case 4:
                print(bachelor.get_speciality())
            case 5:
                print(bachelor.get_surname())
            case 6:
                print(bachelor.get_course())
            case 7:
                bachelor.show_info()
            case 8:
                bachelor.student_type()
            case 9:
                bachelor.is_elephant()
