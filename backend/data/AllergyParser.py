import re
from fhir.resources.R4B.allergyintolerance import AllergyIntolerance

class AllergyParser:
    @staticmethod
    def parse(allergies_data):
        if allergies_data:
            return [AllergyIntolerance.parse_obj(allergy) for allergy in allergies_data]
        return []

    @staticmethod
    def trim_allergy_substance(substance_str):
        patterns = [
            r"^Allergy to\s*",  # Matches "Allergy to " at the beginning
            r"^allergy to\s*",  # Matches "allergy to " at the beginning
            r"\s*allergy$",     # Matches " allergy" at the end
        ]
        for pattern in patterns:
            substance_str = re.sub(pattern, "", substance_str, flags=re.IGNORECASE)
        return substance_str.strip()

    @staticmethod
    def convert_to_tz_naive(dt):
        return dt.replace(tzinfo=None) if dt else "Unknown"

    def str_reactions(allergy):
        if (allergy.reaction and len(allergy.reaction) > 0):
            return ", ".join([reaction.manifestation[0].coding[0].display for reaction in allergy.reaction])
        return "None"

    # expects: list<fhir.resources.r4b.allergyintolerance>
    @staticmethod
    def extract_allergies_info(allergies):
        has_allergy = bool((len(allergies) > 0))
        active_allergies = sum(1 for allergy in allergies if allergy.clinicalStatus.coding[0].code == 'active')
        inactive_allergies = sum(1 for allergy in allergies if allergy.clinicalStatus.coding[0].code == 'inactive')

        allergies_summary = []
        for allergy in allergies:
            allergy_info = {
                "Substance": AllergyParser.trim_allergy_substance(allergy.code.coding[0].display),
                "Type": allergy.type if allergy.type else "Unknown",
                "Severity": allergy.criticality if allergy.criticality else "Unknown",
                "Status": allergy.clinicalStatus.coding[0].code,
                # "Onset": AllergyParser.convert_to_tz_naive(allergy.onsetDateTime) if allergy.onsetDateTime else "Unknown",
                "Reactions": AllergyParser.str_reactions(allergy)
            }
            allergies_summary.append(allergy_info)

        return {
            "Has Allergy": has_allergy,
            "Active Allergies": active_allergies,
            "Inactive Allergies": inactive_allergies,
            "Allergies Summary": allergies_summary
        }

