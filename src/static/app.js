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
    const heading = /^(#{1,6}) (.*)$/.exec(line);
    const bullet = /^- (.*)$/.exec(line);
    const number = /^\d+\. (.*)$/.exec(line);
    if (heading) {
      closeList();
      out.push(`<h${heading[1].length}>${inline(heading[2])}</h${heading[1].length}>`);
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
  const uvx = `uvx --from "${PLUGIN_SOURCE}" openacademy-mentor`;
  const claude = `claude mcp add openacademy -e OPENACADEMY_URL=${origin} -- ${uvx}`;
  const json = JSON.stringify(
    { mcpServers: { openacademy: { command: "uvx", args: ["--from", PLUGIN_SOURCE, "openacademy-mentor"], env: { OPENACADEMY_URL: origin } } } },
    null,
    2
  );
  view.innerHTML = `<h1>Setup</h1>
    <p>Mentor runs inside the AI you already use. Give it this server once; it signs you up, keeps your progress here, and fetches each rung as you reach it. You need <code>uv</code> installed.</p>
    <h2>Claude Code</h2>
    <pre><code>${esc(claude)}</code></pre>
    <h2>Cursor, Codex, Gemini CLI</h2>
    <p>Add this to the agent's MCP servers config:</p>
    <pre><code>${esc(json)}</code></pre>
    <h2>Then</h2>
    <p>Pick a course and tell your AI to start it, for example <code>Start the course mathematics/algebra/linear-algebra.</code> Say <code>Continue the course.</code> to resume; your place is kept on this server.</p>
    <p class="hint">claude.ai and ChatGPT need a public server URL; this one is ${esc(location.hostname)}.</p>`;
}

function renderCourse(field, subfield, course) {
  const flights = (course.flights || [])
    .map(
      (f) =>
        `<li><strong>${esc(f.title)}</strong>${
          (f.rungs || []).length
            ? `<ol>${f.rungs.map((r) => `<li>${esc(r.title)} <span class="kind">${esc(r.kind)}</span></li>`).join("")}</ol>`
            : ` <span class="kind">planned</span>`
        }</li>`
    )
    .join("");
  const tier = course.tier && course.tier !== "free" ? `<span class="badge tier">${esc(course.tier)}</span>` : "";
  const path = `${field.id}/${subfield.id}/${course.id}`;
  view.innerHTML = `<p class="crumbs"><a href="#/">Fields</a> / <a href="#/${field.id}">${esc(field.title)}</a> / <a href="#/${field.id}/${subfield.id}">${esc(subfield.title)}</a> / ${esc(course.title)}</p>
    <h1>${esc(course.title)}${course.status ? ` <span class="badge">${esc(course.status)}</span>` : ""} ${tier}</h1>
    <p>${esc(course.summary || "")}</p>
    <p class="start">Tell your AI: <code>Start the course ${esc(path)}.</code> Not connected yet? <a href="#/setup">Setup</a>.</p>
    ${course.syllabus ? `<section class="syllabus">${markdown(course.syllabus)}</section>` : ""}
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
  if (fieldId === "setup") return renderSetup();
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
