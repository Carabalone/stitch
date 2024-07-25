import pandas as pd

class ExcelExporter:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def export(self, patient_info):
        # Convert extracted information to DataFrames
        patient_df = pd.DataFrame([{
            "Name": patient_info["Name"],
            "Gender": patient_info["Gender"],
            "Birth Date": patient_info["Birth Date"],
            "Age": patient_info["Age"],
            "Has Allergy": patient_info["Has Allergy"],
            "Active Allergies": patient_info["Active Allergies"],
            "Inactive Allergies": patient_info["Inactive Allergies"]
        }])

        allergies_df = pd.DataFrame(patient_info["Allergies Summary"])
        encounters_df = pd.DataFrame(patient_info["Encounters Summary"])
        observations_df = pd.DataFrame(patient_info["Observations Summary"])
        procedures_df = pd.DataFrame(patient_info["Procedures Summary"])

        # Create a Pandas Excel writer using openpyxl as the engine
        with pd.ExcelWriter(self.file_name, engine='openpyxl') as writer:
            patient_df.to_excel(writer, sheet_name='Patient Info', index=False)
            allergies_df.to_excel(writer, sheet_name='Allergies', index=False)
            encounters_df.to_excel(writer, sheet_name='Encounters', index=False)
            observations_df.to_excel(writer, sheet_name='Observations', index=False)
            procedures_df.to_excel(writer, sheet_name='Procedures', index=False)

        print("Excel file created successfully.")

