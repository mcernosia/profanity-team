# Framer Guide — Profanity Creative

Reference for Framer website tasks. Covers layout/component updates, CMS, custom code overrides, SEO, responsive behavior, and publishing.

---

## Common Tasks

### Adding or Editing a Section

1. Open Framer → click the page in the left panel
2. Click **+** to add a frame or component, or click an existing section to select it
3. Use the right panel to adjust layout, spacing, colors, and typography
4. For text: double-click to edit inline
5. Hit **Publish** (top right) when ready

### Updating CMS Content

1. Left panel → **CMS** tab
2. Select the collection (e.g., Projects, Services)
3. Click the item to edit, or **+ New** to add
4. Fill fields → **Save**
5. CMS changes go live on next publish

### Connecting a CMS Collection to a Component

1. Select the component on canvas
2. Right panel → **Content** → **Connect to CMS**
3. Choose the collection and map fields to component slots
4. Use **Collection List** component for repeating items

---

## Custom Code Overrides

Framer supports custom code via **Code Overrides** (component-level) and **Code Components** (full custom components). Paste these into Framer's code editor.

### Adding a Code Override

1. Select the component
2. Right panel → **Override** → **+ New Override**
3. Paste the code block below, modify as needed
4. Assign the override function to the component

### Override Template — Hover Animation

```tsx
import { type ComponentType } from "react"
import { motion } from "framer-motion"

export function withHoverScale(Component): ComponentType {
  return (props) => (
    <motion.div
      whileHover={{ scale: 1.03 }}
      transition={{ duration: 0.2 }}
    >
      <Component {...props} />
    </motion.div>
  )
}
```

### Override Template — On-Click Redirect

```tsx
import { type ComponentType } from "react"

export function withRedirect(Component): ComponentType {
  return ({ onClick, ...props }) => (
    <Component
      {...props}
      onClick={() => window.open("https://your-url.com", "_blank")}
    />
  )
}
```

### Code Component Template (Blank)

```tsx
import { addPropertyControls, ControlType } from "framer"

export default function MyComponent({ text, color }) {
  return (
    <div style={{ color }}>
      {text}
    </div>
  )
}

MyComponent.defaultProps = {
  text: "Hello",
  color: "#000",
}

addPropertyControls(MyComponent, {
  text: { type: ControlType.String, title: "Text" },
  color: { type: ControlType.Color, title: "Color" },
})
```

---

## SEO Basics

1. Page settings → **SEO** tab
2. Set **Title** and **Description** per page (don't use the same on every page)
3. For OG image: upload a 1200×630px image under **Social Image**
4. Framer auto-generates a sitemap — no manual setup needed
5. Connect a custom domain in **Settings → Domains** for clean URLs

---

## Responsive Behavior

- Use **breakpoints** (Desktop / Tablet / Mobile) in the top toolbar
- Set dimensions with `%` or `fr` units for fluid layouts, not fixed `px` where avoidable
- Test all three breakpoints before publishing
- Framer's **Auto Layout** (similar to Flexbox) is the right tool for responsive stacks

---

## Publishing Workflow

1. Make changes on canvas
2. Preview in browser: **Preview** button (top right)
3. **Publish** → confirm the domain
4. Changes are live immediately — no build queue

---

## Framer Limitations (Don't Waste Time On These)

| What you want | Framer reality |
|---|---|
| Server-side logic / backend | Not supported. Use Netlify Functions or a separate service. |
| User authentication | Not built-in. Third-party (Memberstack, Outseta) required. |
| Complex form handling with server logic | Framer forms are basic. Use Tally, Typeform, or a custom Netlify form. |
| Database / dynamic content beyond CMS | Not supported. CMS is the limit. |
| Full e-commerce | Not supported natively. |
| Animations triggered by scroll position (complex) | Limited. Use Lottie or a code override for advanced scroll animations. |

If the request hits one of these walls, say so immediately and propose the right tool instead.

---

## Troubleshooting

**Site not updating after publish:**
- Hard refresh the browser (Cmd+Shift+R / Ctrl+Shift+R)
- Check if you're on a custom domain — DNS propagation can take up to 48 hours after initial setup

**Code override not applying:**
- Make sure the override file saved without TypeScript errors (red underlines = broken)
- Re-assign the override in the right panel — it sometimes needs to be re-selected after edits

**CMS content not showing:**
- Confirm the collection is connected to the component (right panel → Content)
- Check that the CMS item is set to **Published**, not Draft

**Fonts not loading:**
- Framer uses Google Fonts and their own library — custom font files require a workaround via CSS embed
- Settings → **Custom Code** → paste `@font-face` in the `<head>` section
