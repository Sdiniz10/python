(function () {
    var CHAVE = "tema-painel-tarefas";

    function aplicar(tema) {
        document.body.classList.toggle("tema-escuro", tema === "escuro");
        var botao = document.getElementById("btn-tema");
        if (botao) botao.textContent = tema === "escuro" ? "Modo claro" : "Modo escuro";
    }

    var salvo = localStorage.getItem(CHAVE) || "claro";
    aplicar(salvo);

    var botao = document.getElementById("btn-tema");
    if (botao) {
        botao.addEventListener("click", function () {
            var novo = document.body.classList.contains("tema-escuro") ? "claro" : "escuro";
            localStorage.setItem(CHAVE, novo);
            aplicar(novo);
        });
    }
})();
