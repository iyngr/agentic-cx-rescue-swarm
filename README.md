# Agentic Customer Experience Rescue Swarm

This project implements a multi-agent system to proactively handle customer issues based on sentiment analysis of call transcripts. The system is designed to be deployed on Google Cloud's Agent Engine and uses the Agent Development Kit (ADK).

## High-Level Architecture

The system is a sequential multi-agent workflow triggered by a Pub/Sub message from an upstream sentiment analysis system. The message contains the `transcript_id`, `customer_id`, and `negative_sentiment_score`.

The agent swarm is built as a single, stateful application using the Google Agent Development Kit (ADK) and is deployed as a serverless workload on Cloud Run, managed by Agent Engine.

The orchestration is handled by a main controller that invokes the agents in sequence, passing the context from one to the next.

## Agents

The swarm consists of three agents:

1.  **Triage Agent**: This agent validates the alert and gathers initial context by looking up customer details in the CRM and retrieving the full call transcript. It then decides whether to escalate the issue based on the customer's value and the severity of their dissatisfaction.
2.  **Solution Agent**: This agent determines the best resolution path by querying a knowledge base of company policies and checking order status and inventory. It then generates a ranked list of potential solutions.
3.  **Action & Communication Agent**: This agent executes the top-ranked solution by calling the relevant system APIs (e.g., for refunds, re-shipments, or coupons). It then sends a personalized, empathetic communication to the customer and logs the incident in the CRM.

## Getting Started

1.  Install the dependencies:
    ```
    pip install -r requirements.txt
    ```
2.  Run the tests:
    ```
    python -m unittest discover tests
    ```
3.  Run the main application:
    ```
    python src/main.py
    ```
    This will simulate a Pub/Sub trigger and run the agent swarm.
