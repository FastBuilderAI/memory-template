import os
import sys
import json
from typing import List, Dict, Any

# Add parent directory to sys.path to import shared client
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.fastmemory_client import FastMemoryClient

class HealthcareApp:
    def __init__(self):
        self.client = FastMemoryClient("Healthcare-Clinical")
        
        # Healthcare Specific Config
        self.fhir_endpoint = os.getenv("HL7_FHIR_ENDPOINT", "https://healthcare.api.azure.com")
        self.vault_url = os.getenv("AZURE_VAULT_URL", "https://my-vault.vault.azure.net")

    def build_graph(self) -> List[Dict[str, Any]]:
        """
        Builds the Healthcare graph using CBFDAE ontology.
        """
        self.client.logger.info("Defining Healthcare Clinical nodes...")
        atfs = [
            {"id": "C_Patient_Portal", "type": "Component", "description": "Secure interface for patient interaction"},
            {"id": "B_Clinical_Workflow", "type": "Block", "links": ["C_Patient_Portal"], "description": "Structured path for clinical care and diagnostics"},
            {"id": "F_Appointment_Booking", "type": "Function", "links": ["B_Clinical_Workflow"], "description": "Logic for scheduling and resource allocation"},
            {"id": "D_Doctor_Calendar", "type": "Data", "links": ["F_Appointment_Booking"], "description": "Availability registry for healthcare providers"},
            {"id": "A_Role_PHI_Admin", "type": "Access", "links": ["F_Appointment_Booking"], "description": "Authorized access for PHI and administrative tasks"},
            {"id": "E_Patient_Notification", "type": "Event", "links": ["F_Appointment_Booking"], "description": "Trigger for secure patient alerts"}
        ]
        return atfs

    def retrieve_patient_context(self, patient_uuid: str):
        """
        Retrieves clinical context for a specific patient.
        """
        self.client.logger.info(f"Retrieving PHI context for patient: {patient_uuid} via {self.fhir_endpoint}")
        # In production, this would query Neo4j or the FHIR service securely
        return {
            "patient_uuid": patient_uuid,
            "access_level": "RESTRICTED",
            "phi_node": "D_Sensitive_Health_Data",
            "compliance": "HIPAA_Rule_V3",
            "last_visit_function": "F_Retrieve_Lab_Results"
        }

    def run(self):
        """
        Main execution flow.
        """
        self.client.health_check()
        
        # 1. Build and Deploy Graph
        graph = self.build_graph()
        self.client.deploy_graph(graph)
        
        # 2. Simulate Business Logic
        patient_ctx = self.retrieve_patient_context("PA-009-88-21")
        print(f"\n[PATIENT CONTEXT]: {json.dumps(patient_ctx, indent=2)}")
        
        self.client.logger.info("Healthcare App execution completed.")

if __name__ == "__main__":
    app = HealthcareApp()
    try:
        app.run()
    finally:
        app.client.close()
