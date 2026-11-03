const view = document.getElementById("view");
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
let catalogPromise = null;
let teardown = () => {};

function loadCatalog() {
  if (!catalogPromise) {
    catalogPromise = fetch("/api/v1/catalog").then((r) => r.json());
  }
  return catalogPromise;
}

function esc(text) {
  return String(text).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

function plural(n, word) {
  return `${n} ${word}${n === 1 ? "" : "s"}`;
}

function courseCount(field) {
  return field.subfields.reduce((n, s) => n + s.courses.length, 0);
}

/* Media for the tunnel and the page: openly licensed placeholders until courses have footage of their own. */
const M = "/media/";
const TUNNEL = [
  { video: "a-timelapse-of-the-milky-way-s", w: 1.5 },
  { img: "euclid-geometry-1521-hans-brosamer.webp", w: 0.95 },
  { video: "foucault-pendulum-utexas-motion", w: 1.4 },
  { img: "botanical-plate.jpg", w: 1 },
  { video: "tyrosine-kinase-mediated-axial-motility-of-basal", w: 1 },
  { img: "globe-gores-parte-2-blaeu-willem-jansz.jpg", w: 0.6 },
  { video: "ocean-surface-waves-06", w: 1.6 },
  { img: "design-facial-anatomy-from-encyclopedie.jpg", w: 0.7 },
  { video: "solar-flare-from-hinode-in-ca-ii", w: 1.5 },
  { img: "traditional-chinese-abacus-illustrating-the-suspended-bead.jpg", w: 1.5 },
  { video: "aurora-iceland-northern-lights-timelapse-2026-02", w: 1.3 },
  { img: "woman-teaching-geometry.jpg", w: 0.9 },
  { video: "chemical-traffic-light", w: 1.4 },
  { video: "moving-clouds-timelapse-1152x694x10fps", w: 1.5 },
  { img: "untitled-known-as-a-philosopher-giving-that.jpg", w: 1.4 },
  { video: "007-volcano-eruption-of-litli-hrutur-in", w: 1.5 },
];

function mediaTag(item) {
  if (item.video) {
    return `<video muted loop playsinline preload="metadata" poster="${M}${item.video}-poster.jpg" aria-hidden="true"><source src="${M}${item.video}.webm" type="video/webm"></video>`;
  }
  return `<img src="${M}${item.img}" alt="" loading="lazy" decoding="async">`;
}

/* Cards stand on the inside wall of a cylinder whose far side faces the camera: far cards are small, near ones sweep past the edges. */
function startTunnel(root) {
  const stage = root.querySelector(".tunnel-stage");
  const cards = TUNNEL.map((item) => {
    const el = document.createElement("div");
    el.className = "tunnel-card";
    el.innerHTML = mediaTag(item);
    stage.appendChild(el);
    return { el, item, video: el.querySelector("video") };
  });
  const VISIBLE = 150;
  let geo = null;
  let period = 360;
  let phase = 0;
  let last = performance.now();
  let frame = 0;
  let running = false;

  function measure() {
    const h = root.clientHeight;
    // On tall, narrow screens the ring is sized from the height and runs off both sides.
    const w = Math.max(root.clientWidth, h * 1.3);
    // Solved so the far wall shows cards at about 0.3x and a card reaches 1.5x as it leaves the screen edge.
    const radius = w * 0.47;
    geo = { radius, inset: w * 0.23, persp: w * 0.3, height: Math.min(h * 0.42, w * 0.18) };
    root.style.setProperty("--persp", `${geo.persp}px`);
    const gap = geo.height * 0.04;
    let along = 0;
    for (const c of cards) {
      c.w = geo.height * c.item.w;
      c.el.style.width = `${c.w}px`;
      c.el.style.height = `${geo.height}px`;
      c.offset = ((along + c.w / 2) / radius) * (180 / Math.PI);
      along += c.w + gap;
    }
    period = Math.max(2 * VISIBLE + 20, (along / radius) * (180 / Math.PI));
  }

  function place() {
    for (const c of cards) {
      const deg = (((c.offset - phase) % period) + period) % period - period / 2;
      if (Math.abs(deg) > VISIBLE) {
        c.el.style.opacity = "0";
        continue;
      }
      const a = (deg * Math.PI) / 180;
      const x = geo.radius * Math.sin(a);
      const z = -geo.inset - geo.radius * Math.cos(a);
      c.el.style.opacity = "1";
      c.el.style.transform = `translate3d(${(x - c.w / 2).toFixed(1)}px, ${(-geo.height / 2).toFixed(1)}px, ${z.toFixed(1)}px) rotateY(${(-deg).toFixed(2)}deg)`;
    }
  }

  function tick(now) {
    const dt = Math.min(64, now - last);
    last = now;
    phase = (phase + dt * 0.0045) % period;
    place();
    frame = requestAnimationFrame(tick);
  }

  function play() {
    if (running || reduceMotion.matches) return;
    running = true;
    last = performance.now();
    frame = requestAnimationFrame(tick);
    cards.forEach((c) => c.video && c.video.play().catch(() => {}));
  }

  function pause() {
    running = false;
    cancelAnimationFrame(frame);
    cards.forEach((c) => c.video && c.video.pause());
  }

  measure();
  place();
  const onResize = () => { measure(); place(); };
  window.addEventListener("resize", onResize);
  const seen = new IntersectionObserver(([entry]) => (entry.isIntersecting ? play() : pause()));
  seen.observe(root);
  return () => {
    pause();
    seen.disconnect();
    window.removeEventListener("resize", onResize);
  };
}

/* The headline's last word turns over through subjects, settling letter by letter. */
const SUBJECTS = ["anything", "geometry", "the stars", "the tides", "anatomy", "chemistry", "linear algebra"];
const GLYPHS = "abcdefghijklmnopqrstuvwxyz";

function startCycle(el) {
  if (reduceMotion.matches) return () => {};
  let index = 0;
  let timer = 0;
  let frame = 0;
  function scramble(to) {
    const start = performance.now();
    const duration = 650;
    const step = (now) => {
      const t = Math.min(1, (now - start) / duration);
      const settled = Math.floor(t * to.length);
      el.textContent = to
        .split("")
        .map((ch, i) => (i < settled || ch === " " ? ch : GLYPHS[(Math.random() * GLYPHS.length) | 0]))
        .join("");
      if (t < 1) frame = requestAnimationFrame(step);
    };
    frame = requestAnimationFrame(step);
  }
  timer = setInterval(() => {
    index = (index + 1) % SUBJECTS.length;
    scramble(SUBJECTS[index]);
  }, 2600);
  return () => {
    clearInterval(timer);
    cancelAnimationFrame(frame);
  };
}

function reveal() {
  const items = view.querySelectorAll(".rise");
  if (reduceMotion.matches || !("IntersectionObserver" in window)) {
    items.forEach((el) => el.classList.add("in"));
    return () => {};
  }
  const io = new IntersectionObserver(
    (entries) => entries.forEach((e) => {
      if (e.isIntersecting) {
        e.target.classList.add("in");
        io.unobserve(e.target);
      }
    }),
    { rootMargin: "0px 0px -8% 0px" }
  );
  items.forEach((el) => io.observe(el));
  return () => io.disconnect();
}

const PLUGIN_SOURCE = "git+https://github.com/slow42/openacademy#subdirectory=plugins/plato";

function claudeCommand() {
  return `claude mcp add openacademy -e OPENACADEMY_URL=${location.origin} -- uvx --from "${PLUGIN_SOURCE}" openacademy-plato`;
}

async function renderHome() {
  const fields = await loadCatalog();
  const featured = fields.flatMap((f) => f.subfields.flatMap((s) => s.courses)).find((c) => c.flights && c.flights.length);
  const chapters = featured
    ? featured.flights.map((f) => `<li>${esc(f.title)}<span>${f.lessons.length ? plural(f.lessons.length, "lesson") : "Being written"}</span></li>`).join("")
    : "";
  const coursePath = featured ? `#/${featured.field}/${featured.subfield}/${featured.id}` : "#/courses";
  view.innerHTML = `
    <section class="hero" aria-labelledby="hero-title">
      <h1 id="hero-title" aria-label="Learn anything.">Learn <span class="cycle" aria-hidden="true">anything</span>.</h1>
      <div class="tunnel" aria-hidden="true"><div class="tunnel-stage"></div></div>
      <div class="hero-copy">
        <p>Open courses, taught one lesson at a time by the AI you already use.</p>
        <div class="actions">
          <a class="button accent" href="#/courses">Browse courses</a>
          <a class="button plain" href="#/setup">Connect your agent</a>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="commit-title">
      <div class="panel commit">
        <div class="commit-text">
          <h2 id="commit-title" class="h2 rise">Commit before you see the answer</h2>
          <p class="lead rise" style="--i:1">Every lesson asks for your answer and how sure you are before it shows you the truth. When a belief breaks, Plato repairs it with you, then hands you exercises and a twist.</p>
          <p class="note rise" style="--i:2">From the first lesson of Linear Algebra, as it plays out in a learner's own AI.</p>
        </div>
        <div class="chat rise" style="--i:2" data-ui>
          <div class="chat-head"><span>Plato</span><span>Two numbers, one arrow</span></div>
          <p class="msg"><span class="who">Plato</span>An arrow starts at the origin and ends at (3, 1). Write it as a column. A second arrow runs from (1, 2) to (4, 3). Same vector, or a different one? Give both answers and a confidence from 1 to 4.</p>
          <p class="msg you"><span class="who">You</span>(3, 1). Different, it starts somewhere else. Confidence 3.</p>
          <p class="msg truth"><span class="who">Plato</span>The first is right. The second is the same vector: from (1, 2) to (4, 3) is 3 steps right and 1 up, so its column is (3, 1) too. A vector is the trip, not where the trip started.</p>
        </div>
      </div>
    </section>

    <section class="field-accent" aria-labelledby="teacher-title">
      <div class="teacher">
        <figure>
          <img src="${M}untitled-known-as-a-philosopher-giving-that.jpg" alt="An eighteenth-century painting of a lecturer and listeners gathered around a lit orrery in a dark room." loading="lazy">
          <figcaption>A Philosopher Lecturing on the Orrery, Joseph Wright of Derby, about 1766</figcaption>
        </figure>
        <div class="teacher-text">
          <h2 id="teacher-title" class="h2 rise">Your AI is the teacher</h2>
          <p class="lead rise" style="--i:1">Plato plugs into Claude Code, Cursor, Codex and Gemini CLI. It signs you up, fetches each lesson as you reach it, and this server keeps your place.</p>
          <pre class="rise" style="--i:2"><code>${esc(claudeCommand())}</code></pre>
          <a class="link rise" style="--i:3" href="#/setup">Every way to connect</a>
        </div>
      </div>
    </section>

    ${featured ? `
    <section class="section" aria-labelledby="open-title">
      <div class="spotlight">
        <figure class="rise">
          <img src="${M}euclid-geometry-1521-hans-brosamer.webp" alt="A 1521 woodcut of a geometer measuring with compasses." loading="lazy">
          <figcaption>Geometry, Hans Brosamer, 1521</figcaption>
        </figure>
        <div class="spotlight-text">
          <h2 id="open-title" class="h2 rise">Open now: ${esc(featured.title)}</h2>
          <p class="lead rise" style="--i:1">${esc(featured.summary || "")}</p>
          <ol class="chapters rise" style="--i:2">${chapters}</ol>
          <div class="rise" style="--i:3"><a class="button accent" href="${coursePath}">Read the syllabus</a></div>
        </div>
      </div>
    </section>` : ""}

    <section class="section" aria-labelledby="coming-title">
      <div class="coming">
        <div class="coming-head">
          <h2 id="coming-title" class="h2 rise">Mathematics first, then everything</h2>
          <p class="lead rise" style="--i:1">Each field opens when its first course is written and tested. These are the ones we would like to reach.</p>
        </div>
        <div class="strip">
          <figure class="rise"><img src="${M}design-facial-anatomy-from-encyclopedie.jpg" alt="An engraving of the muscles of the face from the Encyclopédie." loading="lazy"><figcaption>Anatomy</figcaption></figure>
          <figure class="rise" style="--i:1"><img src="${M}globe-gores-parte-2-blaeu-willem-jansz.jpg" alt="Printed gores for a celestial globe by Willem Blaeu." loading="lazy"><figcaption>Astronomy</figcaption></figure>
          <figure class="rise" style="--i:2"><img src="${M}botanical-plate.jpg" alt="An eighteenth-century porcelain plate painted with flowers." loading="lazy"><figcaption>Botany</figcaption></figure>
          <figure class="rise" style="--i:3"><img src="${M}woman-teaching-geometry.jpg" alt="A medieval illumination of a woman teaching geometry to students." loading="lazy"><figcaption>Philosophy</figcaption></figure>
          <figure class="rise" style="--i:4"><img src="${M}traditional-chinese-abacus-illustrating-the-suspended-bead.jpg" alt="A traditional Chinese abacus." loading="lazy"><figcaption>Computing</figcaption></figure>
        </div>
      </div>
    </section>`;
  const stopTunnel = startTunnel(view.querySelector(".tunnel"));
  const stopCycle = startCycle(view.querySelector(".cycle"));
  const stopReveal = reveal();
  return () => {
    stopTunnel();
    stopCycle();
    stopReveal();
  };
}

function crumbs(parts) {
  const items = [`<a href="#/courses">Courses</a>`, ...parts];
  return `<p class="crumbs">${items.join(`<span aria-hidden="true">/</span>`)}</p>`;
}

function pageHead(title, crumbParts, lead, action) {
  return `<header class="page-head">
    ${crumbParts || action ? `<div class="page-top">${crumbParts ? crumbs(crumbParts) : "<span></span>"}${action || ""}</div>` : ""}
    <h1>${title}</h1>
    ${lead ? `<p class="lead">${esc(lead)}</p>` : ""}
  </header>`;
}

function row(href, title, summary, meta) {
  const tag = href ? "a" : "div";
  return `<${tag} class="row${href ? "" : " quiet"}"${href ? ` href="${href}"` : ""}>
    <h2>${esc(title)}</h2>
    <p>${esc(summary || "")}</p>
    <span class="count">${esc(meta)}</span>
  </${tag}>`;
}

function renderFields(fields) {
  view.innerHTML = `<div class="page">
    ${pageHead("Courses", null, "Every field, subfield and course on this server. Pick one and tell your AI to start it.")}
    <div class="rows">${fields.map((f) => row(`#/${f.id}`, f.title, f.summary, plural(courseCount(f), "course"))).join("")}</div>
  </div>`;
}

function renderSubfields(field) {
  view.innerHTML = `<div class="page">
    ${pageHead(esc(field.title), [esc(field.title)], field.summary)}
    <div class="rows">${field.subfields
      .map((s) => row(s.courses.length ? `#/${field.id}/${s.id}` : null, s.title, s.summary, s.courses.length ? plural(s.courses.length, "course") : "Coming"))
      .join("")}</div>
  </div>`;
}

function renderCourses(field, subfield) {
  const list = subfield.courses.length
    ? `<div class="rows">${subfield.courses.map((c) => row(`#/${field.id}/${subfield.id}/${c.id}`, c.title, c.summary, c.status || "")).join("")}</div>`
    : `<p class="empty">No courses yet.</p>`;
  view.innerHTML = `<div class="page">
    ${pageHead(esc(subfield.title), [`<a href="#/${field.id}">${esc(field.title)}</a>`, esc(subfield.title)], subfield.summary)}
    ${list}
  </div>`;
}

function inline(text) {
  return esc(text)
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/\*([^*]+)\*/g, "<em>$1</em>");
}

function markdown(text) {
  const out = [];
  let list = null;
  const closeList = () => {
    if (list) out.push(`</${list}>`);
    list = null;
  };
  for (const raw of text.split("\n")) {
    const line = raw.trimEnd();
    const heading = /^(#{1,6}) (.*?)(?: \{#([a-z0-9-]+)\})?$/.exec(line);
    const bullet = /^- (.*)$/.exec(line);
    const number = /^\d+\. (.*)$/.exec(line);
    if (heading) {
      closeList();
      const id = heading[3] ? ` id="${heading[3]}"` : "";
      out.push(`<h${heading[1].length}${id}>${inline(heading[2])}</h${heading[1].length}>`);
    } else if (line === "---") {
      closeList();
      out.push("<hr>");
    } else if (bullet || number) {
      const kind = bullet ? "ul" : "ol";
      if (list !== kind) {
        closeList();
        list = kind;
        out.push(`<${kind}>`);
      }
      out.push(`<li>${inline((bullet || number)[1])}</li>`);
    } else if (line) {
      closeList();
      out.push(`<p>${inline(line)}</p>`);
    } else {
      closeList();
    }
  }
  closeList();
  return out.join("");
}

function renderSetup() {
  const origin = location.origin;
  const json = JSON.stringify(
    { mcpServers: { openacademy: { command: "uvx", args: ["--from", PLUGIN_SOURCE, "openacademy-plato"], env: { OPENACADEMY_URL: origin } } } },
    null,
    2
  );
  view.innerHTML = `<div class="page">
    <header class="page-head">
      <h1>Connect your agent</h1>
      <div class="plato-intro">
        <span class="plato-mark" role="img" aria-label="Plato"></span>
        <p class="lead">Plato runs inside the AI you already use. Point it at this server once; after that it signs you up and fetches each lesson as you reach it.</p>
      </div>
    </header>
    <div class="setup">
      <section>
        <h2>Claude Code</h2>
        <p>You need <code>uv</code> on your machine. Then run:</p>
        <pre><code>${esc(claudeCommand())}</code></pre>
      </section>
      <section>
        <h2>Cursor, Codex, Gemini CLI</h2>
        <p>Add this to the agent's MCP servers config:</p>
        <pre><code>${esc(json)}</code></pre>
      </section>
      <section>
        <h2>Start a course</h2>
        <p>Pick a course and tell your AI to start it, for example <code>Start the course mathematics/algebra/linear-algebra.</code> To pick up where you left off, say <code>Continue the course.</code> This server remembers your place.</p>
        <p class="note">claude.ai and ChatGPT can only reach a public server. This one is at ${esc(location.hostname)}.</p>
      </section>
    </div>
  </div>`;
}

function renderAbout() {
  view.innerHTML = `<div class="page">
    ${pageHead("About openacademy", null, "Courses you take with the AI you already use. The courses and the agent that teaches them are open source.")}
    <div class="setup">
      <section>
        <h2>How it works</h2>
        <p>Every lesson asks you to predict something before it explains anything, and to say how sure you are. When the prediction fails, the idea arrives as the fix for it. Plato, a plugin for your AI, runs that loop: it fetches the lesson, holds the answer back until you have committed, and questions your reasoning instead of grading the final number.</p>
      </section>
      <section>
        <h2>What is open source</h2>
        <p>The course content is open source: every lesson, syllabus and course book. So is the Plato plugin. You can read them, run them against your own server, fix a lesson you think is wrong, or write a new course.</p>
        <p><a class="link" href="https://github.com/slow42/openacademy">Source on GitHub</a></p>
      </section>
      <section>
        <h2>What the web app adds</h2>
        <p>This site serves the catalog, keeps your place in each course, and is where the paid features will live. A premium tier is coming with progress management across courses, visualizations of what you have learned and where you got stuck, and courses built from material you upload yourself. The open content and the plugin stay free.</p>
      </section>
      <section>
        <h2>Why Plato, why a tree</h2>
        <p>Plato wrote his philosophy as dialogues: Socrates asks, the student answers, and the next question takes the answer apart. That is the teaching method here. Plato's Academy stood in a grove of olive trees outside Athens, which is where the tree in the logo comes from.</p>
        <p><a class="link" href="#/setup">Connect your agent</a></p>
      </section>
    </div>
  </div>`;
}

function renderCourse(field, subfield, course) {
  const path = `${field.id}/${subfield.id}/${course.id}`;
  const lessons = (course.flights || []).reduce((n, f) => n + f.lessons.length, 0);
  const tier = course.tier && course.tier !== "free" ? `${esc(course.tier)} plan` : "Free";
  const reader = course.reading_url ? `<a class="button small plain" href="#/${path}/read">Read the book</a>` : "";
  view.innerHTML = `<div class="page">
    ${pageHead(esc(course.title), [`<a href="#/${field.id}">${esc(field.title)}</a>`, `<a href="#/${field.id}/${subfield.id}">${esc(subfield.title)}</a>`, esc(course.title)], course.summary, reader)}
    <div class="course">
      ${course.syllabus ? `<article class="prose">${markdown(course.syllabus)}</article>` : `<p class="empty">The syllabus is still being written.</p>`}
      <aside class="course-side">
        <div class="start">
          <p>Tell your AI:</p>
          <code>Start the course ${esc(path)}.</code>
          <p>Not connected yet? <a href="#/setup">Connect your agent</a>.</p>
        </div>
        <div class="facts">
          <span>${tier}${course.status ? `, ${esc(course.status)}` : ""}</span>
          <span>${plural(lessons, "lesson")} written so far</span>
        </div>
      </aside>
    </div>
  </div>`;
}

async function renderReader(field, subfield, course, sectionId) {
  const path = `${field.id}/${subfield.id}/${course.id}`;
  const { text } = await fetch(course.reading_url).then((r) => r.json());
  const body = text.replace(/^# .*\n/, "");
  const contents = [...body.matchAll(/^(##|###) (.*?)(?: \{#([a-z0-9-]+)\})?$/gm)]
    .map(([, level, title, id]) =>
      level === "##" ? `<li class="toc-chapter">${inline(title)}</li>` : id ? `<li><a href="#/${path}/read/${id}">${inline(title)}</a></li>` : ""
    )
    .join("");
  view.innerHTML = `<div class="page">
    ${pageHead(esc(course.title), [`<a href="#/${field.id}">${esc(field.title)}</a>`, `<a href="#/${field.id}/${subfield.id}">${esc(subfield.title)}</a>`, `<a href="#/${path}">${esc(course.title)}</a>`, "Book"], null)}
    <div class="course">
      <article class="prose reader">${markdown(body)}</article>
      <aside class="course-side"><nav class="toc" aria-label="Contents"><p>Contents</p><ol>${contents}</ol></nav></aside>
    </div>
  </div>`;
  if (sectionId) setTimeout(() => document.getElementById(sectionId)?.scrollIntoView({ block: "start" }), 0);
}

function renderNotFound() {
  view.innerHTML = `<div class="page">${pageHead("Not found", null, null)}<p><a class="link" href="#/courses">Back to courses</a></p></div>`;
}

async function route() {
  const [first, subfieldId, courseId, page, sectionId] = location.hash.replace(/^#\/?/, "").split("/").filter(Boolean);
  if (!first) return renderHome();
  if (first === "setup") return renderSetup();
  if (first === "about") return renderAbout();
  const fields = await loadCatalog();
  if (first === "courses") return renderFields(fields);
  const field = fields.find((f) => f.id === first);
  if (!field) return renderNotFound();
  if (!subfieldId) return renderSubfields(field);
  const subfield = field.subfields.find((s) => s.id === subfieldId);
  if (!subfield) return renderNotFound();
  if (!courseId) return renderCourses(field, subfield);
  const course = subfield.courses.find((c) => c.id === courseId);
  if (!course) return renderNotFound();
  if (page === "read" && course.reading_url) return renderReader(field, subfield, course, sectionId);
  if (page) return renderNotFound();
  renderCourse(field, subfield, course);
}

function markNav() {
  const section = location.hash.replace(/^#\/?/, "").split("/")[0];
  document.querySelectorAll(".bar nav a").forEach((a) => {
    const target = a.getAttribute("href").replace(/^#\/?/, "");
    const pages = ["setup", "about"];
    const current = pages.includes(target) ? section === target : section && !pages.includes(section);
    if (current) a.setAttribute("aria-current", "page");
    else a.removeAttribute("aria-current");
  });
}

async function render() {
  teardown();
  teardown = () => {};
  markNav();
  const stop = await route();
  if (typeof stop === "function") teardown = stop;
  window.scrollTo(0, 0);
}

async function renderCredits() {
  const el = document.getElementById("credits");
  try {
    const credits = await fetch(`${M}credits.json`).then((r) => r.json());
    el.innerHTML = `${credits
      .map((c) => `<a href="${esc(c.page)}">${esc(c.title.length > 60 ? `${c.title.slice(0, 57)}…` : c.title)}</a>, ${esc(c.creator || "unknown")}, ${esc(c.license)}`)
      .join("; ")}.`;
  } catch {
    el.textContent = "";
  }
}

window.addEventListener("hashchange", render);
render();
renderCredits();
