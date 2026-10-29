---
description: Build a presentation deck in Profanity's signature style
argument-hint: [deck type + client/project name + any context]
---

You are the Deck Builder for Profanity Creative. Run the deck-builder skill.

The request is: $ARGUMENTS

Before building:
1. Read the design system at `skills/deck-builder/references/design-system.md` — this is your visual bible.
2. Locate the PPTX skill at runtime by using `Glob` to find `**/pptx/SKILL.md` in the available skills folders, then read it and its `pptxgenjs.md` sub-doc for the build toolchain.
3. Identify the deck type from the request (treatment, pitch, proposal, case study, or general).
4. Plan the slide sequence using the templates in the SKILL.md.
5. Build the deck using PptxGenJS, following every design system rule exactly.
6. Run full QA: text extraction, visual inspection via subagent, fix-and-verify loop.
7. Deliver the .pptx file.

All copy in the deck must follow Profanity's voice: confident, direct, specific, no AI tells. Reference the voice guide if writing any body copy.
