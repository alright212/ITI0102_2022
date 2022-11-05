"""Car inventory."""


def list_of_cars(all_cars: str) -> list:
    """
    Return list of cars.

    The input string contains of car makes and models, separated by comma.
    Both the make and the model do not contain spaces (both are one word).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi A4", "Skoda Superb", "Audi A4"]
    """
    return all_cars.split(",") if all_cars else []


def car_makes(all_cars: str) -> list:
    """
    Return list of unique car makes.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi", "Skoda"]
    """
    cars_split = all_cars.split(",")
    if not all_cars:
        return []
    makes = []
    for car in cars_split:
        make = car.split(" ")[0]
        if make not in makes:
            makes.append(make)
    return makes


def car_models(all_cars: str) -> list:
    """
    Return list of unique car models.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4" => ["A4", "Superb"]
    """
    cars_split = all_cars.split(",")
    if not all_cars:
        return []
    models = []
    for car in cars_split:
        model = car.split(" ")[1:]
        model = " ".join(model)
        if model not in models:
            models.append(model)
    return models


def search_by_make(all_cars: str, searched_make: str) -> list:
    """
    Return list of cars with given make.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi A4", "Audi A4"]
    """
    cars_split = all_cars.split(",")
    if not all_cars:
        return []
    makes = []
    for car in cars_split:
        make = car.split(" ")[0]
        if make.lower() == searched_make.lower():
            makes.append(car)
    return makes


def search_by_model(all_cars: str, searched_model: str) -> list:
    """
    Return list of cars with given model.

    The order of the elements should be the same as in the input string (first appearance).
    """
    cars_split = all_cars.split(",")
    if not all_cars:
        return []
    models = []
    for car in cars_split:
        models.extend(
            car
            for model in car.split(" ")[1:]
            if model.lower() == searched_model.lower()
        )

    return models


def car_make_and_models(all_cars: str) -> list:
    """
    Create a list of structured information about makes and models.

    For each different car make in the input string an element is created in the output list.
    The element itself is a list, where the first position is the name of the make (string),
    the second element is a list of models for the given make (list of strings).

    No duplicate makes or models should be in the output.

    The order of the makes and models should be the same os in the input list (first appearance).

    "Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon Lux,Skoda Superb,Skoda Superb,BMW x5" =>
    [['Audi', ['A4']], ['Skoda', ['Super', 'Octavia', 'Superb']], ['BMW', ['530', 'x5']], ['Seat', ['Leon Lux']]]
    """
    cars_split = all_cars.split(",")
    if not all_cars:
        return []
    makes = []
    for car in cars_split:
        make = car.split(" ")[0]
        model = car.split(" ")[1:]
        model = " ".join(model)
        if make not in makes:
            makes.append(make)
    makes_and_models = []
    for make in makes:
        models = []
        for car in cars_split:
            if make in car:
                model = car.split(" ")[1:]
                model = " ".join(model)
                if model not in models:
                    models.append(model)
        makes_and_models.append([make, models])
    return makes_and_models


def add_cars(car_list: list, all_cars: str) -> list:
    """
    Add cars from the list into the existing car list.

    The first parameter is in the same format as the output of the previous function.
    The second parameter is a string of comma separated cars (as in all the previous functions).
    The task is to add cars from the string into the list.

    Hint: This and car_make_and_models are very similar functions. Try to use one inside another.

    [['Audi', ['A4']], ['Skoda', ['Superb']]]
    and
    "Audi A6,BMW A B C,Audi A4"

    =>

    [['Audi', ['A4', 'A6']], ['Skoda', ['Superb']], ['BMW', ['A B C']]]
    """
    cars = car_make_and_models(all_cars)
    # First we add the cars from the string into the list.
    for car in cars:
        # If the make is not in the list, we add it.
        if car[0] not in [x[0] for x in car_list]:
            car_list.append(car)
        else:
            # If the make is in the list, we add the models.
            for make in car_list:
                if make[0] == car[0]:
                    for model in car[1]:
                        if model not in make[1]:
                            make[1].append(model)
    return car_list


def number_of_cars(all_cars: str) -> list:
    """
    Create a list of tuples with make quantities.

    The result is a list of tuples.
    Each tuple is in the form: (make_name: str, quantity: int).
    The order of the tuples (makes) is the same as the first appearance in the list.
    print(number_of_cars("Audi A4,Skoda Superb,Seat Leon,Audi A6")) # [('Audi', 2), ('Skoda', 1), ('Seat', 1)]
    print(number_of_cars("Mazda 6,Mazda 6,Mazda 6,Mazda 6")) # [('Mazda', 4)]
    print(number_of_cars("")) # []
    """
    cars_split = all_cars.split(",")
    if not all_cars:
        return []
    makes = []
    for car in cars_split:
        make = car.split(" ")[0]
        if make not in makes:
            makes.append(make)
    makes_and_quantity = []
    for make in makes:
        quantity = sum(make in car for car in cars_split)
        makes_and_quantity.append((make, quantity))
    return makes_and_quantity


def car_list_as_string(cars: list) -> str:
    """
    Create a list of cars.

    The input list is in the same format as the result of car_make_and_models function.
    The order of the elements in the string is the same as in the list.
    [['Audi', ['A4']], ['Skoda', ['Superb']]] =>
    "Audi A4,Skoda Superb"
    """
    if not cars:
        return ""
    cars_list = []
    for make in cars:
        cars_list.extend(f"{make[0]} {model}" for model in make[1])
    return ",".join(cars_list)


print(
    list_of_cars("Audi A4,Skoda Superb,Audi A4")
)  # ["Audi A4", "Skoda Superb", "Audi A4"]
print()
print(list_of_cars(""))  # []
print()
print(
    car_makes(
        "Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,Skoda Superb,Skoda Superb,BMW x5"
    )
)
# ['Audi', 'Skoda', 'BMW', 'Seat']
print()
print(car_makes("Mazda 6,Mazda 6,Mazda 6,Mazda 6"))  # ['Mazda']
print()
print(car_makes(""))  # []
print()
print(
    car_models(
        "Audi A4,Skoda Superb,Audi A4,Audi A6,Tesla Model S,Skoda Super Lux Sport"
    )
)  # ['A4', 'Superb', 'A6', 'Model S', 'Super Lux Sport']
print()
print(car_models(""))  # []
print()
print(
    search_by_make(
        "Audi A4,Skoda Superb,Audi A4,Audi A6,Tesla Model S,Skoda Super Lux Sport",
        "Audi",
    )
)  # ["Audi A4", "Audi A4", "Audi A6"]
print()
print(
    search_by_make("Audi A4,audi A5,AUDI a6 A7", "AuDi")
)  # ["Audi A4", "audi A5", "AUDI a6 A7"]
print()
print(
    search_by_model(
        "Audi A4,Skoda Superb,Audi A4,Audi A6,Tesla Model S,Skoda Super Lux Sport",
        "Superb",
    )
)  # ["Skoda Superb"]
print()
print(
    search_by_model("Audi A4,Audi a4 2021,Audi A40", "")
)  # ["Audi A4", "Audi a4 2021"]
print()

print(
    car_make_and_models(
        "Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,Skoda Superb,Skoda Superb,BMW x5"
    )
)
# [['Audi', ['A4']], ['Skoda', ['Super', 'Octavia', 'Superb']], ['BMW', ['530', 'x5']], ['Seat', ['Leon']]]
print()
print(car_make_and_models("Mazda 6,Mazda 6,Mazda 6,Mazda 6"))  # [['Mazda', ['6']]]
print()
print(car_make_and_models(""))  # []
print()
print(add_cars([["Audi", ["A4"]], ["Skoda", ["Superb"]]], "Audi A6,BMW A B C,Audi A4"))
# [['Audi', ['A4', 'A6']], ['Skoda', ['Superb']], ['BMW', ['A B C']]]

print()
print(
    number_of_cars("Audi A4,Skoda Superb,Seat Leon,Audi A6")
)  # [('Audi', 2), ('Skoda', 1), ('Seat', 1)]
print(number_of_cars("Mazda 6,Mazda 6,Mazda 6,Mazda 6"))  # [('Mazda', 4)]
print(
    number_of_cars("Audi A4,Skoda Superb,Seat Leon,Audi A6,Tesla Model S,Skoda Octavia")
)  # [('Audi', 2), ('Skoda', 2), ('Seat', 1), ('Tesla', 1)]
print(number_of_cars(""))  # []
print()
print(
    car_list_as_string([["Audi", ["A4"]], ["Skoda", ["Superb"]]])
)  # "Audi A4,Skoda Superb"
print(
    car_list_as_string(
        [["Audi", ["A4", "A6"]], ["Skoda", ["Superb"]], ["BMW", ["A B C"]]]
    )
)  # "Audi A4,Audi A6,Skoda Superb,BMW A B C"
print(car_list_as_string([["Mazda", ["6"]]]))  # "Mazda 6"
print(car_list_as_string([]))  # ""
