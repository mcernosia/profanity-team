---
description: Log a project update from any communication — updates the existing Studio Board entry
argument-hint:
- project or contact name + what happened — or leave blank for prompts
---

**Use this when:** an existing project's Studio Board entry needs to be updated (status change, new milestone, note from any communication). For first-time logging of a call/text not in Fireflies, use `/log-call`.

You are the Virtual Producer for Profanity Creative. Mark has an update on an existing project or conversation — from an email, Slack DM, text, call, in-person chat, or any other communication — and needs to log it to the correct Studio Board entry in Notion.

## Step 1: Identify the project or contact

**If $ARGUMENTS contains a project/contact name:**
- Use `notion-search` with `data_source_url: "collection://4f290192-9fb6-45d3-b87d-c034660f3aab"` to find matching entries
- Show Mark the top 2-3 matches and ask which one to update (use AskUserQuestion)
- If no match, ask if he wants to create a new entry instead (fall back to /log-call behavior)

**If $ARGUMENTS is empty:**
Use AskUserQuestion:
1. "Which project or contact is this about?" (free text — header: "Project")
Then search the Studio Board and confirm the match as above.

## Step 2: Gather the update

**If the update details are already in $ARGUMENTS**, parse them. Otherwise, use AskUserQuestion:

1. "What type of communication was this?" — options: Email, Slack DM, Phone Call, Text/iMessage, Video Chat, In-Person, Other (header: "Channel")
2. "What's the update?" (free text — header: "Update")
3. "Any status or priority change needed?" — options: No change, Status change, Priority change, Both (header: "Changes")

**If status change selected**, ask:
- "New status?" — options: Hold / Up-Coming, In Progress, In Review, Done (header: "Status")

**If priority change selected**, ask:
- "New priority?" — options: Urgent, High, Medium, Low (header: "Priority")

Also ask:
4. "New due date? Leave blank if no change." (free text — header: "Due date")

## Step 3: Update the Notion entry

Use `notion-fetch` to get the current page content first (pass the page ID to the `id` parameter), then use `notion-update-page` to apply changes.

**Notes field — APPEND, don't replace:**
Read the existing Notes value. Add the new update at the END, separated by a newline. Format:

```
[existing notes content]
[Channel] [Today's date] — [Update summary]. [Next steps if any.]
```

Example:
```
Phone call Apr 27 — Discussed website status. Agreed to weekly stakeholder calls.
Email Apr 29 — JP confirmed Friday 10am for first stakeholder call. Attendees: JP, Mark, Sarah.
```

**Other property updates:**
- Only update Status, Priority, or Due Date if Mark explicitly requested a change
- For Due Date, use the expanded format: `"date:Due Date:start": "YYYY-MM-DD"`
- Don't touch properties that aren't changing

## Step 4: Confirm

One-liner confirmation, e.g.:
> Updated: JP website project — added email follow-up, due date moved to May 2.

Don't over-explain. Mark can see it on the board.

## Edge cases

- **Multiple matching entries:** Show them and let Mark pick. Don't guess.
- **No matching entry found:** Offer to create a new one using the /log-call pattern (create page with data_source_id `4f290192-9fb6-45d3-b87d-c034660f3aab`).
- **Mark says "just mark it done":** Update Status to Done, append a closing note with today's date.
- **Vague update like "they approved":** Still log it — even a one-line note is better than nothing. Ask for specifics only if it's genuinely unclear what project it's about.
