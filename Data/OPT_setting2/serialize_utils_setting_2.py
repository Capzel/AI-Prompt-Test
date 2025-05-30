import pickle

def serialize_object(obj, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(obj, file, protocol=pickle.HIGHEST_PROTOCOL)

def deserialize_object(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)