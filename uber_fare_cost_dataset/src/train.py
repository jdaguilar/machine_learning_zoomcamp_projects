import pandas as pd

from extra.cleaning import clean_data
from extra.feature_engineering import add_features
from extra.model_training import train_model


DATA_FILE = 'data/uber.csv'
DEST_MODEL_PATH = 'models/trained_model.pkl'


def main():

    df = pd.read_csv(DATA_FILE)

    print("Cleaning Dataset.")
    data = clean_data(df)

    print("Applying Feature Engineering.")
    data = add_features(data)

    print("Training the models.")
    train_model(data, save_path=DEST_MODEL_PATH)

if __name__ == "__main__":
    main()
