class Bachelor:
    """Класс для описания бакалавра."""

    __elephant_or_not = "NA"
    __pervash_type = "NA"

    def __init__(self, surname: str="NA", speciality: str="NA", course: int=None) -> None:
        """Инициализация класса.

        Args:
              surname: Фамилия бакалавра.
              speciality: Специальность бакалавра.
              course: Курс бакалвра.
        """

        self.__surname = surname
        self.__speciality = speciality
        self.__course = course

    def set_speciality(self, speciality: str) -> None:
        """Сеттер для специальности бакалвра.

        Args:
            speciality: Специальность бакалавра.
        """

        self.__speciality = speciality

    def get_speciality(self) -> str:
        """Геттер для специальности бакалавра.

        Returns:
            speciality: Специальность бакалвра
        """

        return self.__speciality

    def set_surname(self, surname: str) -> None:
        """Сеттер для фамилии бакалавра.

        Args:
            surname: Фамилия бакалавра.
        """

        self.__surname = surname

    def get_surname(self) -> str:
        """Геттер для фамилии бакалавра.

        Returns:
            surname: Фамилия бакалавра.
        """

        return self.__surname

    def set_course(self, course) -> None:
        """Сеттер для курса бакалавра.

        Args:
            course: Курс бакалавра.
        """

        while course < 1 or course > 4:
            course = int(input('Введите корректный номер курса бакалавра (в диапазоне от 1 до 4): '))

        self.__course = course

    def get_course(self) -> int:
        """Геттер для курса бакалавра.

        Returns:
            course: Курс бакалавра.
        """

        return self.__course

    def show_info(self) -> None:
        """Вывод информации о бакалавре."""

        print(
            f'\nФамилия: {self.get_surname()}\n'
            f'Специальность: {self.get_speciality()}\n'
            f'Курс: {self.get_course()}\n'
        )

    def student_type(self) -> None:
        """Метод для получения информации о том, перваш бакалавр или нет."""

        if self.__course:
            if self.__course > 1:
                print("Не перваш")
            else:
                print("Перваш")

        else:
            print('У бакалавра нет значения курса! Вы можете задать его с помощью команды под номером 3.')

    def is_elephant(self) -> None:
        """Метод для получения информации о том, слоняра ли бакалавр или нет."""

        if self.__speciality != 'NA':
            if self.__speciality == "Цифровая аналитика и инженерия данных" or self.__speciality == "ЦАИД":
                print("Наш слоняра")
            else:
                print("Не слоняра")

        else:
            print('У бакалавра нет значения специальности! Вы можете задать ее с помощью команды под номером 1.')

