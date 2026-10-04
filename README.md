# Sayed Abdallah Portfolio

Cinematic black-and-gold video-editor portfolio with category routing and a two-row client logo marquee using the verified client marks.

Live site: https://sayedabdallah.pages.dev

Production client logo strip refreshed with the approved uploaded marks.

## Portfolio routing

`script.js` is the reviewed source for categories, collections, video IDs and
player behavior. It includes the published portfolio data recovered on
2026-10-04. `site-updates.js` only provides client-strip controls; it must not
mutate category data or render pages after player/reveal initialization.

Run `node --test tests/portfolio-routing.test.cjs` before and after generating
the homepage. The deployment uses the checked-in script rather than fetching
mutable JavaScript from production. Media files are still retrieved from the
existing published media archive during deployment.

Legacy Sports & Events collection bookmarks are normalized to their matching
Sports or Events collection. A bookmark without a collection opens the category
chooser. Unknown routes show an explicit unavailable page.
