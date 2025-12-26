import numpy as np
import math
from normalizer import norm

class lpfFO:
    def __init__(self, fs, norm, fc):
        self.fs = fs
        self.fc = fc
        self.alpha = (2 * math.pi * fc) / (2 * math.pi * fc + fs)
        self.state = 0.0
        self.norm = norm

    def process(self, data):
        output = np.zeros_like(data)

        for i in range(len(data)):
            xn = self.norm.process(data[i])
            yn = self.state + self.alpha * (xn - self.state)
            self.state = yn
            output[i] = yn
        
        return output
        
