class AI:
    def __init__(self, algorithm, model_type):
        self.algorithm = algorithm
        self.model_type = model_type
    
    def fit(self, model, X_train, y_train):
        pass

    def predict(self, model, X_pred):
        pass

class DeepLearning(AI):
    def train_on_epoch(self, model, X_train, y_train, epoch):
        pass
    def fit(self, model, X_train, y_train, learning_rate):
        pass

if __name__ == '__main__':
    ai1 = AI(algorithm='lr', model_type='linear')
    