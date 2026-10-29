# Profanity Creative — agent team plugins

Profanity Creative's AI team plugins. This repo is the source of truth and version history for the team plugins. It is laid out as a Cowork marketplace, but Cowork can't currently read a private GitHub marketplace (open Cowork bug), so plugins are installed by uploading the .plugin files the nightly task builds.

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
3. The same task builds fresh `.plugin` files into Dropbox `plugin-dev/builds/` and names the changed ones in its run summary on the Ops dashboard. Re-upload those in Cowork (remove the old copy first; re-uploading over a same-named plugin doesn't replace it).
4. If Cowork fixes private marketplaces (or this repo goes public), add `mcernosia/profanity-team` as a marketplace and turn on Sync automatically instead.

Never edit an installed plugin inside Cowork: the next sync overwrites it, and the source drifts.

History: until 2026-10-28 this repo held five plugins under old names (profanity-biz-dev, profanity-creative-vcd, profanity-virtual-producer). Those are now profanity-reid, profanity-kai and profanity-sloane.
