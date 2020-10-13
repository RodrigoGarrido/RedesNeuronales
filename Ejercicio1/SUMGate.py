from NANDPerceptron import NANDPerceptron

class SUMGate:
    def __init__(self):
        self.Perceptrons = [NANDPerceptron() for _ in range(5)]