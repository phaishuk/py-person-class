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
    for person in people:
        if "wife" in person and person["wife"] is not None:
            for wife in people:
                if person["wife"] == wife["name"]:
                    Person.people[person["name"]].wife = \
                        Person.people[wife["name"]]
        if "husband" in person and person["husband"] is not None:
            for husband in people:
                if person["husband"] == husband["name"]:
                    Person.people[person["name"]].husband = \
                        Person.people[husband["name"]]
    return instance_list
