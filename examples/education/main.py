import os
import sys
import json
from typing import List, Dict, Any

# Add parent directory to sys.path to import shared client
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.fastmemory_client import FastMemoryClient

class EducationApp:
    def __init__(self):
        self.client = FastMemoryClient("Education-LearnOps")
        
        # Education Specific Config
        self.lms_key = os.getenv("LMS_API_KEY", "canvas-lms-secret")
        self.course_db = os.getenv("COURSE_DB_URI", "postgresql://admin:pass@edu-db:5432/lms")

    def build_graph(self) -> List[Dict[str, Any]]:
        """
        Builds the Education graph using CBFDAE ontology.
        """
        self.client.logger.info("Defining Education Learning Ops nodes...")
        atfs = [
            {"id": "C_Learning_Ops", "type": "Component", "description": "Academic management and curriculum engine"},
            {"id": "B_Academic_Record", "type": "Block", "links": ["C_Learning_Ops"], "description": "Persistent record structure for student history"},
            {"id": "F_Course_Enrollment", "type": "Function", "links": ["B_Academic_Record"], "description": "Logic for course registration and capacity check"},
            {"id": "D_Student_Registrar", "type": "Data", "links": ["F_Course_Enrollment"], "description": "Unified registry of student enrollments"},
            {"id": "A_Role_Academic_Registrar", "type": "Access", "links": ["F_Course_Enrollment"], "description": "Administrative access for course management"},
            {"id": "E_Course_Capacity_Reached", "type": "Event", "links": ["F_Course_Enrollment"], "description": "Trigger when a course is full"}
        ]
        return atfs

    def query_academic_path(self, student_id: str):
        """
        Finds academic context and course eligibility for a student.
        """
        self.client.logger.info(f"Querying academic path for student: {student_id} via {self.course_db}")
        # In production, this would query Neo4j or the LMS
        return {
            "student_id": student_id,
            "eligible_courses": ["CS_101", "MATH_202"],
            "grading_logic": "F_GPA_Calculator",
            "next_event": "E_Submission_Logged"
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
        academic_ctx = self.query_academic_path("ST-2024-55")
        print(f"\n[ACADEMIC CONTEXT]: {json.dumps(academic_ctx, indent=2)}")
        
        self.client.logger.info("Education App execution completed.")

if __name__ == "__main__":
    app = EducationApp()
    try:
        app.run()
    finally:
        app.client.close()
