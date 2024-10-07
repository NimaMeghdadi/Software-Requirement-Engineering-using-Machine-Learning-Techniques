from transformers import BertTokenizer

class DataLoader:
    def __init__(self, model_name='bert-base-uncased'):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)

    def tokenize(self, texts, max_length=128):
        # Tokenize the texts using the BERT tokenizer
        return self.tokenizer(
            texts.tolist(), 
            padding='max_length', 
            truncation=True, 
            max_length=max_length, 
            return_tensors='pt'
        )

    def encode_labels(self, labels, label_map):
        # Map labels to integers
        return [label_map[label] for label in labels]

