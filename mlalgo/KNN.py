class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def _euclidean_distance(self, x1, x2):
        return sum((a - b) ** 2 for a, b in zip(x1, x2)) ** 0.5

    def _get_neighbors(self, X):
        distances = [(self._euclidean_distance(X, x_train), y) for x_train, y in zip(self.X_train, self.y_train)]
        distances.sort(key=lambda x: x[0])
        k_nearest_labels = [y for _, y in distances[:self.k]]
        return k_nearest_labels

    def predict(self, X):
        raise NotImplementedError("This method should be overridden by subclasses")


class KNNRegressor(KNN):
    def predict(self, X):
        predictions = [sum(self._get_neighbors(x)) / self.k for x in X]
        return predictions


class KNNClassificator(KNN):
    def predict(self, X):
        predictions = []
        for x in X:
            neighbors = self._get_neighbors(x)
            label_counts = {}
            for label in neighbors:
                if label in label_counts:
                    label_counts[label] += 1
                else:
                    label_counts[label] = 1
            predictions.append(max(label_counts, key=label_counts.get))
        return predictions
