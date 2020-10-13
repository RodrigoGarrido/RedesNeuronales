from NANDPerceptron import NANDPerceptron

class SUMGate:
    def __init__(self):
        self.Perceptron = NANDPerceptron()

    def compute(self, in1, in2):
        aux1 = self.Perceptron.compute(in1, in2)
        carry = self.Perceptron.compute(aux1, aux1)
        aux2 = self.Perceptron.compute(in1, aux1)
        aux3 = self.Perceptron.compute(aux1, in2)
        sum = self.Perceptron.compute(aux2, aux3)
        return sum, carry
        
