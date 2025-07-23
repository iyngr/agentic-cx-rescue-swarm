import unittest
import json
from src.triage.agent import TriageAgent

class TestTriageAgent(unittest.TestCase):

    def setUp(self):
        self.agent = TriageAgent(
            name="triage_agent",
            model="gemini-2.0-flash",
            description="Agent to triage customer complaints.",
            instruction="You are a Triage Agent for critical customer complaints.",
            tools=[TriageAgent.crm_lookup_tool, TriageAgent.transcript_retrieval_tool],
        )

    def test_triage_agent_escalate(self):
        """
        Tests that the Triage Agent escalates a high-value customer with severe dissatisfaction.
        """
        triage_output_json = self.agent.triage(customer_id="C67890", transcript_id="T12345")
        triage_output = json.loads(triage_output_json)
        self.assertTrue(triage_output["escalate"])
        self.assertIn("case_file", triage_output)

    def test_triage_agent_no_escalate(self):
        """
        Tests that the Triage Agent does not escalate a low-value customer.
        """
        triage_output_json = self.agent.triage(customer_id="C12345", transcript_id="T54321")
        triage_output = json.loads(triage_output_json)
        self.assertFalse(triage_output["escalate"])

if __name__ == '__main__':
    unittest.main()
