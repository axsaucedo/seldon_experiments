import logging

class DummySKModel():
    def transform(self):
        return [0.2, 0.8]

class Model():

    def __init__(self):
        self._model = DummySKModel()

    def predict(self, X, feature_names, meta):
        logging.warning(X)
        logging.warning(feature_names)
        logging.warning(meta)
        return self._model.transform() 


