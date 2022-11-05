"""This is a solution to the OOP tests exercise."""


class Factory:
    def __init__(self):
        """
        Initializes the factory.
        """
        self.cakes = []

    def bake_cake(self, toppings: int, base: int) -> int:
        """
        Bakes a cake with the given amount of toppings and base.
        :param toppings: The amount of toppings.
        :param base: The amount of base.
        :return: The amount of cakes baked.
        """
        if toppings >= 5 and base >= 5:
            self.cakes.append(Cake(5, 5))
            return 1 + self.bake_cake(toppings - 5, base - 5)
        elif toppings >= 2 and base >= 2:
            self.cakes.append(Cake(2, 2))
            return 1 + self.bake_cake(toppings - 2, base - 2)
        elif toppings >= 1 and base >= 1:
            self.cakes.append(Cake(1, 1))
            return 1 + self.bake_cake(toppings - 1, base - 1)
        else:
            return 0

    def get_cakes_baked(self) -> list:
        """
        Returns all the cakes baked.
        :return: A list of cakes.
        """
        return self.cakes

    def get_last_cakes(self, amount: int) -> list:
        """
        Returns the last amount of cakes baked.
        :param amount: The amount of cakes to return.
        :return: A list of cakes.
        """
        return self.cakes[:amount]

    def __str__(self):
        """
        Returns a string representation of the factory.
        @return:
        """
        amount = len(self.cakes)
        if amount == 1:
            return "Factory with 1 cake."
        else:
            return f"Factory with {amount} cakes."


class Cake:
    def __init__(self, toppings: int, base: int):
        """
        Initializes the cake.
        @param toppings:
        @param base:
        """
        while True:
            if toppings == 1 and base == 1:
                self.type = "basic"
                break
            elif toppings == 2 and base == 2:
                self.type = "medium"
                break
            elif toppings == 5 and base == 5:
                self.type = "large"
                break
            else:
                raise WrongIngredientsAmountException("Wrong ingredients amount")

    def __eq__(self, other):
        """
        Checks if the cake is equal to another cake.
        @param other:
        @return:
        """
        return self.type == other.type

    def __repr__(self):
        """
        Returns a string representation of the cake.
        @return:
        """
        return f"Cake({self.type})"


class WrongIngredientsAmountException(Exception):
    """
    This exception is raised when the amount of ingredients is wrong.
    """
    pass

# Style success: 100.00/100.00 xd
