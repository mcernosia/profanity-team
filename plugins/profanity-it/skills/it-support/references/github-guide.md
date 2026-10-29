# GitHub Guide — Profanity Creative

Reference for Git and GitHub tasks. Terminal commands only — in the right order, with one-line explanations. Destructive commands are flagged.

---

## Standard Plugin Repo Structure

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json
├── commands/           # Slash commands (.md files)
├── skills/             # Skill directories (each with SKILL.md)
├── .mcp.json           # MCP tool connections (only if needed)
└── README.md
```

---

## Setting Up a New Repo

### Initialize and push a new plugin repo

```bash
# Navigate to your plugin folder
cd /path/to/plugin-name

# Initialize git
git init

# Stage everything
git add .

# First commit
git commit -m "initial commit"

# Create the repo on GitHub (requires GitHub CLI)
gh repo create profanity-creative/plugin-name --public --source=. --remote=origin --push
```

If you don't have the GitHub CLI (`gh`), create the repo manually on github.com, then:

```bash
# Connect local repo to GitHub remote
git remote add origin https://github.com/profanity-creative/plugin-name.git

# Push and set upstream
git push -u origin main
```

---

## Daily Workflow — Committing and Pushing

```bash
# Check what changed
git status

# Stage specific files (preferred over git add .)
git add .claude-plugin/plugin.json skills/skill-name/SKILL.md

# Or stage everything if you know what you changed
git add .

# Commit with a clear message
git commit -m "update skill trigger phrases"

# Push to GitHub
git push
```

---

## Branching (When You Need It)

For experimental plugin changes you're not sure about:

```bash
# Create and switch to a new branch
git checkout -b feature/new-command

# Work, commit as normal, then push the branch
git push -u origin feature/new-command

# When ready to merge back to main
git checkout main
git merge feature/new-command

# Clean up the branch after merging
git branch -d feature/new-command
git push origin --delete feature/new-command
```

---

## Resolving Common Issues

### Merge conflict

```bash
# See which files have conflicts
git status

# Open the conflicted file — look for <<<<<<, =======, >>>>>>>
# Edit the file to keep what you want, remove the conflict markers

# Stage the resolved file
git add path/to/file.md

# Complete the merge
git commit
```

### Accidentally committed to main — need to undo last commit

⚠️ **This rewrites history. Only safe if you haven't pushed yet.**

```bash
# Undo the last commit but keep the changes staged
git reset --soft HEAD~1
```

⚠️ **This is more destructive — discards the changes entirely:**

```bash
git reset --hard HEAD~1
```

### Need to undo a push (already on GitHub)

Don't rewrite history on a shared repo. Instead, revert:

```bash
# Create a new commit that undoes the last one
git revert HEAD

# Push the revert
git push
```

### Remote is ahead — need to pull before pushing

```bash
# Pull and merge remote changes
git pull

# If there are conflicts, resolve them (see above), then push
git push
```

---

## Connecting a Repo to the Cowork GitHub App

1. Go to github.com/apps/claude-cowork (or whatever the current app URL is)
2. Click **Configure** → select the `profanity-creative` org or your personal account
3. Under **Repository access**, add the plugin repo
4. Back in Cowork, the repo will appear in your plugin marketplace settings

---

## Plugin Versioning

Update the version in `plugin.json` before pushing a meaningful update:

- Bug fix / small tweak → bump patch: `0.1.0` → `0.1.1`
- New skill or command → bump minor: `0.1.0` → `0.2.0`
- Major restructure → bump major: `0.1.0` → `1.0.0`

```bash
# After updating plugin.json version
git add .claude-plugin/plugin.json
git commit -m "bump version to 0.2.0"
git push
```

---

## Useful One-Liners

```bash
# See recent commits
git log --oneline -10

# See what changed in the last commit
git show --stat

# See all remotes
git remote -v

# Discard unstaged changes to a specific file (can't undo this)
git checkout -- path/to/file.md

# See diff of what's staged
git diff --staged
```
