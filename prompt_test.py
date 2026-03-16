import ollama
import csv

# 1. Define your 5 test inputs
test_inputs = [
    "My screen goes black every time I open the dashboard.",
    "I need a refund for the double charge on my Visa card.",
    "How do I change my profile picture in the settings?",
    "The new update is much slower than the previous version.",
    "Can I pay for a yearly subscription instead of monthly?"
]


strategies = {
    "Zero-Shot": "Categorize this ticket as Technical, Billing, or General. Output only the label: ",
    "Few-Shot": "Ticket: 'I forgot my password' Label: Technical. Ticket: 'Where is my invoice?' Label: Billing. Ticket: ",
    "Chain-of-Thought": "Analyze the user intent step-by-step, then categorize as Technical, Billing, or General: "
}

results = []

# 3. Run the 15 tests
print("Running tests on Ollama (Llama 3.2)...")
for input_text in test_inputs:
    row = {"Input": input_text}
    for name, prompt_prefix in strategies.items():
        print(f"Testing {name} for: {input_text[:30]}...")
        response = ollama.generate(model='llama3.2', prompt=f"{prompt_prefix}{input_text}")
        row[name] = response['response'].strip()
    results.append(row)

# 4. Save to a CSV file for your assignment table
with open('results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["Input", "Zero-Shot", "Few-Shot", "Chain-of-Thought"])
    writer.writeheader()
    writer.writerows(results)

print("\nDone! Results saved ")
