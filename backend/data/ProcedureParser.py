from fhir.resources.R4B.procedure import Procedure

class ProcedureParser:
    @staticmethod
    def parse(procedures_data):
        if procedures_data:
            return [Procedure.parse_obj(procedure) for procedure in procedures_data]
        return []

    @staticmethod
    def convert_to_tz_naive(dt):
        return dt.replace(tzinfo=None) if dt else "Unknown"

    # expects: list<fhir.resources.r4b.procedure>
    @staticmethod
    def extract_procedures_info(procedures):
        procedures_summary = []
        for procedure in procedures:
            procedure_info = {
                "Id": procedure.id,
                "Status": procedure.status,
                "Code": procedure.code.coding[0].display if procedure.code else "Unknown",
                "Patient Reference": procedure.subject.reference if procedure.subject else "Unknown",
                "Performed DateTime": ProcedureParser.convert_to_tz_naive(procedure.performedDateTime) if procedure.performedDateTime else "Unknown",
                "Reason Code": [reason.coding[0].display for reason in procedure.reasonCode] if procedure.reasonCode else ["Unknown"],
                "Outcome": procedure.outcome.text if procedure.outcome else "Unknown",
                "Note": [note.text for note in procedure.note] if procedure.note else ["None"]
            }
            procedures_summary.append(procedure_info)

        return {
            "Procedures Summary": procedures_summary
        }

