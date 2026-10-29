# Moodboard output: Claude Design

Claude Design builds the board from a single pasted prompt. The prompt has to stand on its own: Claude Design hasn't seen the brief, the call or the rest of Kai's thinking. Model: `FALL_Climbers_Moodboard_Brief_ClaudeDesign_100526.md` in the workspace ("Gaff and Graphite"). Read it if you can reach the workspace.

## File

Save as `{CLIENT_CODE}_{Project}_Moodboard_Brief_ClaudeDesign_{MMDDYY}.md` in the workspace root. Open it with one line: "Prepared {date} by Kai. Paste the 'Paste into Claude Design' block at the bottom as the prompt. Everything above it is the thinking behind it."

## Sections, in order

1. The standard moodboard brief (Board Title, Core Tension, Image Search Directions, Color Palette Direction, What Does NOT Belong).
2. **How the references map to the sequence** (only when there's a sequence or film): a table of beat | reference (title + URL) | what to borrow. Only list references you actually found and opened. If you could read a page but not watch the video, say so in one line and tell Mark he needs to pull the stills and note timestamps.
3. **Paste into Claude Design**: the prompt block, written to the rules below.

## Rules for the paste block

- **Plain prose, no markdown headers.** Written to Claude Design in second person, as an instruction.
- **First line:** what the board is for, in plain words a stranger understands ("a product film about utility pole climbers (spiked boots lineworkers use)"), then `Title: "<Board Title>"` and the canvas (default: one 16:9 canvas).
- **Concept:** 2-3 sentences on the story or idea and the core tension the board has to hold.
- **Layout:** name the columns or zones left to right, matching the beats or pillars, with 3-4 image tiles under each. Tiles are clearly labeled placeholders for Mark's own stills. Claude Design shouldn't invent or source photos of real products.
- **Palette strip:** a numbered list of the 4-6 palette colors, using the same real-world names as the brief. No hex codes, so Claude Design matches the description, not a guess.
- **Style:** background, type color, at most one accent and where it's allowed, plus what to avoid in the board's own styling (gradients, glow, UI chrome). The board's styling should serve the mood, never compete with it.
- **"Does not belong" list:** a compressed version of the brief's list.
- **Last line, always:** "Keep it presentable to a client's executives. No logos or brand names on the board itself." Drop the second sentence only if Mark says the client's brand belongs on the board.
- Keep the block under ~300 words. Run the anti-AI checklist on it like any other copy.

## Figma

If Mark asks for Figma instead (or as well), follow the Figma steps in `commands/moodboard.md`. The brief sections stay the same. Only the paste block changes.
