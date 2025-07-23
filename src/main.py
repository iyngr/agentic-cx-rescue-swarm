from google.adk.agents import Agent
from src.triage.agent import triage_agent_instance
from src.solution.agent import solution_agent_instance
from src.action.agent import action_agent_instance
import json

class CustomerExperienceRescueSwarm(Agent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.triage_agent = triage_agent_instance
        self.solution_agent = solution_agent_instance
        self.action_agent = action_agent_instance

    def run(self, event, context):
        """
        Triggered from a message on a Cloud Pub/Sub topic.
        Args:
             event (dict): Event payload.
             context (google.cloud.functions.Context): Metadata for the event.
        """
        # The Pub/Sub message is a JSON payload
        message = json.loads(event)

        # Triage Agent
        triage_output_json = self.triage_agent.triage(
            customer_id=message["customer_id"],
            transcript_id=message["transcript_id"]
        )
        triage_output = json.loads(triage_output_json)

        if triage_output["escalate"]:
            case_file_json = json.dumps(triage_output["case_file"])

            # Solution Agent
            solution_output_json = self.solution_agent.get_solution(case_file_json)

            # Add customer email and id to case file for action agent
            case_file = triage_output["case_file"]
            case_file["customer_details"]["email"] = "customer@example.com" # Mock email
            case_file["customer_details"]["customer_id"] = message["customer_id"]
            case_file_json = json.dumps(case_file)


            # Action & Communication Agent
            self.action_agent.execute_and_communicate(case_file_json, solution_output_json)

if __name__ == '__main__':
    # Simulate a Pub/Sub trigger
    event_payload = {
        "transcript_id": "T12345",
        "customer_id": "C67890",
        "sentiment_score": 0.95
    }
    swarm = CustomerExperienceRescueSwarm(
        name="customer_experience_rescue_swarm",
        model="gemini-2.0-flash",
        description="A swarm of agents that work together to resolve customer issues.",
        instruction="You are a swarm of agents that work together to resolve customer issues.",
    )
    swarm.run(json.dumps(event_payload), None)
