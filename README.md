# TRACC LAB

English-language research lab website for Junqiang Zhao at the University of Rochester.

## Publish on GitHub Pages

1. Sign in to GitHub as `tracclab`.
2. Create a public repository named `tracclab.github.io`.
3. Upload the contents of this folder to the repository root, including `index.html`, `styles.css`, `script.js`, and the `assets` folder. Do not upload the ZIP file itself or put everything inside an extra enclosing folder.
4. Open **Settings > Pages**. Select **Deploy from a branch**, choose **main** and **/(root)**, then save.
5. When deployment completes, the website will be available at https://tracclab.github.io/.

## Update content

- `index.html`: biography, publications, links, and page content.
- `styles.css`: colors, typography, and layout.
- `script.js`: research panel content and publication filtering.
- `assets/`: portrait and proposed visual mark.

There are no dependencies or build steps. To preview locally, run `python3 -m http.server 4173` in this folder.

## Team profiles

The Team section in `index.html` has one placeholder profile per group: Postdoctoral Fellows, Graduate Students, Undergraduate Students, and Administrative Staff. All names are `FirstName LastName`, and portrait areas are deliberately empty.

To update a profile, replace its name in the corresponding `team-member` article. When a portrait is available, add it to `assets/` and replace the blank `div.team-photo` with:

```html
<img class="team-photo" src="assets/member-name.jpg" alt="FirstName LastName" width="400" height="500" loading="lazy">
```

Duplicate a `team-member` article within its group to add more members. Names and portraits are static HTML; no JavaScript change is needed.

## Content sources

- https://www.urmc.rochester.edu/people/112365270-junqiang-zhao
- https://pubmed.ncbi.nlm.nih.gov/40022142/
- https://pubmed.ncbi.nlm.nih.gov/40549433/
- https://pubmed.ncbi.nlm.nih.gov/38697178/

The lab name was supplied by the site requester. Its acronym has not been expanded. The headline, research framing, and SVG mark are proposed website copy and design. The Team section contains explicitly requested placeholder names and empty portrait areas; it does not identify actual members. No funded projects or open positions have been invented. Selected publications are not a complete publication list. Contact uses an email link.
