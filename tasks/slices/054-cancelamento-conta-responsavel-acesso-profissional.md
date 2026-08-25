# Slice 054 - Cancelamento da conta do responsável e restrição de acesso profissional

## Status

done

## Objetivo de negócio

Tratar a assinatura do responsável e seus filhos como uma única conta: ao cancelar a assinatura, todos os pacientes dessa conta ficam cancelados/inativos. Profissionais vinculados mantêm somente a possibilidade de remover o próprio vínculo, sem consultar dados clínicos nem montar ou alterar trilhas.

## Entrega verificável

- O cancelamento ou reembolso da assinatura do responsável desativa em cascata seus filhos, sem apagar histórico ou dados persistidos.
- Um profissional recebe erro de autorização ao acessar detalhe, anamnese, evolução, consultas, avatar ou trilhas de paciente cancelado, e não consegue criar, sugerir, editar ou excluir trilhas.
- A lista profissional continua exibindo identificação mínima do paciente cancelado e o estado de conta cancelada, exclusivamente para permitir **Remover vínculo**.
- No perfil web de um paciente cancelado, nenhuma ação clínica, de edição, inativação/reativação ou trilha é apresentada; a única ação disponível é **Remover vínculo**, com confirmação.

## Fora de escopo

- Exclusão física de responsável, paciente, vínculo, trilha, relatórios ou histórico clínico.
- Reativação automática dos pacientes quando uma nova assinatura for contratada.
- Mudanças no checkout ou no fluxo de cancelamento do mobile; o gate existente continua bloqueando o responsável sem acesso.

## Decisões confirmadas

- A conta é do responsável; filhos/pacientes não possuem assinatura independente.
- Cancelar a assinatura do responsável também cancela/inativa todos os pacientes pertencentes a ele.
- Após esse cancelamento, o profissional não pode abrir o perfil nem montar trilhas; pode somente remover seu vínculo.

## Tasks relacionadas

- `tasks/change-requests/605-cancelamento-em-cascata-e-bloqueio-profissional-api.md`
- `tasks/change-requests/606-paciente-cancelado-acoes-restritas-web.md`

## Progresso

- Task 605 — done
- Task 606 — done

## Dependências de contexto

- Slice 039 / Tasks 421 e 423: ciclo de cancelamento/reembolso e gate de assinatura.
- Slice 053 / Tasks 581, 595, 602 e 604: vínculo profissional, autorização atual e ações do perfil do paciente.

## Contexto mínimo

- Este slice, Tasks 605 e 606, Slice 039, Slice 053 e handoffs das Tasks 421, 595, 602 e 604.

## Contexto sob demanda

- Contrato OpenAPI e módulos backend de subscriptions, guardians, patients e trails para a cascata e as autorizações.
- Perfil/lista web de pacientes, serviços/tipos e `front-end/docs/ai/ACCESSIBILITY.md` para o estado restrito.
- `design-system/front/Design_System_Evolente_Desktop.md` para ação destrutiva e mensagem de estado acessível.

## Risco de contexto

- Médio: a mudança cruza assinatura, dados sensíveis e vínculos. A execução deve limitar cada task aos módulos/rotas afetados e não reabrir checkout, app mobile ou relatórios.
