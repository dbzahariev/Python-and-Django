class Technique:
    def __init__(self, name, points):
        self.name = name
        self.points = points


class Gladiator:
    def __init__(self, name):
        self.name = name
        self.technique_list = []
        self.total_points = 0

    def add_technique(self, name, points):
        points = int(points)
        founded_index = find_return_index(name, self.technique_list)
        if founded_index == -1:
            self.total_points += points
            self.technique_list.append(Technique(name, points))

    def remove_technique(self, name):
        founded_index = find_return_index(name, self.technique_list)
        self.total_points -= self.technique_list[founded_index].points
        del self.technique_list[founded_index]

    def __str__(self):
        this_list = [f'{self.name}: {self.total_points} skill']
        self.technique_list = sorted(self.technique_list, key=lambda k: (-k.points, k.name))
        for teh in self.technique_list:
            this_list.append(f"- {teh.name} <!> {teh.points}")
        return '\n'.join(this_list)


def find_return_index(name, this_list):
    for i in range(len(this_list)):
        if this_list[i].name == name:
            return i
    return -1


data_base = []
while True:
    old_data = input()
    data = old_data.split()
    if data[1] == '->':
        data.remove('->')
        data.remove('->')
    else:
        data = old_data
        break

    gladiator_index = find_return_index(data[0], data_base)
    if gladiator_index == -1:
        one_gladiator = Gladiator(data[0])
        one_gladiator.add_technique(data[1], data[2])
        data_base.append(one_gladiator)
    else:
        data_base[gladiator_index].add_technique(data[1], data[2])
    data_base = sorted(data_base, key=lambda x: x.total_points, reverse=True)

while True:
    if data == 'Ave Cesar':
        break
    data = data.split()
    founded_index_1 = find_return_index(data[0], data_base)
    founded_index_2 = find_return_index(data[2], data_base)

    if founded_index_1 == -1 or founded_index_2 == -1:
        data = input()
        continue

    while True:
        count_killed = 0
        for teh_1 in data_base[founded_index_1].technique_list:
            for teh_2 in data_base[founded_index_2].technique_list:
                if teh_1.name == teh_2.name:
                    if teh_1.points > teh_2.points:
                        data_base[founded_index_2].remove_technique(teh_2.name)
                    else:
                        data_base[founded_index_1].remove_technique(teh_1.name)
                    count_killed += 1
        if count_killed == 0:
            data_base = list(filter(lambda x: x.total_points > 0, data_base))
            break

    data = input()

for gladiator in data_base:
    print(gladiator)
