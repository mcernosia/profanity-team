# Profanity Creative — Deck Design System

Extracted from real Profanity decks. This is the canonical reference for every presentation that leaves the studio. Do not deviate.

---

## Philosophy

Profanity decks are dark, minimal, and confident. They don't try to impress with design tricks. They let the work and the ideas breathe against black. The restraint is the design.

Every element on every slide should pass this test: **Does this need to be here?** If the answer isn't an immediate yes, remove it.

---

## Color System

### Primary Palette

```
BACKGROUND:    #000000  (pure black — every slide, no exceptions)
PRIMARY TEXT:  #FFFFFF  (white — headlines, body, primary content)
ACCENT:        #0ABAB5  (Profanity teal — section headers, emphasis, key phrases)
MUTED:         #808080  (gray — dates, metadata, captions, secondary info)
```

### Usage Rules

- **Background is always pure black.** Not dark gray. Not charcoal. `000000`.
- **Teal is surgical.** Use it for content headers on image grid slides, inline emphasis phrases, subtitle text on dividers, and the Profanity mark. Never for large blocks of text or backgrounds.
- **White does the heavy lifting.** All hero headers, body text, and primary content.
- **Gray is for metadata only.** Dates, deck type labels, contact info, slide numbers if used.
- **No other colors.** No blues, no gradients, no additional accent colors. The palette is black, white, teal, gray. Period.

### Overlay System

For section divider slides with background images:
- Full-width black bar: `000000` at ~85-90% opacity
- Bar height: approximately 25% of slide height (~1.4")
- Positioned vertically centered or slightly above center
- All text within the bar, never floating on the image

---

## Typography

### Font Stack

| Role | Font | Fallback | Notes |
|------|------|----------|-------|
| Headlines / Titles | Hanson | Arial Black | Bold, condensed, heavy. This is the Profanity voice in type. |
| Body / Descriptions | Azeret Mono | Consolas | Monospace. Technical. Intentional contrast with the bold headers. |

### Scale

| Element | Font | Size | Weight | Color | Case | Spacing |
|---------|------|------|--------|-------|------|---------|
| Hero title (title slide) | Hanson | 54-72pt | Bold | `FFFFFF` | UPPERCASE | Normal |
| "PROFANITY" wordmark | Hanson or Arial | 14-16pt | Bold | `FFFFFF` | UPPERCASE | `charSpacing: 4-6` (tracked out) |
| Section divider title | Hanson | 44-54pt | Bold | `FFFFFF` | UPPERCASE | Normal |
| Divider subtitle | Azeret Mono | 18-20pt | Regular | `0ABAB5` | UPPERCASE | `charSpacing: 2` |
| Content header (grid slides) | Arial | 28-36pt | Bold | `0ABAB5` | Title Case | Normal |
| Body text | Azeret Mono | 14-16pt | Regular | `FFFFFF` | Sentence case | Normal |
| Inline emphasis | Azeret Mono | 14-16pt | Regular | `0ABAB5` | Sentence case | Normal |
| Date / metadata | Azeret Mono | 11-12pt | Regular | `808080` | UPPERCASE | Normal |
| Contact info | Azeret Mono | 11pt | Regular | `808080` | Normal | Normal |

### Typography Rules

- **Never use more than these two font families in a deck.** Hanson for headers. Azeret Mono for everything else.
- **The contrast between Hanson and Azeret Mono IS the design.** Bold condensed vs. monospace. Heavy vs. light. This pairing is non-negotiable.
- **Uppercase for all headers and titles.** Sentence case for body text only.
- **No italic unless it's a direct quote or publication title.**
- **Track out the PROFANITY wordmark** with `charSpacing: 4-6` to give it presence at small sizes.

---

### FONT EMBEDDING WARNING

Custom fonts (Hanson, Azeret Mono) don't natively embed in `.pptx` exports from pptxgenjs. If a recipient's machine doesn't have these fonts installed, PowerPoint substitutes Calibri/Arial and the deck looks generic. To prevent this:

1. **Default delivery format: PDF.** Export the final deck to PDF for client review and final delivery, fonts always embed in PDF.
2. **If sending .pptx is unavoidable**, install Hanson + Azeret Mono on the recipient's machine first, or fall back to a web-safe pair (Impact + Courier New) for that deck only and document the substitution.
3. **Never assume the deck renders correctly on a client's machine without verification.**

---

## Layout Grid

### Slide Dimensions
- Layout: `LAYOUT_16x9` (10" wide x 5.625" tall)
- All coordinates in inches

### Margins and Positioning

```
LEFT MARGIN:     1.3"   (all text starts here)
RIGHT MARGIN:    0.7"   (text max width ~8.0")
TOP MARGIN:      0.7"   (minimum clearance from top)
BOTTOM MARGIN:   0.5"   (minimum clearance from bottom)
```

### Text Positioning by Slide Type

**Title Slide:**
```
PROFANITY wordmark:   x: 1.3,  y: 2.0,  w: 8.0,  h: 0.4
Client name (hero):   x: 1.3,  y: 2.3,  w: 8.0,  h: 1.0
Subtitle (teal):      x: 1.3,  y: 3.2,  w: 8.0,  h: 0.5
Divider line:         x: 1.3,  y: 3.7,  w: 1.5,  h: 0.0  (white, 2pt)
Date / deck type:     x: 1.3,  y: 3.9,  w: 8.0,  h: 0.3
```

**Personal Note Slide:**
```
Greeting (hero):      x: 1.3,  y: 0.7,  w: 8.0,  h: 0.9
Body text:            x: 1.3,  y: 1.8,  w: 8.0,  h: 3.5
```

**Section Divider (with image background):**
```
Background image:     x: 0,    y: 0,    w: 10.0, h: 5.625  (full bleed)
Black overlay bar:    x: 0,    y: 2.1,  w: 10.0, h: 1.6
Title (in bar):       x: 1.3,  y: 2.2,  w: 8.0,  h: 0.8
Subtitle (in bar):    x: 1.3,  y: 2.9,  w: 8.0,  h: 0.5
```

**Section Divider (no image):**
```
Title:                x: 1.3,  y: 2.2,  w: 8.0,  h: 0.8
Subtitle (teal):      x: 1.3,  y: 2.9,  w: 8.0,  h: 0.5
```

**Concept / Text Slide:**
```
Header:               x: 1.3,  y: 0.7,  w: 8.0,  h: 0.9
Body paragraph(s):    x: 1.3,  y: 1.8,  w: 8.0,  h: 3.0
```

**Image Grid Slide:**
```
Content header:       x: 1.3,  y: 0.7,  w: 8.0,  h: 0.6
Description:          x: 1.3,  y: 1.25,  w: 8.0,  h: 0.5

Image 1:              x: 1.3,  y: 2.2,  w: 2.4,  h: 2.4
Image 2:              x: 3.9,  y: 2.2,  w: 2.4,  h: 2.4
Image 3:              x: 6.5,  y: 2.2,  w: 2.4,  h: 2.4

(Gutter between images: ~0.2-0.3")
```

**Closing Slide:**
```
"THANK YOU.":         x: 0,    y: 1.5,  w: 10.0, h: 1.2   (centered)
Contact info:         x: 0,    y: 4.5,  w: 10.0, h: 0.4   (centered)
```

---

## The Profanity Mark

The Profanity circle-slash mark (a circle with a diagonal line through it) appears on every slide in the bottom-right corner.

**Positioning:**
```
x: 9.2,  y: 4.9,  w: 0.35,  h: 0.35
```

**How to render it:** If a Profanity logo file is available, use it. Otherwise, draw it programmatically:
- Circle: `OVAL` shape, no fill, `0ABAB5` stroke, 1.5pt line
- Diagonal: `LINE` shape from top-left to bottom-right of the circle bounds, `0ABAB5`, 1.5pt

**Appearance:**
- Teal (`0ABAB5`) stroke on black background
- Subtle. Not competing with content.
- Omit on title slide if the PROFANITY wordmark is already present, or place it larger.

---

## Slide Type Recipes

### Recipe: Title Slide

```javascript
let slide = pres.addSlide();
slide.background = { color: "000000" };

// PROFANITY wordmark
slide.addText("PROFANITY", {
  x: 1.3, y: 2.0, w: 8.0, h: 0.4,
  fontFace: "Arial", fontSize: 14, bold: true, color: "FFFFFF",
  charSpacing: 5, margin: 0
});

// Client name — massive
slide.addText("CLIENT NAME", {
  x: 1.3, y: 2.3, w: 8.0, h: 1.0,
  fontFace: "Hanson", fontSize: 64, bold: true, color: "FFFFFF",
  margin: 0
});

// Subtitle in teal
slide.addText("PROJECT SUBTITLE", {
  x: 1.3, y: 3.2, w: 8.0, h: 0.5,
  fontFace: "Hanson", fontSize: 22, bold: true, color: "0ABAB5",
  margin: 0
});

// Divider line
slide.addShape(pres.shapes.LINE, {
  x: 1.3, y: 3.75, w: 1.5, h: 0,
  line: { color: "FFFFFF", width: 2 }
});

// Date and deck type
slide.addText("ANIMATION TREATMENT >> 03.20.26", {
  x: 1.3, y: 3.9, w: 8.0, h: 0.3,
  fontFace: "Azeret Mono", fontSize: 11, color: "808080",
  margin: 0
});
```

### Recipe: Personal Note Slide

```javascript
let slide = pres.addSlide();
slide.background = { color: "000000" };

// Greeting
slide.addText("HEY [NAME]!", {
  x: 1.3, y: 0.7, w: 8.0, h: 0.9,
  fontFace: "Hanson", fontSize: 48, bold: true, color: "FFFFFF",
  margin: 0
});

// Body — use rich text array for teal emphasis
slide.addText([
  { text: "Following up on our call, I put together a few high-level creative directions to help visualize how the product could come to life in a ~15s hero video.", options: { breakLine: true, paraSpaceAfter: 14 } },
  { text: "\n", options: { breakLine: true } },
  { text: "These are intentionally ", options: {} },
  { text: "big-picture explorations using Gen AI", options: { color: "0ABAB5" } },
  { text: ", focused on lightweight performance and integrated strength.", options: { breakLine: true, paraSpaceAfter: 14 } }
], {
  x: 1.3, y: 1.8, w: 8.0, h: 3.2,
  fontFace: "Azeret Mono", fontSize: 14, color: "FFFFFF",
  margin: 0, valign: "top"
});
```

### Recipe: Section Divider (with image)

```javascript
let slide = pres.addSlide();
slide.background = { color: "000000" };

// Background image (blurred, desaturated)
slide.addImage({
  path: "path/to/image.jpg",
  x: 0, y: 0, w: 10.0, h: 5.625,
  sizing: { type: "cover", w: 10.0, h: 5.625 }
});

// Black overlay bar
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0, y: 2.1, w: 10.0, h: 1.6,
  fill: { color: "000000", transparency: 10 }
});

// Section title
slide.addText("BUILT FROM AIR", {
  x: 1.3, y: 2.15, w: 8.0, h: 0.8,
  fontFace: "Hanson", fontSize: 48, bold: true, color: "FFFFFF",
  margin: 0
});

// Treatment number in teal
slide.addText("TREATMENT 01", {
  x: 1.3, y: 2.9, w: 8.0, h: 0.5,
  fontFace: "Azeret Mono", fontSize: 18, color: "0ABAB5",
  charSpacing: 2, margin: 0
});
```

### Recipe: Image Grid Slide

```javascript
let slide = pres.addSlide();
slide.background = { color: "000000" };

// Section header in teal
slide.addText("Weightless Assembly", {
  x: 1.3, y: 0.7, w: 8.0, h: 0.6,
  fontFace: "Arial", fontSize: 32, bold: true, color: "0ABAB5",
  margin: 0
});

// Description
slide.addText("Ultra-light construction, precision engineering, calm confidence.", {
  x: 1.3, y: 1.25, w: 8.0, h: 0.5,
  fontFace: "Azeret Mono", fontSize: 14, color: "FFFFFF",
  margin: 0
});

// Three images
const imgY = 2.2, imgH = 2.4, imgW = 2.4, gutter = 0.25;
const startX = 1.3;

slide.addImage({ path: "img1.jpg", x: startX, y: imgY, w: imgW, h: imgH });
slide.addImage({ path: "img2.jpg", x: startX + imgW + gutter, y: imgY, w: imgW, h: imgH });
slide.addImage({ path: "img3.jpg", x: startX + (imgW + gutter) * 2, y: imgY, w: imgW, h: imgH });
```

### Recipe: Concept / Text Slide

```javascript
let slide = pres.addSlide();
slide.background = { color: "000000" };

// CONCEPT header
slide.addText("CONCEPT", {
  x: 1.3, y: 0.7, w: 8.0, h: 0.9,
  fontFace: "Hanson", fontSize: 44, bold: true, color: "FFFFFF",
  margin: 0
});

// Body paragraphs
slide.addText([
  { text: "This direction treats the product as something that feels almost weightless, assembled from air rather than mass. Motion is calm and precise, emphasizing breathability, reduced padding, and comfort without sacrificing strength.", options: { breakLine: true, paraSpaceAfter: 14 } },
  { text: "\n", options: { breakLine: true } },
  { text: "The product is always grounded in reality, but presented in a clean, high-key environment that reinforces lightness and performance.", options: {} }
], {
  x: 1.3, y: 1.8, w: 8.0, h: 3.0,
  fontFace: "Azeret Mono", fontSize: 14, color: "FFFFFF",
  margin: 0, valign: "top"
});
```

### Recipe: Closing Slide

```javascript
let slide = pres.addSlide();
slide.background = { color: "000000" };

// THANK YOU.
slide.addText("THANK YOU.", {
  x: 0, y: 1.5, w: 10.0, h: 1.2,
  fontFace: "Hanson", fontSize: 64, bold: true, color: "FFFFFF",
  align: "center", margin: 0
});

// Contact info
slide.addText("Mark Cernosia  |  mark@profanity.tv  |  (530) 906-9596", {
  x: 0, y: 4.5, w: 10.0, h: 0.4,
  fontFace: "Azeret Mono", fontSize: 11, color: "808080",
  align: "center", margin: 0
});
```

---

## Profanity Mark Helper

Add this to every slide (call it as a function to avoid object reuse issues):

```javascript
function addProfanityMark(slide, pres) {
  const cx = 9.35, cy = 5.05, r = 0.15;
  // Circle
  slide.addShape(pres.shapes.OVAL, {
    x: cx - r, y: cy - r, w: r * 2, h: r * 2,
    fill: { type: "none" },
    line: { color: "0ABAB5", width: 1.2 }
  });
  // Diagonal slash
  slide.addShape(pres.shapes.LINE, {
    x: cx - r + 0.03, y: cy - r + 0.03, w: (r * 2) - 0.06, h: (r * 2) - 0.06,
    line: { color: "0ABAB5", width: 1.2 },
    rotate: 0
  });
}
```

---

## Anti-Patterns — Never Do These

- **White or light backgrounds.** Never. Not even for one slide.
- **Centered body text.** Left-align everything except closing slide title and contact info.
- **Bullet points.** Profanity decks don't use bullets. Write in paragraphs or use the image grid layout.
- **Decorative elements.** No accent bars under titles, no borders, no drop shadows, no flourishes.
- **More than 3 images per row.** The grid is always 3-across. If you need more images, add another slide.
- **Crowded slides.** If there's no black space breathing around the content, you've put too much on the slide.
- **Generic stock imagery.** If Mark hasn't provided images, use solid black or a subtle dark gray placeholder. Don't reach for stock.
- **Any color outside the palette.** Black, white, teal, gray. That's it.
- **AI copy tells.** No em-dashes, no "delve into," no "seamlessly," no "leverage." Read the voice guide.
