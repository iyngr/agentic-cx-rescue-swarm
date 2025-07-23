from src.tools.action_tools import (
    refund_tool,
    reship_order_tool,
    generate_coupon_tool,
    send_communication_tool,
    log_to_crm_tool,
)
import json

def action_agent(case_file_json: str, ranked_solutions_json: str):
    """
    This agent executes the plan and closes the loop.

    Args:
        case_file_json: A JSON string containing the case file.
        ranked_solutions_json: A JSON string containing the ranked solutions.
    """
    case_file = json.loads(case_file_json)
    ranked_solutions = json.loads(ranked_solutions_json)

    # Select the top-ranked solution
    top_solution = ranked_solutions["ranked_solutions"][0]
    action = top_solution["action"]
    params = top_solution["params"]

    # Call the correct execution tool
    if action == "full_refund":
        refund_tool(**params)
    elif action == "reship_express":
        reship_order_tool(**params)
    elif action == "generate_coupon":
        generate_coupon_tool(**params)

    # Draft a personalized, empathetic email to the customer
    customer_name = "Valued Customer" # In a real implementation, this would be fetched from the CRM
    email_body = f"""
Dear {customer_name},

I am so sorry to hear about the issue with your recent order. I understand how frustrating it must be to receive a damaged item, and I sincerely apologize for the inconvenience this has caused.

To make things right, I have processed a {top_solution['explanation'].lower()}.

We value your business and hope to provide you with a much better experience in the future.

Sincerely,
The Customer Experience Team
"""

    # Call the send_communication_tool to send the email
    send_communication_tool(recipient=case_file["customer_details"]["email"], channel="email", body=email_body)

    # Finally, create a concise summary of the incident and resolution.
    log_entry = f"Incident: {case_file['issue_summary']}. Resolution: {top_solution['explanation']}."

    # Call the log_to_crm_tool to record this summary on the customer's record.
    log_to_crm_tool(customer_id=case_file["customer_details"]["customer_id"], log_entry=log_entry)
