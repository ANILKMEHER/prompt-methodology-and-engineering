#!/usr/bin/env python3
"""
Production-Ready Prompt Payload Compression Engine
Author: Anil K. Meher
Description: Programmatically strips conversational fluff, minifies schema keys, 
             and removes whitespace blocks from complex few-shot contexts to optimize LLM token usage.
"""

import json
import re

# Simulated unoptimized, high-latency enterprise few-shot context payload asset
RAW_FEW_SHOT_CONTEXT = """
[SYSTEM DESIGN CONTEXT]: You are acting as an automated compliance auditor for our cloud infrastructure network.
Please be very careful and kindly ensure that you read through the entire target input block provided below.

[EXAMPLE CASE 1]:
{
  "target_infrastructure_environment_id": "env-prod-904",
  "operational_compliance_status": "NON_COMPLIANT",
  "identified_vulnerability_risk_score": 0.89
}
"""

def compress_prompt_payload(raw_text: str) -> str:
    """Parses raw prompt input text and returns an optimized, high-density string payload."""
    initial_length = len(raw_text)
    print(f"📊 Original Payload Footprint: {initial_length} characters.")
    
    # 1. Purge verbose conversational fluff structures
    clean_text = raw_text.replace(
        "Please be very careful and kindly ensure that you read through the entire target input block provided below.", 
        ""
    )
    clean_text = clean_text.replace(
        "[SYSTEM DESIGN CONTEXT]: You are acting as an automated compliance auditor for our cloud infrastructure network.", 
        "Task: Cloud Compliance Audit."
    )
    
    # 2. Minify structural JSON keys inside example maps to optimize cross-attention token weight
    clean_text = clean_text.replace("target_infrastructure_environment_id", "env_id")
    clean_text = clean_text.replace("operational_compliance_status", "status")
    clean_text = clean_text.replace("identified_vulnerability_risk_score", "risk")
    
    # 3. Locate, parse, and strip formatting space layouts from JSON code blocks
    json_match = re.search(r'\{.*\}', clean_text, re.DOTALL)
    if json_match:
        raw_json_string = json_match.group(0)
        parsed_json = json.loads(raw_json_string)
        # Re-serialize into a single-line string with zero spaces or padding
        minified_json_string = json.dumps(parsed_json, separators=(',', ':'))
        clean_text = clean_text.replace(raw_json_string, minified_json_string)
    
    # 4. Clean up trailing line fragments and blank vertical spacing gaps
    clean_text = re.sub(r'\n\s*\n', '\n', clean_text).strip()
    
    optimized_length = len(clean_text)
    savings_percentage = ((initial_length - optimized_length) / initial_length) * 100
    
    print(f"🚀 Optimized Payload Footprint: {optimized_length} characters.")
    print(f"💰 Calculated Reduction Rate: {savings_percentage:.2f}% Cost Savings achieved.")
    
    return clean_text

if __name__ == "__main__":
    print("--- INITIATING PROMPT COMPRESSION ENGINE PASS ---")
    optimized_payload = compress_prompt_payload(RAW_FEW_SHOT_CONTEXT)
    print("\n--- DEPLOYABLE PRODUCTION PROMPT INGRESS TARGET ---")
    print(optimized_payload)
