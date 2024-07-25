from fhir.resources.R4B.observation import Observation

class ObservationParser:
    @staticmethod
    def parse(observations_data):
        if observations_data:
            return [Observation.parse_obj(observation) for observation in observations_data]
        return []

    @staticmethod
    def convert_to_tz_naive(dt):
        return dt.replace(tzinfo=None) if dt else "Unknown"

    # expects: list<fhir.resources.r4b.observation>
    @staticmethod
    def extract_observations_info(observations):
        observations_summary = []
        for observation in observations:
            observation_info = {
                "Id": observation.id,
                "Status": observation.status,
                "Category": [category.coding[0].display for category in observation.category] if observation.category else ["Unknown"],
                "Code": observation.code.coding[0].display if observation.code else "Unknown",
                "Subject Reference": observation.subject.reference if observation.subject else "Unknown",
                "Effective DateTime": ObservationParser.convert_to_tz_naive(observation.effectiveDateTime) if observation.effectiveDateTime else "Unknown",
                "Issued": ObservationParser.convert_to_tz_naive(observation.issued) if observation.issued else "Unknown",
                "Value": observation.valueQuantity.value if observation.valueQuantity else "Unknown",
                "Unit": observation.valueQuantity.unit if observation.valueQuantity else "Unknown",
                "Interpretation": [interpretation.coding[0].display for interpretation in observation.interpretation] if observation.interpretation else ["Unknown"],
                "Note": [note.text for note in observation.note] if observation.note else ["None"]
            }
            observations_summary.append(observation_info)

        return {
            "Observations Summary": observations_summary
        }

