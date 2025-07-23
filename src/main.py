import json
from src.triage.agent import triage_agent
from src.solution.agent import solution_agent
from src.action.agent import action_agent

def main(event, context):
    """
    Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    # The Pub/Sub message is a JSON payload
    message = json.loads(event)

    # Triage Agent
    triage_output_json = triage_agent(
        customer_id=message["customer_id"],
        transcript_id=message["transcript_id"]
    )
    triage_output = json.loads(triage_output_json)

    if triage_output["escalate"]:
        case_file_json = json.dumps(triage_output["case_file"])

        # Solution Agent
        solution_output_json = solution_agent(case_file_json)

        # Add customer email and id to case file for action agent
        case_file = triage_output["case_file"]
        case_file["customer_details"]["email"] = "customer@example.com" # Mock email
        case_file["customer_details"]["customer_id"] = message["customer_id"]
        case_file_json = json.dumps(case_file)


        # Action & Communication Agent
        action_agent(case_file_json, solution_output_json)

if __name__ == '__main__':
    # Simulate a Pub/Sub trigger
    event_payload = {
        "transcript_id": "T12345",
        "customer_id": "C67890",
        "sentiment_score": 0.95
    }
    main(json.dumps(event_payload), None)
