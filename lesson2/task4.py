worlds = input('Введите предложение: ').split(' ')
for i, world in enumerate(worlds, 1):
    if len(world) > 10:
        world = world[0:10]
    print(i, world)