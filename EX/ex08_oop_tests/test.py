"""Test solution.py"""
import random
import pytest
from solution import Factory, Cake, WrongIngredientsAmountException


@pytest.fixture
def factory() -> Factory:
    """Returns a factory"""
    return Factory()


def test_produce_cake_only_basic(factory):
    """Test that the factory produces only basic cakes"""
    amount = factory.bake_cake(1, 1)
    assert amount == 1


@pytest.mark.dependency()
def test_produce_cake_only_medium(factory):
    """Test that the factory produces only medium cakes"""
    assert factory.bake_cake(2, 2) == 1
    assert factory.bake_cake(4, 4) == 2


@pytest.mark.dependency()
def test_produce_cake_only_large(factory):
    """Test that the factory produces only large cakes"""
    assert factory.bake_cake(5, 5) == 1
    assert factory.bake_cake(10, 10) == 2


@pytest.mark.dependency(depends=["test_produce_cake_only_medium"])
def test_produce_cake_medium_remaining_ingredients_produce_more_cakes(factory):
    """Test that the factory produces more cakes if there are remaining ingredients"""
    assert factory.bake_cake(3, 3) != 1
    assert factory.bake_cake(5, 5) != 2


@pytest.mark.dependency(depends=["test_produce_cake_only_large"])
def test_produce_cake_large_remaining_ingredients_produce_more_cakes(factory):
    """Test that the factory produces more cakes if there are remaining ingredients"""
    assert factory.bake_cake(6, 6) != 1
    assert factory.bake_cake(11, 11) != 2


def test_produce_cake_get_cakes(factory):
    """
    This function tests the ability of the factory to produce cakes.
    It does this by baking a cake, and then checking that the factory
    has a cake in its list of cakes.
    """
    factory.bake_cake(1, 1)
    assert len(factory.get_cakes_baked()) == 1
    cake = factory.get_last_cakes(1)[0]
    assert cake is not None
    assert type(cake) == Cake


def test_produce_cakes_get_last_cakes(factory):
    """
    This function tests the ability of the factory to produce cakes.
    @param factory:
    @return:
    """
    amount = factory.bake_cake(3, 3)
    assert amount == 2
    cakes = factory.get_last_cakes(2)
    assert type(cakes) == list
    assert len(cakes) == 2
    cakes = factory.get_last_cakes(1)
    assert type(cakes) == list
    assert len(cakes) == 1


def test_produce_cakes_order_medium_before(factory):
    """
    This function tests the ability of the factory to produce medium cakes before large cakes.

    @param factory:
    @return:
    """
    factory.bake_cake(3, 3)
    cakes = factory.get_last_cakes(2)
    assert cakes
    assert cakes[0].type == "medium"
    assert cakes[1].type != "medium"


def test_produce_cakes_order_large_before(factory):
    """
    This function tests the ability of the factory to produce large cakes before basic cakes.

    @param factory:
    @return:
    """
    factory.bake_cake(6, 6)
    cakes = factory.get_last_cakes(2)
    assert cakes[0].type == "large"
    assert cakes[1].type != "large"


@pytest.mark.dependency()
def test_get_cakes_correct_amount(factory):
    """
    This test checks that the factory returns the correct amount of cakes.

    @param factory:
    @return:
    """
    factory.bake_cake(9, 9)
    assert len(factory.get_cakes_baked()) == 3


@pytest.mark.dependency()
def test_get_last_cakes_correct_amount(factory):
    """
    This test checks that the factory returns the last cakes correctly.

    @param factory:
    @return:
    """
    factory.bake_cake(9, 9)
    for i in range(0, 3):
        assert len(factory.get_last_cakes(i)) == i


@pytest.mark.dependency(depends=["test_get_cakes_correct_amount"])
def test_get_cakes_returns_cakes(factory):
    """
    This test checks that the factory returns the correct amount of cakes.

    @param factory:
    @return:
    """
    factory.bake_cake(9, 9)
    assert all(type(cake) == Cake for cake in factory.get_cakes_baked())


@pytest.mark.dependency(depends=["test_get_cakes_correct_amount"])
def test_get_last_cakes_returns_cakes(factory):
    """
    Get the last cakes and check that they are of type Cake.

    @param factory:
    @return:
    """
    factory.bake_cake(9, 9)
    assert all(type(cake) == Cake for cake in factory.get_last_cakes(4))


@pytest.mark.dependency(depends=["test_get_cakes_correct_amount", "test_get_last_cakes_correct_amount"])
def test_produce_cakes_order(factory):
    """
    This function tests the ability of the factory to produce cakes in the correct order.

    @param factory:
    @return:
    """
    factory.bake_cake(8, 8)
    assert len(factory.get_cakes_baked()) == 3
    cakes = factory.get_last_cakes(3)
    assert cakes[2].type == "basic"
    assert cakes[1].type == "medium"
    assert cakes[0].type == "large"


def test_cake_basic():
    """
    This test checks that the basic cake is created correctly.
    @return:
    """
    basic_cake = Cake(1, 1)
    assert basic_cake.type == "basic"


def test_cake_medium():
    """
    This test checks that the medium cake is created correctly.
    @return:
    """
    medium_cake = Cake(2, 2)
    assert medium_cake.type == "medium"


def test_cake_large():
    """
    This test checks that the large cake is created correctly.

    @return:
    """
    large_cake = Cake(5, 5)
    assert large_cake.type == "large"


def test_cake_wrong_ingredients_throws_exception():
    """
    This test checks that the cake throws an exception if the ingredients are wrong.

    @return:
    """
    for i in {i for i in range(1000)} - {1, 2, 5}:
        with pytest.raises(WrongIngredientsAmountException):
            Cake(i, i)


def test_cake_equals():
    """
    This test checks that the cake equals function works correctly.

    @return:
    """
    cake_basic_1 = Cake(1, 1)
    cake_basic_2 = Cake(1, 1)
    cake_medium_1 = Cake(2, 2)
    cake_medium_2 = Cake(2, 2)
    cake_large_1 = Cake(5, 5)
    cake_large_2 = Cake(5, 5)
    assert cake_basic_1 == cake_basic_2
    assert cake_medium_1 == cake_medium_2
    assert cake_large_1 == cake_large_2


def test_cake_repr():
    """
    This test checks that the cake representation function works correctly.

    @return:
    """
    cake_basic = Cake(1, 1)
    cake_medium = Cake(2, 2)
    cake_large = Cake(5, 5)
    assert cake_basic.__repr__() == "Cake(basic)"
    assert cake_medium.__repr__() == "Cake(medium)"
    assert cake_large.__repr__() == "Cake(large)"


def test_factory_str_amount(factory):
    """
    This test checks if the string returned by the factory is correct.

    @param factory:
    @return:
    """
    num = random.randint(3, 1000)
    for x in [(1, 1) for _ in range(2, num)]:
        factory.bake_cake(*x)
    assert str(factory) == f"Factory with {num - 2} cakes."


def test_factory_str_single(factory):
    """
    This test checks if the string returned by the factory is correct, if there is only one cake.

    @param factory:
    @return:
    """
    factory.bake_cake(1, 1)
    assert str(factory) == "Factory with 1 cake."
