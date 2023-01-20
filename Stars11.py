class Operation(object):
    def __init__(self, operator, value):
        self.operator = operator
        self.value = value

    def compute(self, old):
        if self.value == "old":
            value = old
        else:
            value = int(self.value)
        if self.operator == "+":
            new = old + value
        if self.operator == "*":
            new = old * value
        return new

class Test(object):
    def __init__(self, value, monkeyTrue, monkeyFalse):
        self.value = value
        self.result = {True: monkeyTrue, False: monkeyFalse}

    def computeTest(self, sample):
        if sample%self.value == 0:
            return True
        else:
            return False
    def computeTrue(self, sample):
        return sample // self.value
    def computeFalse(self, sample):
        return sample % self.value

class Monkey(object):
    def __init__(self, identity, items, operation, test):
        self.id = identity
        self.items = items
        self.operation = operation
        self.test = test
        self.business = 0

with open("puzzle11.txt") as file:
    monkeys = file.read().split("Monkey")
    monkeyDict = dict()
    monkeyYEnATrop = set()
    moduloMagique = 1
    for monkey in monkeys :
        if monkey != "":
            monkey = monkey.splitlines()
            for (i,line) in enumerate(monkey):
                if line != "":
                    line = line.strip()
                    if i == 0 :
                        identity = line[0]
                    if i == 1 :
                        itemsList = line.split(":")[1].split(",")
                        items = [int(item.strip()) for item in itemsList]
                    if i == 2 :
                        rightOperation = line.split(":")[1].split("=")[1].strip().split(" ")
                        operator = rightOperation[1]
                        value = rightOperation[2]
                        operation = Operation(operator, value)
                    if i == 3 :
                        valueTest = int(line.strip().split(" ")[-1])
                        monkeyYEnATrop.add(valueTest)
                    if i == 4 :
                        monkeyTrue = line.strip().split(" ")[-1]
                    if i == 5 :
                        monkeyFalse = line.strip().split(" ")[-1]
                        test = Test(valueTest, monkeyTrue, monkeyFalse)
                        monkeyDict[identity] = Monkey(identity, items, operation, test)
    for modulo in monkeyYEnATrop:
        moduloMagique = moduloMagique * modulo
    for i in range(10000):
        for monkey in monkeyDict.values():
            for item in monkey.items:
                item = monkey.operation.compute(item)%moduloMagique
                if monkey.test.computeTest(item):
                    monkeyDict[monkey.test.result[True]].items.append(item)
                else :
                    monkeyDict[monkey.test.result[False]].items.append(item)
                monkey.business += 1
            monkey.items = []
    bestBusiness = []
    for monkey in monkeyDict.values():
        print(monkey.id, monkey.business)
        bestBusiness.append(monkey.business)
    # pa bo aled
    bestBusiness1 = max(bestBusiness)
    secondBestBusiness = bestBusiness
    secondBestBusiness.remove(bestBusiness1)
    bestBusiness2 = max(secondBestBusiness)

    print("Best business : ", bestBusiness1)
    print("Second best business : ", bestBusiness2)
    print("Monkey business : ", bestBusiness1 * bestBusiness2)



            