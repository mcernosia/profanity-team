# Tech Stack Vocabulary

Reference for cinematographer/CG-fluent language Kai should use so notes map to real nodes Mark can rig.

## 3D / Render
- **Cinema 4D** — primary modeling/scene/animation tool. Native MoGraph for procedural arrays, cloners, dynamics.
- **Houdini** — heavier procedural work, FX, terrain, particles, large-format LED content.
- **Redshift** — primary GPU renderer in C4D. Use terms: Area Light, Dome Light, IES, AOV, RS Material, Bump/Normal, Volumetrics.
- **Octane** — alternate GPU renderer when stylization or specific shader behavior calls for it.
- **Substance 3D Painter** — material authoring, smart materials, ID maps for masking.
- **Camera projection** — for stylized 2.5D moves and matte-painting workflows.

## Compositing / Finish
- **After Effects** — composite, type, color, multi-format outputs.
- **Trapcode Particular** — particle systems for sparks, dust, atmosphere.

## Delivery
- Multi-aspect: 16:9, 9:16, 4:5, 1:1.
- Stadium/LED: ribbon boards (e.g., 26K+ pixel widths), scoreboard reveals.
- Codecs: ProRes 422/4444 masters, H.264 review copies.

## Lighting language to prefer
- "Three-quarter key with a low rim, no fill" (build-ready) instead of "moody."
- "Dome HDRI at 30% with bounce card camera-left" instead of "soft light."
- Name the AOVs you want isolated (Albedo, Reflection, Refraction, AO) when it matters.
