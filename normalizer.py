class norm:
    def __init__(self):
        self.peak = 1e-6

    def process(self, x):
        if abs(x) > self.peak:
            self.peak = abs(x)
        return x / self.peak

    