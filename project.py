class Person:
    def __init__(self, first_name, last_name, age, email, birth_day):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self._birth_day = birth_day

    @property
    def birth_day(self):
        return self._birth_day

    @birth_day.setter
    def birth_day(self, value):
        if not (isinstance(value, tuple) and len(value) == 3):
            raise ValueError("birth_day must be a tuple of three integers (day, month, year).")
        self._birth_day = value

    def get_info(self):
        return f"Name: {self.first_name} {self.last_name}\nAge: {self.age}\nEmail: {self.email}\nBirth Date: {self.birth_day[0]}-{self.birth_day[1]}-{self.birth_day[2]}"

    def get_life_path_number(self):
        def reduce_to_single_digit(n):
            while n > 9:
                n = sum(int(digit) for digit in str(n))
            return n

        day, month, year = self.birth_day
        life_path_number = reduce_to_single_digit(day) + reduce_to_single_digit(month) + reduce_to_single_digit(year)
        return reduce_to_single_digit(life_path_number)

    def get_info_by_number(self, number):
        try:
            with open('life_path_info.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    if line.startswith(f"#{number}"):
                        return line.split(' ', 1)[1].strip()
        except FileNotFoundError:
            return "Error: life_path_info.txt file not found."
        return f"No information found for life path number {number}."

if __name__ == "__main__":
    print("Please enter the following information:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    age = int(input("Age: "))
    email = input("Email: ")
    birth_day = tuple(map(int, input("Birth Date (day month year): ").split()))

    person = Person(first_name, last_name, age, email, birth_day)

    print("\nPersonal Information:")
    print(person.get_info())

    life_path_number = person.get_life_path_number()
    print(f"\nLife Path Number: {life_path_number}")

    info_by_number = person.get_info_by_number(life_path_number)
    print(f"\nPsychological Insight for Life Path Number {life_path_number}:\n{info_by_number}")
