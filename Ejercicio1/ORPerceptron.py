class ANDPerceptron:
    def __init__(self):
        self.w1 = 0.5
        self.w2 = 0.5
        self.t = 0.1

    def compute(self, in1, in2):
        aux = in1*self.w1 + in2*self.w2
        if aux < self.t:
            return 0
        return 1 