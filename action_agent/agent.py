"""
Clean Action Agent using shared tools - demonstrates best practices
"""
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
import json

# Import shared tools (no duplication!)
from shared_tools import REFUND_TOOL, SEND_COMMUNICATION_TOOL

def coordinate_action_execution(action_type: str, order_id: str, amount: float = 0.0, customer_email: str = "customer@example.com") -> str:
    """
    Coordinate the execution of a specific action based on the action type.
    
    This function contains the business logic specific to action execution coordination.
    It expects the agent to have already called the appropriate action tools.

    Args:
        action_type: The type of action to coordinate (e.g., "full_refund", "reship_express").
        order_id: The order ID for the action.
        amount: The amount for refunds (if applicable).
        customer_email: The customer's email address for communication.

    Returns:
        A summary of the action coordination and next steps.
    """
    execution_summary = []
    recommended_communication = ""
    
    # Coordinate based on action type
    if action_type == "full_refund":
        execution_summary.append(f"🔄 COORDINATING: Full refund of ${amount} for order {order_id}")
        execution_summary.append("📋 STEPS: Process refund → Send confirmation → Update customer record")
        recommended_communication = f"""Dear Valued Customer,

We have processed a full refund of ${amount} for your order {order_id}. The refund will appear in your account within 3-5 business days.

We sincerely apologize for the inconvenience and appreciate your understanding.

Best regards,
Customer Experience Team"""
        
    elif action_type == "reship_express":
        execution_summary.append(f"🔄 COORDINATING: Express re-shipment for order {order_id}")
        execution_summary.append("📋 STEPS: Prepare replacement → Expedited shipping → Tracking notification")
        recommended_communication = f"""Dear Valued Customer,

We are expediting a replacement for your order {order_id}. You will receive tracking information within the next hour.

Expected delivery: 1-2 business days.

Best regards,
Customer Experience Team"""
        
    elif action_type == "generate_coupon":
        execution_summary.append(f"🔄 COORDINATING: Generating goodwill coupon for customer")
        execution_summary.append("📋 STEPS: Create coupon code → Set expiration → Send to customer")
        recommended_communication = f"""Dear Valued Customer,

As a gesture of goodwill, we're providing you with a special discount for your next purchase.

Thank you for your patience and continued loyalty.

Best regards,
Customer Experience Team"""
        
    else:
        execution_summary.append(f"🔄 COORDINATING: Standard follow-up for {action_type}")
        recommended_communication = "Standard follow-up communication recommended."
    
    execution_summary.append(f"📧 COMMUNICATION READY: Email drafted for {customer_email}")
    execution_summary.append("✅ COORDINATION COMPLETE: Ready for tool execution")
    
    return json.dumps({
        "coordination_summary": execution_summary,
        "recommended_communication": recommended_communication,
        "next_steps": ["Execute action tools", "Send customer communication", "Update records"]
    }, indent=2)

# Create the action agent using shared tools + agent-specific logic
root_agent = Agent(
    name="action_agent", 
    model="gemini-2.0-flash",
    description="Specialized agent for executing resolutions and communicating with customers using shared action tools.",
    instruction="""You are an Action Agent for customer issue resolution.

Your job is to:
1. Use REFUND_TOOL to process refunds when needed
2. Use SEND_COMMUNICATION_TOOL to notify customers of actions taken
3. Use coordinate_action_execution to plan and coordinate complex action sequences

IMPORTANT: Use the action tools FIRST to execute the specific actions, then use coordinate_action_execution to provide coordination and next steps.

Example workflow:
1. Call REFUND_TOOL if refund is needed
2. Call SEND_COMMUNICATION_TOOL to notify customer
3. Call coordinate_action_execution to summarize and plan follow-up""",
    tools=[
        REFUND_TOOL,                    # Shared tool - call when refund needed
        SEND_COMMUNICATION_TOOL,        # Shared tool - call to notify customer
        FunctionTool(coordinate_action_execution) # Agent-specific logic - call for coordination
    ]
)
