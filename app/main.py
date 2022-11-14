class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    instance_list = [
        Person(person["name"], person["age"]) for person in people
    ]
    for man in people:
        if "wife" in man and man["wife"] is not None:
            for wife in people:
                if man["wife"] == wife["name"]:
                    Person.people[man["name"]].wife = \
                        Person.people[wife["name"]]
    for woman in people:
        if "husband" in woman and woman["husband"] is not None:
            for husband in people:
                if woman["husband"] == husband["name"]:
                    Person.people[woman["name"]].husband = \
                        Person.people[husband["name"]]
    return instance_list
