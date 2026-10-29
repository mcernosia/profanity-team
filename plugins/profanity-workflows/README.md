# Profanity Workflows

Automated workflow chains for Profanity Creative. Each workflow runs a full agent pipeline with a single command — multiple agents in sequence, Dusty voice check at the end, Slack notification when ready for review.

## Commands

| Command | What it does |
|---------|-------------|
| `/content-engine [theme]` | Runs the full Content Engine (Workflow #6): Nora builds a content plan → Dusty writes posts → Nora writes captions → Dusty voice checks → posts to `#wf-content-engine` |
| `/post-mortem-pipeline [project]` | Runs the full Post-Mortem → Portfolio Pipeline (Workflow #9): pulls context → Sloane writes the post-mortem as a Google Doc in the Drive "Post-Mortems" folder → Kai describes style frames → Dusty writes case study → Nora builds launch plan → Dusty voice checks → posts to `#wf-post-mortem` |

## How It Works

1. You say `/content-engine` or `/post-mortem-pipeline [project name]`
2. The full agent chain runs automatically — no input needed between steps
3. Dusty does a final voice check on everything client-facing
4. A summary posts to the workflow's Slack channel
5. You get a batched DM at your next review window (9am / 12pm / 3pm ET)
6. You review, approve, redirect, or kill

## Prerequisites

- Slack channels `#wf-content-engine` and `#wf-post-mortem` must exist (private channels)
- The Profanity agent plugins must be installed (Nora, Dusty, Kai, Sloane)
- Connected tools: Slack, Notion, Gmail, Fireflies, Buffer, Framer

## Setup

Install this plugin locally in Cowork. No external service connections required beyond what's already configured.
