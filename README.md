# Profanity Team

AI-powered team plugins for Profanity Creative — a lean 3D product visualization studio run by Mark Cernosia out of Vermont.

Each plugin gives Claude a specific role and expertise area within the studio. Together they handle the full business and creative operation so Mark can stay focused on the work.

---

## The Team

| Plugin | Name | Role |
|--------|------|------|
| `profanity-virtual-producer` | **Sloane Wilder** | Producer — proposals, scoping, client communication, project documentation |
| `profanity-creative-vcd` | **Kai Morrow** | Creative Director — concepts, moodboards, style frames, animation treatments |
| `profanity-biz-dev` | **Reid Calloway** | Biz Dev — cold outreach, pitch prep, pipeline follow-up, market positioning |
| `profanity-nora` | **Nora Beckett** | Social Media Manager — Instagram, LinkedIn, content calendars, growth strategy |
| `profanity-dusty` | **Dusty Jones** | Copywriter — studio copy, client copy, long-form content, voice editing |

---

## Usage

Each plugin is a Cowork-compatible `.plugin` file. Install via the Cowork desktop app.

Plugins are triggered automatically when you describe a task that matches their domain — or you can use slash commands directly:

```
/proposal  /scope  /email  /brief       ← Sloane (Virtual Producer)
/concept   /treatment  /styleframe      ← Kai (Creative Director)
/outreach  /follow-up  /pitch-prep      ← Reid (Biz Dev)
/post      /plan  /launch  /grow        ← Nora (Social)
/write     /edit  /studio-copy          ← Dusty (Copy)
```

---

## Structure

```
profanity-team/
├── profanity-virtual-producer/   # Sloane Wilder
├── profanity-creative-vcd/       # Kai Morrow
├── profanity-biz-dev/            # Reid Calloway
├── profanity-nora/               # Nora Beckett
└── profanity-dusty/              # Dusty Jones
```

---

## Maintainer

Mark Cernosia — [profanity.tv](https://profanity.tv)
