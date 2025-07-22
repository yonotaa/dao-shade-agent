import json

WHITELIST = {"alice.near", "bob.near", "carol.near"}
MAX_BUDGET = 5000
MIN_DESC_LENGTH = 30

def evaluate_proposal(proposal):
    proposer = proposal.get("proposer")
    if not proposer:
        return False, "No proposer specified"
    if proposer not in WHITELIST:
        return False, f"Proposer '{proposer}' not in whitelist"

    budget = proposal.get("budget")
    if budget is None:
        return False, "No budget specified"
    try:
        budget = float(budget)
    except (ValueError, TypeError):
        return False, "Budget is not a number"
    if budget > MAX_BUDGET:
        return False, f"Budget {budget} exceeds maximum allowed ({MAX_BUDGET})"

    description = proposal.get("description", "")
    if len(description.strip()) < MIN_DESC_LENGTH:
        return False, "Description too short or missing"

    return True, "Proposal approved"

def main():
    with open("test_proposals.json", "r", encoding="utf-8") as f:
        proposals = json.load(f)

    for i, proposal in enumerate(proposals, 1):
        decision, reason = evaluate_proposal(proposal)
        print(f"Proposal #{i}: {'APPROVED' if decision else 'REJECTED'} — {reason}")

if __name__ == "__main__":
    main()