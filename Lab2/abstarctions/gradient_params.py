class gradient_params:
    def __init__(self, maxIter=1000, learningRate=0.05, momentum=0, eps=0.001,
                 dimensions=1):
        self.maxIter = maxIter
        self.rate = learningRate
        self.momentum = momentum
        self.eps = eps
        self.dimensions = dimensions

