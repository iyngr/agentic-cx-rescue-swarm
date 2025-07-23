import unittest
import json
from src.solution.agent import solution_agent

class TestSolutionAgent(unittest.TestCase):

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
        solution_output_json = solution_agent(case_file_json)
        solution_output = json.loads(solution_output_json)
        self.assertIn("ranked_solutions", solution_output)
        self.assertGreater(len(solution_output["ranked_solutions"]), 0)

if __name__ == '__main__':
    unittest.main()
