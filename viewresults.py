import pandas as pd
import re

csv_path = 'results.csv'
html_file = 'view_results.html'

def clean_to_bullets(text):
    if not isinstance(text, str): return text
    
    # 1. Strip out robotic labels, n1, n2, and escaped characters
    text = text.replace('\\n', '\n').replace('\\r', '\n')
    text = re.sub(r'(?i)(Analysis:|Step \d+:|Categorization:|Intent:|Reasoning:|Label:)', '', text)
    text = re.sub(r'\bn\d+\b', '', text) 
    text = re.sub(r'\d+\.\s*', '', text) 
    text = text.replace('**', '').replace('\\', '')
    
    # 2. Strip existing dashes (-) to prevent double bullets
    text = text.replace('- ', ' ').replace('-', ' ')
    
    # 3. Split into sentences and filter
    raw_lines = re.split(r'[.!?\n]', text)
    clean_lines = [line.strip() for line in raw_lines if len(line.strip()) > 5]
    
    # 4. Rejoin with clean HTML bullet points
    if not clean_lines: return text
    return '• ' + '<br>• '.join(clean_lines)

try:
    df = pd.read_csv(csv_path)
    
    for col in ['Few-Shot', 'Chain-of-Thought']:
        if col in df.columns:
            df[col] = df[col].apply(clean_to_bullets)
    
    if 'Zero-Shot' in df.columns:
        df['Zero-Shot'] = df['Zero-Shot'].apply(lambda x: str(x).replace('**', '').strip())

    html_table = df.to_html(classes='table', index=False, escape=False)
    
    # Analysis content without the vertical border-left styling
    analysis_content = """
    <div class='analysis'>
        <h2>Part 1: Analysis of Findings</h2>
        <p><strong>Ticket 1 (Black Screen):</strong> All strategies identified this as Technical. Chain-of-Thought provided the most depth, identifying the issue as a system failure.</p>
        <p><strong>Ticket 2 (Refund Request):</strong> Zero-Shot struggled by defaulting to Technical. Few-Shot was more accurate, and Chain-of-Thought correctly recognized the financial dispute.</p>
        <p><strong>Ticket 3 (Profile Picture):</strong> Identified correctly as General by Few-Shot and CoT. Zero-Shot failed here by defaulting to Technical due to the mention of settings.</p>
        <p><strong>Ticket 4 (Slow Update):</strong> Correctly identified as Technical by all. CoT explained the logic of software performance degradation effectively.</p>
        <p><strong>Ticket 5 (Yearly Subscription):</strong> A standard Billing query. All strategies succeeded, though Few-Shot offered the most concise output.</p>

        <h2>Part 2: Strategy Comparison</h2>
        <p><strong>Zero-Shot:</strong> Efficient but prone to errors when specific keywords were used in a general context.</p>
        <p><strong>Few-Shot:</strong> Strongest for formatting, providing a clear pattern for the model to follow.</p>
        <p><strong>Chain-of-Thought:</strong> Superior reasoning accuracy; avoids classification errors by evaluating logic first.</p>

        <h2>Part 3: Final Recommendation</h2>
        <p><strong>The Best Strategy: Chain-of-Thought (CoT)</strong></p>
        <p>Chain-of-Thought is the recommended strategy. It prevents decisions based on isolated keywords by breaking down user intent into logical steps. This reduces misclassification in borderline cases, leading to higher automation accuracy.</p>
    </div>
    """

    full_html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: 'Segoe UI', Arial, sans-serif; margin: 40px; background: white; color: #333; }}
            .container {{ max-width: 1000px; margin: auto; }}
            h1 {{ color: #4682B4; border-bottom: 2px solid #87CEEB; padding-bottom: 10px; margin-bottom: 30px; }}
            h2 {{ color: #003366; margin-top: 40px; font-size: 1.3em; border-left: none !important; }} /* Forced removal of blue line */
            table {{ border-collapse: collapse; width: 100%; margin: 25px 0; border: 1px solid #e1e8ed; }}
            th {{ background: #87CEEB; color: #003366; padding: 15px; text-align: left; border: 1px solid #ccc; }}
            td {{ padding: 12px; border: 1px solid #eee; vertical-align: top; font-size: 13px; line-height: 1.6; }}
            tr:nth-child(even) {{ background: #f9fcff; }}
            .analysis {{ margin-top: 40px; }}
            p {{ margin-bottom: 15px; }}
        </style>
    </head>
    <body>
        <div class='container'>
            <h1>Assignment 2: Prompt Engineering Analysis</h1>
            {html_table}
            {analysis_content}
        </div>
    </body>
    </html>
    """
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print("Report ready")
except Exception as e:
    print(f"Error: {e}")
