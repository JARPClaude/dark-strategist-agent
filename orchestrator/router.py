"""
Dark Strategist Agent — Router
Detects document domain and selects the correct system prompt.
Version: 2.7.0
"""

import os
import re
import json
import anthropic
from pathlib import Path
from datetime import datetime


PROMPT_CATALOG = {
    "P01": {"file": "system_prompt.md",              "domain": "General",        "unit": "Contextual"},
    "P02": {"file": "system_prompt_trading.md",      "domain": "Trading",        "unit": "UNIT-QUANT"},
    "P03": {"file": "system_prompt_legal.md",        "domain": "Legal",          "unit": "UNIT-INQUISITOR"},
    "P04": {"file": "system_prompt_code.md",         "domain": "Code",           "unit": "UNIT-TECH"},
    "P05": {"file": "system_prompt_financial.md",    "domain": "Financial",      "unit": "UNIT-QUANT"},
    "P06": {"file": "system_prompt_cloud.md",        "domain": "Cloud",          "unit": "UNIT-TECH"},
    "P07": {"file": "system_prompt_cybersecurity.md","domain": "Cybersecurity",  "unit": "UNIT-TECH"},
    "P08": {"file": "system_prompt_agro.md",         "domain": "Agriculture",    "unit": "UNIT-BIO"},
    "P09": {"file": "system_prompt_realestate.md",   "domain": "Real Estate",    "unit": "UNIT-MARKET"},
    "P10": {"file": "system_prompt_science.md",      "domain": "Science",        "unit": "UNIT-QUANT"},
    "P11": {"file": "system_prompt_media.md",        "domain": "Media",          "unit": "UNIT-MARKET"},
    "P12": {"file": "system_prompt_ecommerce.md",    "domain": "E-Commerce",     "unit": "UNIT-MARKET"},
    "P13": {"file": "system_prompt_telecom.md",      "domain": "Telecom",        "unit": "UNIT-GEO"},
    "P14": {"file": "system_prompt_publicsector.md", "domain": "Public Sector",  "unit": "UNIT-COMPLIANCE"},
}


class DomainRouter:
    def __init__(self, config: dict, prompts_dir: str):
        self.config = config
        self.prompts_dir = Path(prompts_dir)
        self.client = anthropic.Anthropic(api_key=config["anthropic"]["api_key"])
        self.router_prompt = self._load_prompt("system_prompt_router.md")

    def _load_prompt(self, filename: str) -> str:
        path = self.prompts_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"Prompt not found: {path}")
        return path.read_text(encoding="utf-8")

    def detect_domain(self, document: str) -> dict:
        response = self.client.messages.create(
            model=self.config["anthropic"]["model"],
            max_tokens=1024,
            system=self.router_prompt,
            messages=[{"role": "user", "content": f"Analyze and route:\n\n{document}"}]
        )
        raw = response.content[0].text
        return self._parse_routing_decision(raw, document)

    def _parse_routing_decision(self, raw_response: str, document: str) -> dict:
        if "UNKNOWN_DOMAIN_DETECTED" in raw_response or "DYNAMIC_TEMPORARY" in raw_response:
            return {
                "prompt_id": "UNKNOWN", "prompt_file": "DYNAMIC_TEMPORARY",
                "domain": self._extract_detected_domain(raw_response),
                "primary_unit": "Contextual", "confidence": "LOW", "is_unknown": True,
                "raw_response": raw_response, "timestamp": datetime.utcnow().isoformat(),
                "key_verification_points": self._extract_key_points(raw_response)
            }
        matched_id = None
        matched_confidence = "LOW"
        for pid, entry in PROMPT_CATALOG.items():
            if pid == "P01":
                continue
            if entry["domain"].upper() in raw_response.upper():
                matched_id = pid
                matched_confidence = "HIGH" if "HIGH" in raw_response else "MODERATE" if "MODERATE" in raw_response else "LOW"
                break
        if not matched_id:
            matched_id = "P01"
            matched_confidence = "LOW"
        entry = PROMPT_CATALOG[matched_id]
        return {
            "prompt_id": matched_id, "prompt_file": entry["file"],
            "domain": entry["domain"], "primary_unit": entry["unit"],
            "confidence": matched_confidence, "is_unknown": False,
            "raw_response": raw_response, "timestamp": datetime.utcnow().isoformat(),
            "key_verification_points": []
        }

    def _extract_detected_domain(self, text: str) -> str:
        match = re.search(r"DETECTED_DOMAIN:\s*([^\n\]]+)", text)
        return match.group(1).strip() if match else "Unknown"

    def _extract_key_points(self, text: str) -> list:
        return [p.strip() for p in re.findall(r"→\s*(.+)", text) if p.strip()]

    def load_domain_prompt(self, routing: dict) -> str:
        if routing["is_unknown"]:
            return self._load_prompt("system_prompt.md")
        return self._load_prompt(routing["prompt_file"])

    def print_routing_summary(self, routing: dict):
        print(f"\n{'='*60}\nDARK STRATEGIST — ROUTING DECISION\n{'='*60}")
        print(f"Domain:    {routing['domain']}")
        print(f"Prompt:    {routing['prompt_file']}")
        print(f"Unit:      {routing['primary_unit']}")
        print(f"Confidence:{routing['confidence']}")
        if routing["is_unknown"]:
            print("⚠️  DOMAIN_EXPANSION_RECOMMENDED will be generated")
        print("="*60)
