from fhir.resources.R4B.encounter import Encounter

class EncounterParser:
    @staticmethod
    def parse(encounters_data):
        if encounters_data:
            return [Encounter.parse_obj(encounter) for encounter in encounters_data]
        return []

    @staticmethod
    def convert_to_tz_naive(dt):
        return dt.replace(tzinfo=None) if dt else "Unknown"

    # expects: list<fhir.resources.r4b.encounter>
    @staticmethod
    def extract_encounters_info(encounters): 
        encounter_summary = []
        for encounter in encounters:
            encounter_info = {
                "Id": encounter.id,
                "Status": encounter.status,
                "Class": encounter.class_fhir.display if encounter.class_fhir else "Unknown",
                "Type": [t.coding[0].display for t in encounter.type] if encounter.type else ["Unknown"],
                "Patient Reference": encounter.subject.reference,
                "Period Start": EncounterParser.convert_to_tz_naive(encounter.period.start) if encounter.period else "Unknown",
                "Period End": EncounterParser.convert_to_tz_naive(encounter.period.end) if encounter.period else "Unknown",
                "Participants": [p.individual.display for p in encounter.participant] if encounter.participant else [],
                "Reason": [r.coding[0].display for r in encounter.reasonCode] if encounter.reasonCode else ["Unknown"]
            }
            encounter_summary.append(encounter_info)

        return {
            "Encounters Summary": encounter_summary
        }

