# Engineering portfolio

Kyle Dick's portfolio at https://kyledick96.github.io, built with GitHub Pages and standard Jekyll/Liquid. No JavaScript framework, external font, custom plugin or npm build is required.

## Content map

| Content | Edit |
| --- | --- |
| Hero, about, contact and social links | `_data/profile.yml` |
| Personal About page | `_includes/about.html` (page: `about.md`) |
| Employment | `_data/experience.yml` |
| Education / coursework | `_data/education.yml` / `_data/coursework.yml` |
| Project cards and shared metadata | `_data/projects.yml` |
| Project case studies | `projects/*.md` |
| Skill categories | `_data/skills.yml` |
| Site settings | `_config.yml` |

Experience displays in YAML order. Keep the two SMART Centre engagements separate and retain their client fields. Education uses `qualification`, `institution`, `location`, `period`, `status`, `details` and `featured`. Coursework groups by `category`; each entry supplies a subject-area title, description and technologies. Its titles need not be official course names. All coursework remains accessible regardless of its featured flag.

## Add or edit a project

1. Add an entry to `_data/projects.yml` with a unique `slug`, title, subtitle/type, summary, featured flag, technologies and `page` path. Use `null` for unknown year/status, an unavailable image or an unconfirmed project GitHub URL. Use `documents: []` when there are no artifacts.
2. Create `projects/<slug>.md` with the front matter below and write the case study in Markdown. Match its permalink to the YAML `page` value.
3. Include documents and technology badges where appropriate using the existing project pages as examples. Titles, summaries and other shared metadata come from YAML.

```yaml
---
layout: project
project: example
permalink: /projects/example/
---
```

`subtitle` currently supplies the project type. An optional separate `type` is supported by the project layout. Optional `dates` overrides the year display on detail pages. Images use `image` and descriptive `image_alt` fields. Document entries use `title` and `url`. The homepage lists all projects in YAML order in a numbered index. The featured flag remains available for other views.

Skills use a list of `category` / `items` groups. Preserve qualifications such as working knowledge; do not add proficiency scores.

## Presentation and assets

`index.md` includes `_includes/home.html`. `about.md` adds a dedicated About page at `/about/`. The monochrome theme uses system monospace fonts, an offset wordmark, and a numbered project index inspired by the supplied skills.sh reference. Shared cards, navigation and small list components live in `_includes/`; page shells live in `_layouts/`. The project layout reads metadata by slug.

Edit the CSS custom properties at the top of `assets/css/style.css` to change the theme. Responsive rules are near the bottom. Navigation and expandable detail sections work without JavaScript.

Keep existing Documents, Diagrams, Presentations, Node-RED Flow and SDACS Datasets paths intact. Add new images or PDFs to the relevant directory without moving old files. Use exact filename case and URL-encode spaces and ampersands. In Markdown, use Jekyll's `relative_url` filter, for example:

```liquid
[Report]({{ '/Documents/report.pdf' | relative_url }})
```

The two robot reports were copied into Documents with their original filenames; their source copies were preserved. Historical PDFs describe the project stage at which they were written. The résumé PDF still needs its candidate/graduation wording reviewed separately.

## Review and deployment

Version 2 work stays on `portfolio-v2-content`. This implementation does not change main, push commits or change GitHub Pages settings. Verify the repository's configured Pages deployment source before publishing; committing to this content branch alone is not a deployment instruction.

Run `git diff --check` and review changed links and YAML before committing. With Python and PyYAML already available, run `python scripts/validate_portfolio.py` for static checks. If Ruby/Jekyll is available, also build with `jekyll build` and inspect the homepage and project pages on desktop and mobile. Static checks do not replace a Jekyll build or browser review.
