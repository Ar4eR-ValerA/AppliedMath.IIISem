class GradientParams:
    def __init__(self, max_iter=1000, learning_rate=0.05, momentum=0, eps=0.001, dimensions=1):
        self.maxIter = max_iter
        self.rate = learning_rate
        self.momentum = momentum
        self.eps = eps
        self.dimensions = dimensions
