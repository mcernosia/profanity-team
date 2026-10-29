# Notion Guide — Profanity Creative

Master reference for Notion operations via MCP tools. Covers the full Notion data model, CRUD patterns, and studio-specific conventions.

---

## Notion Data Model — Core Concepts

### Workspace
The top-level container. Profanity Creative's workspace holds all pages, databases, and teamspaces. Everything lives here.

### Pages
The fundamental unit in Notion. A page can be:
- A standalone document (notes, SOPs, meeting notes)
- A row in a database (a project entry, a client record)
- A parent page containing child pages or databases

Every page has a **title**, optional **icon** and **cover**, and a body made of **blocks**.

### Databases
Structured collections of pages with typed properties. Think of them as smart spreadsheets where each row is a full page. Databases are the backbone of Profanity's project management.

**Database types by layout/view:**
- **Table** — spreadsheet-like grid (default)
- **Board** — Kanban columns grouped by a select/status property
- **Timeline** — Gantt-style view using date properties
- **Calendar** — entries plotted on a calendar by date
- **List** — minimal text list
- **Gallery** — card grid showing cover images or page content

A single database can have multiple views with different layouts, filters, and sorts.

### Blocks
Every piece of content inside a page is a block. Block types include:
- **Text blocks:** paragraph, heading_1, heading_2, heading_3, bulleted_list_item, numbered_list_item, to_do, toggle, quote, callout, divider
- **Media blocks:** image, video, file, bookmark, embed, pdf
- **Advanced blocks:** code, equation, table_of_contents, breadcrumb, link_to_page, synced_block, column_list, column
- **Database blocks:** child_database (inline database), child_page

Blocks can be nested (indented) to create hierarchy. Toggle blocks and bulleted lists support children.

---

## Properties — The Database Schema

Properties define the columns/fields of a database. Each property has a type that determines what data it holds.

### Core Property Types

| Type | What it stores | Use case |
|---|---|---|
| `title` | Page name (every database has exactly one) | Project name, client name |
| `rich_text` | Formatted text | Descriptions, notes |
| `number` | Numeric value (supports formats: number, percent, dollar, euro, etc.) | Budget, hours, quantities |
| `select` | Single choice from predefined options | Status, priority, category |
| `multi_select` | Multiple choices from predefined options | Tags, skills, deliverables |
| `status` | Built-in status with groups: Not started, In progress, Done | Project status |
| `date` | Date or date range (with optional time) | Deadlines, start/end dates |
| `people` | Notion users | Assigned to, created by |
| `files` | File attachments or external URLs | Assets, deliverables |
| `checkbox` | Boolean true/false | Approval flags, completion |
| `url` | URL | Links to external resources |
| `email` | Email address | Client contact |
| `phone_number` | Phone number | Client contact |

### Computed Property Types

| Type | What it does |
|---|---|
| `formula` | Calculates a value from other properties using Notion's formula language |
| `relation` | Links to pages in another database (or the same one for self-relations) |
| `rollup` | Aggregates data from related pages (sum, count, average, etc.) |
| `created_time` | Auto-set when page is created |
| `created_by` | Auto-set to the user who created the page |
| `last_edited_time` | Auto-updated on any edit |
| `last_edited_by` | Auto-updated to the last editor |
| `unique_id` | Auto-incrementing ID with optional prefix |

### Relations and Rollups

**Relations** link databases together. Example: a Projects database related to a Clients database — each project points to its client.

- **One-way relation:** Project → Client (only Project shows the link)
- **Two-way relation:** Project ↔ Client (both databases show the link)

**Rollups** aggregate data across relations. Example: on the Clients database, roll up "Count of all related Projects" or "Sum of Budget from related Projects."

### Formulas (Notion Formula 2.0)

Notion formulas use a functional syntax. Key functions:

```
// Conditionals
if(prop("Status") == "Done", "✅", "⏳")

// Date math
dateBetween(prop("Deadline"), now(), "days")

// Text
prop("Client") + " — " + prop("Project Name")

// Number formatting
format(prop("Budget")) + " USD"

// Empty checks
empty(prop("Deadline"))

// Contains (for multi-select)
contains(prop("Tags"), "3D")
```

---

## CRUD Operations via Notion MCP

The Notion MCP tools available are:

| Tool | Purpose |
|---|---|
| `notion-search` | Search pages and databases by title |
| `notion-fetch` | Get a page, database, or block by URL or ID |
| `notion-create-pages` | Create new pages (in a database or as children of a page) |
| `notion-create-database` | Create a new database with defined properties |
| `notion-update-page` | Update page properties or archive a page |
| `notion-create-view` | Create a new view on a database |
| `notion-update-view` | Update an existing view's filters, sorts, or layout |
| `notion-get-comments` | Get comments on a page or block |
| `notion-create-comment` | Add a comment to a page |
| `notion-duplicate-page` | Duplicate an existing page |
| `notion-move-pages` | Move pages to a different parent |
| `notion-get-users` | List workspace members |
| `notion-get-teams` | List teamspaces |
| `notion-update-data-source` | Update a database's external data source settings |

### Pattern: Search Before Create

**Always search first** to avoid creating duplicates:

1. Use `notion-search` with the title or keywords
2. If found, use `notion-fetch` to inspect the existing page/database
3. Only create if nothing exists

### Pattern: Creating a Database Page (Project Entry)

To add a new row to the Projects database:

1. Search for the Projects database to get its ID
2. Use `notion-create-pages` with the database as parent
3. Set properties matching the database schema
4. Optionally add child blocks for page body content

### Pattern: Creating a Standalone Page

To create a page under a parent page (not a database):

1. Find or know the parent page ID
2. Use `notion-create-pages` with the parent page
3. Add blocks for content (headings, paragraphs, to-dos, etc.)

### Pattern: Querying / Filtering a Database

Use `notion-fetch` on a database URL to get its contents. For filtered results, use database views:

1. `notion-create-view` with filter conditions
2. Filter syntax follows Notion's filter object structure:
   - Property filters: `equals`, `does_not_equal`, `contains`, `does_not_contain`, `starts_with`, `ends_with`, `is_empty`, `is_not_empty`
   - Date filters: `before`, `after`, `on_or_before`, `on_or_after`, `past_week`, `past_month`, `next_week`, `next_month`
   - Compound filters: `and` / `or` arrays

### Pattern: Updating a Page

1. Get the page ID (via search or fetch)
2. Use `notion-update-page` to modify properties
3. To archive (soft delete): set `archived: true`

### Pattern: Building Rich Page Content

When creating pages, use block arrays for structured content instead of dumping plain text:

```
[
  { "type": "heading_2", "content": "Project Overview" },
  { "type": "paragraph", "content": "Description text here..." },
  { "type": "to_do", "content": "First deliverable", "checked": false },
  { "type": "to_do", "content": "Second deliverable", "checked": false },
  { "type": "divider" },
  { "type": "heading_2", "content": "Timeline" },
  { "type": "paragraph", "content": "Key dates and milestones..." }
]
```

---

## Studio Conventions

### Projects Database — Expected Schema

Profanity's central Projects database likely includes properties like:

| Property | Type | Purpose |
|---|---|---|
| Project Name | title | The name of the project |
| Client | relation or select | Who it's for |
| Status | status or select | Current stage (e.g., Pitch, Active, In Review, Complete) |
| Deadline | date | Due date or date range |
| Budget | number | Project budget |
| Deliverables | multi_select | What's being delivered (e.g., Hero Film, Social Cuts, Stills) |
| Priority | select | Urgency level |
| Notes | rich_text | Quick notes or context |

**Before creating or modifying anything in the Projects database, always fetch it first to confirm the actual schema.** Don't assume — inspect.

### Naming Conventions

- Database names: Title Case ("Projects", "Client Directory", "SOPs")
- Page titles: Natural language ("Q1 2026 Revenue Planning", not "q1-2026-rev")
- Select options: Consistent capitalization within each property

---

## Templates

Notion templates are pre-filled page structures that can be created inside databases. When Mark asks to "set up a template" or "create a project template," this means creating a template page within the database that new entries can be based on.

Via MCP, you simulate templates by:
1. Creating a new page with the full block structure
2. Using `notion-duplicate-page` to clone it for new entries

---

## Automations (Notion-Native)

Notion supports database automations (triggers + actions). These are configured in the Notion UI, not via API, but it's useful to know what's possible:

**Triggers:** Page added, property changed, specific property value
**Actions:** Set property, send notification, add page to another database, send Slack message

If Mark asks about automations, guide him through the Notion UI steps — these can't be set up via MCP.

---

## Common Troubleshooting

**"Page not found" errors:**
- The Notion integration may not have access to that page. In Notion: click ••• on the page → Connections → add the integration.

**Properties not matching:**
- Always fetch the database schema first. Property names are case-sensitive and must match exactly.

**Relation not connecting:**
- Both databases must be accessible to the integration. Check connections on both.

**Can't create in a specific database:**
- The integration needs explicit access. Share the database with the Notion integration.

---

## Notion Limitations (Don't Waste Time On These)

| What you want | Notion reality |
|---|---|
| Real-time collaboration via API | API is not real-time — it's request/response. Use webhooks or polling for sync. |
| Inline database formulas referencing other databases | Formulas only reference properties within the same database. Use relations + rollups for cross-database data. |
| Bulk operations (update 100 pages at once) | API processes one page at a time. Batch by looping, but respect rate limits (3 requests/second). |
| Custom block types | Not supported. Work within Notion's existing block types. |
| Exporting to PDF/DOCX via API | Not available. Export is UI-only. |
| Automations via API | Automations are UI-only. API can trigger similar effects by updating properties that automations watch. |
| Permissions management via API | Limited. Page sharing is mostly UI-managed. |
