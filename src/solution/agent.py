from google.adk.agents import Agent
import json

class SolutionAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def policy_lookup_tool(self, query: str) -> str:
        """
        Queries the company policy knowledge base.

        Args:
            query: The query to search for in the knowledge base.

        Returns:
            The text content of the most relevant policy chunks.
        """
        # In a real implementation, this would query a vector database.
        # For this example, we'll use mock data.
        if "lost package" in query and "gold tier" in query:
            return "Policy Snippet 1: For Gold Tier customers with lost packages, a full refund or a free replacement with express shipping is offered."
        else:
            return "Policy Snippet 1: Standard policy for lost packages is to offer a replacement."

    def order_status_tool(self, order_id: str) -> dict:
        """
        Queries the logistics system for the status of an order.

        Args:
            order_id: The ID of the order to look up.

        Returns:
            A dictionary with the order status.
        """
        # In a real implementation, this would query a logistics API.
        # For this example, we'll use mock data.
        if order_id == "O-9987":
            return {"status": "delivered", "delivery_date": "2023-10-26"}
        else:
            return {"status": "in_transit"}

    def inventory_check_tool(self, item_id: str) -> dict:
        """
        Queries the inventory system for the stock of an item.

        Args:
            item_id: The ID of the item to look up.

        Returns:
            A dictionary with the item's stock level.
        """
        # In a real implementation, this would query an inventory API.
        # For this example, we'll use mock data.
        return {"stock_level": 100}

    def get_solution(self, case_file_json: str) -> str:
        """
        This agent determines the best resolution path.

        Args:
            case_file_json: A JSON string containing the case file.

        Returns:
            A JSON object containing a "ranked_solutions" list.
        """
        case_file = json.loads(case_file_json)

        # Deeply analyze the case file to understand the customer's problem.
        # In a real implementation, a large language model would be used for this analysis.
        # Here, we'll use a simplified logic.
        problem = case_file["issue_summary"]
        customer_status = case_file["customer_details"]["status"]

        # Use the policy_lookup_tool to find all relevant company policies for this specific situation.
        policy = self.policy_lookup_tool(f"policy for {problem} for {customer_status} customer")

        # Synthesize the customer's value, the problem, and company policies to generate a ranked list of 2-3 potential solutions.
        # In a real implementation, a large language model would be used for this synthesis.
        # Here, we'll use a simplified logic.
        ranked_solutions = []
        if "full refund" in policy.lower():
            ranked_solutions.append({"solution_id": 1, "action": "full_refund", "params": {"order_id": "O-9987", "amount": 75.50}, "explanation": "Customer's item was damaged, and they are a top-tier client. A full refund is the best path."})
        if "reship" in policy.lower() or "replacement" in policy.lower():
            ranked_solutions.append({"solution_id": 2, "action": "reship_express", "params": {"order_id": "O-9987"}, "explanation": "Re-ship the item with complimentary express shipping."})

        ranked_solutions.append({"solution_id": 3, "action": "generate_coupon", "params": {"value": 50, "unit": "percent"}, "explanation": "Offer a 50% coupon for a future purchase."})


        return json.dumps({"ranked_solutions": ranked_solutions})

solution_agent_instance = SolutionAgent(
    name="solution_agent",
    model="gemini-2.0-flash",
    description="Agent to find solutions for customer complaints.",
    instruction="You are a master Solution Agent. You have received a 'case_file' for a high-value customer.",
    tools=[SolutionAgent.policy_lookup_tool, SolutionAgent.order_status_tool, SolutionAgent.inventory_check_tool],
)
