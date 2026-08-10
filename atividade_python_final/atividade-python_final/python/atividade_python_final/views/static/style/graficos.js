(function () {
    // Frase motivacional da API pública
    var alvoFrase = document.getElementById("frase-dia");
    if (alvoFrase && alvoFrase.textContent.indexOf("Carregando") === 0) {
        fetch("https://api.adviceslip.com/advice")
            .then(function (r) { return r.json(); })
            .then(function (dados) { alvoFrase.textContent = dados.slip.advice; })
            .catch(function () { alvoFrase.textContent = "Não foi possível carregar a frase de hoje."; });
    }

    // Gráfico de tarefas por status (rota Flask que retorna JSON)
    var canvas = document.getElementById("grafico-status");
    if (!canvas || typeof Chart === "undefined") return;

    fetch("/api/v1/tarefas/status")
        .then(function (r) { return r.json(); })
        .then(function (dados) {
            var valores = [
                dados.pendente || 0,
                dados["em andamento"] || 0,
                dados.concluida || 0
            ];

            if (valores.every(function (v) { return v === 0; })) {
                canvas.hidden = true;
                var vazio = document.getElementById("grafico-vazio");
                if (vazio) vazio.hidden = false;
                return;
            }

            new Chart(canvas, {
                type: "bar",
                data: {
                    labels: ["Pendente", "Em andamento", "Concluída"],
                    datasets: [{
                        label: "Tarefas",
                        data: valores,
                        backgroundColor: ["#f59e0b", "#3b82f6", "#22c55e"]
                    }]
                },
                options: {
                    responsive: true,
                    plugins: { legend: { display: false } },
                    scales: { y: { beginAtZero: true, ticks: { precision: 0 } } }
                }
            });
        })
        .catch(function () { canvas.hidden = true; });
})();
