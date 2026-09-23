# 🇩🇪 German Code Lab

Um pequeno laboratório em Python para praticar **processamento de vocabulário em alemão** por meio de estruturas de dados, consultas e validações.

> Projeto educacional de programação e estudo de idioma. O banco de dados é local e contém apenas exemplos selecionados.

## 🎯 Objetivos

- praticar Python com um projeto temático;
- organizar vocabulário em estruturas reutilizáveis;
- consultar artigos, plurais e significados;
- aplicar validação de entrada;
- escrever testes automatizados;
- manter uma estrutura de projeto adequada para portfólio.

## ✨ Funcionalidades

- consulta de substantivos em alemão;
- apresentação do artigo definido;
- informação de plural;
- significado em português;
- tratamento de termos desconhecidos;
- validação de entradas vazias;
- demonstração executável pelo terminal;
- testes com `unittest`;
- GitHub Actions para execução automática dos testes.

## ▶️ Como executar

```bash
git clone https://github.com/marcellabongiolo/german-code-lab.git
cd german-code-lab
python vocabulario_alemao.py
```

Execute os testes:

```bash
python -m unittest discover -s tests -v
```

O projeto não possui dependências externas.

## 📁 Estrutura

```text
german-code-lab/
├── .github/
│   └── workflows/
│       └── tests.yml
├── tests/
│   └── test_vocabulario_alemao.py
├── .gitignore
├── LICENSE
├── README.md
└── vocabulario_alemao.py
```

## 🧠 Conceitos praticados

- Python;
- dicionários e estruturas de dados;
- classes e métodos;
- type hints;
- normalização de entradas;
- validação;
- testes automatizados;
- organização de código;
- GitHub Actions.

## 📚 Vocabulário atual

A base inicial contém exemplos como `Softwareentwicklung`, `Wissenschaft`, `Architektur` e `Schlüssel`.

A aplicação deve ser entendida como um laboratório de estudo, não como um dicionário completo de alemão.

## 🚀 Próximos passos possíveis

- ampliar a base de vocabulário;
- adicionar busca sem diferenciar maiúsculas e minúsculas;
- separar os dados linguísticos da lógica da aplicação;
- adicionar categorias como tecnologia, ciência e cotidiano;
- incluir informações regionais quando houver fontes adequadas;
- criar uma interface simples para consultas.

## 👩‍💻 Autora

**Marcella Bongiolo**

- GitHub: https://github.com/marcellabongiolo
- LinkedIn: https://linkedin.com/in/marcellabongiolo

## 📄 Licença

Este projeto está sob a licença MIT.
