const form = document.querySelector("#creator-form");
const profileSelect = document.querySelector("#profile");
const metadataSection = document.querySelector("#metadata-section");
const metadata = document.querySelector("#metadata");
const profileHelp = document.querySelector("#profile-help");
const statusBox = document.querySelector("#status");
const preview = document.querySelector("#preview");
const steps = [...document.querySelectorAll("[data-step]")];

const LABELS = {
  author: "Autor",
  title: "Título",
  english_title: "Título em inglês",
  centro_ensino: "Centro de ensino",
  centro_ensino_sigla: "Sigla do centro",
  nivel_ensino: "Nível de ensino",
  curso: "Curso",
  status_curso: "Status do curso",
  cidade: "Cidade",
  estado: "Estado",
  grau_ensino: "Grau de ensino",
  grau_obtido: "Grau obtido",
  email: "E-mail",
  day: "Dia",
  month: "Mês",
  year: "Ano",
};

let catalog = [];
let selectedProfile = null;

function escapeHtml(value) {
  return String(value ?? "").replace(/[&<>"']/g, (char) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", """: "&quot;", "'": "&#039;",
  }[char]));
}

function setStep(current) {
  steps.forEach((step) => {
    const active = Number(step.dataset.step) === current;
    if (active) step.setAttribute("aria-current", "step");
    else step.removeAttribute("aria-current");
  });
}

function renderMetadata(profile) {
  metadata.replaceChildren();
  const fields = profile?.required_metadata ?? [];
  metadataSection.classList.toggle("hidden", fields.length === 0);

  fields.forEach((field) => {
    const wrapper = document.createElement("div");
    wrapper.className = "field-group";
    const label = document.createElement("label");
    label.htmlFor = "meta-" + field;
    label.textContent = LABELS[field] || field.replaceAll("_", " ");
    const input = document.createElement("input");
    input.className = "field";
    input.id = "meta-" + field;
    input.name = field;
    input.required = true;
    input.autocomplete = field === "email" ? "email" : "off";
    if (field === "email") input.type = "email";
    if (["day", "month", "year"].includes(field)) input.inputMode = "numeric";
    wrapper.append(label, input);
    metadata.appendChild(wrapper);
  });
}

function readMetadata() {
  return Object.fromEntries(
    (selectedProfile?.required_metadata ?? []).map((field) => [
      field,
      document.querySelector("#meta-" + CSS.escape(field))?.value.trim() ?? "",
    ])
  );
}

function buildDocument() {
  return {
    type: selectedProfile?.id ?? "",
    metadata: readMetadata(),
    sections: [{
      title: document.querySelector("#section-title").value.trim(),
      content: document.querySelector("#section-content").value.trim(),
    }],
    references: document.querySelector("#references").value.trim(),
    assets: [],
  };
}

function renderPreview(data = buildDocument()) {
  preview.textContent = JSON.stringify(data, null, 2);
}

function updateStatus(message, ok = false) {
  statusBox.textContent = message;
  statusBox.classList.toggle("ok", ok);
}

function selectProfile(id) {
  selectedProfile = catalog.find((profile) => profile.id === id) ?? null;
  renderMetadata(selectedProfile);
  if (selectedProfile) {
    profileHelp.textContent =
      selectedProfile.name + " · " +
      selectedProfile.required_metadata_count +
      " campos obrigatórios · " +
      selectedProfile.source;
    setStep(2);
  } else {
    profileHelp.textContent = "Selecione um perfil para começar.";
    setStep(1);
  }
  renderPreview();
}

async function loadProfiles() {
  try {
    const response = await fetch("./data/profiles.json", {
      headers: { Accept: "application/json" },
    });
    if (!response.ok) throw new Error("Não foi possível carregar o catálogo de perfis.");
    const data = await response.json();
    catalog = Array.isArray(data.profiles) ? data.profiles : [];
    if (!catalog.length) throw new Error("O catálogo não contém perfis.");

    profileSelect.replaceChildren(
      new Option("Selecione um perfil…", "", true, true),
      ...catalog.map((profile) => new Option(profile.name, profile.id))
    );

    const requested = new URLSearchParams(window.location.search).get("type");
    const initial = catalog.some((profile) => profile.id === requested)
      ? requested
      : catalog[0].id;
    profileSelect.value = initial;
    selectProfile(initial);
    updateStatus("Perfil carregado. Preencha os campos obrigatórios para continuar.");
  } catch (error) {
    updateStatus(error.message, false);
    profileSelect.replaceChildren(new Option("Catálogo indisponível", ""));
    profileSelect.disabled = true;
  }
}

profileSelect.addEventListener("change", () => selectProfile(profileSelect.value));

form.addEventListener("input", () => {
  renderPreview();
  const active = document.activeElement;
  if (active?.closest("#metadata-section")) setStep(2);
  else if (active?.id === "section-title" || active?.id === "section-content" || active?.id === "references") setStep(3);
});

form.addEventListener("submit", (event) => {
  event.preventDefault();
  setStep(4);
  if (!form.reportValidity()) {
    updateStatus("Existem campos obrigatórios pendentes.", false);
    return;
  }

  const documentData = buildDocument();
  renderPreview(documentData);
  updateStatus(
    "Formulário consistente. A validação normativa completa será executada pelo núcleo Python.",
    true
  );
});

document.querySelector("#reset-btn").addEventListener("click", () => {
  form.reset();
  const first = catalog[0];
  if (first) {
    profileSelect.value = first.id;
    selectProfile(first.id);
  }
  updateStatus("Formulário limpo. Nenhuma validação normativa foi executada.", false);
  setStep(1);
  renderPreview();
});

loadProfiles();
