const view = document.getElementById("view");
let catalogPromise = null;

function loadCatalog() {
  if (!catalogPromise) {
    catalogPromise = fetch("/api/realms").then((r) => r.json());
  }
  return catalogPromise;
}

function esc(text) {
  return String(text).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

function card(href, title, summary, badge) {
  return `<a class="card" href="${href}">
    <h2>${esc(title)}${badge ? ` <span class="badge">${esc(badge)}</span>` : ""}</h2>
    <p>${esc(summary || "")}</p>
  </a>`;
}

function renderRealms(realms) {
  view.innerHTML = `<h1>Realms</h1><div class="cards">${realms
    .map((r) => card(`#/${r.id}`, r.title, r.summary, `${r.courses.length} course${r.courses.length === 1 ? "" : "s"}`))
    .join("")}</div>`;
}

function renderCourses(realm) {
  view.innerHTML = `<p class="crumbs"><a href="#/">Realms</a> / ${esc(realm.title)}</p>
    <h1>${esc(realm.title)}</h1>
    <div class="cards">${realm.courses.map((c) => card(`#/${realm.id}/${c.id}`, c.title, c.summary, c.status)).join("")}</div>`;
}

function renderCourse(realm, course) {
  const downloadUrl = `/api/realms/${realm.id}/courses/${course.id}/download`;
  const flights = (course.flights || [])
    .map(
      (f) => `<li><strong>${esc(f.title)}</strong><ol>${(f.rungs || [])
        .map((r) => `<li>${esc(r.title)} <span class="kind">${esc(r.kind)}</span></li>`)
        .join("")}</ol></li>`
    )
    .join("");
  view.innerHTML = `<p class="crumbs"><a href="#/">Realms</a> / <a href="#/${realm.id}">${esc(realm.title)}</a> / ${esc(course.title)}</p>
    <h1>${esc(course.title)}${course.status ? ` <span class="badge">${esc(course.status)}</span>` : ""}</h1>
    <p>${esc(course.summary || "")}</p>
    <a class="button" href="${downloadUrl}" download>Download for your agent</a>
    <section>
      <h2>Flights</h2>
      <ol class="flights">${flights}</ol>
    </section>
    <section>
      <h2>Attach it to your AI</h2>
      <ol>
        <li>Unzip the download. It contains <code>course/</code> and <code>addon/</code>.</li>
        <li>Follow <code>addon/README.md</code> for your agent: Claude Code, claude.ai, Cursor, Codex, Gemini, or ChatGPT.</li>
        <li>Open your agent in that folder and say: <em>Start the course in ./course.</em></li>
      </ol>
    </section>`;
}

function renderNotFound() {
  view.innerHTML = `<h1>Not found</h1><p><a href="#/">Back to realms</a></p>`;
}

async function render() {
  const [realmId, courseId] = location.hash.replace(/^#\/?/, "").split("/").filter(Boolean);
  const realms = await loadCatalog();
  if (!realmId) return renderRealms(realms);
  const realm = realms.find((r) => r.id === realmId);
  if (!realm) return renderNotFound();
  if (!courseId) return renderCourses(realm);
  const course = realm.courses.find((c) => c.id === courseId);
  if (!course) return renderNotFound();
  renderCourse(realm, course);
}

window.addEventListener("hashchange", render);
render();
