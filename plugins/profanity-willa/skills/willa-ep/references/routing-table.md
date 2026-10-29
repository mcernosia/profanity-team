# Willa's Routing Table

One lead per job. Use the plugin-prefixed command names, since `/brief` exists in both Sloane's and Kai's plugins.

## Who leads

| Ask | Lead | Commands | Chain |
| --- | --- | --- | --- |
| New lead, cold outreach, follow-up, pitch prep, "should I take this?" | Reid | `profanity-reid:outreach`, `:follow-up`, `:pitch-prep`, `:strategy`, `:build-deck` | Reid → Dusty voice check |
| Scope, proposal, quote, price check, client email, post-mortem, internal brief | Sloane | `profanity-sloane:scope`, `:proposal`, `:price-check`, `:email`, `:post-mortem`, `:brief` | Sloane → Lyle if the client sends their own terms → Dusty voice check |
| Logging a call, text or update | Sloane | `profanity-sloane:log-call`, `:log-update` | Sloane only |
| Concept, moodboard, style frames, treatment, creative brief | Kai | `profanity-kai:concept`, `:moodboard`, `:styleframe`, `:treatment`, `:brief` | Kai → Dusty for any copy |
| Copy: site, blog, case study, client brand copy, SEO | Dusty | `profanity-dusty:write`, `:write-content`, `:studio-copy`, `:brand-copy`, `:seo-audit` | Dusty only |
| Social: content plan, captions, launch, growth | Nora | `profanity-nora:plan`, `:post`, `:launch`, `:grow` | Content Engine for a full cycle |
| Contract, MSA, SOW terms, NDA, T&C change | Lyle | `profanity-lyle:contract`, `:nda`, `:our-paper` | Lyle → Sloane for the client conversation |
| Margin, cash, runway, A/R, 1099s, CPA prep, monthly pulse | James | `profanity-james:project-profit`, `:cash-flow`, `:ar-aging`, `:categorize`, `:contractor-check`, `:cpa-prep`, `:finance-check` | James → Sloane drafts any collection email |
| Site, Framer, Notion, GitHub, deploy, plugins, scheduled tasks | IT | `profanity-it:framer`, `:create-in-notion`, `:github`, `:deploy`, `:plugin-dev` | IT only; system changes need Mark's OK first |

## Workflow chains (from `Profanity_Agent_Workflows.md`)

| Trigger | Workflow | Chain |
| --- | --- | --- |
| Cold lead to signed deal | 1. Full Pipeline | Reid outreach → Reid pitch prep → Sloane scope → Sloane proposal → Lyle if client paper → Dusty |
| Deal signed | 2. Kickoff Cascade | Sloane brief → Kai concept → Sloane schedule note |
| Work ready to show | 3. Launch Sequence | Nora launch → Dusty → Nora captions |
| Golf push | 4. Golf Vertical Blitz | Reid strategy → Reid outreach → Dusty |
| Client went quiet | 5. Recovery | Reid follow-up → Dusty |
| Weekly content | 6. Content Engine | `profanity-workflows:content-engine` |
| Big pitch coming | 7. Pitch Prep War Room | Reid pitch prep → Kai concept → Sloane price check → Dusty |
| Retainer opportunity | 8. Retainer Upsell | Reid strategy → Sloane scope → James margin check → Dusty |
| Project wrapped | 9. Post-Mortem Pipeline | `profanity-workflows:post-mortem-pipeline` |
| Inbound lead | 10. Inbound Response Sprint | Reid → Sloane scope → Dusty |

## Ties

- **Pricing a new job:** Sloane leads. James adds past-margin data when asked.
- **"Is this client worth it?":** Reid leads. James adds margin history.
- **Contract arrived with a proposal reply:** Lyle reviews first, then Sloane responds.
- **Copy inside another agent's deliverable:** that agent drafts, Dusty voice-checks. Dusty doesn't lead.
