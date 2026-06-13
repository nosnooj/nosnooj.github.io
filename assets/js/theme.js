// 테마 토글 — html[data-theme] 전환 + localStorage 영속.
// FOUC 방지용 초기 설정은 base.html <head> 인라인 스크립트가 담당한다.
function toggleTheme() {
  var root = document.documentElement;
  var next = root.dataset.theme === "dark" ? "light" : "dark";
  root.dataset.theme = next;
  try { localStorage.setItem("theme", next); } catch (e) {}
}

// OS 테마가 바뀌면, 사용자가 수동 저장한 값이 없을 때만 따라간다.
try {
  matchMedia("(prefers-color-scheme: dark)").addEventListener("change", function (e) {
    if (!localStorage.getItem("theme")) {
      document.documentElement.dataset.theme = e.matches ? "dark" : "light";
    }
  });
} catch (e) {}
