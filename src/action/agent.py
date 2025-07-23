from google.adk.agents import Agent
import json

class ActionAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def refund_tool(self, order_id: str, amount: float) -> dict:
        """
        Issues a refund for a given order.

        Args:
            order_id: The ID of the order to refund.
            amount: The amount to refund.

        Returns:
            A dictionary with the refund status.
        """
        # In a real implementation, this would call a payment gateway API.
        # For this example, we'll use mock data.
        print(f"Refund of ${amount} for order {order_id} processed successfully.")
        return {"status": "success"}

    def reship_order_tool(self, order_id: str) -> dict:
        """
        Re-ships a given order.

        Args:
            order_id: The ID of the order to re-ship.

        Returns:
            A dictionary with the re-shipment status.
        """
        # In a real implementation, this would call a logistics API.
        # For this example, we'll use mock data.
        print(f"Re-shipment for order {order_id} processed successfully.")
        return {"status": "success"}

    def generate_coupon_tool(self, value: int, unit: str) -> dict:
        """
        Generates a coupon for a customer.

        Args:
            value: The value of the coupon.
            unit: The unit of the coupon (e.g., "percent", "dollars").

        Returns:
            A dictionary with the coupon code.
        """
        # In a real implementation, this would call a coupon generation API.
        # For this example, we'll use mock data.
        coupon_code = "WELCOME50" if unit == "percent" else "WELCOME10"
        print(f"Coupon for {value}{unit} generated successfully: {coupon_code}")
        return {"coupon_code": coupon_code}

    def send_communication_tool(self, recipient: str, channel: str, body: str) -> dict:
        """
        Sends a communication to a customer.

        Args:
            recipient: The recipient of the communication.
            channel: The channel of the communication (e.g., "email", "sms").
            body: The body of the communication.

        Returns:
            A dictionary with the communication status.
        """
        # In a real implementation, this would call an email or SMS API.
        # For this example, we'll use mock data.
        print(f"Communication sent to {recipient} via {channel}: {body}")
        return {"status": "success"}

    def log_to_crm_tool(self, customer_id: str, log_entry: str) -> dict:
        """
        Logs an incident and resolution in the CRM.

        Args:
            customer_id: The ID of the customer.
            log_entry: The log entry to add to the customer's record.

        Returns:
            A dictionary with the logging status.
        """
        # In a real implementation, this would call a CRM API.
        # For this example, we'll use mock data.
        print(f"Log entry for customer {customer_id} added to CRM: {log_entry}")
        return {"status": "success"}

    def execute_and_communicate(self, case_file_json: str, ranked_solutions_json: str):
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
            self.refund_tool(**params)
        elif action == "reship_express":
            self.reship_order_tool(**params)
        elif action == "generate_coupon":
            self.generate_coupon_tool(**params)

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
        self.send_communication_tool(recipient=case_file["customer_details"]["email"], channel="email", body=email_body)

        # Finally, create a concise summary of the incident and resolution.
        log_entry = f"Incident: {case_file['issue_summary']}. Resolution: {top_solution['explanation']}."

        # Call the log_to_crm_tool to record this summary on the customer's record.
        self.log_to_crm_tool(customer_id=case_file["customer_details"]["customer_id"], log_entry=log_entry)

action_agent_instance = ActionAgent(
    name="action_agent",
    model="gemini-2.0-flash",
    description="Agent to execute solutions and communicate with customers.",
    instruction="You are the Action and Communication Agent. Your job is to execute the resolution and inform the customer with empathy.",
    tools=[ActionAgent.refund_tool, ActionAgent.reship_order_tool, ActionAgent.generate_coupon_tool, ActionAgent.send_communication_tool, ActionAgent.log_to_crm_tool],
)
