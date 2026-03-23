# Handoff by CAIO

**Move any Claude conversation to a new chat with zero re-explanation.**

*By Stefanos Karagos | Lead Instructor & AI Strategist at [CAIO](https://wearecaio.com)*

> **New here?** See the [installation guide](../../README.md#how-to-install-a-skill) for step-by-step setup instructions (Claude Projects, Cowork, or Claude Code).

---

## The Problem

Claude conversations hit context limits. Important sessions die mid-task. You open a new chat and spend 15 minutes re-explaining everything. Context is lost. Momentum is gone.

## The Solution

Type `/handoff` (or say "move to a new chat") and the skill generates a structured Markdown file that captures everything: what you were working on, every decision made, every artifact produced, and a paste-ready resume prompt.

Drop that file into a new chat. You're back in motion in seconds.

## What It Produces

The handoff file includes:

- **Session type detection** with suggested chat naming (e.g., `PROP — SaaS Pricing v2`)
- **Decision log** with reasoning captured from the conversation
- **Artifact classification**: each output is tagged as Carry Over (include full content), Reference (summary only), or Archive (noted, excluded)
- **Current state**: what's done, in progress, and not started
- **Next steps**: specific, executable actions for the new chat
- **Resume prompt**: a self-contained paragraph you paste as your first message

## Installation

1. Copy `SKILL.md` from this folder
2. Add it to your Claude Project's knowledge base
3. Type `/handoff` whenever you need to move

## Trigger Phrases

The skill activates on any of these:

- `/handoff`
- "move to a new chat"
- "continue in a new chat"
- "handoff file"
- "new conversation" (when context implies session transfer)

No confirmation needed. It executes immediately.

---

*Handoff by CAIO | [wearecaio.com](https://wearecaio.com)*
