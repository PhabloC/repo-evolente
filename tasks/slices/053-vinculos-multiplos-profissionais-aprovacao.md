# Slice 053 - Vínculos múltiplos de profissionais com aprovação

## Status

done

## Objetivo de negócio

Permitir que uma criança seja acompanhada por mais de um profissional, preservando o controle do responsável: um vínculo iniciado pelo código da criança só passa a conceder acesso após aprovação explícita do responsável.

## Entrega verificável

- O código de uma criança pode gerar solicitações para profissionais diferentes.
- A solicitação nasce como `pending` e não libera dados, trilhas ou relatórios ao profissional.
- O responsável visualiza o profissional solicitante e aprova ou recusa o vínculo na web e no app.
- Uma aprovação torna o vínculo `active`; uma recusa o torna `rejected`.
- Os vínculos ativos existentes são preservados na migração.

## Fora de escopo

- Convites por e-mail ou notificação push.
- Troca de responsável da criança.
- Gestão de vínculo pelo profissional após a recusa.

## Decisões confirmadas

- A mesma criança pode ter mais de um profissional.
- O vínculo por código depende de aprovação do responsável.
- A aprovação deve estar disponível na área web e no app mobile do responsável.

## Premissas adotadas

- O cadastro de uma nova família feito pelo próprio profissional continua criando vínculo ativo, pois não é uma solicitação sobre uma criança já pertencente a outro responsável.
- Uma nova solicitação do mesmo profissional para a mesma criança não duplica o vínculo; o profissional recebe o estado atual.

## Tasks relacionadas

- `tasks/change-requests/581-vinculos-multiplos-api-aprovacao.md`
- `tasks/change-requests/582-vinculos-multiplos-web-aprovacao.md`
- `tasks/change-requests/583-vinculos-multiplos-mobile-aprovacao.md`
- `tasks/change-requests/584-avatar-profissional-vinculo-web-mobile.md`
- `tasks/change-requests/585-especialidade-profissional-perfil-e-vinculos.md`
- `tasks/change-requests/586-indicador-camera-hover-foto-crianca-web.md`
- `tasks/change-requests/587-corrigir-lint-backend-web-mobile.md`
- `tasks/change-requests/588-consultas-presenciais-timeline-paciente.md`

## Progresso

- Task 581 — done
- Task 582 — done
- Task 583 — done
- Task 584 — done
- Task 585 — done
- Task 586 — done
- Task 587 — in_progress
- Task 587 — done
- Task 588 — done
- Task 590 — done (erro de vínculos no mobile)
- Task 591 — done (falha parcial no perfil do filho web)
- Task 593 — done (erro de consultas no perfil do paciente web)
- Task 595 — done (anamnese protegida e resolução atômica de vínculo)
- Task 596 — done (consultas presenciais compatíveis com modo sem banco)
