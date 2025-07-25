"""
Clean Solution Agent using shared tools - demonstrates best practices
"""
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
import json

# Import shared tools (no duplication!)
from shared_tools import POLICY_LOOKUP_TOOL, ORDER_STATUS_TOOL

def rank_solutions(customer_status: str, issue_type: str, policy_text: str, order_value: float = 100.0) -> str:
    """
    Rank solution options based on customer status, issue type, and company policies.
    
    This function contains the business logic specific to solution ranking.
    It expects the agent to have already called the policy lookup tools.

    Args:
        customer_status: The customer's tier status (e.g., "Gold Tier", "Silver Tier").
        issue_type: Type of issue (e.g., "damaged", "wrong_item", "late_delivery").
        policy_text: The relevant policy information from policy lookup.
        order_value: The value of the order in question.

    Returns:
        A JSON object containing ranked solution options.
    """
    ranked_solutions = []
    
    # Solution ranking based on customer tier and policies
    if "gold tier" in customer_status.lower() or "vip" in customer_status.lower():
        # Premium solutions for high-value customers
        if "full refund" in policy_text.lower():
            ranked_solutions.append({
                "solution_id": 1,
                "action": "full_refund",
                "params": {"order_id": "O-9987", "amount": order_value},
                "explanation": f"Customer is {customer_status} - immediate full refund is appropriate",
                "priority": "HIGH"
            })
        
        if "replacement" in policy_text.lower() or "reship" in policy_text.lower():
            ranked_solutions.append({
                "solution_id": 2,
                "action": "reship_express",
                "params": {"order_id": "O-9987"},
                "explanation": "Premium customer gets expedited replacement",
                "priority": "HIGH"
            })
        
    else:
        # Standard solutions for regular customers
        if "replacement" in policy_text.lower():
            ranked_solutions.append({
                "solution_id": 1,
                "action": "reship_standard",
                "params": {"order_id": "O-9987"},
                "explanation": "Standard replacement with regular shipping",
                "priority": "MEDIUM"
            })
    
    # Universal options
    ranked_solutions.append({
        "solution_id": len(ranked_solutions) + 1,
        "action": "generate_coupon",
        "params": {"value": 25 if "gold" in customer_status.lower() else 15, "unit": "percent"},
        "explanation": f"Goodwill gesture appropriate for {customer_status} customer",
        "priority": "LOW"
    })
    
    return json.dumps({
        "ranked_solutions": ranked_solutions,
        "recommended_solution": ranked_solutions[0] if ranked_solutions else None
    }, indent=2)

# Create the solution agent using shared tools + agent-specific logic
root_agent = Agent(
    name="solution_agent",
    model="gemini-2.0-flash",
    description="Specialized agent for finding optimal solutions using shared policy tools.",
    instruction="""You are a Solution Agent for customer issue resolution.

Your job is to:
1. Use POLICY_LOOKUP_TOOL to get relevant company policies for the issue
2. Use ORDER_STATUS_TOOL if order information is needed
3. Use rank_solutions to generate ranked solution options based on the policy data

IMPORTANT: Always call the policy lookup tools FIRST to gather policy information, then use rank_solutions to analyze that data.

Example workflow:
1. Call POLICY_LOOKUP_TOOL with relevant query 
2. Call ORDER_STATUS_TOOL if order details needed
3. Call rank_solutions with the gathered policy information""",
    tools=[
        POLICY_LOOKUP_TOOL,       # Shared tool - call this first
        ORDER_STATUS_TOOL,        # Shared tool - call if needed
        FunctionTool(rank_solutions) # Agent-specific logic - call this last
    ]
)
