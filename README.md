# Stitch: Healthcare Data Centralization and Transfer App

## Overview

Stitch is a healthcare application designed to centralize and transfer data efficiently. It currently only parses FHIR (Fast Healthcare Interoperability Resources) data, processes it using a Python backend with Flask, and presents it through a React Native frontend. The app handles various FHIR resource types, including Patient, AllergyIntolerance, Encounter, Observation, and Procedure, ensuring comprehensive and accurate data management.

## Features

- **Data Parsing:** Efficiently parses FHIR JSON files, extracting and processing critical healthcare data.
- **Resource Handling:** Manages multiple FHIR resource types for a holistic view of patient information.
- **Python Backend:** Utilizes Flask for robust data processing and API handling.
- **React Native Frontend:** Delivers a seamless user experience with a responsive and intuitive interface.
- **Excel Export:** Allows exporting of processed data to Excel files, facilitating easy sharing and analysis.

## Data Requirements

To get started, download the required FHIR data from [Synthea's Oh Canada! Sample of Canadian FHIR Data](https://synthea.mitre.org/downloads) or use any other patient data in FHIR R4B format.
