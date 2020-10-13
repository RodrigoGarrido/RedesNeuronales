from random import uniform

class PositionLearningPerceptron:
    def __init__(self, lr):
        self.w1 = 0.5
        self.w2 = 0.5
        self.bias = 0
        self.lr = lr

    def learn(self, x, y, realOutput, desiredOutput):
        diff = desiredOutput - realOutput

        self.w1 += self.lr*x*diff
        self.w2 += self.lr*y*diff

        self.bias += self.lr*diff

    def compute(self, x, y):
        if (self.w1*x+self.w2*y > self.bias):
            return 1
        return 0
    
    def iteration(self, x, y, desiredOutput):
        realOutput = self.compute(x, y)
        self.learn(x, y, realOutput, desiredOutput)


def lineTraining(per, m, n, points):
    for _ in range(points):
        x = uniform(-10, 10)
        y = uniform(n-10, n+10)
        des = 0 if (y < m*x+n) else 1
        per.iteration(x, y, des)

def lineTest(per, m, n, points):
    successes = 0
    mistakes = 0
    for _ in range(points):
        x = uniform(-10, 10)
        y = uniform(n-10, n+10)
        res = per.compute(x, y)
        des = 0 if (y < m*x+n) else 1
        if res == des:
            successes += 1
        else:
            mistakes += 1
    return successes, mistakes

p = PositionLearningPerceptron(0.001)
m = 1
n = 2
lineTraining(p, m, n, 10000000)
print(lineTest(p, m, n, 3000))

