import unittest
import json
from src.triage.agent import triage_agent

class TestTriageAgent(unittest.TestCase):

    def test_triage_agent_escalate(self):
        """
        Tests that the Triage Agent escalates a high-value customer with severe dissatisfaction.
        """
        triage_output_json = triage_agent(customer_id="C67890", transcript_id="T12345")
        triage_output = json.loads(triage_output_json)
        self.assertTrue(triage_output["escalate"])
        self.assertIn("case_file", triage_output)

    def test_triage_agent_no_escalate(self):
        """
        Tests that the Triage Agent does not escalate a low-value customer.
        """
        triage_output_json = triage_agent(customer_id="C12345", transcript_id="T54321")
        triage_output = json.loads(triage_output_json)
        self.assertFalse(triage_output["escalate"])

if __name__ == '__main__':
    unittest.main()
