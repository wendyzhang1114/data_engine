import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder


class Project_C:

    def get_data(self):
        data = pd.read_csv('./CarPrice_Assignment.csv')
        return data

    def train(self):
        data = self.get_data()
        train_x = data[['symboling', 'fueltype', 'aspiration', 'doornumber', 'carbody', 'drivewheel', 'enginelocation', 'wheelbase', 'carlength', 'carwidth', 'carheight', 'curbweight',
                        'enginetype', 'cylindernumber', 'enginesize', 'fuelsystem', 'boreratio', 'stroke', 'compressionratio', 'horsepower', 'peakrpm', 'citympg', 'highwaympg', 'price']]

        # LabelEncoder
        le = LabelEncoder()
        train_x['fueltype'] = le.fit_transform(train_x['fueltype'])
        train_x['aspiration'] = le.fit_transform(train_x['aspiration'])
        train_x['doornumber'] = le.fit_transform(train_x['doornumber'])
        train_x['carbody'] = le.fit_transform(train_x['carbody'])
        train_x['drivewheel'] = le.fit_transform(train_x['drivewheel'])
        train_x['enginelocation'] = le.fit_transform(train_x['enginelocation'])
        train_x['enginetype'] = le.fit_transform(train_x['enginetype'])
        train_x['cylindernumber'] = le.fit_transform(train_x['cylindernumber'])
        train_x['fuelsystem'] = le.fit_transform(train_x['fuelsystem'])

        kmeans = KMeans(n_clusters=3)
        min_max_scaler = preprocessing.MinMaxScaler()
        train_x = min_max_scaler.fit_transform(train_x)
        kmeans.fit(train_x)
        predict_y = kmeans.predict(train_x)

        result = pd.concat((data, pd.DataFrame(predict_y)), axis=1)
        result.rename({0: u'result'}, axis=1, inplace=True)
        print(result)
        result.to_csv("result.csv",index=False)


if __name__ == "__main__":
    project = Project_C()
    project.train()
