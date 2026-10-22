/* DISTORSI front-end interactions */
(() => {
  const menuToggle = document.getElementById("menuToggle");
  const mainNav = document.getElementById("mainNav");

  if (menuToggle && mainNav) {
    menuToggle.addEventListener("click", () => {
      const isOpen = mainNav.classList.toggle("open");
      menuToggle.setAttribute("aria-expanded", String(isOpen));
    });
    mainNav.querySelectorAll("a").forEach(link => {
      link.addEventListener("click", () => {
        mainNav.classList.remove("open");
        menuToggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  let cart = [];
  try {
    cart = JSON.parse(localStorage.getItem("distorsiCart") || "[]");
    if (!Array.isArray(cart)) cart = [];
  } catch (_) {
    cart = [];
  }

  const cartCount = document.getElementById("cartCount");
  const toast = document.getElementById("toast");
  let toastTimer;

  function updateCart() {
    if (cartCount) cartCount.textContent = cart.length;
    try { localStorage.setItem("distorsiCart", JSON.stringify(cart)); } catch (_) {}
  }

  function showToast(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add("show");
    window.clearTimeout(toastTimer);
    toastTimer = window.setTimeout(() => toast.classList.remove("show"), 2400);
  }

  document.querySelectorAll(".add-cart").forEach(button => {
    button.addEventListener("click", () => {
      const product = button.dataset.product || "Produk";
      cart.push(product);
      updateCart();
      showToast(`${product} ditambahkan ke keranjang demo.`);
      const original = button.textContent;
      button.textContent = "✓ ADDED";
      window.setTimeout(() => { button.textContent = original; }, 1100);
    });
  });

  const backTop = document.getElementById("backTop");
  if (backTop) backTop.addEventListener("click", event => {
    event.preventDefault();
    window.scrollTo({ top: 0, behavior: "smooth" });
  });

  updateCart();
})();
