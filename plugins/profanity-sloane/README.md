# Profanity Virtual Producer

A Cowork plugin for Profanity Creative — meet **Sloane Mercer**, your Virtual Producer. She handles the business side of creative work so Mark can stay in the creative.

## What It Does

Sloane handles proposals, project scoping, client communication, internal production documentation, and project post-mortems for Profanity Creative. She understands the studio's pricing model, communication style, and how a lean 3D production shop actually operates.

## Commands

| Command | What it does |
|---------|-------------|
| `/proposal [brief]` | Generates a complete client-ready proposal with 3-tier pricing, scoped deliverables, timeline, and a pre-send checklist |
| `/price-check [deliverable + your numbers]` | Researches live market rates, frames commodity vs. honest comps, checks your tiers, saves a dated pricing-research doc and logs the comps |
| `/scope [description]` | Breaks down a project — deliverables, complexity flags, hour estimates, price range, and questions to ask before committing |
| `/email [situation]` | Drafts a client email in Mark's voice. For difficult conversations, provides both a Soft and Firm version |
| `/brief [project info]` | Creates internal project documentation — project briefs, shot lists, delivery specs, or change orders |
| `/post-mortem [project]` | Runs a project post-mortem and saves it as a branded Google Doc in the Drive folder "Post-Mortems" (never pasted in chat). Close-out email and portfolio handoff on request |

## Skill

The `sloane-producer` skill loads automatically when you describe a business task related to a Profanity project. You can also trigger it by mentioning:

- "write a proposal," "quote this project," "help me pitch this"
- "scope this out," "what should I charge," "is this feasible"
- "write an email," "how do I respond to this," "draft a follow-up"
- "write a brief," "document this project," "create a shot list"
- "run a post-mortem," "project wrap-up," "close out this project," "lessons learned"

## Pricing Defaults

- **Minimum engagement (direct-to-client):** $15,000
- **Standard timeline:** 3–4 weeks
- **Pricing structure:** Always 3-tier (Essentials / Full Production / Premium)
- **Target tier:** Middle option
- Pricing is always presented as a suggested range — final numbers confirmed with Mark before sending

## Reference Files

The skill includes three internal reference documents:

- **Pricing Framework** — 3-tier structure, phase-based hour estimates, add-on pricing, payment terms
- **Studio Context** — Deliverable types and specs, typical project phases, client types, Mark's voice examples
- **Scope Flags** — Common scope creep patterns, red-flag client behaviors, pre-commitment checklist

## Setup

Requires connected MCPs: Notion (project board logging), Fireflies (call transcripts), Gmail (draft client emails — drafts only, never sent). Google Calendar and QuickBooks optional but useful.
