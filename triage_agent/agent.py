"""
Clean Triage Agent using shared tools - demonstrates best practices
"""
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
import json

# Import shared tools (no duplication!)
from shared_tools import CRM_LOOKUP_TOOL, TRANSCRIPT_RETRIEVAL_TOOL

def make_triage_decision(customer_ltv: float, customer_status: str, transcript_sentiment: str) -> str:
    """
    Make a triage decision based on customer data and transcript analysis.
    
    This function contains the business logic specific to triage decisions.
    It expects the agent to have already called the CRM and transcript tools.

    Args:
        customer_ltv: The customer's lifetime value.
        customer_status: The customer's tier status (e.g., "Gold Tier", "Silver Tier").
        transcript_sentiment: Analysis of the transcript sentiment.

    Returns:
        A JSON string with the triage decision and reasoning.
    """
    # Triage-specific business logic
    severe_dissatisfaction = any(phrase in transcript_sentiment.lower() 
                               for phrase in ["never again", "worst experience", "damaged", "unhappy", "furious", "angry"])
    
    high_value_customer = customer_ltv > 500 or customer_status in ["Gold Tier", "VIP", "Platinum"]
    
    # Triage decision logic (specific to this agent)
    if high_value_customer and severe_dissatisfaction:
        decision = {
            "escalate": True,
            "priority": "HIGH",
            "reason": f"High-value {customer_status} customer with severe dissatisfaction detected",
            "recommended_actions": ["immediate_response", "manager_review", "retention_measures"]
        }
    elif high_value_customer:
        decision = {
            "escalate": True,
            "priority": "MEDIUM", 
            "reason": f"High-value {customer_status} customer requires attention",
            "recommended_actions": ["priority_handling", "personalized_response"]
        }
    elif severe_dissatisfaction:
        decision = {
            "escalate": True,
            "priority": "MEDIUM",
            "reason": "Severe customer dissatisfaction detected",
            "recommended_actions": ["empathetic_response", "solution_focused"]
        }
    else:
        decision = {
            "escalate": False,
            "priority": "LOW",
            "reason": "Standard issue, can be handled through normal channels",
            "recommended_actions": ["standard_support_process"]
        }
    
    return json.dumps(decision, indent=2)

# Create the triage agent using shared tools + agent-specific logic
root_agent = Agent(
    name="triage_agent",
    model="gemini-2.0-flash",
    description="Specialized agent for triaging customer complaints using shared CRM tools.",
    instruction="""You are a Triage Agent for customer complaints. 

Your job is to:
1. Use CRM_LOOKUP_TOOL to get customer information (LTV, status, order history)
2. Use TRANSCRIPT_RETRIEVAL_TOOL to analyze call transcripts for sentiment
3. Use make_triage_decision to determine escalation based on customer value and severity

IMPORTANT: Always call the CRM and transcript tools FIRST to gather data, then use make_triage_decision to analyze that data.

Example workflow:
1. Call CRM_LOOKUP_TOOL with customer_id
2. Call TRANSCRIPT_RETRIEVAL_TOOL with transcript_id  
3. Call make_triage_decision with the gathered data""",
    tools=[
        CRM_LOOKUP_TOOL,          # Shared tool - call this first
        TRANSCRIPT_RETRIEVAL_TOOL, # Shared tool - call this second
        FunctionTool(make_triage_decision) # Agent-specific logic - call this last
    ]
)
