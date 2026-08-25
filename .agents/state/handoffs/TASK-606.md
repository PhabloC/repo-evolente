# Handoff Task 606

## Status

done

## Slice

- Slice 054 — cancelamento da conta do responsável e restrição de acesso profissional.

## Decisões preservadas

- Vínculo `canceled` aparece como **Conta cancelada** na lista profissional.
- O menu desse estado não oferece perfil nem reativação: somente **Remover vínculo**, confirmado antes do PATCH para `inactive`.
- Se a rota direta for negada pela API, não há dados ou ações clínicas renderizadas.

## Contexto utilizado

- Tipos/serviço de pacientes, lista e perfil, Design System desktop e checklist de acessibilidade.

## Arquivos alterados

- Tipo de paciente, lista de pacientes e testes focados de lista/perfil.

## Validações

- Lint e 14 testes focados passaram.
- Build global segue bloqueado por mocks legados de guardian/PatientDetail fora do escopo.

## Pendências

- Criar manutenção isolada para corrigir os mocks de testes e recuperar o build global.
