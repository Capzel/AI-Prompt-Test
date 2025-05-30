import pickle

def serialize_to_file(obj, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(obj, file)

def deserialize_from_file(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)