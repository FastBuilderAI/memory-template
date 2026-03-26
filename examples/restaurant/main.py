import os
import json

# --- Configuration ---
# KDS (Kitchen Display System)
KDS_IP_ADDRESS = os.getenv("KDS_IP_ADDRESS", "192.168.1.50")
RECIPE_DB_PATH = os.getenv("RECIPE_DB_PATH", "./data/recipes.json")

def build_restaurant_graph():
    """
    Builds FastMemory graph for Restaurant Kitchen and Table Service.
    """
    print("Building Restaurant FastMemory Graph...")
    atfs = [
        {"id": "C_Table_Service", "type": "Component"},
        {"id": "B_KDS_Display", "type": "Block", "links": ["C_Table_Service"]},
        {"id": "F_Course_Timing", "type": "Function", "links": ["B_KDS_Display"]},
        {"id": "D_Recipe_Scale", "type": "Data", "links": ["F_Course_Timing"]},
        {"id": "A_Role_Sous_Chef", "type": "Access", "links": ["F_Course_Timing"]},
        {"id": "E_Ticket_Cleared", "type": "Event", "links": ["F_Course_Timing"]}
    ]
    return atfs

def calculate_table_context(table_number):
    """
    Retrieves recipe and wastage context for a specific table.
    """
    print(f"Calculating context for Table: {table_number}")
    return {
        "table": table_number,
        "active_order": "ORD-553",
        "waste_tracking": "F_Waste_Tracker",
        "payment_logic": "F_Split_Check"
    }

if __name__ == "__main__":
    rest_graph = build_restaurant_graph()
    print(f"Restaurant Graph: {len(rest_graph)} nodes.")
    
    context = calculate_table_context(12)
    print(f"Table Context: {json.dumps(context, indent=2)}")
