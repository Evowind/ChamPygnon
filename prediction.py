import sys
import pickle

def predict(model_path, features):
    # Load the trained model
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)

    # Prepare the features for prediction
    redValue, blueValue, greenValue, shape, surface = features[:5]
    # Convert categorical features to one-hot encoded format
    shape_encoded = [1 if s == shape else 0 for s in ['Polypore', 'Convex', 'Bell', 'Depressed', 'CupFungi', 'CoralFungi', 'Conical', 'Flat', 'JellyFungi', 'Stinkhorns', 'Earthstars', 'Puffballs', 'Corticioid', 'Chanterelles', 'Funnel', 'Cylindrical', 'Knobbed', 'Shell', 'Truffles', 'Bolete', 'FalseMorels', 'ToothFungi', 'TrueMorels', 'Cauliflower']]
    surface_encoded = [1 if s == surface else 0 for s in ['Smooth', 'FlatScales', 'Fibrous', 'Patches', 'RaisedScales', 'Hairy', 'Powder', 'Silky', 'Velvety']]

    # Combine all features
    feature_values = [float(redValue), float(blueValue), float(greenValue)] + shape_encoded + surface_encoded

    # Make predictions
    predictions = model.predict([feature_values])

    return predictions[0]

if __name__ == "__main__":
    # Get the model path and features from command line arguments
    model_path = sys.argv[1]
    features = sys.argv[2:]

    # Perform prediction
    result = predict(model_path, features)

    # Print the result
    print(result)
