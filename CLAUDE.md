# CLAUDE.md — Dark Strategist Agent
# Instructions for Claude when operating within this repository

## What is this repo

`dark-strategist-agent` is THE SOVEREIGN ADVERSARY — a forensic audit agent and adversarial orchestrator. Its function is to subject any solution, proposal, plan, or argument to the most severe possible scrutiny before it is executed, presented, or defended.

This is not a validator. Not an improvement assistant. Not a coach.
It is a systematic destructor of unproven assumptions — and a Director who coordinates specialized micro-agents to confirm every finding.

**Version:** 2.4.0  
**License:** MIT — Open Source  
**Repository:** https://github.com/JARPClaude/dark-strategist-agent

## Repository Structure

```
dark-strategist-agent/
├── README.md                              ← Public documentation
├── CLAUDE.md                              ← This file (Claude instructions)
├── CHANGELOG.md                           ← Version history
├── prompts/
│   └── system_prompt.md                   ← Production-ready system prompt (EN)
├── examples/
│   ├── example_01_business_plan.md        ← Business plan analysis
│   ├── example_02_tech_architecture.md    ← Tech architecture analysis
│   └── example_03_war_room.md             ← Multi-domain War Room orchestration
└── docs/
    ├── severity_taxonomy.md               ← Severity levels reference
    ├── micro_agents_catalog.md            ← 7 standard micro-agents + activation matrix
    ├── output_format.md                   ← Report structure (Blocks 0–6)
    ├── governance.md                      ← Protocol versioning governance (§4.14)
    └── deprecation.md                     ← Deprecation conditions and protocol (§4.15)
```

## How to use this agent

### Option A — Claude.ai Projects
1. Open Claude.ai → Projects → New Project
2. In "Project Instructions", paste the contents of `prompts/system_prompt.md`
3. Start conversation and present your proposal

### Option B — Claude API
```python
import anthropic

with open("prompts/system_prompt.md", "r", encoding="utf-8") as f:
    system_prompt = f.read()

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=8192,
    system=system_prompt,
    messages=[{"role": "user", "content": "Here is my proposal: [YOUR PROPOSAL]"}]
)
print(message.content[0].text)
```

### Option C — Claude Code (registered agent)
Add the corresponding entry in your `AGENTS.md`.

## When to use this agent

| Situation | Use agent? |
|---|---|
| Before executing a business plan | ✅ Yes |
| Before presenting to investors or stakeholders | ✅ Yes |
| Before launching a technical architecture to production | ✅ Yes |
| Before defending a strategy in a high-level meeting | ✅ Yes |
| Before entering a new market or geography | ✅ Yes |
| For friendly feedback | ❌ No — use another agent |
| For validating something already in production that cannot change | ❌ Not useful |

## Protocol Governance (§4.14)

- Only the registered repository author may approve modifications to the production system prompt
- Forks must maintain their own CHANGELOG
- Every candidate version must be self-audited before release — REPORT_ID logged in CHANGELOG
- Version types: Major (X.0.0) = architecture change | Minor (X.Y.0) = section corrections | Patch (X.Y.Z) = text fixes

## Deprecation (§4.15)

This protocol is **ACTIVE — v2.4.0**. See `docs/deprecation.md` for conditions under which this version should be considered obsolete.

## Rules for extending this agent

1. Any modification to the system prompt must increment the version in `CHANGELOG.md`
2. Examples in `examples/` must follow the exact prompt format (Blocks 0–6 + Verdict)
3. Do not add instructions that soften the critical tone
4. If a specialized domain variant is added, create `system_prompt_[domain].md` separately in `prompts/`
5. The ES/EN terminology equivalence map in §4.4 must be maintained in any language variant
