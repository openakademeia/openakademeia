const view = document.getElementById("view");
let catalogPromise = null;

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

const PLUGIN_SOURCE = "git+https://github.com/slow42/openacademy#subdirectory=plugins/mentor";

function connectSnippets(course) {
  const origin = location.origin;
  const uvx = `uvx --from "${PLUGIN_SOURCE}" openacademy-mentor`;
  const claude = `claude mcp add openacademy -e OPENACADEMY_URL=${origin} -- ${uvx}`;
  const json = JSON.stringify(
    { mcpServers: { openacademy: { command: "uvx", args: ["--from", PLUGIN_SOURCE, "openacademy-mentor"], env: { OPENACADEMY_URL: origin } } } },
    null,
    2
  );
  const ask = `Start the course ${course.field}/${course.subfield}/${course.id}.`;
  return { claude, json, ask };
}

function renderCourse(field, subfield, course) {
  const flights = (course.flights || [])
    .map(
      (f) => `<li><strong>${esc(f.title)}</strong><ol>${(f.rungs || [])
        .map((r) => `<li>${esc(r.title)} <span class="kind">${esc(r.kind)}</span></li>`)
        .join("")}</ol></li>`
    )
    .join("");
  const snippets = connectSnippets({ ...course, field: field.id, subfield: subfield.id });
  const tier = course.tier && course.tier !== "free" ? `<span class="badge tier">${esc(course.tier)}</span>` : "";
  view.innerHTML = `<p class="crumbs"><a href="#/">Fields</a> / <a href="#/${field.id}">${esc(field.title)}</a> / <a href="#/${field.id}/${subfield.id}">${esc(subfield.title)}</a> / ${esc(course.title)}</p>
    <h1>${esc(course.title)}${course.status ? ` <span class="badge">${esc(course.status)}</span>` : ""} ${tier}</h1>
    <p>${esc(course.summary || "")}</p>
    <section>
      <h2>Connect your AI</h2>
      <p>Mentor runs inside the AI you already use. Give it this server once; it signs you up, keeps your progress here, and fetches each rung as you reach it.</p>
      <h3>Claude Code</h3>
      <pre><code>${esc(snippets.claude)}</code></pre>
      <h3>Cursor, Codex, Gemini CLI</h3>
      <p>Add this to the agent's MCP servers config:</p>
      <pre><code>${esc(snippets.json)}</code></pre>
      <h3>Then say</h3>
      <pre><code>${esc(snippets.ask)}</code></pre>
      <p class="hint">Needs <code>uv</code> installed. claude.ai and ChatGPT need a public server URL; this one is ${esc(location.hostname)}.</p>
    </section>
    <section>
      <h2>Flights</h2>
      <ol class="flights">${flights}</ol>
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
