from extract import extract_data
from transform import transform_data
from load import load_data

if __name__ == "__main__":
    file_path = "../data/raw/application_train.csv"

    df = extract_data(file_path)
    df = transform_data(df)
    load_data(df)
