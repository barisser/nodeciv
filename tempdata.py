import city
import resources
import world

def init_cities(world):
    London = city.City('London', 30, 30, 100)
    Paris = city.City('Paris', 60, 20, 50)
    world.cities.append(London)
    world.cities.append(Paris)
    return world

def init_data():
    data = {}
    data['resources'] = resources.init_resources()
    protoworld = world.World(data)
    protoworld = init_cities(protoworld)

    data['world'] = protoworld
    data['players'] = []
    return data
