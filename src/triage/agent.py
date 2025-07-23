from google.adk.agents import Agent
import json

class TriageAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def crm_lookup_tool(self, customer_id: str) -> dict:
        """
        Fetches customer data from the CRM.

        Args:
            customer_id: The ID of the customer to look up.

        Returns:
            A dictionary containing the customer's LTV, status, and recent order count.
        """
        # In a real implementation, this would fetch data from a CRM API.
        # For this example, we'll use mock data.
        if customer_id == "C67890":
            return {"ltv": 1500, "status": "Gold Tier", "recent_order_count": 12}
        else:
            return {"ltv": 100, "status": "Silver Tier", "recent_order_count": 1}

    def transcript_retrieval_tool(self, transcript_id: str) -> str:
        """
        Fetches the full call transcript.

        Args:
            transcript_id: The ID of the transcript to retrieve.

        Returns:
            The full text of the conversation.
        """
        # In a real implementation, this would fetch the transcript from a database or storage.
        # For this example, we'll use mock data.
        if transcript_id == "T12345":
            return "Customer: I am very unhappy with my recent purchase. The item arrived damaged. I will never buy from you again. This is the worst experience I have ever had."
        else:
            return "Customer: I am happy with my purchase."

    def triage(self, customer_id: str, transcript_id: str) -> str:
        """
        This agent validates the alert and gathers initial context.

        Args:
            customer_id: The ID of the customer.
            transcript_id: The ID of the transcript.

        Returns:
            A JSON string with the agent's decision.
        """

        customer_details = self.crm_lookup_tool(customer_id)
        transcript_text = self.transcript_retrieval_tool(transcript_id)

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

triage_agent_instance = TriageAgent(
    name="triage_agent",
    model="gemini-2.0-flash",
    description="Agent to triage customer complaints.",
    instruction="You are a Triage Agent for critical customer complaints.",
    tools=[TriageAgent.crm_lookup_tool, TriageAgent.transcript_retrieval_tool],
)
