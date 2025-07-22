DAO Shade Agent is an autonomous reviewer for NEAR DevHub governance proposals. It reads proposals from a JSON file, evaluates them using customizable rules, and returns an approve or reject decision with a short explanation.

Features:

Reads proposals from test_proposals.json
Checks if the proposer is on a whitelist
Validates that the budget is reasonable
Ensures the task description is clear and sufficiently detailed
Returns an approve or reject decision with an explanation
Easily extendable for more rules or integration with LLMs
Setup:

Clone the repository and enter the dao-shade-agent directory.
(Optional) Create a Python virtual environment.
No external dependencies are required for the basic agent.
Usage:

Place your proposals in test_proposals.json (see examples below).
Run the agent with: python main.py
The agent will print the decision and explanation for each proposal.
Example test_proposals.json:

[ { "id": 1, "title": "Add new voting feature", "description": "Implement a new voting system for the DAO with flexible quorum and delegation options. This will improve governance and participation.", "budget": 3000, "proposer": "alice.near" }, { "id": 2, "title": "DAO T-shirt design", "description": "T-shirt design.", "budget": 200, "proposer": "bob.near" }, { "id": 3, "title": "Massive marketing campaign", "description": "Launch a global marketing campaign across all major platforms to increase DAO awareness and attract new members.", "budget": 10000, "proposer": "unknown.near" } ]

Logic:

Only proposals from addresses in the whitelist are approved.
Proposals with a budget above the set maximum are rejected.
Proposals with a description shorter than 30 characters are rejected.
You can adjust these rules in main.py.
To add more rules, edit the evaluate_proposal function in main.py. To integrate with LLMs or a UI, see the comments in the code for extension points.