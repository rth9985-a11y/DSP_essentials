import numpy as np
import math
import normalizer as norm

class hpfFO:
    def __init__(self, fs, norm, fc):
        self.fs = fs
        self.norm = norm
        self.fc = fc
        self.alpha = 1 / (1 + (2 * math.pi * fc) / fs)
        self.state = 0.0

    def process(self, data):
        output = np.zeros_like(data)

        for i in range(len(data)):
            xn = norm.process(data[i])
            yn = self.alpha * (self.state + xn - self.state)
            self.state = yn
            output[i] = yn
        
        return output