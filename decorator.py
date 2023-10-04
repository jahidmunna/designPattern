class Pizza:
    def cost(self):
        return 10


class TomatoToppingDecorator:
    def __init__(self, pizza):
        self._pizza = pizza

    def cost(self):
        return self._pizza.cost() + 2


class CheeseToppingDecorator:
    def __init__(self, pizza):
        self._pizza = pizza

    def cost(self):
        return self._pizza.cost() + 3


if __name__ == "__main__":
    pizza = Pizza()
    pizza_with_tomato = TomatoToppingDecorator(pizza)
    pizza_with_cheese = CheeseToppingDecorator(pizza)

    print(f"Pizza cost: {pizza.cost()}")  # Output: Pizza cost: 10
    # Output: Pizza with Tomato cost: 12
    print(f"Pizza with Tomato cost: {pizza_with_tomato.cost()}")
    # Output: Pizza with Cheese cost: 13
    print(f"Pizza with Cheese cost: {pizza_with_cheese.cost()}")
