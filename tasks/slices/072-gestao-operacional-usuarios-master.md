# Slice 072 - Gestão operacional de usuários master

## Status

done

## Objetivo de negocio

Permitir que o master exclua contas, edite dados, isente profissional ou responsável da mensalidade e marque um master para também atuar como profissional na página de usuários web.

## Entrega verificavel

- Master exclui um usuário autenticável com confirmação.
- Master edita dados de um usuário sem alterar o papel (troca de papel descartada na Task 802).
- ~~Master isenta profissional ou responsável da mensalidade~~ (removido na Task 803).
- Master marcado como "também atua como profissional" alterna para o modo profissional sem mensalidade e mantém o cargo master.

## Fora de escopo

- Exclusão de filho/paciente sem login
- UI mobile desta gestão
- Criar perfil clínico completo (CPF, especialidades) ao trocar o papel

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- backend
- front-end

## Contrato

- `contracts/openapi.yaml#/paths/~1users~1{userId}`
- `contracts/openapi.yaml#/components/schemas/User`

## Referencia visual por stack

### Web

- tipo: tela existente
- fonte primaria: página de Usuários do master (`front-end/src/pages/Main/AdminUsers/`)
- complementar: `design-system/front/Design_System_Evolente_Desktop.md`

## Permissoes e atores

- Apenas master

## Casos de erro e borda

- Master não pode excluir a própria conta
- Master não pode excluir o último master
- Isenção não se aplica a master
- Filho/paciente sem login não tem mensalidade

## Decisoes humanas confirmadas

- Pedido humano: exclusão com modal, edição de perfil e isenção de mensalidade para profissional ou paciente (conta pagante = profissional ou responsável)
- Premissa antiga “inativar, não excluir” deixa de valer para esta operação administrativa
- Revisão humana (Task 802): descartar a troca de perfil; master pode também atuar como profissional, sem mensalidade, mantendo o cargo

## Premissas adotadas

- `feeExempt` no usuário libera o gate de assinatura imediatamente
- Exclusão remove a conta e os dependentes necessários para respeitar FKs
- Troca de papel não fabrica CPF/especialidades; stub de perfil profissional só quando faltar

## Tasks relacionadas

- `tasks/change-requests/800-api-excluir-editar-isentar-usuario-master.md`
- `tasks/change-requests/801-ui-excluir-editar-isentar-usuario-master-web.md`
- `tasks/change-requests/802-master-atua-como-profissional-sem-mensalidade.md`
- `tasks/change-requests/803-remover-isencao-mensalidade-profissional-responsavel.md`
- `tasks/change-requests/804-especialidades-master-atua-como-profissional.md`

## Dependencias do slice

- Slice 009 (administração master) — done
- Task 610 (visualizar perfis) — done
- Task 188 (modal de inativação) — done
