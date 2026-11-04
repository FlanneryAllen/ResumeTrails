---
name: author-job-proof-trail
description: Author a job-specific proof trail from a vault of evidence cards. Takes a job description, extracts requirements, matches against the local vault (desktop, proof folder, or OKF cards), and generates a shareable one-page HTML proof trail that maps each major job bullet to specific evidence with replicas and results. Fully local. Use when the user says "make a proof page for this job", "drop in this JD and generate the trail", "create a tailored portfolio for [role]", or invokes /author-job-proof-trail.
---

# Author Job Proof Trail

Turn a job description into a one-page, evidence-anchored proof trail. The trail is the website. Each section is a marker: the job’s language on one side, the matching proof card (context, action, result, replica) on the other.

This is the investigation trail adapted for hiring. You do not pick the cards. The skill walks the vault, ranks matches, leaves gaps visible, and writes the page.

## When to fire

- “Make a proof page for this job description”
- “Drop in the JD and generate the trail”
- “Create a tailored portfolio for the Cisco role”
- Explicit `/author-job-proof-trail`

## Vault assumptions

The vault can be:

- A designated folder of OKF/markdown proof cards with frontmatter (`type`, `tags`, `good_for`, `confidentiality`, `description`)
- The user’s desktop or a project folder (as in the July run)
- A mix

Only cards marked `confidentiality: public` or `replica` are used for published pages. Raw-private stays out.

## Authoring workflow

### 1. Extract requirements

Read the job description. Pull the real impact bullets and must-haves. Ignore fluff. Write them as a short ordered list. This is the “flow.”

### 2. Walk the vault

Search the vault for matching evidence. Use frontmatter tags and descriptions first, then read the strongest candidates. Rank against each requirement. Prefer cards that can be framed in the job’s language without inventing claims.

### 3. Select markers

For each major requirement, choose the primary proof card. Optional supporting card allowed. If no strong match, mark the gap. Exactly one subject marker for the overall strongest fit or the key proof.

### 4. Write the page

Generate a single self-contained HTML file. Structure:

- Header: Role + company + “Proof trail for this posting”
- One section per major requirement
- Job language quoted or closely paraphrased
- Proof: context, what I did, result (numbers where real)
- Replica or skeleton note
- Gap note when partial
- Footer: public/replica subset only

Quality bar from the original skill: factual, one claim per section, no editorializing, active voice, present tense, real identifiers.

### 5. Deliver

Write the HTML to a stable path (e.g. `sites/<slug>.html`). Optionally also write a small TrailPayload JSON if the local viewer is wanted. The HTML is the primary shareable artifact.

## Output rules

- Never invent proof, numbers, or outcomes.
- Gaps stay visible.
- Same card can support multiple requirements with different framing.
- Page must stand alone for a hiring manager who has never seen the vault.

## Example invocation

User pastes the Cisco Director, Internal Communications JD.

Skill extracts the five impact bullets, walks the vault, selects Cisco AI messaging framework + narrative systems + patents + employee listening work, and writes `sites/cisco-dir-internal-comms.html`.
