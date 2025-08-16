window.addEventListener("scroll", function () {
  const header = document.querySelector(".md-header");
  const tabs = document.querySelector(".md-tabs");
  if (!header) return;

  // Use tabs height as threshold, fallback to 50 if tabs not found
  const threshold = tabs ? tabs.offsetHeight : 50;

  if (window.scrollY > threshold) {
    header.classList.add("scrolled");
  } else {
    header.classList.remove("scrolled");
  }
});
