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
