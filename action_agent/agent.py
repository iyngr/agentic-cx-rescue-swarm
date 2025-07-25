"""
Clean Action Agent using shared tools - demonstrates best practices
"""
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
import json

# Import shared tools (no duplication!)
from shared_tools import REFUND_TOOL, SEND_COMMUNICATION_TOOL

def execute_and_communicate(solution_json: str) -> str:
    """
    Agent-specific execution and communication logic.
    
    This function contains the business logic specific to executing actions.
    It uses shared tools but implements action-specific orchestration.

    Args:
        solution_json: A JSON string containing the solution to execute.

    Returns:
        A summary of the actions taken.
    """
    solution = json.loads(solution_json)
    
    # Use shared tools (imported, not duplicated)
    from shared_tools.action_tools import refund_tool, send_communication_tool
    
    # Action-specific execution logic
    action_type = solution.get("action")
    params = solution.get("params", {})
    explanation = solution.get("explanation", "")
    
    execution_log = []
    
    # Execute the specific action
    if action_type == "full_refund":
        refund_result = refund_tool(params["order_id"], params["amount"])
        if refund_result["status"] == "success":
            execution_log.append(f"✅ Refund processed: ${params['amount']} for order {params['order_id']}")
        else:
            execution_log.append(f"❌ Refund failed for order {params['order_id']}")
    
    elif action_type == "reship_express":
        execution_log.append(f"✅ Express re-shipment initiated for order {params['order_id']}")
    
    elif action_type == "generate_coupon":
        execution_log.append(f"✅ Generated {params['value']}{params['unit']} coupon")
    
    # Send customer communication
    email_body = f"""Dear Valued Customer,

Thank you for contacting us about your recent concern. We have taken the following action to resolve your issue:

{explanation}

We sincerely apologize for any inconvenience and appreciate your patience.

Best regards,
Customer Experience Team"""
    
    comm_result = send_communication_tool("customer@example.com", "email", email_body)
    if comm_result["status"] == "success":
        execution_log.append("✅ Customer notification sent via email")
    
    return "\n".join(execution_log)

# Create the action agent using shared tools + agent-specific logic
root_agent = Agent(
    name="action_agent", 
    model="gemini-2.0-flash",
    description="Specialized agent for executing resolutions and communicating with customers using shared action tools.",
    instruction="""You are an Action Agent for customer issue resolution.

Your job is to:
1. Execute specific resolution actions (refunds, re-shipments, coupons)
2. Send appropriate communications to customers
3. Provide execution summaries and status updates

Use the shared tools to perform actions and communications, then apply action-specific orchestration logic.""",
    tools=[
        REFUND_TOOL,                    # Shared tool
        SEND_COMMUNICATION_TOOL,        # Shared tool
        FunctionTool(execute_and_communicate) # Agent-specific logic
    ]
)
