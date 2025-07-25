"""
Clean Customer Experience Rescue Swarm using shared tools - demonstrates best practices
"""
from google.adk.agents import Agent
from google.adk.tools import FunctionTool

# Import shared tools (no more duplication!)
from shared_tools import (
    CRM_LOOKUP_TOOL,
    TRANSCRIPT_RETRIEVAL_TOOL, 
    POLICY_LOOKUP_TOOL,
    REFUND_TOOL,
    SEND_COMMUNICATION_TOOL
)

def process_customer_issue(customer_id: str, transcript_id: str, issue_description: str) -> str:
    """
    Complete workflow to process a customer issue from triage to resolution.
    Updated to use shared tools - demonstrates consolidated agent with clean architecture.

    Args:
        customer_id: The ID of the customer
        transcript_id: The ID of the transcript
        issue_description: Description of the customer issue

    Returns:
        A summary of actions taken
    """
    # Use shared tools instead of duplicated functions
    from shared_tools.crm_tools import crm_lookup_tool, transcript_retrieval_tool
    from shared_tools.policy_tools import policy_lookup_tool
    from shared_tools.action_tools import refund_tool, send_communication_tool
    
    # Step 1: Triage
    customer_details = crm_lookup_tool(customer_id)
    transcript_text = transcript_retrieval_tool(transcript_id)
    
    # Check for escalation criteria
    severe_dissatisfaction = any(phrase in transcript_text.lower() 
                               for phrase in ["never again", "worst experience", "damaged", "unhappy"])
    
    if (customer_details["ltv"] > 500 or customer_details["status"] in ["Gold Tier", "VIP"]) and severe_dissatisfaction:
        # Step 2: Find solution
        policy = policy_lookup_tool(f"policy for damaged item for {customer_details['status']} customer")
        
        # Step 3: Execute resolution
        if "full refund" in policy.lower():
            refund_tool("O-9987", 75.50)
            solution = "full refund processed"
        else:
            solution = "replacement offered"
        
        # Step 4: Communicate
        email_body = f"""Dear Valued Customer,

I sincerely apologize for the issue with your recent order. As a {customer_details['status']} customer, 
we want to make this right immediately.

I have processed a {solution} for you.

Best regards,
Customer Experience Team"""
        
        send_communication_tool("customer@example.com", "email", email_body)
        
        return f"Issue escalated and resolved: {solution}. Customer notified via email."
    else:
        return "Issue does not meet escalation criteria. Standard support process recommended."

# Define the main agent for ADK Web discovery
root_agent = Agent(
    name="customer_experience_rescue_swarm",
    model="gemini-2.0-flash",
    description="A swarm of agents that work together to resolve customer issues through triage, solution finding, and action execution.",
    instruction="""You are a Customer Experience Rescue Swarm. Your job is to:

1. Analyze customer complaints and issues
2. Determine if escalation is needed based on customer value and issue severity  
3. Find appropriate solutions using company policies
4. Execute resolutions (refunds, replacements, etc.)
5. Communicate empathetically with customers

Use the available tools to:
- Look up customer data (CRM)
- Retrieve call transcripts  
- Check company policies
- Process refunds
- Send communications
- Handle the complete customer issue workflow

When a user describes a customer issue, use the process_customer_issue function to handle it end-to-end.""",
    tools=[
        # Use shared tools (imported at top)
        CRM_LOOKUP_TOOL,
        TRANSCRIPT_RETRIEVAL_TOOL,
        POLICY_LOOKUP_TOOL,
        REFUND_TOOL,
        SEND_COMMUNICATION_TOOL,
        # Keep the consolidated workflow function
        FunctionTool(process_customer_issue)
    ]
)
