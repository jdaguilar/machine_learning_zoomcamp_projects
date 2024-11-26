import pickle


def load_model(model_path="models/trained_model.pkl"):
    """Load the trained model."""
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model
