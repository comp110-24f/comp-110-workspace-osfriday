"""How much money is needed to host a tea party?"""

__author__: str = "730566893"


def main_planner(guests: int) -> None:
    """Breaks down number of tea bags and treats and total cost of party."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """How many tea bags needed depending on number of guests"""
    return 2 * people


def treats(people: int) -> int:
    """How many treats needed depending on number of guests"""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Summing the total costs for teas and treats."""
    return 0.50 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

# Comments
# Why couldn't the conditional statement go at the start? -> the function/program?
#   Wasn't defined yet so there was nothing to look for.
# Why put "people=people" arguments in code??? Is it because it changes when from
#   people -> guests so it's important to keep your variables clearly defined?
