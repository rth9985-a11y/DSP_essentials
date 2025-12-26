class norm:
    def __init__(self):
        # Prevent divison by 0 on first sample
        self.peak = 1e-6

    def process(self, x):
        if abs(x) > self.peak:
            self.peak = abs(x)
        return x / self.peak

    