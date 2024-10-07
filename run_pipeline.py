from src import Dataset, DataLoader
from pathlib import Path
from src.config.config import DATA_PATH
import argparse
from src.features.build_features import DataLoader
from src.models.bert.train_model import train_model
from src.models.bert.predict_model import predict
from src.visualization.visualize import plot_confusion_matrix
from sklearn.metrics import accuracy_score

def run_pipeline():
    dataset = Dataset()
    # Step 1: Load the dataset
    # Usage example
    print("Loading dataset...")
    train_data, test_data = dataset.load_data(csv_file= DATA_PATH)
    dataset.save_data(train_data, test_data)
        
    # Preprocess the dataset (tokenization)
    print("Tokenizing and encoding dataset...")
    dataloader = DataLoader(model_name='bert-base-uncased')
    
    # Tokenize the training and test texts
    train_encodings = dataloader.tokenize(train_data['RequirementText'])
    test_encodings = dataloader.tokenize(test_data['RequirementText'])
    
    # Map labels to integers
    label_map = {label: idx for idx, label in enumerate(['F', 'A', 'FT', 'L', 'LF', 'MN', 'O', 'PE', 'PO', 'SC', 'SE', 'US'])}
    train_labels = dataloader.encode_labels(train_data['class'], label_map)
    test_labels = dataloader.encode_labels(test_data['class'], label_map)
    
    # Train the model
    # if args.train:
    print("Training model...")
    train_model(train_encodings, train_labels, test_encodings, test_labels, model_name='bert-base-uncased')
    print("Model training completed.")

    # Evaluate the model
    # if args.predict:
    print("Evaluating the model on test data...")
    y_true = test_labels
    y_pred = []

    for text in test_data['RequirementText']:
        predicted_class = predict(text, model_dir='./saved_model', model_name='bert-base-uncased')
        y_pred.append(label_map[predicted_class])

    # Calculate accuracy
    accuracy = accuracy_score(y_true, y_pred)
    print(f"Test Accuracy: {accuracy * 100:.2f}%")

    # Plot confusion matrix
    plot_confusion_matrix(y_true, y_pred, labels=list(label_map.keys()))


if __name__ == "__main__":
    # Argument parsing
    # parser = argparse.ArgumentParser(description="Run BERT model pipeline")
    # parser.add_argument('--csv_file', type=str, default='requirements.csv', help="Path to the dataset CSV file")
    # parser.add_argument('--model_name', type=str, default='bert-base-uncased', help="Pretrained BERT model to use")
    # parser.add_argument('--train', action='store_true', help="Train the model")
    # parser.add_argument('--predict', action='store_true', help="Run prediction and evaluation")
    
    # args = parser.parse_args()
    run_pipeline()