# TRACC Lab website

A static, responsive research lab website for the University of Rochester TRACC Lab — Translating Research into Action in Cancer Care.

## Pages

- `index.html`: mission, expertise, research overview, news, and contact.
- `research.html`: four research areas, current projects with expandable full descriptions, and future directions.
- `people.html`: principal investigator and research team biographies.
- `news.html`: lab news and the supplied symposium photograph.

## Editing

Edit `content/site.json`, then run:

```sh
python3 tools/build_site.py
```

The builder uses only the Python standard library and writes the four HTML files. Commit both the content change and regenerated HTML. Appearance is controlled by `styles.css`; `script.js` controls only the mobile navigation. Project descriptions use native HTML details elements and work without JavaScript.

To add a member, use an existing person record in `content/site.json` as a model. Place their portrait in `assets/` and reference its relative path in `photo`. Use `null` to keep an empty portrait area. Members are alphabetized by surname within each group; the PI remains first and Research management remains last. All current biographies are sourced from the supplied lab documents; the previous fictional placeholder profiles have been removed.

## Preview and publication

```sh
python3 -m http.server 4186
```

Open http://localhost:4186/. GitHub Pages publishes the repository root from `main`. This site needs no dependency installation, build service, framework, or server backend. The contact action opens the visitor's email application.

Use a feature branch in the contributor fork and open a pull request against `tracclab/tracclab.github.io:main`. Merging the pull request updates the published website.

## Content provenance

The redesign uses the supplied `Website content - TRACC Lab.docx` for page content and `Yutong Xu bio and photo.docx` for Yutong's biography and higher-resolution portrait. The Thematic Research Poster Version 2 supplies the lab goal and future directions. The Poster itself and all original Word/PowerPoint/PDF documents are intentionally excluded from the website and repository.

The supplied monochrome lab logo is used for the site identity. Available standalone portraits and the symposium photograph are included. The PI portrait was retained from the existing website. No portraits were inferred by cropping the Poster's group composite.

Zijun Xie's spelling was explicitly confirmed by the requester despite the photo caption's spelling variant. At the requester's direction, graduate titles are standardized to Research Assistant · PhD Candidate or Research Assistant · MS Candidate, and only the PI has a degree suffix after the name. Research management follows the student groups. Grammar corrections include the undergraduate's opening sentence and replacing a conflicting pronoun in Jingqiu Zhang's biography with her name.

The older website archive supplied under Downloads could not be read as a ZIP; its file signature indicates a protected container. It was not used.

No project findings, recruitment openings, funding awards, or news dates beyond the supplied year have been invented. Previous selected-publication content has been replaced by the supplied current research material; the PI's full publication record remains linked through Google Scholar. The knowledge-base project links to its supplied publication URL.
