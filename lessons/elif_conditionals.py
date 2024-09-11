"""Practice with elif Statements, Local Variables and Conditionals"""

# Variables
#   Declaration of a variable
#       <name>: <type> = 300
# Update a Variable
#   <name> = <new value>
#


def less_than_10(num: int) -> None:
    """Tell me if num is < 10."""
    dub: int = num * 2
    print(dub)
    if num < 10:
        print("Small number!")
    else:
        print("Big Number!")
    print("Have a nice day!")


less_than_10(num=7)


def number_info(num: int) -> None:
    if num < 10:
        print("Small number.")
    elif num % 2 == 0:
        print("Even number.")
    else:
        print("Odd number.")


number_info(num=13)


def get_weather_report() -> str:
    """Results of asking what the weather is."""
    weather: str = input("What's the weather?")
    if (
        weather == "rainy" or weather == "cold"
    ):  # Must check for weather == to both "rainy" or "cold"
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()
