EXECUTIVE FRAME SITE — SIGNATURE GRADIENT UPDATE (Aug 2026)
============================================================
Ties executiveframe.co.nz into the amended sarahanticich.co.nz
design: the orange highlight (#E8A06A) is retired on the flagship
"spine" pages and replaced with the EF signature gradient +
the EF default sage-green accent (#6E9E86), exactly as used on
the personal site. Every arm keeps its own accent colour
(Law rust, Health green, Corporate blue, Women rose,
Neurodiversity violet, etc.) — arm pages are untouched.

CHANGED FILES (11)
  site.css          — · nav active link now follows the page accent
                      · footer accent orange → EF green
                      · "Premium" resource tags orange → signature mauve
                      · intake form focus ring / button glow now follow
                        the page accent (no hard-coded orange)
                      · new --sig-soft gradient variable
                      · new "SIGNATURE INK" layer: on pages whose <body>
                        has class "sigink", headline italics render in the
                        signature gradient, and card rules / quote bands /
                        list rules use the gradient
  index.html        — accent #E8A06A → #6E9E86, body class "sigink"
  why.html          —   (same)
  how.html          —   (same)
  about-sarah.html  —   (same)
  resources.html    —   (same)
  partners.html     —   (same)
  intake.html       —   (same)
  enquire.html      —   (same)
  library.html      — redirect stub link colour orange → green
  store.html        — redirect stub link colour orange → green

TO PUBLISH
  Replace these 11 files at the web root of executiveframe.co.nz
  (or commit them to the site's GitHub repo main branch — the
  deploy picks them up automatically). All other files unchanged.
