# API Com FastAPI Utilizando TDD

![Logo](https://github.com/digitalinnovationone/store_api/blob/main/docs/img/img-tdd.png?raw=true)

## Descrição

Este projeto demonstra a criação de uma API utilizando o framework FastAPI, seguindo a metodologia de Desenvolvimento Orientado a Testes (TDD). O objetivo é fornecer um exemplo prático de como construir APIs robustas e de alta qualidade, garantindo a confiabilidade e manutenibilidade do código através de testes automatizados.

## Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e de alto desempenho para a construção de APIs com Python 3.7+.
- **Pytest**: Ferramenta de testes em Python que facilita a escrita de testes simples e escaláveis.
- **SQLAlchemy**: Biblioteca SQL para mapeamento objeto-relacional (ORM) em Python.
- **Alembic**: Ferramenta de migração de banco de dados para uso com SQLAlchemy.
- **Docker**: Plataforma para desenvolvimento, envio e execução de aplicações em containers.

## Importância do TDD

### O que é TDD?

Desenvolvimento Orientado a Testes (TDD) é uma prática de desenvolvimento de software onde os testes são escritos antes do código funcional. O ciclo TDD segue três etapas principais:

1. **Red**: Escreva um teste que falha.
2. **Green**: Escreva o código mínimo necessário para passar no teste.
3. **Refactor**: Refatore o código para melhorar sua estrutura e qualidade, mantendo todos os testes passando.

### Benefícios do TDD

- **Qualidade do Código**: TDD incentiva a escrita de código limpo e bem estruturado, pois o desenvolvedor precisa pensar nos requisitos antes de implementar a funcionalidade.
- **Confiança nas Alterações**: Com uma suíte de testes abrangente, é possível fazer alterações no código com confiança, sabendo que os testes irão capturar regressões.
- **Documentação Viva**: Os testes servem como documentação viva do comportamento esperado do sistema, facilitando a compreensão do código por novos desenvolvedores.
- **Design Orientado a Testes**: TDD promove um design de software mais modular e desacoplado, pois o código precisa ser testável desde o início.

## Funcionalidades da API

- **CRUD de Recursos**: Endpoints para criação, leitura, atualização e exclusão de recursos.
- **Autenticação e Autorização**: Implementação de autenticação de usuários e controle de acesso.
- **Validação de Dados**: Validação robusta de dados de entrada utilizando Pydantic.
- **Documentação Automática**: Documentação automática da API com Swagger e Redoc.
- **Testes Automatizados**: Testes unitários e de integração para garantir a qualidade do código.

## Como Executar o Projeto

### Clone o Repositório:

  ```
    git clone https://github.com/SeuUsuario/API-Com-FastAPI-Utilizando-TDD.git
    cd API-Com-FastAPI-Utilizando-TDD
 ```

## Configure o Ambiente:
```
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Execute a Aplicação:
```
uvicorn app.main:app --reload
```
## Execute os Testes:
```
pytest
```

## Contribuição

Faça um fork deste repositório.
Crie uma nova branch (git checkout -b feature/nova-funcionalidade).
Faça commit das suas alterações (git commit -m 'Adiciona nova funcionalidade').
Envie para o repositório remoto (git push origin feature/nova-funcionalidade).
Abra um Pull Request.
























