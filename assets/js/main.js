(function () {
  var apps = window.SAMZLAB_APPS || [];
  var grid = document.getElementById("apps-grid");
  var plist = document.getElementById("policies");
  var count = document.getElementById("app-count");
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function play(a) { return "https://play.google.com/store/apps/details?id=" + encodeURIComponent(a.package); }

  if (grid) {
    grid.innerHTML = apps.map(function (a) {
      var live = a.status === "live";
      return '<article class="card reveal">' +
        '<div class="card-top"><img class="app-icon" src="' + esc(a.icon) + '" width="72" height="72" alt="' + esc(a.short) + ' icon">' +
        '<div><h3>' + esc(a.name) + '</h3><p class="tagline">' + esc(a.tagline) + '</p></div></div>' +
        '<p class="desc">' + esc(a.description) + '</p>' +
        '<ul class="tags">' + a.tags.map(function (t) { return "<li>" + esc(t) + "</li>"; }).join("") + "</ul>" +
        '<div class="actions">' +
        (live ? '<a class="btn primary" href="' + play(a) + '" rel="noopener">Get it on Google Play</a>'
              : '<span class="btn soon" aria-disabled="true">Coming soon to Google Play</span>') +
        '<a class="btn ghost" href="' + esc(a.privacy) + '">Privacy policy</a></div></article>';
    }).join("");
  }
  if (plist) plist.innerHTML = apps.map(function (a) { return '<a href="' + esc(a.privacy) + '">' + esc(a.short) + " privacy</a>"; }).join("");
  if (count) count.textContent = apps.length + (apps.length === 1 ? " app" : " apps");
  document.querySelectorAll("[data-email]").forEach(function (el) {
    var e = window.SAMZLAB_EMAIL; el.textContent = e; el.setAttribute("href", "mailto:" + e);
  });
  var y = document.getElementById("year"); if (y) y.textContent = new Date().getFullYear();

  // theme toggle (remembered when storage is available)
  var root = document.documentElement, btn = document.getElementById("theme");
  try { var t = localStorage.getItem("theme"); if (t) root.setAttribute("data-theme", t); } catch (e) {}
  if (btn) btn.addEventListener("click", function () {
    var cur = root.getAttribute("data-theme") || (matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark");
    var next = cur === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", next);
    try { localStorage.setItem("theme", next); } catch (e) {}
  });

  // gentle reveal on scroll
  var items = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }); }, { threshold: 0.12 });
    items.forEach(function (el, i) { el.style.transitionDelay = (i % 3) * 70 + "ms"; io.observe(el); });
  } else items.forEach(function (el) { el.classList.add("in"); });
})();
