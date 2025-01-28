"""Program to plan a tea party, Ishan Bheda"""

__author__: str = "730606044"


def tea_bags(people: int) -> int:
    """This function will tell how many tea bags we need"""
    return people * 2


def treats(people: int) -> int:
    """This function tells how many treats we need"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Determines the cost of the tea party"""
    return tea_count * 0.5 + treat_count * 0.75


def main_planner(guests: int) -> None:
    """This summarizes all the information for the party"""
    print("A Cozy Tea Party For", guests, "People!")
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print(
        "Cost:",
        "$"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        ),
    )
    return None


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your party?")))
