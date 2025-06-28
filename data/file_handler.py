import json
import os
from pathlib import Path

STORAGE_DIR = Path(__file__).parent / "storage"

# Reads a JSON file and returns the data

def read_json(filename):
    filepath = STORAGE_DIR / filename
    if not filepath.exists():
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

# Writes a python object

def write_json(filename, data):
    filepath = STORAGE_DIR / filename
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

# Appends a new record to a list stored in a JSON file

def append_json(filename, record):
    data = read_json(filename)
    data.append(record)
    write_json(filename, data)

# Updates a record in a list of dicts

def update_json(filename, key, value, update_data):
    data = read_json(filename)
    updated = False
    for item in data:
        if item.get(key) == value:
            item.update(update_data)
            updated = True
    if updated:
        write_json(filename, data)
    return updated

# Deletes a record from a JSON file

def delete_json(filename, key, value):
    data = read_json(filename)
    new_data = [item for item in data if item.get(key) != value]
    if len(new_data) != len(data):
        write_json(filename, new_data)
        return True
    return False
