import math


def price_change(current_supply, base_demand, price_elasticity, change_in_supply, current_price):
    if current_supply == 0:
        current_supply = 1
    price_shoot = math.pow(change_in_supply / current_supply + 1.0, -1) * current_price
    new_price = current_price + price_shoot
    equ_new_diff = new_price - equilibrium_price(current_supply + change_in_supply, base_demand, price_elasticity)
    equ_decay_factor = 0.9 #1 is full momentum, 0 is full equilibrium
    equ_new_diff = equ_new_diff * (1-equ_decay_factor)
    return new_price - equ_new_diff


def equilibrium_price(supply, base_demand, price_elasticity):
    if supply < 0.5:
        supply = 0.5
    p = base_demand - math.log(supply) / (price_elasticity + 0.01)
    if p < 0:
        p = 0
    return p


def find_price(previous_supply, new_supply, previous_price, base_demand, price_elasticity):
    return equilibrium_price(new_supply, base_demand, price_elasticity)


def how_much_to_consume(total_money, population, resource, supply):
    to_consume = 1.0
    return to_consume

#def simple_price(supply, base_de,amd. price_elasticity, population, money_supply):
