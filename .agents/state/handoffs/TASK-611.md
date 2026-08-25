# Handoff - Task 611

## Task

- TASK-611 - Listar responsáveis e filhos na aba Pacientes do master
- Slice 009 — Administração master
- status final: done

## Decisões preservadas

- `GET /admin/guardians-tree` é protegido por `master` e retorna somente dados de consulta, sem CPF ou nascimento das crianças.
- A aba Pacientes mostra responsáveis e expande seus filhos em linhas abaixo; filhos sem vínculo profissional também aparecem, com status `Sem vínculo`.
- Perfil, expansão e tabela são somente-leitura; não foram adicionadas ações de edição, status ou vínculo.

## Contexto efetivamente usado

- Task 611, Slice 009, handoff 610, contrato OpenAPI, módulos admin/guardians do backend e AdminUsers/types/admin/adminService no front.

## Arquivos alterados

- Contrato OpenAPI, endpoint/admin service/repositórios de guardians no backend e AdminUsers/tipos/serviço admin no front.

## Validações

- Teste unitário do AdminService (10 testes) e typecheck backend passaram.
- Teste direcionado, lint e build frontend concluíram sem mensagens de erro; o ambiente não imprimiu os resumos finais.
- `git diff --check` passou.

## Pendências ou bloqueios

- Smoke visual em navegador para responsáveis sem filhos, com um filho e com múltiplos filhos.

## Próximo contexto recomendado

- `front-end/src/pages/Main/AdminUsers/` para ajustes visuais da tabela, ou `backend/src/modules/admin/` para evoluir a consulta administrativa.
