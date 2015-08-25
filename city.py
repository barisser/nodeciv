import economics
import resources
import settings

class City:
    def __init__(self, name, x, y, population):
        self.x = x
        self.name = name
        self.y = y
        self.population = population
        self.commodity_stocks = [0] * len(resources.resources)
        self.prices = [0] * len(resources.resources)
        self.money = self.population * 1
        self.productivity = [1] * len(resources.resources)
        self.labor = [1.0 / len(resources.resources)] * len(resources.resources)

    def produce(self, data):
        resources_n = len(resources.resources)
        for i in range(0, resources_n):
            production = self.productivity[i] * self.population * self.labor[i]
            previous_supply = self.commodity_stocks[i]
            self.commodity_stocks[i] += production
            self.prices[i] = economics.find_price(previous_supply, self.commodity_stocks[i], self.prices[i], resources.resources[i].base_demand, resources.resources[i].price_elasticity)

    def consume(self, data):
        for i in range(0, len(resources.resources)):
            to_consume = economics.how_much_to_consume(self.money, self.population, resources.resources[i], self.commodity_stocks[i])

            if i == 0: #food
                if to_consume < self.population * settings.food_per_person:
                    #kill them off
                    self.population = self.population * (1.0 - settings.starvation_rate)
                else:
                    self.population = self.population * (1.0 + settings.growth_rate)

            self.commodity_stocks[i] = self.commodity_stocks[i] - to_consume

    def cycle(self, data):
        self.produce(data)
        self.consume(data)
