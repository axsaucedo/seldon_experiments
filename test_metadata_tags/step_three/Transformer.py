import logging

class Transformer():

    def __init__(self):
        self._tags = {}

    def predict_raw(self, request):
        request["meta"]["tags"]["current"] = "three"
        request["meta"]["tags"]["three"] = "yes"
        return request

    def predict(self, X, feature_names, meta):
        logging.warning(X)
        logging.warning(feature_names)
        logging.warning(meta)
        self._tags["value"] = X.tolist()
        self._tags["current"] = "three"
        self._tags["three"] = "yes"
        return X

    def tags(self):
        return self._tags

