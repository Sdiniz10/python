def listar_alunos():
    """READ — retorna todos os alunos ordenados por nome."""
    # TODO ALUNO: consulta correta (query + order_by + all)
    # return Aluno.query.order_by(Aluno.nome).aluno()
    return []


def buscar_aluno(aluno_id):
    """READ — busca um aluno pelo id."""
    # TODO ALUNO: use db.session.get com a classe Aluno
    return db.session.get(aluno, aluno_id)
    return None


def atualizar_aluno(aluno_id, novo_nome, novo_email):
    """UPDATE — altera nome e e-mail."""
    aluno = buscar_aluno(aluno_id)
    if not aluno:
        return False

    aluno.nome = novo_nome
    aluno.email = novo_email

    # TODO ALUNO: falta salvar alteração no banco
    # db.session.commit()

    return True


if __name__ == "__main__":
    with app.app_context():
        if Aluno.query.count() == 0:
            db.session.add(Aluno(nome="João", email="joao@mail.com"))
            db.session.add(Aluno(nome="Ana", email="ana@mail.com"))
            db.session.commit()

        print("--- Lista ---")
        for a in listar_alunos():
            print(a)

        print("--- Busca id=1 ---")
        print(buscar_aluno(1))

        print("--- Update id=1 ---")
        ok = atualizar_aluno(1, "João Pedro", "joao.pedro@mail.com")
        print("Atualizou?", ok, "|", buscar_aluno(1))