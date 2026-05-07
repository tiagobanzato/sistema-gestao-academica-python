import json
import os

# ============================================================
# DADOS CENTRALIZADOS
# Em vez de 5 variáveis soltas, tudo num dicionário só
# ============================================================
dados = {
    "estudantes": [],
    "disciplinas": [],
    "professores": [],
    "turmas": [],
    "matriculas": []
}


# ============================================================
# PERSISTÊNCIA — salvar e carregar JSON
# ============================================================
def salvar_dados():
    for nome, lista in dados.items():
        with open(f"{nome}.json", "w", encoding="utf-8") as f:
            json.dump(lista, f, ensure_ascii=False, indent=4)


def carregar_dados():
    for nome in dados:
        if os.path.exists(f"{nome}.json"):
            with open(f"{nome}.json", "r", encoding="utf-8") as f:
                dados[nome] = json.load(f)


# ============================================================
# FUNÇÕES GENÉRICAS — evitam repetição de código
# ============================================================
def pegar_codigo(mensagem):
    """Lê e valida um código inteiro. Retorna None se inválido."""
    try:
        return int(input(mensagem))
    except ValueError:
        print("Erro: código inválido.")
        input("Pressione ENTER para continuar.")
        return None


def codigo_ja_existe(lista, codigo):
    """Verifica se um código já está cadastrado na lista."""
    return any(item["codigo"] == codigo for item in lista)


def buscar_por_codigo(lista, codigo):
    """Retorna o item com o código informado, ou None se não encontrar."""
    for item in lista:
        if item["codigo"] == codigo:
            return item
    return None


def pausar():
    input("Pressione ENTER para continuar.")


# ============================================================
# ESTUDANTES
# ============================================================
def incluir_estudante():
    codigo = pegar_codigo("Código do estudante (inteiro): ")
    if codigo is None:
        return
    if codigo_ja_existe(dados["estudantes"], codigo):
        print("Erro: código já cadastrado.")
        return pausar()
    nome = input("Nome do estudante: ")
    dados["estudantes"].append({"codigo": codigo, "nome": nome})
    salvar_dados()
    print("Estudante cadastrado com sucesso.")
    pausar()


def listar_estudantes():
    print("\nEstudantes:")
    if not dados["estudantes"]:
        print("Nenhum estudante cadastrado.")
    for e in dados["estudantes"]:
        print(f"  [{e['codigo']}] {e['nome']}")
    pausar()


def atualizar_estudante():
    listar_estudantes()
    codigo = pegar_codigo("Código do estudante a atualizar: ")
    if codigo is None:
        return
    item = buscar_por_codigo(dados["estudantes"], codigo)
    if item:
        item["nome"] = input("Novo nome: ")
        salvar_dados()
        print("Estudante atualizado com sucesso.")
    else:
        print("Estudante não encontrado.")
    pausar()


def excluir_estudante():
    listar_estudantes()
    codigo = pegar_codigo("Código do estudante a excluir: ")
    if codigo is None:
        return
    item = buscar_por_codigo(dados["estudantes"], codigo)
    if item:
        dados["estudantes"].remove(item)
        salvar_dados()
        print("Estudante excluído com sucesso.")
    else:
        print("Estudante não encontrado.")
    pausar()


def menu_estudantes():
    while True:
        print("\n--- Menu de Estudantes ---")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("9. Voltar")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            incluir_estudante()
        elif opcao == "2":
            listar_estudantes()
        elif opcao == "3":
            atualizar_estudante()
        elif opcao == "4":
            excluir_estudante()
        elif opcao == "9":
            break
        elif opcao == "0":
            exit()
        else:
            print("Opção inválida.")


# ============================================================
# DISCIPLINAS
# ============================================================
def incluir_disciplina():
    codigo = pegar_codigo("Código da disciplina (inteiro): ")
    if codigo is None:
        return
    if codigo_ja_existe(dados["disciplinas"], codigo):
        print("Erro: código já cadastrado.")
        return pausar()
    nome = input("Nome da disciplina: ")
    dados["disciplinas"].append({"codigo": codigo, "nome": nome})
    salvar_dados()
    print("Disciplina cadastrada com sucesso.")
    pausar()


def listar_disciplinas():
    print("\nDisciplinas:")
    if not dados["disciplinas"]:
        print("Nenhuma disciplina cadastrada.")
    for d in dados["disciplinas"]:
        print(f"  [{d['codigo']}] {d['nome']}")
    pausar()


def atualizar_disciplina():
    listar_disciplinas()
    codigo = pegar_codigo("Código da disciplina a atualizar: ")
    if codigo is None:
        return
    item = buscar_por_codigo(dados["disciplinas"], codigo)
    if item:
        item["nome"] = input("Novo nome: ")
        salvar_dados()
        print("Disciplina atualizada com sucesso.")
    else:
        print("Disciplina não encontrada.")
    pausar()


def excluir_disciplina():
    listar_disciplinas()
    codigo = pegar_codigo("Código da disciplina a excluir: ")
    if codigo is None:
        return
    item = buscar_por_codigo(dados["disciplinas"], codigo)
    if item:
        dados["disciplinas"].remove(item)
        salvar_dados()
        print("Disciplina excluída com sucesso.")
    else:
        print("Disciplina não encontrada.")
    pausar()


def menu_disciplinas():
    while True:
        print("\n--- Menu de Disciplinas ---")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("9. Voltar")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            incluir_disciplina()
        elif opcao == "2":
            listar_disciplinas()
        elif opcao == "3":
            atualizar_disciplina()
        elif opcao == "4":
            excluir_disciplina()
        elif opcao == "9":
            break
        elif opcao == "0":
            exit()
        else:
            print("Opção inválida.")


# ============================================================
# PROFESSORES
# ============================================================
def incluir_professor():
    codigo = pegar_codigo("Código do professor (inteiro): ")
    if codigo is None:
        return
    if codigo_ja_existe(dados["professores"], codigo):
        print("Erro: código já cadastrado.")
        return pausar()
    nome = input("Nome do professor: ")
    cpf = input("CPF do professor: ")
    dados["professores"].append({"codigo": codigo, "nome": nome, "cpf": cpf})
    salvar_dados()
    print("Professor cadastrado com sucesso.")
    pausar()


def listar_professores():
    print("\nProfessores:")
    if not dados["professores"]:
        print("Nenhum professor cadastrado.")
    for p in dados["professores"]:
        print(f"  [{p['codigo']}] {p['nome']} — CPF: {p['cpf']}")
    pausar()


def atualizar_professor():
    listar_professores()
    codigo = pegar_codigo("Código do professor a atualizar: ")
    if codigo is None:
        return
    item = buscar_por_codigo(dados["professores"], codigo)
    if item:
        item["nome"] = input("Novo nome: ")
        item["cpf"] = input("Novo CPF: ")
        salvar_dados()
        print("Professor atualizado com sucesso.")
    else:
        print("Professor não encontrado.")
    pausar()


def excluir_professor():
    listar_professores()
    codigo = pegar_codigo("Código do professor a excluir: ")
    if codigo is None:
        return
    item = buscar_por_codigo(dados["professores"], codigo)
    if item:
        dados["professores"].remove(item)
        salvar_dados()
        print("Professor excluído com sucesso.")
    else:
        print("Professor não encontrado.")
    pausar()


def menu_professores():
    while True:
        print("\n--- Menu de Professores ---")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("9. Voltar")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            incluir_professor()
        elif opcao == "2":
            listar_professores()
        elif opcao == "3":
            atualizar_professor()
        elif opcao == "4":
            excluir_professor()
        elif opcao == "9":
            break
        elif opcao == "0":
            exit()
        else:
            print("Opção inválida.")


# ============================================================
# TURMAS
# ============================================================
def incluir_turma():
    codigo = pegar_codigo("Código da turma (inteiro): ")
    if codigo is None:
        return
    if codigo_ja_existe(dados["turmas"], codigo):
        print("Erro: código já cadastrado.")
        return pausar()
    nome = input("Nome da turma: ")
    dados["turmas"].append({"codigo": codigo, "nome": nome})
    salvar_dados()
    print("Turma cadastrada com sucesso.")
    pausar()


def listar_turmas():
    print("\nTurmas:")
    if not dados["turmas"]:
        print("Nenhuma turma cadastrada.")
    for t in dados["turmas"]:
        print(f"  [{t['codigo']}] {t['nome']}")
    pausar()


def atualizar_turma():
    listar_turmas()
    codigo = pegar_codigo("Código da turma a atualizar: ")
    if codigo is None:
        return
    item = buscar_por_codigo(dados["turmas"], codigo)
    if item:
        item["nome"] = input("Novo nome: ")
        salvar_dados()
        print("Turma atualizada com sucesso.")
    else:
        print("Turma não encontrada.")
    pausar()


def excluir_turma():
    listar_turmas()
    codigo = pegar_codigo("Código da turma a excluir: ")
    if codigo is None:
        return
    item = buscar_por_codigo(dados["turmas"], codigo)
    if item:
        dados["turmas"].remove(item)
        salvar_dados()
        print("Turma excluída com sucesso.")
    else:
        print("Turma não encontrada.")
    pausar()


def menu_turmas():
    while True:
        print("\n--- Menu de Turmas ---")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("9. Voltar")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            incluir_turma()
        elif opcao == "2":
            listar_turmas()
        elif opcao == "3":
            atualizar_turma()
        elif opcao == "4":
            excluir_turma()
        elif opcao == "9":
            break
        elif opcao == "0":
            exit()
        else:
            print("Opção inválida.")


# ============================================================
# MATRÍCULAS
# ============================================================
def incluir_matricula():
    codigo = pegar_codigo("Código da matrícula (inteiro): ")
    if codigo is None:
        return
    if codigo_ja_existe(dados["matriculas"], codigo):
        print("Erro: código já cadastrado.")
        return pausar()
    estudante_codigo = pegar_codigo("Código do estudante: ")
    if estudante_codigo is None:
        return
    disciplina_codigo = pegar_codigo("Código da disciplina: ")
    if disciplina_codigo is None:
        return
    dados["matriculas"].append({
        "codigo": codigo,
        "estudante_codigo": estudante_codigo,
        "disciplina_codigo": disciplina_codigo
    })
    salvar_dados()
    print("Matrícula cadastrada com sucesso.")
    pausar()


def listar_matriculas():
    print("\nMatrículas:")
    if not dados["matriculas"]:
        print("Nenhuma matrícula cadastrada.")
    for m in dados["matriculas"]:
        print(f"  [{m['codigo']}] Estudante: {m['estudante_codigo']} — Disciplina: {m['disciplina_codigo']}")
    pausar()


def excluir_matricula():
    listar_matriculas()
    codigo = pegar_codigo("Código da matrícula a excluir: ")
    if codigo is None:
        return
    item = buscar_por_codigo(dados["matriculas"], codigo)
    if item:
        dados["matriculas"].remove(item)
        salvar_dados()
        print("Matrícula excluída com sucesso.")
    else:
        print("Matrícula não encontrada.")
    pausar()


def menu_matriculas():
    while True:
        print("\n--- Menu de Matrículas ---")
        print("1. Incluir")
        print("2. Listar")
        print("3. Excluir")
        print("9. Voltar")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            incluir_matricula()
        elif opcao == "2":
            listar_matriculas()
        elif opcao == "3":
            excluir_matricula()
        elif opcao == "9":
            break
        elif opcao == "0":
            exit()
        else:
            print("Opção inválida.")


# ============================================================
# MENU PRINCIPAL
# ============================================================
def mostrar_menu_principal():
    print("\n===== MENU PRINCIPAL =====")
    print("1. Estudante")
    print("2. Disciplina")
    print("3. Professor")
    print("4. Turma")
    print("5. Matrícula")
    print("0. Sair")


def rodar():
    carregar_dados()
    while True:
        mostrar_menu_principal()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            menu_estudantes()
        elif opcao == "2":
            menu_disciplinas()
        elif opcao == "3":
            menu_professores()
        elif opcao == "4":
            menu_turmas()
        elif opcao == "5":
            menu_matriculas()
        elif opcao == "0":
            salvar_dados()
            print("Até logo!")
            exit()
        else:
            print("Opção inválida.")


rodar()