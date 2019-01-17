#simple 2 player NN tutorial
class NeuralNetwork:
    def __init__(self, x,y):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1],4)
        self.weights2 = np.random.rand(4,1)
        self.y        = y
        self.output = np.zeos(y.shape)
    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))
    def backdrop(self):
        # application of the chain tule to find the derrivative of the loss function with respect to weight
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights2 = np.dot(self.input.t, (np.dot(2*self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T)* sigmoid_derivative(self.layer1))

        #update weights with derivative of loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2
            
