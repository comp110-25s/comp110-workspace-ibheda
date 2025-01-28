"""My first excercise in Comp110!"""

__author__ = "730606044"


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("What is your name?")))
