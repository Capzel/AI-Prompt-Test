Certainly! Below are two functions that use Python's `pickle` module to serialize and deserialize objects. This module is suitable for basic serialization tasks, but be cautious with untrusted data as it can execute arbitrary code during deserialization.

import pickle
import os

def save_object_to_file(obj, file_path):
    """
    Serializes an object and saves it to a file.
    
    :param obj: The object to serialize.
    :param file_path: The path to the file where the object will be saved.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'wb') as file:
        pickle.dump(obj, file, protocol=pickle.HIGHEST_PROTOCOL)

def load_object_from_file(file_path):
    """
    Loads and returns a serialized object from a file.
    
    :param file_path: The path to the file from which the object will be loaded.
    :return: The deserialized object.
    """
    with open(file_path, 'rb') as file:
        return pickle.load(file)

- **Do not load data from untrusted sources**: `pickle` can execute arbitrary code, making it a security risk if the source of the data is not trusted.
- **Use `pickle.HIGHEST_PROTOCOL`**: This ensures the most efficient and secure serialization protocol available.
- **Ensure file path security**: Validate and sanitize file paths to prevent directory traversal attacks.

For scenarios where security is a concern, consider using safer serialization formats like JSON (for simple data types) or third-party libraries like `jsonpickle` with appropriate security measures.