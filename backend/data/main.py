import os
from FHIRParser import FHIRParser 
from ExcelExporter import ExcelExporter

folder_path = './fhir'
patients_data = []

parser = FHIRParser(folder_path)
total = len(os.listdir(folder_path))

for index, filename in enumerate(os.listdir(folder_path)[:18]):
    if filename.endswith('.json'):
        print(f"{index + 1} / {total}")
        file_path = os.path.join(folder_path, filename)
        resources = parser.parse_json_files(file_path)

        patient_info = parser.parse_resources(resources)
        if patient_info:
            patients_data.append(patient_info)

exporter = ExcelExporter("patient_info.xlsx")
for patient_info in patients_data:
    exporter.export(patient_info)

