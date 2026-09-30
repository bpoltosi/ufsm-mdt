const form = document.querySelector("#creator-form");
const profileSelect = document.querySelector("#profile");
const metadataSection = document.querySelector("#metadata-section");
const metadata = document.querySelector("#metadata");
const profileHelp = document.querySelector("#profile-help");
const statusBox = document.querySelector("#status");
const preview = document.querySelector("#preview");
const structureEditor = document.querySelector("#structure-editor");
const sectionTitle = document.querySelector("#section-title");
const sectionContent = document.querySelector("#section-content");
const sectionHelp = document.querySelector("#section-help");
const steps = [...document.querySelectorAll("[data-step]")];

const LABELS = {
  author:"Autor", title:"Título", english_title:"Título em inglês",
  centro_ensino:"Centro de ensino", centro_ensino_sigla:"Sigla do centro",
  nivel_ensino:"Nível de ensino", curso:"Curso", status_curso:"Status do curso",
  cidade:"Cidade", estado:"Estado", grau_ensino:"Grau de ensino",
  grau_obtido:"Grau obtido", email:"E-mail", day:"Dia", month:"Mês", year:"Ano",
};

const DEFAULT_SECTIONS = [
  {title:"Introdução",content:""},
  {title:"Desenvolvimento",content:""},
  {title:"Conclusão",content:""},
];

let catalog = [];
let selectedProfile = null;
let sections = DEFAULT_SECTIONS.map((item) => ({...item}));
let selectedSection = 0;

function setStep(current) {
  steps.forEach((step) => {
    if (Number(step.dataset.step) === current) step.setAttribute("aria-current","step");
    else step.removeAttribute("aria-current");
  });
}

function renderMetadata(profile) {
  metadata.replaceChildren();
  const fields = profile?.required_metadata ?? [];
  metadataSection.classList.toggle("hidden", fields.length === 0);
  fields.forEach((field) => {
    const wrapper=document.createElement("div"); wrapper.className="field-group";
    const label=document.createElement("label"); label.htmlFor="meta-"+field;
    label.textContent=LABELS[field] || field.replaceAll("_"," ");
    const input=document.createElement("input");
    input.className="field"; input.id="meta-"+field; input.name=field; input.required=true;
    input.autocomplete=field==="email"?"email":"off";
    if(field==="email") input.type="email";
    if(["day","month","year"].includes(field)) input.inputMode="numeric";
    wrapper.append(label,input); metadata.appendChild(wrapper);
  });
}

function readMetadata() {
  return Object.fromEntries((selectedProfile?.required_metadata ?? []).map((field) => [
    field, document.querySelector("#meta-"+CSS.escape(field))?.value.trim() ?? "",
  ]));
}

function syncSelectedSection() {
  const current=sections[selectedSection];
  if(!current) return;
  current.title=sectionTitle.value.trim() || current.title;
  current.content=sectionContent.value;
}

function selectSection(index) {
  syncSelectedSection();
  selectedSection=Math.max(0,Math.min(index,sections.length-1));
  const current=sections[selectedSection];
  sectionTitle.value=current?.title ?? "";
  sectionContent.value=current?.content ?? "";
  sectionHelp.textContent=sections.length
    ? "Seção "+(selectedSection+1)+" de "+sections.length+"."
    : "Adicione uma seção para começar.";
  renderStructure();
  renderPreview();
  setStep(3);
}

function renderStructure() {
  structureEditor.replaceChildren();
  if(!sections.length) {
    const empty=document.createElement("p"); empty.className="structure-empty";
    empty.textContent="Nenhuma seção. Adicione a primeira seção.";
    structureEditor.appendChild(empty); return;
  }
  sections.forEach((item,index) => {
    const row=document.createElement("div");
    row.className="structure-row"; row.dataset.index=String(index);
    row.setAttribute("aria-selected",String(index===selectedSection));
    const number=document.createElement("span"); number.className="structure-number";
    number.textContent=String(index+1).padStart(2,"0");
    const input=document.createElement("input"); input.className="structure-title";
    input.value=item.title; input.setAttribute("aria-label","Título da seção "+(index+1));
    input.addEventListener("change",()=>{
      item.title=input.value.trim() || "Seção sem título";
      if(index===selectedSection) sectionTitle.value=item.title;
      renderPreview();
    });
    input.addEventListener("focus",()=>selectSection(index));
    const actions=document.createElement("div"); actions.className="structure-actions";
    [
      ["up","Mover para cima",index===0],
      ["down","Mover para baixo",index===sections.length-1],
      ["delete","Remover seção",false],
    ].forEach(([action,label,disabled])=>{
      const button=document.createElement("button"); button.type="button";
      button.textContent=action==="up"?"↑":action==="down"?"↓":"×";
      button.title=label; button.setAttribute("aria-label",label); button.disabled=disabled;
      button.addEventListener("click",(event)=>{
        event.stopPropagation();
        if(action==="delete"){
          sections.splice(index,1);
          selectedSection=Math.min(selectedSection,Math.max(0,sections.length-1));
        } else {
          const next=action==="up"?index-1:index+1;
          [sections[index],sections[next]]=[sections[next],sections[index]];
          if(selectedSection===index) selectedSection=next;
          else if(selectedSection===next) selectedSection=index;
        }
        renderStructure();
        selectSection(selectedSection);
      });
      actions.appendChild(button);
    });
    row.append(number,input,actions);
    row.addEventListener("click",()=>selectSection(index));
    structureEditor.appendChild(row);
  });
}

function buildDocument() {
  syncSelectedSection();
  return {
    type:selectedProfile?.id ?? "",
    metadata:readMetadata(),
    sections:sections.map((item)=>({title:item.title,content:item.content})),
    references:document.querySelector("#references").value.trim(),
    assets:[],
  };
}

function renderPreview(data=buildDocument()) {
  preview.textContent=JSON.stringify(data,null,2);
}

function updateStatus(message,ok=false) {
  statusBox.textContent=message;
  statusBox.classList.toggle("ok",ok);
}

function selectProfile(id) {
  selectedProfile=catalog.find((profile)=>profile.id===id) ?? null;
  renderMetadata(selectedProfile);
  if(selectedProfile) {
    profileHelp.textContent=selectedProfile.name+" · "+selectedProfile.required_metadata_count+
      " campos obrigatórios · "+selectedProfile.source;
    setStep(2);
  } else {
    profileHelp.textContent="Selecione um perfil para começar.";
    setStep(1);
  }
  renderPreview();
}

async function loadProfiles() {
  try {
    const response=await fetch("./data/profiles.json",{headers:{Accept:"application/json"}});
    if(!response.ok) throw new Error("Não foi possível carregar o catálogo de perfis.");
    const data=await response.json();
    catalog=Array.isArray(data.profiles)?data.profiles:[];
    if(!catalog.length) throw new Error("O catálogo não contém perfis.");
    profileSelect.replaceChildren(
      new Option("Selecione um perfil…","",true,true),
      ...catalog.map((profile)=>new Option(profile.name,profile.id))
    );
    const requested=new URLSearchParams(window.location.search).get("type");
    const initial=catalog.some((profile)=>profile.id===requested)?requested:catalog[0].id;
    profileSelect.value=initial;
    selectProfile(initial);
    renderStructure();
    selectSection(0);
    updateStatus("Perfil carregado. Preencha os campos obrigatórios para continuar.");
  } catch(error) {
    updateStatus(error.message,false);
    profileSelect.replaceChildren(new Option("Catálogo indisponível",""));
    profileSelect.disabled=true;
  }
}

profileSelect.addEventListener("change",()=>selectProfile(profileSelect.value));

document.querySelector("#add-section-btn").addEventListener("click",()=>{
  syncSelectedSection();
  sections.push({title:"Nova seção",content:""});
  selectSection(sections.length-1);
  document.querySelector("#section-title").focus();
  updateStatus("Seção adicionada ao rascunho.",true);
});

sectionTitle.addEventListener("input",()=>{
  if(!sections[selectedSection]) return;
  sections[selectedSection].title=sectionTitle.value;
  renderPreview(); setStep(3);
});

sectionTitle.addEventListener("change",()=>{
  if(!sections[selectedSection]) return;
  sections[selectedSection].title=sectionTitle.value.trim() || "Seção sem título";
  sectionTitle.value=sections[selectedSection].title;
  renderStructure(); renderPreview();
});

sectionContent.addEventListener("input",()=>{
  if(!sections[selectedSection]) return;
  sections[selectedSection].content=sectionContent.value;
  renderPreview(); setStep(3);
});

document.querySelector("#references").addEventListener("input",()=>renderPreview());

form.addEventListener("submit",(event)=>{
  event.preventDefault();
  if(!form.reportValidity()){
    updateStatus("Existem campos obrigatórios pendentes.",false);
    return;
  }
  setStep(4);
  const documentData=buildDocument();
  renderPreview(documentData);
  updateStatus("Formulário e estrutura consistentes. A validação normativa completa será executada pelo núcleo Python.",true);
});

document.querySelector("#reset-btn").addEventListener("click",()=>{
  form.reset();
  sections=DEFAULT_SECTIONS.map((item)=>({...item}));
  selectedSection=0;
  const first=catalog[0];
  if(first){profileSelect.value=first.id;selectProfile(first.id);}
  renderStructure(); selectSection(0);
  updateStatus("Formulário e estrutura limpos. Nenhuma validação normativa foi executada.",false);
  setStep(1); renderPreview();
});

loadProfiles();
