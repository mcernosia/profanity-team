# profanity-it

Virtual IT and Web resource for Profanity Creative. Handles the technical side of the studio's digital infrastructure — website, GitHub, hosting, deployment, and Cowork plugin development — so Mark can stay focused on creative work.

---

## Stack

- **Framer** — primary website
- **GitHub** — version control and Cowork plugin hosting
- **Netlify** — standalone tool deployment
- **Vercel** — Next.js / edge deploys
- **Notion** — studio operating system (projects, CRM, knowledge base)
- **Figma** — design context and Code Connect for client work
- **Claude Cowork** — AI plugin infrastructure

---

## Components

### Skill: `it-support`

Loads automatically when you ask a technical question about the studio's stack. Detects which mode applies (Framer, GitHub, plugin dev, or deployment) and routes to the right expertise.

**Trigger phrases:**
- Framer: "update the site," "add a section," "something's broken on the site," "Framer question," "how do I change"
- GitHub: "push this," "commit," "set up a repo," "something broke in GitHub," "help with git," "plugin repo"
- Plugin dev: "build a plugin," "update a plugin," "add a skill file," "add a slash command," "plugin isn't working," "help with plugin.json"
- Deployment: "deploy this," "Netlify," "something's not loading," "set up a domain," "how do I host this," "auto-deploy"

### Commands

| Command | What it does |
|---|---|
| `/framer [task]` | Framer website help — layout, CMS, custom code overrides, SEO, responsive behavior, publishing |
| `/github [task]` | Git and GitHub help — commits, repos, branching, plugin version control, Cowork marketplace connection |
| `/plugin-dev [task]` | Cowork plugin development — manifests, skill files, slash commands, MCP configs, debugging |
| `/deploy [task]` | Netlify deployment — Drop, GitHub-connected auto-deploy, custom domains, environment variables, debugging |
| `/create-in-notion [task]` | Notion CRUD — create, read, update, query pages and databases |

---

## Usage

Ask naturally and the `it-support` skill auto-triggers:

> "How do I add a hover animation to a button in Framer?"
> "I need to push my latest plugin changes to GitHub."
> "Help me set up auto-deploy for this tool on Netlify."

Or use a slash command for direct mode access:

```
/framer add a new projects section to the homepage
/github set up a new plugin repo and push it
/plugin-dev write a skill file for a new client communication skill
/deploy connect my GitHub repo to Netlify for auto-deploy
```

---

## Setup

Wires the Notion MCP for the `/create-in-notion` command. Other commands use Bash (git, `gh`, build scripts) and skill knowledge — no additional MCP setup required.

---

## Customization

If the stack changes (e.g., moving from Framer to another platform, or adding a new deployment target), update the relevant reference file in `skills/it-support/references/` and bump the version in `plugin.json`.
