def simplify_prompt(text, domain):
    """
    Creates a structured prompt for simplifying legal or medical text
    """

    return f"""
You are an expert {domain} document assistant.

Your task is to help non-experts understand complex documents.

INSTRUCTIONS:
1. Rewrite the content in very simple, layman-friendly English.
2. Break long sentences into short ones.
3. List the important points clearly.
4. Highlight any risks, warnings, or critical conditions if mentioned.

DOCUMENT TEXT:
{text}

FORMAT YOUR RESPONSE AS:

Simplified Explanation:
<simple explanation here>

Key Points:
- point 1
- point 2
- point 3

Warnings / Risks (if any):
- warning 1
- warning 2
"""
