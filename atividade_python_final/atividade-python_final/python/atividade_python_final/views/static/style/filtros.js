(function () {
    var seletor = document.getElementById("filtro-status");
    var tabela = document.getElementById("tabela-tarefas");
    var aviso = document.getElementById("sem-resultado");
    if (!seletor || !tabela) return;

    seletor.addEventListener("change", function () {
        var escolhido = seletor.value;
        var visiveis = 0;

        tabela.querySelectorAll("tbody tr").forEach(function (linha) {
            var mostrar = escolhido === "todas" || linha.dataset.status === escolhido;
            linha.hidden = !mostrar;
            if (mostrar) visiveis++;
        });

        tabela.hidden = visiveis === 0;
        if (aviso) aviso.hidden = visiveis !== 0;
    });
})();
