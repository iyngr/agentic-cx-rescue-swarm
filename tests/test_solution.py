import unittest
import json
from src.solution.agent import SolutionAgent

class TestSolutionAgent(unittest.TestCase):

    def setUp(self):
        self.agent = SolutionAgent(
            name="solution_agent",
            model="gemini-2.0-flash",
            description="Agent to find solutions for customer complaints.",
            instruction="You are a master Solution Agent. You have received a 'case_file' for a high-value customer.",
            tools=[SolutionAgent.policy_lookup_tool, SolutionAgent.order_status_tool, SolutionAgent.inventory_check_tool],
        )

    def test_solution_agent(self):
        """
        Tests that the Solution Agent returns a ranked list of solutions.
        """
        case_file = {
            "customer_details": {"ltv": 1500, "status": "Gold Tier", "recent_order_count": 12},
            "transcript_text": "Customer: I am very unhappy with my recent purchase. The item arrived damaged.",
            "issue_summary": "Customer is a high-value client and is extremely dissatisfied with a recent purchase that arrived damaged."
        }
        case_file_json = json.dumps(case_file)
        solution_output_json = self.agent.get_solution(case_file_json)
        solution_output = json.loads(solution_output_json)
        self.assertIn("ranked_solutions", solution_output)
        self.assertGreater(len(solution_output["ranked_solutions"]), 0)

if __name__ == '__main__':
    unittest.main()
