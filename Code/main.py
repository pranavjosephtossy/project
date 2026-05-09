import json
import hashlib
import datetime
import os
from openai import OpenAI
from dotenv import load_dotenv
from chain_of_custody import add_chain_of_custody_entry

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_AI_API_KEY"))

USE_CASE = "hate speech and abuse"


def analyse_with_llm(content_type, text):
    prompt = f"""
Analyse this YouTube {content_type} for: {USE_CASE}

Content: {text}

Reply in raw JSON only:
{{"severity": "low/medium/high/none - give on a scale of 1 - 10", "reasoning": "a sentence describing why you assigned that severity",
"content":"exact copy of the comment the analysis was done on"}}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a digital forensics content analyser."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
        max_tokens=200,
    )

    raw = response.choices[0].message.content.strip()
    raw = raw.replace("```json", "").replace("```", "").strip()
    result = json.loads(raw)
    return result


def analysis(comment):
    """Takes a single comment dict from pipeline.py, returns (analysis_json, analysis_log)."""
    text = comment.get("comment_text", "")
    output = analyse_with_llm("comment", text)

    analysis_json = {
        "comment_id": comment.get("comment_id"),
        "llm_severity": output['severity'],
        "llm_reasoning": output['reasoning'],
        "content": output['content']
    }

    analysis_log = [add_chain_of_custody_entry("analysis", "analysis_module")]

    return analysis_json, analysis_log