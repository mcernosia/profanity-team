# profanity-reid

Reid Calloway — Biz Dev Lead for Profanity Creative.

Helps Mark find, approach, and close the right clients in outdoor, lifestyle, and action sports. Positions Profanity as a strategic creative partner, not a production vendor. Operates in four modes: prospect outreach, pitch preparation, follow-up and pipeline, and positioning strategy.

Now includes the **Deck Builder** — builds presentation decks (treatments, pitches, proposals, case studies) in Profanity's signature dark, minimal visual style using PptxGenJS.

---

## Commands

| Command | What it does |
|---------|-------------|
| `/outreach [brand]` | Writes a personalized, ready-to-send outreach message for a specific brand |
| `/pitch-prep [brand]` | Generates a pre-call brief for an upcoming meeting — brand snapshot, conversation arc, smart questions |
| `/follow-up [context]` | Writes a follow-up message and gives an honest read on deal status |
| `/strategy [question]` | Delivers practical positioning, pricing, or go-to-market advice |
| `/build-deck [type + context]` | Builds a .pptx deck in Profanity's signature style — treatment, pitch, proposal, or case study |

---

## Skills

**reid-biz-dev** — The core biz dev skill. Loads Reid's full persona, all four modes, and general principles. Triggers automatically when you describe a biz dev situation in plain language.

**deck-builder** — Builds presentation decks in the Profanity design system: pure black backgrounds, Hanson + Azeret Mono typography (Impact + Courier New as web-safe fallback when recipients don't have the brand fonts installed), `#0ABAB5` teal accents, image grids, and the Profanity mark. Triggers when you say "build me a deck," "make a presentation," or reference any deck type. **Note:** custom fonts don't embed in `.pptx` natively, so default delivery is PDF.

### Reference Files (loaded on demand)

- **brand-sector-intel.md** — Outdoor, lifestyle, and action sports brand ecosystems
- **pricing-and-positioning.md** — Pricing tiers, anchoring, objection handling
- **outreach-frameworks.md** — Research checklist, OVNQ email framework, follow-up sequencing
- **design-system.md** — Full Profanity deck design system: colors, typography, layout grid, slide type recipes

---

## Usage

You can use commands or just talk naturally:

- `/outreach Burton` — Reid will research Burton and write outreach
- `/pitch-prep Arc'teryx` — Reid will write a pre-call brief
- `/follow-up Cotopaxi — sent proposal 2 weeks ago, no response` — Reid reads the situation and writes the follow-up
- `/strategy how do I get in front of DTC lifestyle brands?` — Reid gives tactical advice
- `/build-deck treatment deck for FallTech Ultra-Lite harness` — Builds a full treatment deck in the Profanity style
- `/build-deck pitch deck for Osprey meeting` — Builds a capabilities/pitch deck
- Or just say: "build me a deck for the Yeti proposal" and it runs automatically

---

## Setup

No external integrations or environment variables required. The deck builder requires the PPTX skill to be available (part of the standard Cowork skill set).

---

## About

Built for Profanity Creative, a lean 3D product visualization studio run by Mark Cernosia out of Burlington, VT. Profanity is repositioning upstream: from production vendor to embedded creative intelligence partner.
