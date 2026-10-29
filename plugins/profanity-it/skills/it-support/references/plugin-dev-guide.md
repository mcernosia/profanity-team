# Cowork Plugin Development Guide — Profanity Creative

Reference for building and updating Cowork plugins. Complete file templates — ready to drop in, not fragments.

---

## Plugin Directory Structure

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json       # Required: manifest
├── commands/             # Slash commands (one .md per command)
├── skills/               # Skills (one subdirectory per skill)
│   └── skill-name/
│       ├── SKILL.md
│       └── references/   # Detailed docs loaded on demand
├── .mcp.json             # MCP server connections (only if needed)
└── README.md
```

Only create directories for components the plugin actually uses. Don't add empty folders.

---

## plugin.json — Complete Template

```json
{
  "name": "plugin-name",
  "version": "0.1.0",
  "description": "One-sentence description of what this plugin does",
  "author": {
    "name": "Profanity Creative"
  },
  "keywords": ["relevant", "keywords", "here"]
}
```

**Name rules:** kebab-case only (`my-plugin`, not `My Plugin` or `my_plugin`).
**Version:** semver — start at `0.1.0`. Bump patch for fixes, minor for new components, major for restructures.

---

## Slash Command — Complete Template

File location: `commands/command-name.md`

```markdown
---
description: Short description shown in /help (under 60 chars)
argument-hint: [describe expected argument]
allowed-tools: Read, Write, Edit, Bash, WebSearch, WebFetch
---

Instructions for Claude here. Write these as directives — what Claude should DO,
not what the user should read.

The user's argument is available as: $ARGUMENTS
Positional args: $1, $2, $3

Include a file in context: @path/to/file.md
Run a bash command inline: !`git status`
Reference a plugin file portably: @${CLAUDE_PLUGIN_ROOT}/skills/skill-name/SKILL.md
```

**Key rule:** Commands are instructions FOR Claude, not documentation for the user.

### Example — /scope command

```markdown
---
description: Scope a project — hours, pricing, complexity
argument-hint: [project description]
allowed-tools: Read
---

The user wants to scope a project: $ARGUMENTS

Review the project description and provide:
1. Estimated hours broken down by phase (pre-production, production, revisions, delivery)
2. Recommended price range based on Profanity's rates
3. Top 3 questions to ask the client before committing to a number
4. Any red flags or scope risks to flag upfront

Be direct. Give ranges, not vague estimates. Flag anything that could balloon the scope.
```

---

## Skill — Complete Template

File location: `skills/skill-name/SKILL.md`

```markdown
---
name: skill-name
description: >
  This skill should be used when the user says "trigger phrase one,"
  "trigger phrase two," or asks about [topic]. Also trigger when the
  user mentions [related concept] or needs help with [specific task].
version: 0.1.0
---

# Skill Title

Core knowledge here. Keep this file under 2,000 words — move detailed
reference content to the references/ folder.

## Section One

Content here.

## Section Two

Content here.

## Reference Files

- **`references/detail.md`** — description of what's in there
```

**Frontmatter description rules:**
- Third-person ("This skill should be used when...")
- Include specific trigger phrases in quotes
- The more specific the trigger phrases, the more reliably the skill fires

---

## Common Gotchas

**Skill not triggering:**
- Check that `description` in frontmatter has specific quoted trigger phrases matching what you'd actually say
- Rebuild/reload the plugin in Cowork after any file change

**Command not showing up in /help:**
- Check that the file is in `commands/` at the plugin root, not nested deeper
- Filename must end in `.md`

**plugin.json errors:**
- `name` must be kebab-case — no spaces, no underscores, no capitals
- All JSON must be valid — trailing commas will break it

**plugin.json `commands` or `skills` path overrides:**
- Only needed if you're using a non-standard directory name
- Default auto-discovery finds `commands/` and `skills/` automatically — don't add path overrides unless you have a reason

**Changes not reflecting after push:**
- Cowork pulls from GitHub — changes need to be committed and pushed, not just saved locally
- Then sync/reload the plugin in Cowork

---

## Building, releasing, and verifying plugins

Mark's actual build toolchain lives in `plugin-dev/scripts/`. Use these — don't hand-zip.

### 1. Edit source
Plugin source lives in `plugin-dev/<plugin-name>/`. Edit there. The folder structure is:

```
plugin-dev/<plugin-name>/
├── .claude-plugin/plugin.json        # manifest (name, version, description, keywords)
├── .mcp.json                          # optional, only if the plugin wires MCPs
├── README.md
├── commands/                          # each .md is a slash command (needs YAML frontmatter)
│   └── <command-name>.md
└── skills/<skill-name>/
    ├── SKILL.md                       # the skill definition (needs YAML frontmatter)
    └── references/                    # optional supporting files the skill reads
        └── *.md
```

### 2. Build
```
cd /Users/markc/Library/CloudStorage/Dropbox/Claude_Projects/PROFANITY/plugin-dev
./scripts/plugin-build.sh <plugin-name>
```

Output lands in `plugin-dev/builds/<plugin-name>.plugin`.

### 3. Version + release
For a real version bump (not just a build), use:
```
./scripts/plugin-release.sh <plugin-name>
```

This bumps the version in `plugin.json`, builds, and logs the release.

### 4. Verify installed vs. source
Drift between source and what's actually installed is a real problem (we've shipped malformed commands that never registered). Always run:
```
./scripts/plugin-status.sh
```

This compares each local plugin's source vs. its installed/deployed copy. Anything out of sync means: rebuild + reinstall.

### 5. Install / reinstall
After building, install the `.plugin` file from `plugin-dev/builds/` via Cowork's plugin install flow. There's no CLI install step; this is the only manual touchpoint.

### 6. Backup
`backup-cowork.sh` runs daily via launchd. It snapshots all plugins, skills, and extensions. Don't worry about losing work between sessions.

### Common gotchas
- **Slash commands need YAML frontmatter** (`---\ndescription: ...\n---`). Without it, the command never registers — even if the .md file exists. (We've burned ourselves on this; check it first when a command is "missing.")
- **Skill `name:` field collisions** — two skills with the same `name:` in their frontmatter will fight at runtime. If you fork or copy a skill, rename the `name:` field.
- **Stale absolute paths** — don't hardcode session paths (`/sessions/<name>/...`); they don't survive across sessions. Use Glob to locate files at runtime.

---

## Adding an MCP Server Connection

Only add `.mcp.json` if the plugin needs external tool access (Notion, Slack, Figma, Netlify, Vercel, etc.).

Real example — wiring the Notion MCP (this is what `profanity-it` actually uses for `/create-in-notion`):

```json
{
  "mcpServers": {
    "notion": {
      "type": "http",
      "url": "https://mcp.notion.com/mcp"
    }
  }
}
```

For SSE-type servers:
```json
{
  "mcpServers": {
    "server-name": {
      "type": "sse",
      "url": "https://mcp.service.com/sse"
    }
  }
}
```

**GitHub does NOT have an MCP in this setup** — use git/`gh` via Bash for all GitHub operations.

Document any required environment variables in README.md.
