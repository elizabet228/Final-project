import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Konwerter formatów plików .xml, .json, .yml")
    parser.add_argument('input_file', type=str, help='Ścieżka do pliku wejściowego')
    parser.add_argument('output_file', type=str, help='Ścieżka do pliku wyjściowego')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    print(f"Input file: {args.input_file}")
    print(f"Output file: {args.output_file}")

import json

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        print(f"Błąd dekodowania JSON: {e}")
        return None
    except FileNotFoundError:
        print(f"Plik {file_path} nie został znaleziony.")
        return None

def save_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Błąd zapisu JSON: {e}")

import yaml

def load_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except yaml.YAMLError as e:
        print(f"Błąd dekodowania YAML: {e}")
        return None
    except FileNotFoundError:
        print(f"Plik {file_path} nie został znaleziony.")
        return None

def save_yaml(data, file_path):
    try:
        with open(file_path, 'w') as file:
            yaml.safe_dump(data, file)
    except Exception as e:
        print(f"Błąd zapisu YAML: {e}")

import xml.etree.ElementTree as ET

def load_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f"Błąd parsowania XML: {e}")
        return None
    except FileNotFoundError:
        print(f"Plik {file_path} nie został znaleziony.")
        return None
