# AI Skills by CAIO

Custom AI skills built by [Stefanos Karagos](https://www.linkedin.com/in/stefanoskaragos/), Lead Instructor & Senior GenAI Consultant at [CAIO](https://wearecaio.com).

These are production-grade skills designed for Claude Projects and Claude Cowork. Each one encodes a specific workflow, methodology, or thinking framework that turns Claude into a specialized operator for a defined task.

Not prompts. Not templates. Operational intelligence.

---

## Skills Catalog

| Skill | Description | Type |
|-------|-------------|------|
| [Handoff by CAIO](skills/handoff-by-caio/) | Move any Claude conversation to a new chat with zero re-explanation. Generates a structured handoff file with full context, classified artifacts, and a paste-ready resume prompt. | Workflow |
| [The Sun Tzu Lens](skills/the-sun-tzu-lens/) | Strategic intelligence layer for executives. Applies Sun Tzu's 13-chapter framework to real business decisions with live web research. Seven modes including War Council, Enemy's Eyes, and Negotiation Table. | Strategy |

---

## Skill Showcase

### Handoff by CAIO

**Category:** Workflow Automation
**Trigger:** `/handoff` or say "move to a new chat"

Claude conversations hit context limits. Important ones die mid-task. This skill solves that problem completely.

When triggered, it scans the full conversation, extracts decisions, classifies every artifact (carry over, reference, or archive), and generates a single Markdown file. That file contains everything the next chat needs to pick up exactly where you left off. It includes a paste-ready resume prompt: drop it into a fresh conversation and you're back in motion.

**What it produces:**
- Session type detection and suggested chat naming
- Full decision log with reasoning
- Artifact classification (carry over / reference / archive)
- Current state tracking (done, in progress, not started)
- Executable next steps
- One-paste resume prompt for the new chat

**Installation:** Copy `skills/handoff-by-caio/SKILL.md` into your Claude Project's knowledge base.

---

### The Sun Tzu Lens

**Category:** Executive Strategy
**Triggers:** `/warcouncil` `/lens` `/enemy` `/audit` `/debrief` `/terrain` `/negotiate` `/suntzu` `/help`

Every executive decision has a geometry. Most executives never see it. The Sun Tzu Lens applies 2,500 years of strategic logic to the specific terrain in front of you, grounded in what is happening in the world today (not in a textbook).

Seven modes. Each applies a different dimension of Sun Tzu's intelligence to your situation. The skill searches the web before every response, finding real-world parallels that mirror your decision.

**The seven modes:**

| Command | Mode | What it does |
|---------|------|-------------|
| `/warcouncil` | The War Council | Bring any strategic decision. Get the relevant chapter, a verdict, the question you are not asking, and one move for this week. |
| `/lens` | Strategic Analysis | Paste a document. See what it reveals beneath the surface. |
| `/enemy` | Enemy's Eyes | See your position from your opponent's perspective. |
| `/audit` | Five Factors Audit | Score your readiness before committing resources. |
| `/debrief` | General's Debrief | Analyze a failure. Find the principle that was violated. |
| `/terrain` | Terrain Map | Map new territory before entering it. |
| `/negotiate` | Negotiation Table | Enter a negotiation with Sun Tzu's counsel. |

**Installation:** Copy `skills/the-sun-tzu-lens/SKILL.md` and the `references/` folder into your Claude Project's knowledge base.

For the full story behind this skill, see the [skill's README](skills/the-sun-tzu-lens/README.md).

---

## How to Use These Skills

**For Claude Projects (claude.ai):**
1. Open or create a Claude Project
2. Navigate to the skill folder you want
3. Add the `SKILL.md` file (and any `references/` folder) to your project's knowledge base
4. Start using the skill's commands

**For Claude Cowork:**
1. Drop the skill folder into your Cowork skills directory
2. The skill activates automatically based on trigger phrases

Each skill is self-contained. No dependencies between them. Install one or all.

---

## Adding a New Skill

When adding a new skill to this repo:

1. Create a folder under `skills/` with a lowercase, hyphenated name
2. Include at minimum a `SKILL.md` with proper frontmatter (name, description)
3. Add a `README.md` if the skill needs explanation beyond the SKILL.md
4. Place any reference files in a `references/` subfolder
5. Update this README: add a row to the **Skills Catalog** table and a new section under **Skill Showcase**

See any existing skill folder for the expected structure.

---

## About CAIO

CAIO helps executives and corporate teams move beyond basic AI tool usage to strategic AI collaboration. Not tool training. Capability building.

**Core philosophy:** AI is an intelligence to communicate with, not a tool to operate.

Visit [wearecaio.com](https://wearecaio.com) or connect with [Stefanos on LinkedIn](https://www.linkedin.com/in/stefanoskaragos/).

---

*Built by Stefanos Karagos | [CAIO](https://wearecaio.com)*
