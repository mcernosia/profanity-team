# Post-Mortem Format (standard, every time)

Set 2026-10-01 from the Lochinvar Regent and Type One Bull Run post-mortems. Every post-mortem uses this structure, this voice, this look, and this destination.

## Destination: Google Drive, not chat

- Folder: **Post-Mortems** (Google Drive, My Drive root). Folder ID: `1dS3pqg5piqEkMoQrLksDJnZOZN-sWAvA`
- File name: `<Project> Post-Mortem`, for example `Type One Bull Run Post-Mortem`. A Google Doc.
- The document never gets pasted into chat. The chat reply is the doc link as a markdown link, plus a few short lines: the one number that matters, anything unexpected, and what is still open. If the folder ID ever fails, search Drive for a folder titled `Post-Mortems` before creating a new one. Never create a second folder.
- Do not build a Claude doc first. Go straight to Drive.

## Process

1. **Gather.** Fireflies, Gmail, Notion, QuickBooks. Gmail rule from CLAUDE.md applies: `search_threads` finds thread IDs only, then `get_thread` on every candidate and read the full message list. Large threads get saved to a file by the tool, so read the file with `jq`, not the snippet. Pull the invoice from QuickBooks for the real send date and balance.
2. **Ask about hours.** Total hours is the one number the files can't show. Ask Mark with a multiple-choice question before drafting. If he doesn't know, write "Hours: not tracked" and say so in Open items. Never invent a figure.
3. **Draft in first person, as Mark.** Run the voice rules below, then Dusty's checklist from `profanity-dusty/skills/dusty-jones/references/voice-guide.md` and Part 4 of `anti-ai-writing-reference.md`. Fix before uploading.
4. **Create the doc.** Drive `create_file` with `contentMimeType: "text/html"`, `parentId` set to the folder ID, `title` set to the file name. Drive converts the HTML into a native Doc.
5. **Brand it.** `read_doc` the new doc. The result is usually too big for chat and gets saved to a file. Run `python3 scripts/gdoc_brand.py <saved read_doc file> > batch.json` (path is relative to this skill folder), then pass its `requests` and `writeControl` to the Docs `update_doc` in one call. The script handles the wrapper object around the read result.
6. **Verify.** `read_file_content` for the text (check the tables came through). `read_doc` again and confirm Azeret Mono everywhere, heading rules, teal table headers. Say plainly that you checked structure and haven't seen the rendered page.
7. **Reply.** Link plus short flags. Offer nothing else unless something is genuinely open.

If the Docs editor connector is off, the doc still gets created unbranded. Tell Mark to turn the connector on, then brand the same file. Never create a second copy to get around it.

## Document structure

Title (H1) `<Project> Post-Mortem`, then the date as plain text. Then these sections, in this order, with these exact headings:

| Section | Content |
|---|---|
| Snapshot | One lead sentence with the outcome. Table `Item / Detail` with rows: Client (names and roles, end client), Project, Scope, Fee (amount, how it was agreed, invoice number, sent and paid dates), Delivered (dated), Hours |
| Timeline | One lead sentence. Table `Date / What happened`, one row per dated event, oldest first |
| What went well | One lead sentence, then 3 to 6 bullets. Each bullet is a specific thing with a date or number |
| What went wrong | One lead sentence, then bullets. Be honest, name my own misses |
| Pricing and scope | Lead sentence with the effective hourly rate and per-day rate and the gap to the $15K minimum. Table `Number / Where it came from`. Then short paragraphs: break-even hours against $900/day, the pattern across jobs for the same client, the cost that doesn't show in hours |
| What changes next time | One lead sentence, then a numbered list of concrete rules, not platitudes |
| Open items | One lead sentence, then bullets of what only Mark can fill: exact hours, unconfirmed dates, calls with no transcript, whether the work can be shown publicly |

Optional, only when it applies: a **Specialist notes** section if outside collaborators were used, and a **Client relationship** section (repeat potential, retainer candidate, red flags, upsell) when Mark asks for it. The client close-out email and the portfolio handoff are not part of the doc. Produce them only when asked or when the post-mortem pipeline calls for them.

## Math, every time

- Hourly rate = fee / hours. Day rate = hourly x 8.
- Break-even hours against the $900/day freelance rate = fee / 900 x 8.
- Gap to minimum = $15,000 minus fee, when the fee is under it.
- Same client, repeat pattern: add the fees, add the hours, state the worst-case blended hourly rate.
- Show only numbers you can source. Mark estimates as estimates.

## Voice

- First person, Mark talking about his own studio's job. Never "Mark did." Never talk to Mark inside the doc ("for you to edit", "your notes").
- No automation jargon: no "board", "sync", "canonical", "TBD", "per the note of". Say "my tracker" if the tracker matters.
- No em-dashes anywhere. Ranges use en-dashes (7/22–23, $4,500–$5,000). Dates as 8/5, times as 5:04pm.
- No "not X but Y", no mandatory triplets, no bold labels that restate their sentence, no summary closer.
- Specific over adjective. A line of dry humor is fine when the record supports it (quote Mark's own email when it's good).
- Anything unconfirmed is stated as unconfirmed in plain words, then listed under Open items.

## HTML conventions for the upload

`<h1>` title, `<p>` date, `<h2>` sections, `<table border="1">` with a `<th>` header row, `<ul>` and `<ol>` for lists, literal en-dash characters. No inline styles: the brand script handles all styling afterward.

## The look (Profanity branding)

Applied by `scripts/gdoc_brand.py` from `brand-reference.md` in the workspace root:

- Azeret Mono for everything, near-black `#1A1A1A`
- Title and headings bold, each with a teal `#0ABAB5` rule underneath, keep-with-next on
- Date line gray `#808080`
- Tables: thin gray borders, teal header row, bold header text
- White page

Not applied: the logo (the asset is a white wordmark, so it needs a dark header band, and Docs can only insert an image from a public URL) and Hanson for headings (not a Google font). If Mark supplies a public logo URL on a dark band, add it above the title.
