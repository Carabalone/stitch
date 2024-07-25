from fhir.resources.R4B.patient import Patient
from datetime import datetime

class PatientParser:
    @staticmethod
    def parse(patient_data):
        return Patient.parse_obj(patient_data) if patient_data else None
    
    @staticmethod
    def extract_full_name(human_name):
        full_name = []
        if human_name.prefix:
            full_name.extend(human_name.prefix)
        if human_name.given:
            full_name.extend(human_name.given)
        if human_name.family:
            full_name.append(human_name.family)
        if human_name.suffix:
            full_name.extend(human_name.suffix)
        return " ".join(full_name)
    
    @staticmethod
    def date_to_datetime(date):
        return datetime(
            year=date.year,
            month=date.month,
            day=date.day,
        )
    
    @staticmethod
    def calculate_age(birth_date):
        birth_date = PatientParser.date_to_datetime(birth_date)
        return (datetime.now() - birth_date).days // 365
    
    @staticmethod
    def extract_patient_info(patient):
        if patient:
            name = PatientParser.extract_full_name(patient.name[0]) if patient.name else "N/A"
            gender = patient.gender if patient.gender else "N/A"
            birth_date = patient.birthDate if patient.birthDate else "N/A"
            age = PatientParser.calculate_age(birth_date) if birth_date else "N/A"
            return {
                "Name": name,
                "Gender": gender,
                "Birth Date": birth_date,
                "Age": age
            }
        return {}

