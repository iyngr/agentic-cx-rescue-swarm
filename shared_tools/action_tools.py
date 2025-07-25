"""
Shared communication tools for all agents
"""
from google.adk.tools import FunctionTool

def send_communication_tool(recipient: str, channel: str, body: str) -> dict:
    """
    Sends a communication to a customer.

    Args:
        recipient: The recipient of the communication.
        channel: The channel of the communication (e.g., "email", "sms").
        body: The body of the communication.

    Returns:
        A dictionary with the communication status.
    """
    print(f"Communication sent to {recipient} via {channel}: {body}")
    return {"status": "success"}

def refund_tool(order_id: str, amount: float) -> dict:
    """
    Issues a refund for a given order.

    Args:
        order_id: The ID of the order to refund.
        amount: The amount to refund.

    Returns:
        A dictionary with the refund status.
    """
    print(f"Refund of ${amount} for order {order_id} processed successfully.")
    return {"status": "success"}

# Export as ADK FunctionTool instances
SEND_COMMUNICATION_TOOL = FunctionTool(send_communication_tool)
REFUND_TOOL = FunctionTool(refund_tool)
