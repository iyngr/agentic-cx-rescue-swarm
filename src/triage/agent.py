from src.tools.triage_tools import crm_lookup_tool, transcript_retrieval_tool
import json

def triage_agent(customer_id: str, transcript_id: str) -> str:
    """
    This agent validates the alert and gathers initial context.

    Args:
        customer_id: The ID of the customer.
        transcript_id: The ID of the transcript.

    Returns:
        A JSON string with the agent's decision.
    """

    customer_details = crm_lookup_tool(customer_id)
    transcript_text = transcript_retrieval_tool(transcript_id)

    # Analyze the transcript for explicit phrases of severe dissatisfaction
    severe_dissatisfaction = False
    dissatisfaction_phrases = ["never again", "worst experience", "reporting you", "unhappy", "damaged"]
    for phrase in dissatisfaction_phrases:
        if phrase in transcript_text.lower():
            severe_dissatisfaction = True
            break

    # Make a decision
    if (customer_details["ltv"] > 500 or customer_details["status"] in ["Gold Tier", "VIP"]) and severe_dissatisfaction:
        case_file = {
            "customer_details": customer_details,
            "transcript_text": transcript_text,
            "issue_summary": "Customer is a high-value client and is extremely dissatisfied with a recent purchase that arrived damaged."
        }
        return json.dumps({"escalate": True, "case_file": case_file})
    else:
        return json.dumps({"escalate": False})
