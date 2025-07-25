"""
Clean Solution Agent using shared tools - demonstrates best practices
"""
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
import json

# Import shared tools (no duplication!)
from shared_tools import POLICY_LOOKUP_TOOL, ORDER_STATUS_TOOL

def get_solution(case_file_json: str) -> str:
    """
    Agent-specific solution finding logic.
    
    This function contains the business logic specific to finding solutions.
    It uses shared tools but implements solution-specific decision making.

    Args:
        case_file_json: A JSON string containing the case file.

    Returns:
        A JSON object containing a "ranked_solutions" list.
    """
    case_file = json.loads(case_file_json)

    # Use shared tools (imported, not duplicated)
    from shared_tools.policy_tools import policy_lookup_tool
    
    # Solution-specific business logic
    problem = case_file["issue_summary"]
    customer_status = case_file["customer_details"]["status"]

    # Use shared policy lookup tool
    policy = policy_lookup_tool(f"policy for {problem} for {customer_status} customer")

    # Solution-specific ranking logic
    ranked_solutions = []
    if "full refund" in policy.lower():
        ranked_solutions.append({
            "solution_id": 1, 
            "action": "full_refund", 
            "params": {"order_id": "O-9987", "amount": 75.50}, 
            "explanation": "Customer's item was damaged, and they are a top-tier client. A full refund is the best path."
        })
    if "reship" in policy.lower() or "replacement" in policy.lower():
        ranked_solutions.append({
            "solution_id": 2, 
            "action": "reship_express", 
            "params": {"order_id": "O-9987"}, 
            "explanation": "Re-ship the item with complimentary express shipping."
        })

    ranked_solutions.append({
        "solution_id": 3, 
        "action": "generate_coupon", 
        "params": {"value": 50, "unit": "percent"}, 
        "explanation": "Offer a 50% coupon for a future purchase."
    })

    return json.dumps({"ranked_solutions": ranked_solutions})

# Create the solution agent using shared tools + agent-specific logic
root_agent = Agent(
    name="solution_agent",
    model="gemini-2.0-flash",
    description="Specialized agent for finding optimal solutions using shared policy tools.",
    instruction="""You are a Solution Agent for customer issue resolution.

Your job is to:
1. Analyze case files from triage agents
2. Look up relevant company policies using shared tools
3. Generate ranked solution options based on customer value and policies

Use the shared tools to gather policy information, then apply solution-specific logic to rank options.""",
    tools=[
        POLICY_LOOKUP_TOOL,       # Shared tool
        ORDER_STATUS_TOOL,        # Shared tool
        FunctionTool(get_solution) # Agent-specific logic
    ]
)
