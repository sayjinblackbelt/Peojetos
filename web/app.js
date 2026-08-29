async function loadDashboardData() {
  try {
    const [documentsResponse, requirementsResponse] = await Promise.all([
      fetch("../automation/sample_data/project_documents.csv"),
      fetch("../automation/sample_data/project_requirements.csv")
    ]);

    const documentsText = await documentsResponse.text();
    const requirementsText = await requirementsResponse.text();

    const documents = parseCSV(documentsText);
    const requirements = parseCSV(requirementsText);

    const documentProgress = average(documents.map(item => Number(item.progresso)));
    const completed = requirements.filter(item => item.status === "concluido").length;
    const requirementsCompletion = requirements.length ? completed / requirements.length * 100 : 0;
    const overall = (documentProgress + requirementsCompletion) / 2;

    document.getElementById("documents").textContent = documents.length;
    document.getElementById("documentProgress").textContent = documentProgress.toFixed(1) + "%";
    document.getElementById("requirementsCompletion").textContent = requirementsCompletion.toFixed(1) + "%";
    document.getElementById("overall").textContent = overall.toFixed(1) + "%";
  } catch (error) {
    console.error("Não foi possível carregar os dados demonstrativos.", error);
  }
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
  return values.length ? values.reduce((total, value) => total + value, 0) / values.length : 0;
}

loadDashboardData();
