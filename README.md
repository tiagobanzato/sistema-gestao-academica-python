# 🎓 Sistema de Gestão Acadêmica em Python

Projeto acadêmico desenvolvido em Python para a disciplina de **Raciocínio Computacional** do curso de Análise e Desenvolvimento de Sistemas.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/Persistência-JSON-orange?style=flat)
![Status](https://img.shields.io/badge/Status-Concluído-green?style=flat)

---

## 📋 Sobre o projeto

Sistema de Gestão Acadêmica (SGA) com interface via terminal, que gerencia **5 módulos completos** com persistência de dados em arquivos JSON. O sistema carrega os dados automaticamente ao iniciar e salva a cada operação.

---

## 🗂️ Módulos

| Módulo | Operações disponíveis |
|--------|----------------------|
| 👨‍🎓 Estudantes | Incluir, Listar, Atualizar, Excluir |
| 📚 Disciplinas | Incluir, Listar, Atualizar, Excluir |
| 👨‍🏫 Professores | Incluir, Listar, Atualizar, Excluir |
| 🏫 Turmas | Incluir, Listar, Atualizar, Excluir |
| 📝 Matrículas | Incluir, Listar, Excluir |

---

## ⚙️ Funcionalidades técnicas

- **CRUD completo** em 4 dos 5 módulos
- **Persistência em JSON** — dados salvos automaticamente a cada operação
- **Carregamento automático** ao iniciar o sistema
- **Validação de entradas** com `try/except` para códigos inválidos
- **Verificação de duplicatas** antes de cadastrar novos registros
- **Navegação por menus** aninhados com laços `while`
- **Modularização** — cada módulo tem suas próprias funções separadas

---

## 📁 Estrutura do projeto

```
sistema-gestao/
├── main.py              # Código principal com todos os menus e funções
├── estudantes.json      # Dados persistidos dos estudantes
├── disciplinas.json     # Dados persistidos das disciplinas
├── professores.json     # Dados persistidos dos professores
├── turmas.json          # Dados persistidos das turmas
└── matriculas.json      # Dados persistidos das matrículas
```

---

## ▶️ Como rodar

```bash
python main.py
```

Navegue pelo menu usando os números correspondentes a cada opção.

---

## 🛠️ Tecnologias

- **Python** — linguagem principal
- **JSON** — persistência de dados (`json.dump` / `json.load`)
- **Manipulação de arquivos** — leitura e escrita com `open()`
- **Tratamento de exceções** — `try/except` para entradas inválidas

---

## 👨‍💻 Autor

**Tiago Banzato** — Estudante de ADS

[![LinkedIn](https://img.shields.io/badge/LinkedIn-tiagobanzato-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/tiagobanzato)
