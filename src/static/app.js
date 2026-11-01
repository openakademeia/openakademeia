const view = document.getElementById("view");
let catalogPromise = null;

function loadCatalog() {
  if (!catalogPromise) {
    catalogPromise = fetch("/api/fields").then((r) => r.json());
  }
  return catalogPromise;
}

function esc(text) {
  return String(text).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

function plural(n, word) {
  return `${n} ${word}${n === 1 ? "" : "s"}`;
}

function card(href, title, summary, badge) {
  return `<a class="card" href="${href}">
    <h2>${esc(title)}${badge ? ` <span class="badge">${esc(badge)}</span>` : ""}</h2>
    <p>${esc(summary || "")}</p>
  </a>`;
}

function courseCount(field) {
  return field.subfields.reduce((n, s) => n + s.courses.length, 0);
}

function renderFields(fields) {
  view.innerHTML = `<h1>Fields</h1><div class="cards">${fields
    .map((f) => card(`#/${f.id}`, f.title, f.summary, plural(courseCount(f), "course")))
    .join("")}</div>`;
}

function renderSubfields(field) {
  view.innerHTML = `<p class="crumbs"><a href="#/">Fields</a> / ${esc(field.title)}</p>
    <h1>${esc(field.title)}</h1>
    <div class="cards">${field.subfields
      .map((s) => card(`#/${field.id}/${s.id}`, s.title, s.summary, plural(s.courses.length, "course")))
      .join("")}</div>`;
}

function renderCourses(field, subfield) {
  const cards = subfield.courses.length
    ? subfield.courses.map((c) => card(`#/${field.id}/${subfield.id}/${c.id}`, c.title, c.summary, c.status)).join("")
    : `<p class="empty">No courses yet.</p>`;
  view.innerHTML = `<p class="crumbs"><a href="#/">Fields</a> / <a href="#/${field.id}">${esc(field.title)}</a> / ${esc(subfield.title)}</p>
    <h1>${esc(subfield.title)}</h1>
    <p>${esc(subfield.summary || "")}</p>
    <div class="cards">${cards}</div>`;
}

function renderCourse(field, subfield, course) {
  const downloadUrl = `/api/fields/${field.id}/subfields/${subfield.id}/courses/${course.id}/download`;
  const flights = (course.flights || [])
    .map(
      (f) => `<li><strong>${esc(f.title)}</strong><ol>${(f.rungs || [])
        .map((r) => `<li>${esc(r.title)} <span class="kind">${esc(r.kind)}</span></li>`)
        .join("")}</ol></li>`
    )
    .join("");
  view.innerHTML = `<p class="crumbs"><a href="#/">Fields</a> / <a href="#/${field.id}">${esc(field.title)}</a> / <a href="#/${field.id}/${subfield.id}">${esc(subfield.title)}</a> / ${esc(course.title)}</p>
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
  view.innerHTML = `<h1>Not found</h1><p><a href="#/">Back to fields</a></p>`;
}

async function render() {
  const [fieldId, subfieldId, courseId] = location.hash.replace(/^#\/?/, "").split("/").filter(Boolean);
  const fields = await loadCatalog();
  if (!fieldId) return renderFields(fields);
  const field = fields.find((f) => f.id === fieldId);
  if (!field) return renderNotFound();
  if (!subfieldId) return renderSubfields(field);
  const subfield = field.subfields.find((s) => s.id === subfieldId);
  if (!subfield) return renderNotFound();
  if (!courseId) return renderCourses(field, subfield);
  const course = subfield.courses.find((c) => c.id === courseId);
  if (!course) return renderNotFound();
  renderCourse(field, subfield, course);
}

window.addEventListener("hashchange", render);
render();
