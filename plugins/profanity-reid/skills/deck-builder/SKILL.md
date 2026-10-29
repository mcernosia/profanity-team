---
name: deck-builder
description: >
  Build presentation decks in Profanity Creative's signature visual style. Use this skill when Mark
  says "build me a deck," "make a presentation," "put together slides," "treatment deck," "pitch deck,"
  "capabilities deck," "project deck," "case study deck," or any request involving creating a .pptx
  file for Profanity Creative or its clients. Also trigger for "deck for [brand]," "slides for [project],"
  or "presentation for [meeting]." This skill handles all deck types: animation treatments, pitch decks,
  project proposals, case studies, capabilities presentations, and client-facing creative decks.
version: 0.3.0
---

# Deck Builder — Profanity Creative

You build presentation decks that look like they came from Profanity Creative's studio, not from a template library. Every deck follows the Profanity design system: dark, confident, minimal, and unmistakably intentional.

**Before you build anything:** Read the design system reference at `references/design-system.md` and locate the PPTX skill at runtime by globbing for `**/pptx/SKILL.md` in the available skills folders (plus its `pptxgenjs.md` sub-doc). The design system is your visual bible. The PPTX skill is your build toolchain.

---

## MODE DETECTION

Read the request and identify the deck type. Don't ask. Just build.

| Trigger phrases | Deck Type |
|-----------------|-----------|
| "treatment deck," "animation treatment," "creative directions," "visual directions for" | TREATMENT DECK |
| "pitch deck," "capabilities deck," "about us deck," "who we are" | PITCH / CAPABILITIES DECK |
| "proposal deck," "project proposal," "quote deck" | PROPOSAL DECK |
| "case study deck," "project showcase," "portfolio deck" | CASE STUDY DECK |
| "build me a deck," "make a presentation," "slides for" (generic) | GENERAL DECK — ask one clarifying question about content, then build |

---

## DESIGN SYSTEM — NON-NEGOTIABLES

These rules apply to every slide, every deck, no exceptions. Full details in `references/design-system.md`.

### Color Palette

| Role | Hex | Usage |
|------|-----|-------|
| Background | `000000` | Every slide. Pure black. No exceptions. |
| Primary text | `FFFFFF` | Headlines, titles, body copy |
| Accent | `0ABAB5` | Section headers, subtitle text, key phrases, the teal that defines Profanity |
| Muted | `808080` | Dates, metadata, captions, secondary info |
| Overlay | `000000` at 85% opacity | Black bar behind text on image-heavy slides |

### Typography Hierarchy

| Element | Font | Weight | Size | Color | Case |
|---------|------|--------|------|-------|------|
| Slide title (hero) | Hanson | Bold | 54-72pt | `FFFFFF` | UPPERCASE |
| Section header | Hanson | Bold | 36-44pt | `FFFFFF` | UPPERCASE |
| Content header | Arial | Bold | 28-36pt | `0ABAB5` | Title Case |
| Body text | Azeret Mono | Regular | 14-16pt | `FFFFFF` | Sentence case |
| Metadata/date | Azeret Mono | Regular | 12pt | `808080` | UPPERCASE |
| Contact info | Azeret Mono | Regular | 11pt | `808080` | Normal |

### Layout Rules

- **Widescreen only.** 16:9 (10" x 5.625"). Always.
- **Left-aligned everything.** Text starts at x: 1.3". Never center body text.
- **Generous margins.** 1.3" left, 0.7" right, 0.7" top minimum.
- **Breathing room everywhere.** If it feels tight, it's wrong. Add space.
- **Image grids:** 3 images in a row, equal size, evenly spaced. Images sit in the lower 60% of the slide. Header and description live in the upper portion.
- **No decorative lines under titles.** No accent bars. No gradients. The black does the work.
- **Profanity mark:** Small circle-slash icon in bottom-right corner of every slide (except title slide where it's larger or omitted).

### Slide Types

**1. Title Slide**
- "PROFANITY" wordmark top-left (small, 14pt, tracked out)
- Client/project name massive below it (54-72pt, white, uppercase, Hanson)
- Subtitle in teal below that (20-24pt, uppercase)
- Thin white horizontal line as a divider
- Date/deck type in muted gray below the line (12pt, Azeret Mono)
- Profanity circle-slash mark bottom-right

**2. Personal Note Slide**
- Big, bold greeting: "HEY [NAME]!" (44-54pt, white, uppercase, Hanson)
- Body text in Azeret Mono (14pt, white), left-aligned
- Conversational tone. This is Mark talking, not a brand.
- Teal used for emphasis on key phrases inline

**3. Section Divider Slide**
- Background: blurred/desaturated product image (if available) or solid black
- Black overlay bar (~25% height) across the middle of the slide
- Section title in white, bold, uppercase (44-54pt) inside the bar
- Subtitle in teal below the title (18-20pt) inside the bar

**4. Concept / Text Slide**
- "CONCEPT" or section name as hero header (44pt, white, uppercase, Hanson)
- 2-3 paragraphs of body text in Azeret Mono (14pt, white)
- Massive negative space below. Don't fill it. The emptiness is intentional.

**5. Image Grid Slide**
- Content header in teal (28-36pt, Title Case, Arial Bold)
- One-line description in white Azeret Mono (14pt) directly below
- 3 square or landscape images in a row, evenly spaced
- Images positioned in lower 55-60% of slide
- Equal gutters between images (~0.3")

**6. Closing Slide**
- "THANK YOU." centered, massive (54-72pt, white, uppercase, Hanson)
- Optional: peace sign or similar gesture below (keep it Profanity)
- Contact info bottom-center in muted gray Azeret Mono (11pt)
- Format: `Mark Cernosia  |  mark@profanity.tv  |  (530) 906-9596`
- Profanity mark bottom-right

---

## BUILD PROCESS

### Step 1: Gather Content

Before building, determine:
- **Who is this for?** (Client name, contact name for greeting)
- **What type of deck?** (Treatment, pitch, proposal, case study)
- **What content goes on each slide?** (Sections, concepts, descriptions)
- **Are there images?** (If user provides images, use them. If not, use placeholder rectangles with a subtle border or skip image slides.)

If Mark provides a brief or raw content, restructure it into the slide framework. Don't ask for clarification unless something critical is missing.

### Step 2: Plan the Slide Sequence

Every Profanity deck follows this rhythm:

**Treatment Deck:**
1. Title slide (Profanity + client + project + date)
2. Personal note to client
3. For each treatment direction:
   - Section divider (treatment name + number)
   - Concept text slide
   - 2-4 image grid slides (one per visual theme)
4. Closing slide

**Pitch / Capabilities Deck:**
1. Title slide
2. Personal note or opening statement
3. Who we are (1 slide)
4. What we do (1-2 slides with image grids)
5. How we work (process, 1 slide)
6. Selected work (2-4 image grid slides)
7. Closing slide

**Proposal Deck:**
1. Title slide
2. Personal note
3. Project understanding (concept slide)
4. Scope overview (concept slide)
5. Visual direction (1-2 image grids if applicable)
6. Timeline (concept slide)
7. Investment (concept slide)
8. Closing slide

**Case Study Deck:**
1. Title slide
2. Project overview (concept slide)
3. Challenge / brief (concept slide)
4. Process slides (image grids)
5. Final work (image grids)
6. Results / impact (concept slide)
7. Closing slide

### Step 3: Build with PptxGenJS

Use the PPTX skill's `pptxgenjs.md` guide for all technical implementation. Key setup:

```javascript
const pptxgen = require("pptxgenjs");
let pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.author = "Profanity Creative";
```

**Critical PptxGenJS rules:**
- No `#` in hex colors. `"0ABAB5"` not `"#0ABAB5"`.
- Never reuse option objects between calls (PptxGenJS mutates them).
- Use `breakLine: true` between text array items.
- Set `margin: 0` on text boxes when aligning with shapes.
- Use `charSpacing` for tracked-out text (not `letterSpacing`).

### Step 4: QA

Follow the PPTX skill's QA process exactly:
1. Extract text with `python -m markitdown output.pptx`
2. Convert to images with `soffice` + `pdftoppm`
3. **Use a subagent for visual inspection** — you've been staring at the code and will see what you expect, not what's there
4. Fix issues and re-verify

---

## VOICE IN DECKS

All text in Profanity decks follows the studio voice:
- **Confident, not arrogant.** State things directly.
- **Specific, not generic.** "3D product film for the FT-One Ultra-Lite" not "immersive brand content."
- **No AI tells.** No em-dashes. No "delve into." No "seamlessly." No "leverage." Read the voice guide.
- **Short, punchy descriptions.** Image grid captions are one line. Concept paragraphs are 2-3 sentences max.
- **Conversational where personal.** The "Hey [Name]!" slide sounds like Mark, not a brand.

---

## REFERENCE FILES

- `references/design-system.md` — Full color, typography, spacing, and layout specs extracted from Profanity's actual decks
- PPTX build toolchain — locate at runtime via `Glob` for `**/pptx/SKILL.md` in the available skills folders
- PptxGenJS API reference — locate at runtime via `Glob` for `**/pptx/pptxgenjs.md` in the same folder as the PPTX skill
- Profanity voice and tone guide — locate at runtime via `Glob` for `**/profanity-dusty/**/voice-guide.md`
