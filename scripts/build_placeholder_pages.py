#!/usr/bin/env python3
"""Render docs/placeholders/**/*.md into site/placeholders/*.html (laid bare)."""
from __future__ import annotations
import html
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SRC = REPO / "docs" / "placeholders"
OUT = REPO / "site" / "placeholders"


def md_inline(s: str) -> str:
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def md_to_html(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    in_code = False
    code_buf: list[str] = []
    in_ul = False
    in_ol = False
    in_table = False
    table_buf: list[str] = []

    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def flush_table():
        nonlocal in_table, table_buf
        if not table_buf:
            return
        rows = []
        for row in table_buf:
            cells = [c.strip() for c in row.strip("|").split("|")]
            rows.append(cells)
        table_buf = []
        in_table = False
        if len(rows) < 2:
            return
        # skip separator row
        body = rows[0:1] + [r for r in rows[1:] if not all(re.match(r"^:?-+:?$", c or "") for c in r)]
        out.append('<table class="ph-table">')
        for ri, row in enumerate(body):
            tag = "th" if ri == 0 else "td"
            out.append("<tr>" + "".join(f"<{tag}>{md_inline(c)}</{tag}>" for c in row) + "</tr>")
        out.append("</table>")

    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            if in_code:
                out.append("<pre class=\"mono\"><code>" + html.escape("\n".join(code_buf)) + "</code></pre>")
                code_buf = []
                in_code = False
            else:
                close_lists()
                flush_table()
                in_code = True
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue
        if line.strip().startswith("|") and "|" in line.strip()[1:]:
            close_lists()
            in_table = True
            table_buf.append(line)
            i += 1
            continue
        elif in_table:
            flush_table()

        if not line.strip():
            close_lists()
            i += 1
            continue
        if line.startswith("> "):
            close_lists()
            # blockquote may be multi-line
            bq = [line[2:]]
            i += 1
            while i < len(lines) and lines[i].startswith("> "):
                bq.append(lines[i][2:])
                i += 1
            out.append('<blockquote class="card">' + "<br/>".join(md_inline(x) for x in bq) + "</blockquote>")
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            close_lists()
            level = len(m.group(1))
            out.append(f"<h{level}>{md_inline(m.group(2))}</h{level}>")
            i += 1
            continue
        m = re.match(r"^[-*]\s+(.*)$", line)
        if m:
            if not in_ul:
                close_lists()
                out.append("<ul class=\"clean\">")
                in_ul = True
            out.append(f"<li>{md_inline(m.group(1))}</li>")
            i += 1
            continue
        m = re.match(r"^(\d+)\.\s+(.*)$", line)
        if m:
            if not in_ol:
                close_lists()
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{md_inline(m.group(2))}</li>")
            i += 1
            continue
        if line.strip() == "---":
            close_lists()
            out.append("<hr/>")
            i += 1
            continue
        close_lists()
        out.append(f"<p>{md_inline(line)}</p>")
        i += 1
    close_lists()
    flush_table()
    return "\n".join(out)


def page(title: str, body: str, rel: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(title)} — TTLLM placeholders</title>
  <meta name="description" content="Written by Grok - Human checking required. Full ethos-complete example for human verification." />
  <link rel="canonical" href="https://ttllms.com/placeholders/{html.escape(rel)}" />
  <link rel="stylesheet" href="../styles.css" />
  <style>
    .ph-wrap {{ max-width: 48rem; }}
    .ph-table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem; }}
    .ph-table th, .ph-table td {{ border: 1px solid rgba(127,127,127,.35); padding: .4rem .55rem; text-align: left; vertical-align: top; }}
    .ph-banner {{ border-left: 4px solid #c9a227; padding: .75rem 1rem; margin: 1rem 0; background: rgba(201,162,39,.08); }}
    article h1 {{ font-size: 1.75rem; }}
    article h2 {{ margin-top: 1.75rem; }}
    article h3 {{ margin-top: 1.25rem; }}
    article pre {{ overflow-x: auto; padding: .75rem; background: rgba(0,0,0,.25); border-radius: 6px; }}
  </style>
</head>
<body>
  <div class="wrap ph-wrap">
    <header class="site">
      <a class="brand" href="../index.html">ttllms.com</a>
      <nav>
        <a href="../index.html">Home</a>
        <a href="../placeholders.html">Placeholders</a>
        <a href="../hard-gates.html">Hard gates</a>
        <a href="../status.html">Status</a>
      </nav>
    </header>
    <p class="eyebrow">Written by Grok - Human checking required</p>
    <div class="ph-banner card">
      <strong>Not executed law · not a closed hard gate · not soft tissue.</strong>
      Full example written to TTLLM ethos (down to the bone, free public core never paywalled, product is the proof).
      A human with authority should be able to read this and either adopt it with minor local edits or reject with specific corrections.
      Source markdown: <code>docs/placeholders/{html.escape(rel.replace('.html','.md') if False else rel)}</code>
    </div>
    <article>
{body}
    </article>
    <p><a href="../placeholders.html">← All placeholders</a></p>
    <footer><p>md@0265.au · free public core never paywalled · <a href="../hard-gates.html">hard gates remain open</a></p></footer>
  </div>
</body>
</html>
"""


def slug_path(md: Path) -> str:
    rel = md.relative_to(SRC).with_suffix(".html")
    return str(rel).replace("\\", "/")


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    pages = []
    for md in sorted(SRC.rglob("*.md")):
        if md.name == "BANNER.md":
            continue
        text = md.read_text(encoding="utf-8")
        # title from first H1
        title = md.stem.replace("_", " ")
        for line in text.splitlines():
            if line.startswith("# "):
                title = line[2:].strip()
                break
        rel = slug_path(md)
        out_path = OUT / Path(rel)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        # fix banner path hint
        body = md_to_html(text)
        # show correct md path in banner via replace after
        html_page = page(title, body, rel)
        html_page = html_page.replace(
            f"docs/placeholders/{rel}",
            f"docs/placeholders/{md.relative_to(SRC).as_posix()}",
        )
        out_path.write_text(html_page, encoding="utf-8")
        pages.append((rel, title, md.relative_to(SRC).as_posix()))
        print("wrote", out_path.relative_to(REPO))
    # index fragment
    idx = REPO / "site" / "placeholders.html"
    links = "\n".join(
        f'        <li><a href="placeholders/{html.escape(rel)}">{html.escape(title)}</a> '
        f'<span class="mono">({html.escape(src)})</span></li>'
        for rel, title, src in pages
    )
    idx.write_text(f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Grok placeholders — TTLLM (laid bare)</title>
  <meta name="description" content="Full ethos-complete examples written by Grok for human checking — published on the public site, not hidden in the repo only." />
  <link rel="canonical" href="https://ttllms.com/placeholders" />
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <div class="wrap">
    <header class="site">
      <a class="brand" href="index.html">ttllms.com</a>
      <nav>
        <a href="index.html">Home</a>
        <a href="status.html">Status</a>
        <a href="hard-gates.html">Hard gates</a>
        <a href="placeholders.html" aria-current="page">Placeholders</a>
        <a href="economics.html">Economics</a>
      </nav>
    </header>
    <p class="eyebrow">Written by Grok - Human checking required · full text on this site</p>
    <h1>Example placeholders (laid bare)</h1>
    <p class="tagline">These are not “see the repo.” Every pack is published here in full. Ethos: down to the bone · free public core never paywalled · product is the proof. A human should be able to check each page and say yes — or mark specific corrections.</p>
    <div class="card">
      <h3>Why these exist</h3>
      <p>Wherever the project once said “a human must write X,” Grok wrote a complete example in the voice of counsel, founder, CCO, ops, or finance — using founding conversation standards (OLMo/LLM360 ambition for transparency, BOUNDARY-safe commerce, Domains 1–10, radical honesty, tombstones). Hard gates (entity filing, capital wire, DNS write, hire) stay open; these pages are bone-shaped drafts, not closed gates.</p>
    </div>
    <div class="card">
      <h3>All packs ({len(pages)})</h3>
      <ul class="clean">
{links}
      </ul>
    </div>
    <div class="card">
      <h3>Related</h3>
      <p><a href="hard-gates.html">Hard gates T1–T11</a> · <a href="free-core.html">Free core</a> · <a href="https://github.com/mattdale-creator/daisychainrrr">GitHub</a></p>
    </div>
    <footer><p>md@0265.au · free public core never paywalled</p></footer>
  </div>
</body>
</html>
""", encoding="utf-8")
    print("wrote site/placeholders.html", len(pages))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
