#!/usr/bin/env python3
"""Sync plugin source (a folder of plugin dirs from Dropbox plugin-dev) into this marketplace repo.

Usage: sync_plugins.py <extracted_src_dir> <repo_root>
- Copies each plugin listed in PLUGINS into <repo>/plugins/<name>/ (full replace).
- If a plugin's content changed but its plugin.json version did not go up, bumps the patch
  version so Cowork's marketplace sync sees an update. Bumps are printed as
  BUMP <name> <old> <new> so the caller can write the same version back to Dropbox.
- Regenerates .claude-plugin/marketplace.json.
Prints CHANGED <name> for every plugin whose content changed, and NOCHANGE if none did.
"""
import sys, os, json, hashlib, shutil, re, pathlib

PLUGINS = ["profanity-willa","profanity-lyle","profanity-james","profanity-sloane","profanity-reid",
           "profanity-kai","profanity-dusty","profanity-nora","profanity-it","profanity-workflows"]
SKIP = {".DS_Store", "__pycache__", ".mcpb-cache", ".git"}

def files(d):
    out = []
    for root, dirs, fs in os.walk(d):
        dirs[:] = [x for x in dirs if x not in SKIP]
        for f in fs:
            if f in SKIP or f.endswith(".pyc"): continue
            out.append(pathlib.Path(root, f))
    return sorted(out)

def digest(d):
    """Content hash that ignores version numbers, so a pure version bump isn't a 'change'."""
    h = hashlib.sha256()
    for p in files(d):
        rel = p.relative_to(d).as_posix(); b = p.read_bytes()
        if rel == ".claude-plugin/plugin.json":
            j = json.loads(b); j.pop("version", None); b = json.dumps(j, sort_keys=True).encode()
        elif rel.endswith("SKILL.md"):
            b = re.sub(rb"(?m)^version:.*$", b"version:", b)
        h.update(rel.encode() + b"\0" + b + b"\0")
    return h.hexdigest()

def vtuple(v):
    try: return tuple(int(x) for x in v.split("."))
    except Exception: return (0, 0, 0)

def main(src, repo):
    src, repo = pathlib.Path(src), pathlib.Path(repo)
    entries, changed = [], []
    for name in PLUGINS:
        s = src / name; dst = repo / "plugins" / name
        if not (s / ".claude-plugin/plugin.json").exists():
            print(f"MISSING {name}"); continue
        sj = json.loads((s / ".claude-plugin/plugin.json").read_text())
        if sj.get("name") != name: print(f"NAMEMISMATCH {name} {sj.get('name')}"); continue
        old_v = None
        if (dst / ".claude-plugin/plugin.json").exists():
            old_v = json.loads((dst / ".claude-plugin/plugin.json").read_text()).get("version")
        is_changed = not dst.exists() or digest(s) != digest(dst)
        if is_changed:
            if dst.exists(): shutil.rmtree(dst)
            shutil.copytree(s, dst, ignore=shutil.ignore_patterns(*SKIP, "*.pyc"))
            changed.append(name); print(f"CHANGED {name}")
            v = sj.get("version", "0.0.0")
            if old_v and vtuple(v) <= vtuple(old_v):
                a, b, c = (list(vtuple(old_v)) + [0, 0, 0])[:3]; new_v = f"{a}.{b}.{c+1}"
                pj = dst / ".claude-plugin/plugin.json"; j = json.loads(pj.read_text()); j["version"] = new_v
                pj.write_text(json.dumps(j, indent=2) + "\n"); print(f"BUMP {name} {v} {new_v}")
        j = json.loads((dst / ".claude-plugin/plugin.json").read_text())
        entries.append({"name": name, "source": f"./plugins/{name}", "description": j.get("description", ""), "version": j.get("version")})
    mk = {"name": "profanity", "owner": {"name": "Mark Cernosia"},
          "metadata": {"description": "Profanity Creative's agent team plugins. Source of truth; edited in Dropbox plugin-dev and pushed nightly."},
          "plugins": entries}
    (repo / ".claude-plugin").mkdir(exist_ok=True)
    (repo / ".claude-plugin/marketplace.json").write_text(json.dumps(mk, indent=2) + "\n")
    if not changed: print("NOCHANGE")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
