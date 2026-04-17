# AI Skills by CAIO Group

Custom AI skills built by [Stefanos Karagos](https://www.linkedin.com/in/karagos/), Lead Instructor & Senior GenAI Consultant at [CAIO Group](https://wearecaio.com).

These are production-grade skills designed for Claude Projects and Claude Cowork. Each one encodes a specific workflow, methodology, or thinking framework that turns Claude into a specialized operator for a defined task.

Not prompts. Not templates. Operational intelligence.

---

## Skills Catalog

| Skill | Description | Type |
|-------|-------------|------|
| [Handoff by CAIO](skills/handoff-by-caio/) | Move any Claude conversation to a new chat with zero re-explanation. Generates a structured handoff file with full context, classified artifacts, and a paste-ready resume prompt. | Workflow |
| [The Sun Tzu Lens](skills/the-sun-tzu-lens/) | Strategic intelligence layer for executives. Applies Sun Tzu's 13-chapter framework to real business decisions with live web research. Seven modes including War Council, Enemy's Eyes, and Negotiation Table. | Strategy |
| [LinkedIn Carousel](skills/linkedin-carousel/) | Turn any text, URL, or document into an on-brand LinkedIn carousel PDF. Four templates (executive-minimal, training-breakdown, quote-forward, mobile-optimized). Fully brandable via one YAML file. | Content |

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

**Files needed:** `SKILL.md` only. See [How to Install](#how-to-install-a-skill) below.

---

### The Sun Tzu Lens

**Category:** Executive Strategy
**Triggers:** `war council:` `strategic lens:` `enemy's eyes:` `audit:` `debrief:` `terrain:` `negotiate:` `sun tzu:` or type **"sun tzu help"** for the full command reference

Every executive decision has a geometry. Most executives never see it. The Sun Tzu Lens applies 2,500 years of strategic logic to the specific terrain in front of you, grounded in what is happening in the world today (not in a textbook).

Seven modes. Each applies a different dimension of Sun Tzu's intelligence to your situation. The skill searches the web before every response, finding real-world parallels that mirror your decision.

**The seven modes:**

| Type this | Mode | What it does |
|-----------|------|-------------|
| `war council:` | The War Council | Bring any strategic decision. Get the relevant chapter, a verdict, the question you are not asking, and one move for this week. |
| `strategic lens:` | Strategic Analysis | Paste a document. See what it reveals beneath the surface. |
| `enemy's eyes:` | Enemy's Eyes | See your position from your opponent's perspective. |
| `audit:` | Five Factors Audit | Score your readiness before committing resources. |
| `debrief:` | General's Debrief | Analyze a failure. Find the principle that was violated. |
| `terrain:` | Terrain Map | Map new territory before entering it. |
| `negotiate:` | Negotiation Table | Enter a negotiation with Sun Tzu's counsel. |

**Files needed:** `SKILL.md` + the `references/` folder. See [How to Install](#how-to-install-a-skill) below.

For the full story behind this skill, see the [skill's README](skills/the-sun-tzu-lens/README.md).

---

### LinkedIn Carousel

**Category:** Content Production
**Trigger:** "make a LinkedIn carousel about X" or "turn this article into a carousel"

LinkedIn rewards carousels. Multi-slide posts get roughly 3x the dwell time of plain text updates, and the algorithm keeps resurfacing them for days. Building one from scratch every time is the reason most people never publish them.

This skill turns a topic, an article, or an uploaded document into a 7-slide carousel PDF (1080x1350, LinkedIn's preferred aspect ratio). Four layout templates cover the most common use cases. All four read from a single `brand-config.yaml` file: change your color, fonts, and footer once, and every future carousel matches.

**The four templates:**

| Template | When to use it |
|----------|----------------|
| `executive-minimal` | Strategic takes, leadership posts, opinion pieces |
| `training-breakdown` | Step-by-step frameworks, numbered methodologies, teaching content |
| `quote-forward` | Big-idea posts, manifestos, punchy declarative content |
| `mobile-optimized` | Maximum-readability posts for phone-first feeds |

**What it produces:** a ready-to-upload PDF with a cover hook, 3-5 body slides, a takeaway, and a CTA slide. Your headshot appears on the CTA (or your initials on a colored circle if no headshot is uploaded).

**Design rules enforced at render time:** no em dashes, no AI filler phrases ("delve," "leverage," "landscape," "navigate"), no hedging words. Executive copy that reads naturally out loud.

**Files needed:** the full `skills/linkedin-carousel/` folder, plus `playwright`, `jinja2`, and `pyyaml` installed. One-line setup command is in the [skill's README](skills/linkedin-carousel/README.md).

**One-click install for Cowork users:** download [`releases/linkedin-carousel.plugin`](releases/linkedin-carousel.plugin) and drop it into Claude Desktop under **Customize > Skills > Upload a skill**.

---

## How to Install a Skill

Each skill is self-contained. Pick the one you want, follow the steps for your setup, and you're ready to go.

### Option 1: Claude.ai (Projects)

This works for anyone with a Claude Pro, Team, or Enterprise account.

1. Go to [claude.ai](https://claude.ai) and open an existing **Project** (or create a new one)
2. Click the **Project Knowledge** section (the area where you add files and instructions)
3. Download the skill's `SKILL.md` file from this repo. If the skill has a `references/` folder, download those files too
4. Upload all the files into your Project Knowledge
5. Start a new conversation inside that Project and use the skill's commands

That's it. The skill is now active in every conversation within that Project.

### Option 2: Claude Cowork (Desktop App)

Cowork lets you install skills as uploadable ZIP files or pre-built `.plugin` bundles.

**Fastest path (if a `.plugin` file is available):**

1. Check the `releases/` folder in this repo (e.g., `releases/linkedin-carousel.plugin`)
2. Download the `.plugin` file
3. Open Claude Desktop, switch to **Cowork**
4. Go to **Customize > Skills**, click **"+"** then **"Upload a skill"**
5. Select the `.plugin` file. Toggle it on.

**Manual path (any skill in this repo):**

1. Download the skill folder from this repo (e.g., `skills/handoff-by-caio/`)
2. **Package it as a ZIP file.** The ZIP must contain the skill folder at its root:
   ```
   handoff-by-caio.zip
   └── handoff-by-caio/
       ├── SKILL.md
       └── (any other files)
   ```
3. Open the Claude Desktop app and switch to **Cowork**
4. Go to **Customize > Skills** in the left sidebar
5. Click **"+"** then **"Upload a skill"**
6. Select your ZIP file
7. The skill appears in your Skills list. Toggle it on.

**Prerequisite:** Make sure **Code execution and file creation** is enabled in Settings > Capabilities.

### Option 3: Claude Code (CLI)

For developers using Claude Code in the terminal:

1. Clone this repo or download the skill folder you want
2. Copy the skill folder into your project's `.claude/skills/` directory:
   ```bash
   cp -r skills/the-sun-tzu-lens .claude/skills/
   ```
3. Claude Code picks it up automatically on the next conversation

### Quick Download Tip

To grab a single skill folder without cloning the whole repo, you can use the GitHub web interface: navigate to the skill folder, click the three-dot menu (or use "Download directory" browser extensions), and download just that folder.

---

## About CAIO Group

CAIO Group helps executives and corporate teams move beyond basic AI tool usage to strategic AI collaboration. Not tool training. Capability building.

**Core philosophy:** AI is an intelligence to communicate with, not a tool to operate.

Visit [wearecaio.com](https://wearecaio.com) or connect with [Stefanos on LinkedIn](https://www.linkedin.com/in/karagos/).

---

*Built by Stefanos Karagos | [CAIO](https://wearecaio.com)*
