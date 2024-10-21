def decision_tree(k_base):
    """
    A function to navigate through the decision tree.
    
    :param k_base: The knowledge base as a nested dictionary.
    """
    current_node = k_base

    while isinstance(current_node, dict):
        # Get the first (and only) question from the current node
        question = list(current_node.keys())[0]
        answer = input(f"{question} (Yes/No): ").strip().capitalize()

        # Check if the answer is valid
        if answer in current_node[question]:
            current_node = current_node[question][answer]
        else:
            print("Invalid answer. Please respond with 'Yes' or 'No'.")

    print(f"Recommendation: {current_node}")


# Define the knowledge base
K_Base = {
    "Is the computer powering on?": {
        "Yes": {
            "Is there a beeping sound?": {
                "Yes": "Check the RAM and CPU",
                "No": {
                    "Is the display showing any output?": {
                        "Yes": "Check the display connections and settings",
                        "No": "Check the power supply and motherboard"
                    }
                }
            }
        },
        "No": "Check the power supply and cables"
    }
}

# Start the decision tree
if __name__ == "__main__":
    print("Computer Troubleshooting Decision Tree")
    decision_tree(K_Base)
