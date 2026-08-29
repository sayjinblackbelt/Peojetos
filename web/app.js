async function loadDashboardData() {
  try {
    const [documentsResponse, requirementsResponse, analysisResponse] = await Promise.all([
      fetch("automation/sample_data/project_documents.csv"),
      fetch("automation/sample_data/project_requirements.csv"),
      fetch("automation/output/document_analysis_report.json")
    ]);

    const documentsText = await documentsResponse.text();
    const requirementsText = await requirementsResponse.text();

    const documents = parseCSV(documentsText);
    const requirements = parseCSV(requirementsText);
    const analysis = await analysisResponse.json();

    const documentProgress = average(documents.map(item => Number(item.progresso)));
    const completed = requirements.filter(item => item.status === "concluido").length;
    const requirementsCompletion = requirements.length ? completed / requirements.length * 100 : 0;
    const overall = (documentProgress + requirementsCompletion) / 2;

    document.getElementById("documents").textContent = documents.length;
    document.getElementById("documentProgress").textContent = documentProgress.toFixed(1) + "%";
    document.getElementById("requirementsCompletion").textContent = requirementsCompletion.toFixed(1) + "%";
    document.getElementById("overall").textContent = overall.toFixed(1) + "%";

    renderAnalysis(analysis);
  } catch (error) {
    console.error("Não foi possível carregar os dados demonstrativos.", error);
    document.getElementById("analysisStatus").textContent =
      "Não foi possível carregar a análise documental.";
  }
}

function renderAnalysis(analysis) {
  const results = analysis.resultados || [];
  const alerts = analysis.alertas || [];
  const qualityScore = average(results.map(item => Number(item.score_qualidade)));

  document.getElementById("analyzedDocuments").textContent =
    analysis.documentos_analisados ?? results.length;
  document.getElementById("qualityScore").textContent =
    qualityScore.toFixed(1) + "%";
  document.getElementById("analysisAlerts").textContent = alerts.length;

  const status = document.getElementById("analysisStatus");
  const list = document.getElementById("alertsList");

  if (!alerts.length) {
    status.textContent = "Nenhuma inconsistência foi identificada nos dados demonstrativos.";
    list.innerHTML = "";
    return;
  }

  status.textContent = "Alertas identificados pela análise automatizada:";
  list.innerHTML = alerts.map(alert => `
    <article class="alert-card">
      <strong>${escapeHTML(alert.codigo)}</strong>
      <span>${escapeHTML(alert.tipo)}</span>
      <p>${escapeHTML(alert.mensagem)}</p>
    </article>
  `).join("");
}

function parseCSV(text) {
  const lines = text.trim().split(/\r?\n/);
  const headers = lines.shift().split(",");
  return lines.map(line => {
    const values = line.split(",");
    return Object.fromEntries(headers.map((header, index) => [header, values[index]]));
  });
}

function average(values) {
  return values.length
    ? values.reduce((total, value) => total + value, 0) / values.length
    : 0;
}

function escapeHTML(value) {
  return String(value ?? "").replace(/[&<>"']/g, character => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#039;"
  })[character]);
}

loadDashboardData();
