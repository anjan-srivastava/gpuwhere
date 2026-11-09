/* First-party, cookieless page analytics for GPU Where.
 *
 * Posts small JSON events to /a, where the edge worker writes them to Workers
 * Analytics Engine (see server/api_worker.mjs and scripts/analytics_report.py).
 *
 * No cookies. A random session id lives in sessionStorage for the tab. The
 * referrer is sent in full but reduced to its hostname at the edge. Do Not
 * Track, Global Privacy Control and automated browsers are not measured.
 */
(function () {
  "use strict";

  var sid = "";
  try {
    sid = sessionStorage.getItem("ga.sid") || "";
    if (!sid) {
      sid = (window.crypto && crypto.randomUUID)
        ? crypto.randomUUID()
        : String(Date.now()) + Math.random().toString(16).slice(2);
      sessionStorage.setItem("ga.sid", sid);
    }
  } catch (e) {}

  var off = navigator.doNotTrack === "1"
    || navigator.globalPrivacyControl === true
    || navigator.webdriver === true;

  var lastPath = "";
  var lastAt = 0;

  function send(event, label, target) {
    if (off) return;
    var body = JSON.stringify({
      e: event,
      s: sid,
      p: location.hash || location.pathname || "/",
      l: String(label || "").slice(0, 120),
      t: String(target || "").slice(0, 300),
      r: document.referrer || ""
    });
    try {
      if (navigator.sendBeacon) {
        navigator.sendBeacon("/a", new Blob([body], { type: "text/plain;charset=UTF-8" }));
      } else {
        fetch("/a", {
          method: "POST",
          body: body,
          keepalive: true,
          headers: { "content-type": "text/plain;charset=UTF-8" }
        }).catch(function () {});
      }
    } catch (e) {}
  }

  window.TRACK = {
    pageview: function () {
      var path = location.hash || location.pathname || "/";
      var now = Date.now();
      if (path === lastPath && now - lastAt < 800) return;
      lastPath = path;
      lastAt = now;
      send("pageview", document.title, "");
    },
    click: function (label, target) { send("click", label, target); },
    search: function (query) { send("search", "", query); }
  };
})();
