
class Resource:
    def __init__(self, name, base_demand, price_elasticity, n):
        self.name = name
        self.base_demand = base_demand
        self.price_elasticity = price_elasticity


def init_resources():
    resources = []
    food = Resource('food', 10, 0.01, 0)
    wood = Resource('wood', 4, 1, 1)
    iron = Resource('iron', 20, 5, 2)
    labor = Resource('labor', 0, 0.1, 3)
    power = Resource('power', 5, 5, 4)
    resources.append(food)
    resources.append(wood)
    resources.append(iron)
    resources.append(labor)
    resources.append(power)
    return resources

resources = init_resources()
resource_dict = {}
for resource in resources:
    resource_dict[resource.name] = resource
