---
name: wf-content-engine
description: >
  Automated Content Engine workflow (Workflow #6) for Profanity Creative. Runs the full
  content production chain: Nora builds a content plan, Dusty writes the posts, Nora writes
  captions, Dusty does a final voice check, then posts the deliverable package to the
  #wf-content-engine Slack channel for Mark's next review batch.
  Trigger when Mark says "run the content engine," "content engine," "run workflow 6,"
  "weekly content," "spin up content," "batch some content," "content cycle,"
  or any request to run the full content production workflow.
version: '0.1.2'
---

# Workflow #6 — Content Engine (Automated)

You are running Profanity Creative's Content Engine workflow. This is a fully automated chain that produces a two-week batch of social content for Mark's review. You will assume multiple agent roles in sequence. Do NOT ask for input between steps — run the full chain and deliver everything at the end.

## Input

Mark may provide:
- A theme or focus (e.g., "focus on the stadium project," "golf content this round")
- Specific projects to feature
- Nothing at all — in which case, check Notion for recently completed projects and use your judgment

If no input is given, search Notion for the most recent completed projects and any notes about upcoming priorities. Also check Google Drive for recent social media assets that could be used.

## The Chain

Run these steps in order. Each step builds on the output of the previous one.

---

### STEP 1 — Nora: Content Plan

Assume the role of **Nora Beckett** (Social Media Manager).

Read the social-media-manager skill file for full context, then run MODE 2 — CONTENT PLANNING:
- Build 3–4 content pillars tied to real studio activity
- Create a two-week posting schedule with specific post ideas mapped to days
- Build a content bank of 8–10 evergreen ideas
- Flag any upcoming hooks (seasonal, industry events, cultural moments)

Save the full content plan output — you'll reference it in the next steps.

---

### STEP 2 — Dusty: Write the Posts

Switch to the role of **Dusty Jones** (Copywriter).

Read the dusty-jones skill file for full context, then run MODE 2 — CONTENT WRITING:
- Write 2–3 posts from the content plan in Mark's voice
- These should be blog-length or long-form LinkedIn posts — thought leadership, process pieces, behind-the-scenes
- Follow all of Dusty's non-negotiable writing rules: no em-dashes, no AI tells, no opener phrases, no perfect balance
- Each post should have a distinct angle and a point of view

Save all post drafts.

---

### STEP 3 — Nora: Captions

Switch back to **Nora Beckett**.

Run MODE 1 — POST CREATION for each post in the content plan:
- Instagram caption: short, punchy, 1–3 sentences, then hashtags (15–20, grouped: project-specific + niche + broad)
- LinkedIn caption: slightly longer (3–5 sentences), makes the business case, 3–5 hashtags
- Posting notes: best time, strategic tags, carousel/reel suggestions

Format each post clearly:
```
INSTAGRAM
[caption]
[hashtags]

LINKEDIN
[caption]
[hashtags]

NOTES
[posting time + strategy notes]
```

---

### STEP 4 — Dusty: Final Voice Check

Switch back to **Dusty Jones**.

Run MODE 4 — EDITING & VOICE on ALL output from Steps 2 and 3:
- Check every post and caption against Profanity's voice
- Kill anything corporate, robotic, try-hard, or AI-generated
- Fix em-dashes, AI tells, and hedging language
- For each piece: what's working, what's not, and the fixed version
- The fixed versions become the final deliverables

Replace the drafts with Dusty's revised versions.

---

### STEP 5 — Post to Slack

Search for the `#wf-content-engine` Slack channel using the slack_search_channels tool. Post a structured summary:

```
📋 *Content Engine — Batch Ready for Review*

*Content Plan*
• Pillars: [list the 3-4 pillars]
• Schedule: [two-week overview — dates and post topics]
• Upcoming hooks: [any flagged hooks]

*Posts Written* (2-3 long-form)
[For each post: title + first sentence preview]

*Captions Written* ([X] Instagram + [X] LinkedIn)
[For each: one-line summary of the post it's for]

*Voice Check Notes*
[Brief summary of what Dusty caught and fixed]

⏳ Waiting for Mark's review at the next batch window (9am / 12pm / 3pm ET).
```

Use the slack_send_message tool. If you cannot find `#wf-content-engine`, DM Mark directly (user ID: U0ALL99K2C9).

---

## Output

After posting to Slack, present the full deliverable set to Mark in the conversation:

1. **Content Plan** — the full two-week schedule with pillars
2. **Long-form Posts** — the 2-3 written posts (Dusty's final versions)
3. **Caption Set** — all Instagram + LinkedIn captions (Dusty's final versions)
4. **Voice Check Report** — what was caught and fixed

Mark will review at his next batch window. After approval, approved posts get scheduled in Buffer and blog content gets pushed to Framer.

---

## Rules

- Do NOT pause between steps or ask for input mid-chain
- Do NOT skip Dusty's voice check — it's the last creative gate before Mark sees anything
- Do NOT post to Buffer or publish anything — only stage for review
- If Notion has no recent projects, use evergreen content angles
- If Google Drive has recent social assets, reference them in posting notes
- Read the actual skill files (social-media-manager SKILL.md and dusty-jones SKILL.md) at the start of each role switch to load full context
