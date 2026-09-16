# LAUNCH READINESS — Executive Frame™ + Sarah Anticich Consulting
_Pre-launch commercial & brand review · 23 Aug 2026 · package: ef-and-sarahanticich-sites_

## 1 · Changes made in this review pass
- **Resources is now the commercial product hub.** Product-led hero
  ("Shop the tools" is the primary CTA), and the flagship shelf sits
  directly under the hero: 4 products, each with a visual tile,
  audience line, one-sentence benefit, format, price, and ONE clear
  CTA. Context rows, free tools, groups, professional, Capacity
  Check close, and FAQ follow. Nothing is hidden behind filters.
- **Honest availability language everywhere.** "Direct checkout
  opening soon" replaced across the whole site with real actions:
  "Join the waitlist →" (pre-filled waitlist email per product) or
  "Enquire to enrol →". No "Coming soon", no fake Buy buttons.
- **Arm mini-stores relabelled to the four standard tiers**:
  Ways to work with EF|[Arm] · Start free → Work through it
  yourself → Learn alongside others → Work with a professional.
  Same components (site.css), arm-specific products and language.
- **Site roles separated.** sarahanticich.co.nz nav "Library" →
  "Publications"; the page is framed as the research & media
  record, and its tools band sends people to EF Resources ("Looking
  for tools? They live on Executive Frame™."). executiveframe.co.nz
  holds the framework, programmes, groups, products, and checkout.
- **Delivery expectations standardised**: digital products read
  "delivered by email after purchase"; thank-you.html explains the
  email delivery and has no download buttons.

## 2 · Live products (real checkout)
| Product | Price | Checkout |
|---|---|---|
| EF Health — DGBI Participant Workbook | $49 NZD | https://buy.stripe.com/7sY7sLgSj4wIcag9md4Ja00 (live, verified via Stripe API; tax-inclusive) |

Placements + tracking ids: Resources shelf (resources-health-workbook),
DGBI hub (dgbi-health-workbook), patient library (library-health-workbook),
EF|Health arm page (health-arm-workbook).

Live group registration: EF|Law 2026 cohort → https://tally.so/r/1ADR8g
(external Tally form — test from a NZ browser before launch).

## 3 · Products still needing Stripe links / fulfilment
| Product | Price shown | Current CTA |
|---|---|---|
| The Compassionate Gut Toolkit | $49 | Join the waitlist |
| S.H.I.F.T.™ Desk Cards | $39 | Join the waitlist (needs shipping fulfilment too) |
| C³ Values™ Deck | $59 | Join the waitlist (shipping) |
| EF Health Self-Paced Programme | $295–$495 | Enquire to enrol (needs tier pricing decision) |
| EF Neurodiversity Workbook | from $49 | Join the waitlist |
| EF Law Workbook | $89 | Join the waitlist |
| EF Health Tool Library (18-tool) | — | Email order on DGBI/library pages (price to confirm) |
Fulfilment note: ALL digital sales are currently fulfilled manually —
when a Stripe payment lands, someone must email the PDF. Decide who,
and how fast, before scaling. (Stripe payment links can't attach files;
consider a delivery automation later.)

## 4 · Redirects & hosting items to test after publishing
- _redirects file is Cloudflare Pages / Netlify format. Every retired
  page also has a meta-refresh stub, so redirects work either way —
  but TEST each on the live host: /ef-health, /ef-health-products,
  /health-elearning, /health-gut-brain, /library, /store.
- /assessment(.html): non-forced redirect to /executive-frame-assessment
  — only fires if the host has no assessment file. If a live
  assessment.html exists on the server, decide which is canonical.
- In Stripe dashboard: point the payment link's after-payment
  redirect at /thank-you.html (currently /resources.html) — I could
  not change it (API key is read-only).
- Intake form has no server endpoint (uses email-client fallback).
  Add a Formspree/endpoint URL for silent submission if wanted.
- Rotate the GitHub token in the Drive-mirrored .git/config.

## 5 · End-to-end purchase test (run on the live site, on a phone)
1. Home → Resources → flagship shelf visible without scrolling past
   more than the hero.
2. Tap "Buy now — $49" on the DGBI Participant Workbook → Stripe
   checkout opens in a new tab, shows $49 NZD → pay with a real card
   (refund after) → confirm redirect lands on the thank-you page.
3. Confirm the confirmation email from Stripe arrives, and the
   WORKBOOK PDF is emailed to the buyer (manual step — time it).
4. Tap "Join the waitlist" on the Gut Toolkit → email opens
   pre-addressed with the product name in the subject.
5. EF|Law → "Reserve a place" → Tally form loads and submits.
6. Intake form → submit → email arrives at admin@.
7. Download three free PDFs (starter bundle, phase worksheets, a
   FAQ sheet) on mobile data, not Wi-Fi.
8. Check /ef-health and /library redirect correctly.
9. Refund the test purchase in Stripe.


## Drive-sourced free libraries (populated Aug 2026)

Each arm page's "Start free" tier now links real, self-hosted PDFs sourced from the EF Google Drive
(21 new files in `/downloads/`). Highlights: a 9-item EF-ADHD library on the Neurodiversity page,
law handouts (family-lawyers intro, court cover triage form), the fillable EF|Elite Capacity Check,
per-arm real-time tools cards (Elite/Corporate/Women/Family), and two new EF|Health tools
(Triage Self-Assessment, Tracking Logs — also in the EF Health library page).
Paid workbooks discovered in Drive (Neurodiversity Workbook 1–3, Chaos to Clarity, EF-LAW Workbook — Centre)
remain unlisted as downloads; their shop cards stay waitlist-only until live Stripe Payment Links exist.
All internal/clinical documents (report templates, supervision records, facilitator manuals) were excluded.
