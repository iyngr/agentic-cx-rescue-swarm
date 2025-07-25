"""
Shared policy and solution tools for all agents
"""
from google.adk.tools import FunctionTool

def policy_lookup_tool(query: str) -> str:
    """
    Queries the company policy knowledge base.

    Args:
        query: The query to search for in the knowledge base.

    Returns:
        The text content of the most relevant policy chunks.
    """
    if "lost package" in query and "gold tier" in query:
        return "Policy Snippet 1: For Gold Tier customers with lost packages, a full refund or a free replacement with express shipping is offered."
    else:
        return "Policy Snippet 1: Standard policy for lost packages is to offer a replacement."

def order_status_tool(order_id: str) -> dict:
    """
    Queries the logistics system for the status of an order.

    Args:
        order_id: The ID of the order to look up.

    Returns:
        A dictionary with the order status.
    """
    if order_id == "O-9987":
        return {"status": "delivered", "delivery_date": "2023-10-26"}
    else:
        return {"status": "in_transit"}

# Export as ADK FunctionTool instances
POLICY_LOOKUP_TOOL = FunctionTool(policy_lookup_tool)
ORDER_STATUS_TOOL = FunctionTool(order_status_tool)
