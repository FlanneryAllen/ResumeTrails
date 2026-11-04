# Resume Trail Platform

A job description goes in. A one-page resume trail comes out.

## Folder structure

```
resume-trail-platform/
├── vault/
│   └── cards/          ← evidence cards (markdown + frontmatter)
├── generator/
│   └── generate.py     ← simple script that builds a trail HTML from a job + selected cards
├── templates/
│   └── trail.html      ← the page template (Radical Optimism + flanneryallen look)
├── sites/              ← generated trails live here
├── skills/
│   └── author-job-proof-trail/SKILL.md
└── README.md
```

## Evidence card format

Each card is a markdown file with YAML frontmatter:

```yaml
---
type: evidence
tags: [strategy, internal-comms, ai]
good_for: [strategic-internal-comms, ai-vision]
confidentiality: public   # public | replica | raw-private
description: One line a stranger can understand.
---
```

Body: context, what you did, result, and a replica note. Only `public` and `replica` cards are used in published trails.

## How to generate a trail today

1. Add or edit cards in `vault/cards/`.
2. Run the generator (see below) with a job description and the card filenames that match.
3. Open the HTML in `sites/`.

## Generator (simple version)

```bash
cd generator
python generate.py --job "path/to/job.txt" --cards cisco-ai-messaging.md narrative-agent-prototypes.md --out ../sites/my-trail.html
```

The script reads the job, pulls the selected cards, and writes a self-contained HTML file using the template. No server required. Host the `sites/` folder on GitHub Pages.

## Next steps to make it fully automatic

- Add an LLM step that reads the job and ranks cards by `tags` + `good_for` + description.
- Hook the existing chatbot on flanneryallen.com so a hiring manager can paste a JD and get the page.
- Keep the vault in Git so every new piece of work is one commit.

## Home page

`index.html` is the entry point. A hiring manager (or you) pastes a job description or drops a URL and clicks Generate trail. The current version is the UI; the generate button is ready to call the skill / generator that walks the vault and writes a new file into `sites/`.

Open `index.html` in a browser or host the whole folder on GitHub Pages.
