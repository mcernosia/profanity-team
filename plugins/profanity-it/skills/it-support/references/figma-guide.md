# Figma — design context and Code Connect

## When IT uses Figma
- Mark asks for design context for a coding task → `mcp__<figma>__get_design_context`.
- Mark wants Code Connect templates linking Figma components to code → see "Code Connect" below.
- Mark needs to push code/page changes into Figma → `use_figma` write actions.
- Mark needs to read existing variables/styles → `get_variable_defs`, `search_design_system`.

## Code Connect basics
Code Connect templates map Figma component instances to code snippets. Files end `.figma.ts` or `.figma.js`.

Workflow:
1. Search for the component in the design system (`search_design_system`).
2. Build a template mapping the component's props to your code's props.
3. Push via `send_code_connect_mappings`.

Use the dedicated `figma:figma-code-connect` skill for the actual template format.

## Profanity context
Mark's studio site lives in Framer (not Figma), so Code Connect is mostly relevant for client work where the design system is in Figma. For pure design-context fetching, the Figma MCP is the right tool either way.

## Common gotchas
- Always call the `figma-use` skill BEFORE calling `use_figma` write actions — it's a mandatory prerequisite.
- For new blank Figma files, use the `figma-create-new-file` skill first.
- The duplicate-skill collision pattern can hit here too: don't name new skills `figma` if a similar one exists.
