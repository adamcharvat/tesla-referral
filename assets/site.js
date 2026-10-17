/* Referral landing page · site.js
   Progressive enhancement only. Without this file the page still works:
   links, FAQ, language selector and the readonly referral field are native.
   Here: theme toggle and persistence, copy to clipboard, language menu
   closing, language suggestion bar, sticky header hairline, scroll reveal. */
(() => {
  "use strict";

  const root = document.documentElement;
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  /* ---------------------------------------------------------------- theme */
  const THEME_KEY = "theme";
  const systemDark = window.matchMedia("(prefers-color-scheme: dark)");
  const themeToggle = document.querySelector("[data-theme-toggle]");
  const themeMetas = Array.from(document.querySelectorAll('meta[name="theme-color"]'));
  themeMetas.forEach((meta) => { meta.dataset.systemColor = meta.content; });

  const storedTheme = () => {
    try {
      const value = window.localStorage.getItem(THEME_KEY);
      return value === "light" || value === "dark" ? value : null;
    } catch (error) {
      return null;
    }
  };

  const syncThemeUi = () => {
    const theme = root.getAttribute("data-theme");
    if (themeToggle) themeToggle.setAttribute("aria-pressed", String(theme === "dark"));
    // An explicit choice overrides the system-based browser chrome colour.
    const chosen = storedTheme();
    const color = chosen ? getComputedStyle(root).getPropertyValue("--color-bg").trim() : null;
    themeMetas.forEach((meta) => { meta.content = color || meta.dataset.systemColor; });
  };

  const applyTheme = (theme, animate) => {
    const commit = () => {
      root.setAttribute("data-theme", theme);
      syncThemeUi();
    };
    if (!animate || reduceMotion.matches) {
      commit();
    } else if (typeof document.startViewTransition === "function") {
      document.startViewTransition(commit);
    } else {
      root.classList.add("theme-transition");
      commit();
      window.setTimeout(() => root.classList.remove("theme-transition"), 400);
    }
  };

  if (themeToggle) {
    themeToggle.addEventListener("click", () => {
      const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      try {
        window.localStorage.setItem(THEME_KEY, next);
      } catch (error) {
        /* storage blocked: the choice lasts for this page view only */
      }
      applyTheme(next, true);
    });
  }

  systemDark.addEventListener("change", (event) => {
    if (!storedTheme()) applyTheme(event.matches ? "dark" : "light", true);
  });

  syncThemeUi();

  /* ------------------------------------------------------- copy to clipboard */
  const resetTimers = new WeakMap();

  const legacyCopy = (input) => {
    // Selecting the field and running the copy command fires the input's
    // "copy" listener below, which swaps in the full URL.
    input.focus({ preventScroll: true });
    input.select();
    input.setSelectionRange(0, input.value.length);
    let copied = false;
    try {
      copied = document.execCommand("copy");
    } catch (error) {
      copied = false;
    }
    return copied;
  };

  document.querySelectorAll("[data-copy]").forEach((block) => {
    const input = block.querySelector("input[data-copy-value]");
    const button = block.querySelector("[data-copy-button]");
    const status = block.querySelector("[data-copy-status]");
    if (!input || !button || !status) return;

    const fullUrl = input.dataset.copyValue;
    const shortUrl = input.value;

    input.addEventListener("copy", (event) => {
      if (!event.clipboardData) return;
      event.clipboardData.setData("text/plain", fullUrl);
      event.preventDefault();
    });
    input.addEventListener("focus", () => input.select());
    input.addEventListener("blur", () => {
      if (!block.classList.contains("is-manual")) input.value = shortUrl;
    });

    const showResult = (copied) => {
      window.clearTimeout(resetTimers.get(block));
      block.classList.remove("is-copied", "is-manual");
      status.textContent = "";
      if (copied) {
        block.classList.add("is-copied");
        status.textContent = status.dataset.copied;
        input.value = shortUrl;
        resetTimers.set(block, window.setTimeout(() => {
          block.classList.remove("is-copied");
          status.textContent = "";
        }, 2600));
      } else {
        // Last resort: show and select the full URL so the user can copy it.
        block.classList.add("is-manual");
        input.value = fullUrl;
        input.focus({ preventScroll: true });
        input.select();
        status.textContent = status.dataset.manual;
      }
    };

    button.addEventListener("click", async () => {
      let copied = false;
      if (navigator.clipboard && window.isSecureContext) {
        try {
          await navigator.clipboard.writeText(fullUrl);
          copied = true;
        } catch (error) {
          copied = false;
        }
      }
      if (!copied) copied = legacyCopy(input);
      if (copied) input.blur();
      showResult(copied);
    });
  });

  /* --------------------------------------------------------- language menu */
  document.querySelectorAll("[data-lang-menu]").forEach((menu) => {
    const summary = menu.querySelector("summary");
    menu.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && menu.open) {
        menu.open = false;
        summary.focus();
      }
    });
    menu.addEventListener("focusout", (event) => {
      if (menu.open && event.relatedTarget && !menu.contains(event.relatedTarget)) menu.open = false;
    });
    document.addEventListener("click", (event) => {
      if (menu.open && !menu.contains(event.target)) menu.open = false;
    });
  });

  /* ------------------------------------------------- language suggestion */
  // On the x-default page only (the generator embeds #lang-suggest there).
  // Suggests the version in the visitor's browser language; never redirects.
  const LANG_KEY = "lang-choice";
  const readChoice = () => {
    try { return window.localStorage.getItem(LANG_KEY); } catch (error) { return null; }
  };
  const storeChoice = (code) => {
    try { window.localStorage.setItem(LANG_KEY, code); } catch (error) { /* storage blocked */ }
  };

  document.addEventListener("click", (event) => {
    const link = event.target.closest(".lang__option, .site-footer__langs a, .lang-suggest__action");
    if (link && link.hreflang) storeChoice(link.hreflang);
  });

  const suggestSource = document.getElementById("lang-suggest");
  if (suggestSource) {
    let offers = null;
    try { offers = JSON.parse(suggestSource.textContent); } catch (error) { offers = null; }
    const current = root.lang;
    const choice = readChoice();
    let target = null;
    if (offers && choice !== current) {
      if (choice && offers[choice]) {
        target = choice;
      } else {
        const preferred = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || ""];
        for (const tag of preferred) {
          const code = String(tag).toLowerCase().split("-")[0];
          if (code === current) break;
          if (offers[code]) { target = code; break; }
        }
      }
    }

    if (target) {
      const offer = offers[target];
      const bar = document.createElement("div");
      bar.className = "lang-suggest";
      bar.lang = target;
      bar.setAttribute("role", "region");
      bar.setAttribute("aria-label", offer.label);

      const inner = document.createElement("div");
      inner.className = "lang-suggest__inner";
      const text = document.createElement("p");
      text.className = "lang-suggest__text";
      text.textContent = offer.text;
      const action = document.createElement("a");
      action.className = "lang-suggest__action";
      action.href = offer.href;
      action.hreflang = target;
      action.textContent = offer.action;
      const close = document.createElement("button");
      close.type = "button";
      close.className = "lang-suggest__close";
      close.setAttribute("aria-label", offer.dismiss);

      close.addEventListener("click", () => {
        storeChoice(current);
        bar.classList.remove("is-visible");
        window.setTimeout(() => bar.remove(), reduceMotion.matches ? 0 : 320);
      });

      inner.append(text, action, close);
      bar.append(inner);
      document.body.append(bar);
      window.requestAnimationFrame(() => window.requestAnimationFrame(() => bar.classList.add("is-visible")));
    }
  }

  /* ------------------------------------------------- header hairline on scroll */
  const header = document.querySelector("[data-header]");
  if (header && "IntersectionObserver" in window) {
    const sentinel = document.createElement("div");
    sentinel.className = "header-sentinel";
    sentinel.setAttribute("aria-hidden", "true");
    document.body.prepend(sentinel);
    new IntersectionObserver(([entry]) => {
      header.classList.toggle("is-stuck", !entry.isIntersecting);
    }).observe(sentinel);
  }

  /* ----------------------------------------------------------- scroll reveal */
  const revealItems = Array.from(document.querySelectorAll("[data-reveal]"));
  if (revealItems.length && "IntersectionObserver" in window && !reduceMotion.matches) {
    // Measure once, then write: only content below the first screen is hidden.
    const fold = window.innerHeight;
    const pending = revealItems.filter((item) => item.getBoundingClientRect().top > fold);
    pending.forEach((item) => item.classList.add("is-pending"));

    const reveal = (item, delay) => {
      item.style.setProperty("--reveal-delay", `${delay}ms`);
      item.classList.remove("is-pending");
    };

    const observer = new IntersectionObserver((entries) => {
      let order = 0;
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        reveal(entry.target, Math.min(order, 4) * 70);
        order += 1;
        observer.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -8% 0px" });

    pending.forEach((item) => observer.observe(item));
    window.addEventListener("beforeprint", () => pending.forEach((item) => reveal(item, 0)));
  }
})();
