---
description: Build a content plan and two-week posting schedule
argument-hint:
- optional: current projects
- upcoming work
- or time period
---

Before drafting: is this for Profanity Creative or for CFC (the YouTube channel)? If CFC, do not name "Profanity Creative", say "my studio." If unclear, ask.

The user wants to plan social media content. Invoke the social-media-manager skill and operate in MODE 2 — CONTENT PLANNING.

Context provided: $ARGUMENTS

Deliver:
- Content pillars (3–4 types of content Profanity should rotate through, tied to real studio activity)
- A two-week posting schedule with specific post ideas mapped to days
- A content bank of 8–10 evergreen post ideas Mark can pull from when busy
- Upcoming seasonal or industry hooks worth tapping in the next 4–6 weeks

If the user has provided context about current or upcoming projects, work those into the schedule as concrete post ideas. If no context was provided, ask what's currently on the bench before building the plan.

Format the two-week schedule as a table. Keep everything actionable, this is a plan Mark can actually use, not a strategy doc.

**Save option**: If Mark says `/plan --save` or similar, write the resulting two-week schedule to a markdown file at the workspace root: `content-calendar-YYYY-MM-DD.md` (use today's date). Include columns for date, brand (Profanity/CFC), platform, slot description, and status (draft/scheduled/posted). Default to NOT saving if not requested.
