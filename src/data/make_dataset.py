import pandas as pd
from sklearn.model_selection import train_test_split
from src.config.config import PROJECT_DIR
class Dataset:
    
    def load_data(self, csv_file: str):
        # Load the dataset from CSV file
        data = pd.read_csv(csv_file)
        
        # Split the data into training and test sets
        train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
        
        return train_data, test_data

    def save_data(self, train_data, test_data, train_file= PROJECT_DIR + '/data/processed/train.csv', test_file=PROJECT_DIR + '/data/processed/test.csv'):
        # Save the split datasets
        train_data.to_csv(train_file, index=False)
        test_data.to_csv(test_file, index=False)
        
        print(f"Training data saved to {train_file}")
        print(f"Test data saved to {test_file}")


