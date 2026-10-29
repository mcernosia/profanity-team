# Profanity Creative — agent team plugins

Cowork plugin marketplace for Profanity Creative's AI team. This repo is the source of truth for installed plugins.

| Plugin | Agent | Role |
| --- | --- | --- |
| profanity-willa | Willa Prescott | EP: routes asks, runs chains |
| profanity-sloane | Sloane Mercer | Producer |
| profanity-reid | Reid Calloway | Biz dev |
| profanity-kai | Kai Morrow | Creative director |
| profanity-dusty | Dusty Jones | Copy and voice |
| profanity-nora | Nora Beckett | Social |
| profanity-lyle | Lyle Whitlock | Legal (runs on Anthropic's Legal plugin) |
| profanity-james | James Halloran | Finance |
| profanity-it | Profanity IT | Tech and infra |
| profanity-workflows | — | Content Engine, Post-Mortem Pipeline |

## How it flows
1. Edit plugins in Dropbox: `PROFANITY/plugin-dev/<plugin>/`.
2. The nightly `plugin-git-sync` scheduled task packages plugin-dev, runs `scripts/sync_plugins.py`, and pushes any changes here. If content changed but the version didn't, it bumps the patch version (here and back in plugin-dev) so Cowork sees an update.
3. Cowork installs from this marketplace with **Sync automatically** on.

Never edit an installed plugin inside Cowork: the next sync overwrites it, and the source drifts.

History: until 2026-10-28 this repo held five plugins under old names (profanity-biz-dev, profanity-creative-vcd, profanity-virtual-producer). Those are now profanity-reid, profanity-kai and profanity-sloane.
