import pathlib
import json
from PatientParser import PatientParser
from AllergyParser import AllergyParser
from EncounterParser import EncounterParser
from ObservationParser import ObservationParser
from ProcedureParser import ProcedureParser

class FHIRParser:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def parse_json_files(self, filename):
        file = pathlib.Path(filename)
        resources = {"Patient": None, "AllergyIntolerance": [], "Encounter": [], "Observation": [], "Procedure": []}

        with open(file) as f:
            file_contents = json.load(f)
            for entry in file_contents.get("entry", []):
                resource_type = entry['resource']['resourceType']
                if resource_type == "Patient":
                    resources["Patient"] = entry['resource']
                elif resource_type == "AllergyIntolerance":
                    resources["AllergyIntolerance"].append(entry['resource'])
                elif resource_type == "Encounter":
                    resources["Encounter"].append(entry['resource'])
                elif resource_type == "Observation":
                    resources["Observation"].append(entry['resource'])
                elif resource_type == "Procedure":
                    resources["Procedure"].append(entry['resource'])

        return resources

    def parse_resources(self, resources):
        patient = PatientParser.parse(resources["Patient"]) if resources["Patient"] else None
        if (not patient):
            raise ValueError('Unable to parse patient')

        allergies = AllergyParser.parse(resources["AllergyIntolerance"])
        encounters = EncounterParser.parse(resources["Encounter"])
        observations = ObservationParser.parse(resources["Observation"])
        procedures = ProcedureParser.parse(resources["Procedure"])

        patient_info = PatientParser.extract_patient_info(patient)
        allergies_info = AllergyParser.extract_allergies_info(allergies)
        encounters_info = EncounterParser.extract_encounters_info(encounters)
        observations_info = ObservationParser.extract_observations_info(observations) if observations else {}
        procedures_info = ProcedureParser.extract_procedures_info(procedures) if procedures else {}

        return {**patient_info, **allergies_info, **encounters_info, **observations_info, **procedures_info}

