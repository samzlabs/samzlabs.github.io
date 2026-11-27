# SAMZLAB website (GitHub Pages)

**Publish:** repo `samzlabs/samzlabs.github.io` -> delete the old files -> upload everything in this folder (keep the folder structure and the hidden `.nojekyll`) -> Settings > Pages > Deploy from branch `main` / root. Live at https://samzlabs.github.io/

**Add a new app:** open `assets/js/apps.js`, copy one `{ ... }` block, change name / package / tagline / description / tags, add its icon to `assets/img/`, and (optional) a privacy page: copy `privacy/rimota/`, edit `policy_*.md`, run `python _build_pages.py`. The app appears on the home page automatically.

**App status:** `status: "soon"` shows "Coming soon", `status: "live"` shows the Google Play button. Rimota: change it to `"live"` the day it is published.

**Privacy URLs for Play Console:** `https://samzlabs.github.io/privacy/rimota/` and `https://samzlabs.github.io/privacy/languardpro/`
Email, colours (top of `assets/css/style.css`) and text are all plain files - no build step.

**Terms:** `terms/rimota/index.html` is a hand-made standalone page (kept exactly as published) - the page builder does not touch it.
