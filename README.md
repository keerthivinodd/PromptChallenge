markdown
# Prompt Engineering Analysis: Ticket Categorization

This project evaluates three distinct prompt engineering strategies—**Zero-Shot**, **Few-Shot**, and **Chain-of-Thought**—to determine the most effective method for automating the categorization of customer support tickets using local AI.

## 🚀 Overview
The system uses the **Ollama** framework to run the **Llama 3.2** model locally. It processes five real-world support scenarios (Technical, Billing, and General) through three different prompting logic layers to compare accuracy and reasoning depth.

## 🛠️ Software Requirements
* **Ollama**:
* **Llama 3.2**: Install via terminal: `ollama pull llama3.2`
* **Python 3.10+**: Ensure Python is installed.
* **Libraries**: Install via terminal:
  ```bash
  pip install ollama pandas
Use code with caution.

📂 Project Structure
main.py: The core script that runs the AI tests, cleans the data, and generates reports.
results.csv: A raw data export of all 15 model interactions.
view_results.html: A polished, CSS-styled report containing the final comparison table and analysis.
🧠 Prompting Strategies Evaluated
Zero-Shot: Direct labeling without any prior examples. Fast, but prone to keyword bias.
Few-Shot: Providing specific "Ticket -> Label" examples to establish a pattern for the model.
Chain-of-Thought (CoT): Requiring the model to explain its logic step-by-step before categorizing. This proved to be the most accurate method.
⚙️ How to Run
Ensure Ollama is running in your system tray.
Run the Python script:
bash
python main.py
Use code with caution.

Open view_results.html in any web browser to view the formatted results and final recommendations.
📊 Key Findings
Chain-of-Thought is the superior strategy for complex intent.
Zero-Shot often misclassifies "General" tickets as "Technical" if technical keywords (like "settings") are mentioned.
Regex Cleaning is essential to transform robotic AI outputs into human-readable bullet points.
