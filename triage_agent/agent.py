"""
Clean Triage Agent using shared tools - demonstrates best practices
"""
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
import json

# Import shared tools (no duplication!)
from shared_tools import CRM_LOOKUP_TOOL, TRANSCRIPT_RETRIEVAL_TOOL

def triage_logic(customer_id: str, transcript_id: str) -> str:
    """
    Agent-specific triage logic (not shared).
    
    This function contains the business logic specific to triage decisions.
    It uses shared tools but implements triage-specific decision making.

    Args:
        customer_id: The ID of the customer.
        transcript_id: The ID of the transcript.

    Returns:
        A JSON string with the agent's triage decision.
    """
    # Use shared tools (imported, not duplicated)
    from shared_tools.crm_tools import crm_lookup_tool
    from shared_tools.crm_tools import transcript_retrieval_tool
    
    customer_details = crm_lookup_tool(customer_id)
    transcript_text = transcript_retrieval_tool(transcript_id)

    # Triage-specific business logic
    severe_dissatisfaction = any(phrase in transcript_text.lower() 
                               for phrase in ["never again", "worst experience", "damaged", "unhappy"])
    
    # Triage decision logic (specific to this agent)
    if (customer_details["ltv"] > 500 or customer_details["status"] in ["Gold Tier", "VIP"]) and severe_dissatisfaction:
        case_file = {
            "customer_details": customer_details,
            "transcript_text": transcript_text,
            "issue_summary": "Customer is a high-value client and is extremely dissatisfied with a recent purchase that arrived damaged."
        }
        return json.dumps({"escalate": True, "case_file": case_file})
    else:
        return json.dumps({"escalate": False})

# Create the triage agent using shared tools + agent-specific logic
root_agent = Agent(
    name="triage_agent",
    model="gemini-2.0-flash",
    description="Specialized agent for triaging customer complaints using shared CRM tools.",
    instruction="""You are a Triage Agent for customer complaints. 

Your job is to:
1. Look up customer information using CRM tools
2. Retrieve and analyze call transcripts  
3. Decide whether issues need escalation based on customer value and severity

Use the shared tools to gather data, then apply triage-specific logic to make escalation decisions.""",
    tools=[
        CRM_LOOKUP_TOOL,          # Shared tool
        TRANSCRIPT_RETRIEVAL_TOOL, # Shared tool  
        FunctionTool(triage_logic) # Agent-specific logic
    ]
)
