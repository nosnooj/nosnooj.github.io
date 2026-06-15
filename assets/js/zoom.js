// 도면 라이트박스 — .fig.zoomable 클릭 시 전체화면으로 크게 보기.
// 확대(+)/축소(−)/원래대로(⤢)/닫기(✕), Esc·배경 클릭으로 닫힘, 휠로 확대/축소.
// 인라인 SVG를 복제하므로 페이지 테마(data-theme) 색상이 그대로 유지된다.
(function () {
  var overlay, stage, scrollArea, scale = 1, lastFocused;

  function ensure() {
    if (overlay) return;
    overlay = document.createElement("div");
    overlay.id = "lightbox";
    overlay.setAttribute("role", "dialog");
    overlay.setAttribute("aria-modal", "true");
    overlay.setAttribute("aria-label", "도면 확대 보기");
    overlay.innerHTML =
      '<div class="lb-bar">' +
      '<span class="lb-cap"></span>' +
      '<span class="lb-actions">' +
      '<button class="lb-btn" data-z="out" aria-label="축소">−</button>' +
      '<button class="lb-btn" data-z="reset" aria-label="원래 크기">⤢</button>' +
      '<button class="lb-btn" data-z="in" aria-label="확대">+</button>' +
      '<button class="lb-btn lb-close" data-z="close" aria-label="닫기">✕</button>' +
      "</span></div>" +
      '<div class="lb-scroll"><div class="lb-stage"></div></div>';
    document.body.appendChild(overlay);
    stage = overlay.querySelector(".lb-stage");
    scrollArea = overlay.querySelector(".lb-scroll");

    overlay.addEventListener("click", function (e) {
      var z = e.target.getAttribute("data-z");
      if (e.target === overlay || e.target === scrollArea || z === "close") return close();
      if (z === "in") zoom(1.25);
      else if (z === "out") zoom(0.8);
      else if (z === "reset") setScale(1);
    });
    scrollArea.addEventListener("wheel", function (e) {
      if (!e.ctrlKey && !e.metaKey) return; // Ctrl/⌘+휠로만 확대 (일반 스크롤 보존)
      e.preventDefault();
      zoom(e.deltaY < 0 ? 1.1 : 0.9);
    }, { passive: false });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") close();
    });
  }

  function setScale(s) {
    scale = Math.max(0.5, Math.min(6, s));
    stage.style.width = (scale * 100) + "%";
  }
  function zoom(f) { setScale(scale * f); }

  function open(fig) {
    ensure();
    var svg = fig.querySelector("svg");
    if (!svg) return;
    stage.innerHTML = "";
    var clone = svg.cloneNode(true);
    clone.removeAttribute("style");
    clone.style.width = "100%";
    clone.style.height = "auto";
    clone.style.display = "block";
    stage.appendChild(clone);
    var cap = fig.querySelector(".cap");
    overlay.querySelector(".lb-cap").textContent = cap ? cap.firstChild.textContent.trim() : "";
    setScale(1);
    lastFocused = document.activeElement;
    overlay.classList.add("on");
    document.body.style.overflow = "hidden";
    var closeBtn = overlay.querySelector(".lb-close");
    if (closeBtn) closeBtn.focus();
  }
  function close() {
    if (!overlay) return;
    overlay.classList.remove("on");
    document.body.style.overflow = "";
    if (lastFocused && lastFocused.focus) { lastFocused.focus(); lastFocused = null; }
  }

  document.addEventListener("click", function (e) {
    var fig = e.target.closest(".fig.zoomable");
    if (fig) { e.preventDefault(); open(fig); }
  });
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Enter" && e.key !== " ") return;
    var fig = e.target.closest && e.target.closest(".fig.zoomable");
    if (fig) { e.preventDefault(); open(fig); }
  });
})();
