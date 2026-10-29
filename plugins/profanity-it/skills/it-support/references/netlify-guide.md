# Netlify Guide — Profanity Creative

Reference for hosting and deployment. Covers Netlify Drop, GitHub-connected auto-deploy, domains, environment variables, and debugging.

---

## Which Deployment Method to Use

| Scenario | Method |
|---|---|
| Quick one-off HTML tool or prototype | Netlify Drop |
| Ongoing project that will be updated | GitHub → Netlify connected deploy |
| Framer site | Framer's built-in publish (not Netlify) |

---

## Netlify Drop — Quick Deploy

For standalone HTML tools (calculators, generators, single-page apps).

1. Go to [app.netlify.com/drop](https://app.netlify.com/drop)
2. Drag your project folder (or single `.html` file) onto the drop zone
3. Netlify generates a random URL instantly (e.g., `https://random-name-123.netlify.app`)
4. To rename: **Site settings → Site details → Change site name**

**Limitation:** Netlify Drop doesn't auto-redeploy on changes. To update, drag again — it replaces the current deploy.

---

## GitHub → Netlify Connected Deploy (Auto-Deploy on Push)

For tools and projects that will be updated regularly.

### Initial Setup

1. Push your project to a GitHub repo
2. Log in to [app.netlify.com](https://app.netlify.com) → **Add new site → Import an existing project**
3. Choose **GitHub** → authorize if needed → select the repo
4. Configure build settings:
   - **Base directory:** leave blank unless your project is in a subfolder
   - **Build command:** e.g., `npm run build` (or leave blank for static HTML)
   - **Publish directory:** e.g., `dist`, `build`, or `.` for root
5. Click **Deploy site**

After setup, every push to `main` triggers a new deploy automatically.

### Checking Deploy Status

- Dashboard → select the site → **Deploys** tab
- Each deploy shows status (Published, Failed, Building)
- Click a deploy to see the build log

---

## Custom Domain and DNS Setup

1. **Site settings → Domain management → Add custom domain**
2. Enter your domain (e.g., `tools.profanitycreative.com`)
3. Netlify shows you the DNS records to add:
   - For a subdomain: add a **CNAME** record pointing to your Netlify site URL
   - For a root domain: add an **A record** (or ALIAS/ANAME) pointing to Netlify's load balancer IP
4. Add these records in your domain registrar's DNS settings (wherever you bought the domain)
5. DNS propagation: up to 48 hours, usually faster

**HTTPS:** Netlify provisions a free SSL certificate automatically once the domain is verified. It can take a few minutes after DNS propagates.

---

## Environment Variables

For API keys, secrets, or config values your project needs.

1. **Site settings → Environment variables → Add a variable**
2. Set the key (e.g., `API_KEY`) and value
3. Redeploy the site — env vars are injected at build time

**Never commit secrets to the repo.** Use Netlify env vars for anything sensitive.

In your code, access them as:
```javascript
// In a Netlify Function
process.env.API_KEY

// In a Vite/React build (must be prefixed with VITE_)
import.meta.env.VITE_API_KEY
```

---

## Netlify Functions (Serverless)

For anything needing server-side logic that Framer can't handle.

Create a `netlify/functions/` directory in your project root:

```
project/
├── netlify/
│   └── functions/
│       └── my-function.js
├── index.html
```

Basic function template:

```javascript
// netlify/functions/my-function.js
exports.handler = async (event, context) => {
  const { param } = JSON.parse(event.body)

  return {
    statusCode: 200,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ result: "success" }),
  }
}
```

Access at: `https://your-site.netlify.app/.netlify/functions/my-function`

Build command for projects with functions: `netlify build` (requires Netlify CLI) or just push and let Netlify detect them.

---

## Debugging Failed Deploys

1. **Deploys tab → click the failed deploy → read the build log**
   - Scroll to the first red error — that's usually the cause
2. **Common causes:**
   - Missing `node_modules` — build command needs `npm install` before `npm run build`
   - Wrong publish directory — check what your build actually outputs
   - Missing environment variables — build might be referencing a var that isn't set
   - Node version mismatch — set in **Site settings → Environment variables** with key `NODE_VERSION` and value `18` (or whatever your project requires)

### Fix Node version

```
Key:   NODE_VERSION
Value: 18
```

Trigger a new deploy after adding this.

---

## CORS Issues for API-Connected Tools

If your Netlify-hosted tool is hitting a CORS error when calling an external API:

**Option 1 — Use a Netlify Function as a proxy** (cleanest)

```javascript
// netlify/functions/proxy.js
const fetch = require("node-fetch")

exports.handler = async (event) => {
  const response = await fetch("https://external-api.com/endpoint", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${process.env.API_KEY}`,
      "Content-Type": "application/json",
    },
    body: event.body,
  })

  const data = await response.json()

  return {
    statusCode: 200,
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
    body: JSON.stringify(data),
  }
}
```

**Option 2 — Add a `_headers` file** (only works if you control both ends)

```
# _headers (in your project root)
/*
  Access-Control-Allow-Origin: *
```

---

## Netlify CLI (Optional but Useful)

```bash
# Install
npm install -g netlify-cli

# Login
netlify login

# Deploy current folder manually (like Netlify Drop but from terminal)
netlify deploy --dir=. --open

# Deploy to production
netlify deploy --dir=. --prod

# Run locally with functions support
netlify dev
```

---

## Vercel

Vercel is the second deploy target. Use it when the project is Next.js or needs edge functions; stick with Netlify for everything else.

### Pick Vercel vs Netlify

| Project type | Use |
|---|---|
| Framer site | Framer publish (neither) |
| Static HTML, single-page tool, anything with Netlify Forms | **Netlify** |
| Next.js app | **Vercel** |
| Edge functions / middleware | **Vercel** |
| Quick drag-and-drop one-off | **Netlify** Drop |

If it's not obvious, ask Mark before deploying.

### Deploying via the Vercel MCP

The Vercel MCP is wired in this setup. Key tools:

- `mcp__a659a248-7ba3-432b-886c-f4096930c956__deploy_to_vercel` — kick off a deploy from the current project
- `mcp__a659a248-7ba3-432b-886c-f4096930c956__list_deployments` — list recent deployments for a project
- `mcp__a659a248-7ba3-432b-886c-f4096930c956__get_deployment` — inspect a specific deployment (status, URL, age)
- `mcp__a659a248-7ba3-432b-886c-f4096930c956__get_deployment_build_logs` — pull build logs for a failed or in-flight deploy
- `mcp__a659a248-7ba3-432b-886c-f4096930c956__get_runtime_logs` — runtime logs for a running deployment
- `mcp__a659a248-7ba3-432b-886c-f4096930c956__list_projects` / `get_project` — project metadata
- `mcp__a659a248-7ba3-432b-886c-f4096930c956__check_domain_availability_and_price` — domain lookup before buying

### Where to check Vercel build logs

1. First try the MCP: `get_deployment_build_logs` with the deployment ID.
2. If you need the UI: Vercel dashboard → project → **Deployments** → click the failed build → **Build Logs** tab.
3. Runtime errors (after deploy succeeds but pages crash) live in **Logs** → **Runtime Logs** in the dashboard, or `get_runtime_logs` via MCP.

### Domains on Vercel

Same idea as Netlify — point a CNAME at `cname.vercel-dns.com` for subdomains, or use Vercel's A record for the apex. Vercel issues SSL automatically once DNS resolves.
