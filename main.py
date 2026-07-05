import json


def load_knowledge_base(filename):
    with open(filename, "r") as file:
        return json.load(file)


def find_issue(user_input, knowledge_base):
    for issue, details in knowledge_base.items():
        if details["symptom"].lower() in user_input.lower():
            return issue, details
    return None, None


def diagnose_issue(issue):
    if issue == "slow_internet":
        print("\nDiagnostic questions:")
        response = input("Have you restarted your router? (yes/no): ").strip().lower()

        if response == "no":
            print("Please restart your router and check your connection again.")
        else:
            print("Try resetting your network settings or contacting your provider.")


def automate_fix(issue):
    if issue == "slow_internet":
        print("\nAttempting automated fix...")
        print("Resetting network settings...")
        print("Network settings have been reset.")
    else:
        print("\nNo automated fix is available for this issue.")


def main():
    knowledge_base = load_knowledge_base("troubleshooting_knowledge_base.json")

    user_input = input("Please describe your problem:\n")

    issue, details = find_issue(user_input, knowledge_base)

    if issue is None:
        print("\nNo matching issue found in the knowledge base.")
        return

    print(f"\nPossible solution:\n{details['solution']}")

    diagnose_issue(issue)

    automate_fix(issue)


if __name__ == "__main__":
    main()

