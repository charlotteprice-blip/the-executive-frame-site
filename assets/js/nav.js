document.addEventListener('DOMContentLoaded', function() {
  var nav = document.getElementById('site-nav');
  if (nav) {
    nav.outerHTML = `<nav class="site-nav site-nav-dark">
  <div class="nb-brand">
    <a href="index.html" class="nb-top">Executive Frame<span class="tm">™</span></a>
    <div class="nb-sub">Human first. Then performance.</div>
  </div>
  <div class="nl">
    <a href="framework.html" class="nav-link">What</a>
    <a href="science.html" class="nav-link">Why</a>
    <a href="method.html" class="nav-link">How</a>
    <a href="about-sarah.html" class="nav-link nav-link-sarah">About Sarah</a>
    <div class="nav-dropdown">
      <a class="nav-link nav-dropdown-trigger">Programs <span class="caret">▾</span></a>
      <div class="nav-dropdown-panel">
        <a href="health.html" class="nav-dd-item"><span class="dd-dot" style="background:#5B8F7B;"></span>Executive Frame Health</a>
        <a href="health-dgbi.html" class="nav-dd-item nav-dd-sub"><span class="dd-dot" style="background:#5B8F7B;"></span>↳ Executive Frame Health — DGBI</a>
        <a href="health-elearning.html" class="nav-dd-item nav-dd-sub"><span class="dd-dot" style="background:#5B8F7B;"></span>↳ Executive Frame Health — eLearning</a>
        <a href="elite.html" class="nav-dd-item"><span class="dd-dot" style="background:#C9874E;"></span>Executive Frame Elite</a>
        <a href="corporate.html" class="nav-dd-item"><span class="dd-dot" style="background:#6B8AA8;"></span>Executive Frame Corporate</a>
        <a href="law.html" class="nav-dd-item"><span class="dd-dot" style="background:#8FA3B8;"></span>Executive Frame Law</a>
        <a href="law-family.html" class="nav-dd-item nav-dd-sub"><span class="dd-dot" style="background:#8FA3B8;"></span>↳ Executive Frame Law — Family</a>
        <a href="women.html" class="nav-dd-item"><span class="dd-dot" style="background:#C28699;"></span>Executive Frame Women</a>
        <a href="neurodiversity.html" class="nav-dd-item"><span class="dd-dot" style="background:#8B7BA8;"></span>Executive Frame Neurodiversity</a>
        <a href="family.html" class="nav-dd-item"><span class="dd-dot" style="background:#B68A6F;"></span>Executive Frame Family Systems</a>
        <a href="consulting.html" class="nav-dd-item"><span class="dd-dot" style="background:#6FA0A4;"></span>C³ Consulting</a>
        <a href="partners.html" class="nav-dd-item nav-dd-divider"><span class="dd-dot" style="background:#FFFFFF;opacity:0.5;"></span>Partner organisations</a>
      </div>
    </div>
    <a href="deck.html" class="nav-link nav-link-accent">The Deck</a>
    <a href="partners.html" class="nav-link nav-link-partners">For Partners</a>
    <a href="store.html" class="nav-link">Store</a>
    <a href="enquire.html" class="nav-link">Get in touch</a>
    <a href="referral.html" class="nav-cta">Make a referral</a>
  </div>
</nav>`;
  }
});
