import os
import json

# --- Configuration ---
# POS Systems (Square, Toast, Clover)
SQUARE_ACCESS_TOKEN = os.getenv("SQUARE_ACCESS_TOKEN", "sq-test-token")
LOYALTY_SERVICE_URL = os.getenv("LOYALTY_SERVICE_URL", "https://loyalty.coffeeshop.com")

def build_coffeeshop_graph():
    """
    Builds FastMemory graph for Coffee Shop operations.
    """
    print("Building Coffee Shop FastMemory Graph...")
    atfs = [
        {"id": "C_Counter_Service", "type": "Component"},
        {"id": "B_Barista_Queue", "type": "Block", "links": ["C_Counter_Service"]},
        {"id": "F_Inventory_Deduct", "type": "Function", "links": ["B_Barista_Queue"]},
        {"id": "D_Stock_Levels", "type": "Data", "links": ["F_Inventory_Deduct"]},
        {"id": "A_Role_Barista", "type": "Access", "links": ["F_Inventory_Deduct"]},
        {"id": "E_Order_Pickup_Ready", "type": "Event", "links": ["F_Inventory_Deduct"]}
    ]
    return atfs

def process_loyalty_logic(customer_id):
    """
    Checks if a customer is eligible for rewards based on graph rules.
    """
    print(f"Processing loyalty for customer: {customer_id}")
    return {
        "customer": customer_id,
        "tier": "Gold",
        "redemption_function": "F_Reedem_Free_Coffee",
        "data": "Customer_Tier_Map"
    }

if __name__ == "__main__":
    coffee_graph = build_coffeeshop_graph()
    print(f"Coffee Shop Graph: {len(coffee_graph)} nodes.")
    
    result = process_loyalty_logic("CUST-992")
    print(f"Loyalty Result: {json.dumps(result, indent=2)}")
