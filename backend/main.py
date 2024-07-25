from flask import Flask, jsonify, request
import os
import glob
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'data'))

from AllergyParser import AllergyParser
from EncounterParser import EncounterParser
from ExcelExporter import ExcelExporter
from FHIRParser import FHIRParser
from ObservationParser import ObservationParser
from PatientParser import PatientParser
from ProcedureParser import ProcedureParser

app = Flask(__name__)

# Path to the folder containing FHIR JSON files
FOLDER_PATH = './data/fhir'

def find_file_by_uid(uid):
    search_pattern = os.path.join(FOLDER_PATH, f"*_{uid}*.json")
    files = glob.glob(search_pattern)
    return files[0] if files else None

@app.route('/', methods=['GET'])
def hello():
    def validate_filename(fname):
        return fname.endswith(".json") and "practitionerinformation" not in fname.lower() \
                and "hospitalinformation" not in fname.lower()


    data_dir = os.path.join(os.path.dirname(__file__), 'data', 'fhir')
    patient_files = [f for f in os.listdir(data_dir) if validate_filename(f)]
    
    patients = []
    for file_name in patient_files:
        params = file_name.split("_")
        name = " ".join(params[0:2])
        uid = params[2].removesuffix('.json')
        patients.append({"name": name, "uid": uid})
    
    return jsonify(patients)

@app.route('/patient_info/<uid>', methods=['GET'])
def get_patient_info(uid):
    parser = FHIRParser(FOLDER_PATH)
    file_path = find_file_by_uid(uid)
    
    if not file_path:
        return jsonify({"error": "File not found"}), 404

    resources = parser.parse_json_files(file_path)
    patient_info = parser.parse_resources(resources)
    
    return jsonify(patient_info)

@app.route('/patient_allergies/<uid>', methods=['GET'])
def get_patient_allergies(uid):
    parser = FHIRParser(FOLDER_PATH)
    file_path = find_file_by_uid(uid)
    
    if not file_path:
        return jsonify({"error": "File not found"}), 404

    resources = parser.parse_json_files(file_path)
    allergies = AllergyParser.parse(resources.get("AllergyIntolerance", []))
    allergies_info = AllergyParser.extract_allergies_info(allergies)
    
    return jsonify(allergies_info)

@app.route('/patient_encounters/<uid>', methods=['GET'])
def get_patient_encounters(uid):
    parser = FHIRParser(FOLDER_PATH)
    file_path = find_file_by_uid(uid)
    
    if not file_path:
        return jsonify({"error": "File not found"}), 404

    resources = parser.parse_json_files(file_path)
    encounters = EncounterParser.parse(resources.get("Encounter", []))
    encounters_info = EncounterParser.extract_encounters_info(encounters)
    
    return jsonify(encounters_info)

@app.route('/patient_observations/<uid>', methods=['GET'])
def get_patient_observations(uid):
    parser = FHIRParser(FOLDER_PATH)
    file_path = find_file_by_uid(uid)
    
    if not file_path:
        return jsonify({"error": "File not found"}), 404

    resources = parser.parse_json_files(file_path)
    observations = ObservationParser.parse(resources.get("Observation", []))
    observations_info = ObservationParser.extract_observations_info(observations)
    
    return jsonify(observations_info)

@app.route('/patient_procedures/<uid>', methods=['GET'])
def get_patient_procedures(uid):
    parser = FHIRParser(FOLDER_PATH)
    file_path = find_file_by_uid(uid)
    
    if not file_path:
        return jsonify({"error": "File not found"}), 404

    resources = parser.parse_json_files(file_path)
    procedures = ProcedureParser.parse(resources.get("Procedure", []))
    procedures_info = ProcedureParser.extract_procedures_info(procedures)
    
    return jsonify(procedures_info)

if __name__ == '__main__':
    app.run(debug=True)

