import unittest
import json
from src.action.agent import action_agent
from io import StringIO
import sys

class TestActionAgent(unittest.TestCase):

    def test_action_agent(self):
        """
        Tests that the Action & Communication Agent runs without errors.
        """
        case_file = {
            "customer_details": {"customer_id": "C67890", "email": "customer@example.com"},
            "issue_summary": "Customer is a high-value client and is extremely dissatisfied with a recent purchase that arrived damaged."
        }
        ranked_solutions = {
            "ranked_solutions": [
                {"solution_id": 1, "action": "full_refund", "params": {"order_id": "O-9987", "amount": 75.50}, "explanation": "Customer's item was damaged, and they are a top-tier client. A full refund is the best path."}
            ]
        }
        case_file_json = json.dumps(case_file)
        ranked_solutions_json = json.dumps(ranked_solutions)

        # Redirect stdout to capture print statements
        captured_output = StringIO()
        sys.stdout = captured_output

        action_agent(case_file_json, ranked_solutions_json)

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Check that the print statements are working as expected
        output = captured_output.getvalue()
        self.assertIn("Refund of $75.5 for order O-9987 processed successfully.", output)
        self.assertIn("Communication sent to customer@example.com via email", output)
        self.assertIn("Log entry for customer C67890 added to CRM", output)


if __name__ == '__main__':
    unittest.main()
