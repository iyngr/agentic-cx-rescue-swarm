"""
Shared CRM tools for all agents
"""
from google.adk.tools import FunctionTool

def crm_lookup_tool(customer_id: str) -> dict:
    """
    Fetches customer data from the CRM.

    Args:
        customer_id: The ID of the customer to look up.

    Returns:
        A dictionary containing the customer's LTV, status, and recent order count.
    """
    if customer_id == "C67890":
        return {"ltv": 1500, "status": "Gold Tier", "recent_order_count": 12}
    else:
        return {"ltv": 100, "status": "Silver Tier", "recent_order_count": 1}

def transcript_retrieval_tool(transcript_id: str) -> str:
    """
    Fetches the full call transcript.

    Args:
        transcript_id: The ID of the transcript to retrieve.

    Returns:
        The full text of the conversation.
    """
    if transcript_id == "T12345":
        return "Customer: I am very unhappy with my recent purchase. The item arrived damaged. I will never buy from you again. This is the worst experience I have ever had."
    else:
        return "Customer: I am happy with my purchase."

# Export as ADK FunctionTool instances
CRM_LOOKUP_TOOL = FunctionTool(crm_lookup_tool)
TRANSCRIPT_RETRIEVAL_TOOL = FunctionTool(transcript_retrieval_tool)
