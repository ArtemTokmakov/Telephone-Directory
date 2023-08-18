import csv
from typing import List, Dict


class Phonebook:
    def __init__(self):
        self.contacts: List[Dict[str, str]] = self.load_contacts()

    def display_contacts(self, page_number: int, page_size: int) -> None:
        """
        Функция для вывода постраничного списка записей.

        :param page_number: Номер страницы
        :param page_size: Количество записей на странице
        """
        start_index = (page_number - 1) * page_size
        end_index = start_index + page_size
        page_contacts = self.contacts[start_index:end_index]

        for contact in page_contacts:
            print(contact)

    def add_contact(self) -> None:
        """
        Функция для добавления новой записи в справочник.
        """
        last_name: str = input("Введите фамилию: ")
        first_name: str = input("Введите имя: ")
        middle_name: str = input("Введите отчество: ")
        organization: str = input("Введите название организации: ")
        work_phone: str = input("Введите рабочий телефон: ")
        personal_phone: str = input("Введите личный телефон: ")

        contact: Dict[str, str] = {
            'last_name': last_name,
            'first_name': first_name,
            'middle_name': middle_name,
            'organization': organization,
            'work_phone': work_phone,
            'personal_phone': personal_phone
        }

        self.contacts.append(contact)
        self.save_contacts()

    def save_contacts(self) -> None:
        """
        Функция для сохранения записей в файл.
        """
        with open('contacts.csv', 'w', newline='') as csvfile:
            fieldnames: List[str] = [
                'last_name',
                'first_name',
                'middle_name',
                'organization',
                'work_phone',
                'personal_phone']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.contacts)

    def load_contacts(self) -> List[Dict[str, str]]:
        """
        Функция для загрузки записей из файла.

        :return: Список контактов
        """
        contacts: List[Dict[str, str]] = []
        try:
            with open('contacts.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    contacts.append(row)
        except FileNotFoundError:
            print("Файл с контактами не найден.")
        return contacts

    def edit_contact(self) -> None:
        """
        Функция для редактирования записей.
        """
        self.display_contacts(1, len(self.contacts))
        index: int = int(input(
            "Введите номер записи, которую хотите отредактировать: ")) - 1

        if 0 <= index < len(self.contacts):
            contact: Dict[str, str] = self.contacts[index]

            print("\nТекущая запись:")
            print(contact)

            # Запрашиваем новые значения для каждого поля
            for field in contact:
                new_value: str = input(f"Введите новое значение для {field}: ")
                contact[field] = new_value

            self.save_contacts()
            print("Запись успешно отредактирована.")
        else:
            print("Введен некорректный номер записи.")

    def search_contacts(self) -> None:
        """
        Функция для поиска записей по характеристикам.
        """
        last_name: str = input("Введите фамилию: ")
        first_name: str = input("Введите имя: ")
        organization: str = input("Введите название организации: ")

        search_results: List[Dict[str, str]] = []
        for contact in self.contacts:
            if (last_name == "" or contact['last_name'] == last_name) and \
               (first_name == "" or contact['first_name'] == first_name) and \
               (organization == "" or contact['organization'] == organization):
                search_results.append(contact)

        if search_results:
            print("\nРезультаты поиска:")
            for contact in search_results:
                print(contact)
        else:
            print("По вашему запросу ничего не найдено.")


phonebook = Phonebook()

while True:
    print("\nТелефонный справочник")
    print("1. Вывести записи на экран")
    print("2. Добавить новую запись")
    print("3. Редактировать запись")
    print("4. Поиск записей")
    print("0. Выход")

    choice: str = input("Выберите действие: ")

    if choice == '1':
        page_number: int = int(input("Введите номер страницы: "))
        page_size: int = 5  # Устанавливаем количество записей на страницу
        phonebook.display_contacts(page_number, page_size)
    elif choice == '2':
        phonebook.add_contact()
    elif choice == '3':
        phonebook.edit_contact()
    elif choice == '4':
        phonebook.search_contacts()
    elif choice == '0':
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")

print("Завершение программы.")
