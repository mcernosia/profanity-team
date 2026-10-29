---
description: Generate a client-ready proposal for a Profanity project
argument-hint:
- client brief or project description
- or "revise <client/project>: what to change"
---

# /proposal

Generate a client-ready proposal for a Profanity Creative project using the Fireflies → `generate_proposal.py` workflow.

## Pick the mode first

- **New proposal**: no earlier proposal exists for this client and project. Follow "The actual workflow" below.
- **Revise**: Mark says revise, update, v2, change the price, swap an option, or there's already a `{CLIENT_CODE}_{Project_Code}_Proposal_*.pdf` in the workspace for this job. Follow "Revise mode." Never rebuild a revision from Fireflies.

If it's unclear whether this is a new job or a revision of an existing one, list the matching proposals you found and ask.

## The actual workflow (do NOT freelance this)

1. **Search Fireflies** for the relevant client call transcript (use the most recent call with the project's primary contact, or whichever call established scope). Pull: project name, deliverables discussed, timeline, budget signals, decision-makers and roles.

2. **Extract scope** from the transcript:
   - Client name and project name
   - Primary contact name + role + email
   - Deliverable list (specific videos, formats, ratios, frames)
   - Timeline (kickoff, key milestones, delivery)
   - Pricing total + payment terms

3. **Update the `PROJECT` dict** in the workspace-root `generate_proposal.py` script with the extracted info. Read the file first to see the current schema; don't guess field names.

4. **Run the script via bash**:
   ```
   cd /Users/markc/Library/CloudStorage/Dropbox/Claude_Projects/PROFANITY
   python3 generate_proposal.py
   ```

5. **Confirm output**: a branded 2-page proposal PDF (sections 01–04 on page 1, Investment Options and Terms on page 2) plus a `_preview.html` should drop in the workspace folder. Verify it rendered correctly.

6. **Snapshot the data**: write the exact `PROJECT` dict you ran as JSON next to the PDF, using the same base name: `{CLIENT_CODE}_{Project_Code}_Proposal_{MMDDYY}.project.json`. The script keeps only one `PROJECT` dict and every new proposal overwrites it, so this snapshot is the only way a later revision can start from the real data.

7. Tell Mark the proposal is ready for review.

## Revise mode

1. **Find the latest version**: list `{CLIENT_CODE}_{Project_Code}_Proposal_*.pdf` in the workspace and take the newest date stamp.
2. **Load its data**, in this order:
   a. its `.project.json` snapshot, if there is one;
   b. otherwise, if the `PROJECT` dict currently in `generate_proposal.py` has the same `client_code` and `project_code`, use that;
   c. otherwise, rebuild the dict from that version's `_preview.html` (it holds every field as rendered). Tell Mark it was rebuilt from the preview.
3. **Change only what Mark asked for.** Leave every other field exactly as it is, including wording he didn't mention. If a change knocks on to something else (a price change affects the "all options" total, a date change affects the deadline or terms), make that follow-on change too and call it out.
4. **Re-stamp**: set `date` to today. The filename picks up the new MMDDYY automatically. Never overwrite the earlier PDF. If a version with today's stamp already exists, tell Mark before you replace it.
5. **Run, verify and snapshot** as in steps 4–6 above.
6. **Report a change list**: the old value → the new value for each change, plus a fresh math check on every price and total. Keep it short.

Revisions skip the full Dusty pass unless new copy was written. Any new or rewritten sentence still gets the anti-AI checklist.

## When the script doesn't fit

If the project is structurally weird (multi-phase, retainer, hybrid scope) and the 2-page format genuinely can't hold it, flag that for Mark and offer to draft a structured Word/markdown proposal instead. But default to the script — it exists because Mark wanted proposals consistent and fast.

## Before sending (whether script-generated or freeform)

- Run the result through Dusty's voice-check (/edit-voice) — proposals are the highest-stakes Profanity copy a client sees.
- Verify pricing math.
- Confirm contact info is current (`mark@profanity.tv | (530) 906-9596`).
- The proposal goes to Mark for review. He sends, you don't.
