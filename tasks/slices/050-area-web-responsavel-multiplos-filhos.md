# Slice 050 - Área web do responsável e cadastro de filhos

## Status

done

## Objetivo de negocio

Depois do pagamento, o responsável usa a web: dashboard dos filhos, cadastro de um ou mais filhos (com anamnese, perfil, código único e trilha individual), relatórios e configuração de perfil.

## Entrega verificavel

- Login web com `accessGranted` leva ao dashboard do responsável, não mais a `/baixar-app`
- Navegação web: Dashboard, Filhos, Relatórios, Configuração (perfil)
- Responsável autenticado cadastra N filhos; cada um tem perfil, anamnese, `patientCode` único e `suggestedTrailCategories` próprias
- Dashboard lista os filhos cadastrados e o estado vazio com CTA para cadastrar o primeiro

## Fora de escopo

- Execução da trilha, jogos e notificações na web (continuam no mobile)
- Edição da trilha semanal pelo responsável na web
- Cadastro de filho no app mobile
- Seletor de filho no mobile (Slice 051)
- Mudança do fluxo `POST /patients` do profissional
- Limite comercial de filhos (definido depois no Slice 074: no máximo 3)

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- front-end
- backend (já entregue no Slice 049; este slice consome)

## Contrato

- `POST /guardians/me/children`
- `GET /guardians/me/children`
- `GET/PATCH /guardians/me`
- paths de reports já existentes para o responsável

## Referencia visual por stack

### Web

- tipo: artefato de design system
- fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md` (shell autenticado, tabelas, formulários, estados)
- fontes adjacentes: shell atual em `front-end/src/layout/**` e wizard de anamnese em `front-end/src/pages/Auth/RegisterGuardian/**`
- lacuna: **não há prints** da área web do responsável; não inventar um produto visual novo — reutilizar shell, tokens e padrões do dashboard profissional, com navegação reduzida aos itens confirmados

### Mobile

- tipo: nao se aplica

## Permissoes e atores

- Responsável com `accessGranted=true`
- Sem acesso completo, permanece no gate `/assinatura`
- Criança sem login

## Casos de erro e borda

- Zero filhos (empty state + CTA cadastrar)
- CPF da criança igual ao do responsável ou já existente
- Anamnese incompleta / pergunta 6 vazia
- Relatório ainda não disponibilizado pelo profissional (403 já existente)
- Conta antiga com um filho já criado no register atômico aparece na listagem

## Decisoes humanas confirmadas

- Após acessar a conta, o responsável cadastra mais de um filho
- Cada filho tem perfil, trilha individualizada e código único
- Versão web do responsável é liberada com dashboard, filhos, relatórios e configuração (perfil)
- O cadastro que era da criança no onboarding público passa a ser feito dentro da plataforma

## Premissas adotadas

- Cadastro de filho só depois do pagamento (`accessGranted`)
- Parentesco é por filho, não mais obrigatório no perfil do responsável
- Trilha individualizada = anamnese + `suggestedTrailCategories` + trilhas já persistidas por `childId` (modelo atual)
- A montagem/execução da trilha permanece no mobile (Slice 047); o dashboard web da 559 só resume status. Visão analítica (gráficos) é o Slice 052.
- Relatórios web do responsável reutilizam a API já existente (só os disponibilizados)
- Configuração = perfil do responsável (nome, telefone, senha/avatar se já existirem), não o perfil da criança

## Tasks relacionadas

- `tasks/change-requests/559-area-web-responsavel-shell-dashboard.md`
- `tasks/change-requests/560-cadastro-filho-autenticado-web.md`
- `tasks/change-requests/567-balao-download-app-sidebar-responsavel.md`
- `tasks/change-requests/568-claymorphism-balao-download-sidebar-responsavel.md`
- `tasks/change-requests/569-reduzir-espaco-cta-icones-header.md`
- `tasks/change-requests/570-refinar-layout-pagina-filhos.md`
- `tasks/change-requests/571-alinhar-perfil-filho-responsavel-perfil-paciente.md`
- `tasks/change-requests/572-reproduzir-composicao-perfil-profissional-filho.md`
- `tasks/change-requests/573-remover-card-acesso-plataforma-perfil-responsavel.md`

## Dependencias do slice

- Slice 049 (register sem filho + POST children)
- Slice 005/039 (gate de assinatura)
- Slice 011 (relatórios já existentes)
- Slice 047 (trilha por criança já existe)

## Contexto minimo recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice
- `tasks/slices/049-cadastro-responsavel-sem-filho.md`

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | shell/dashboard | sim |
| A11y | `front-end/docs/ai/ACCESSIBILITY.md` | UI | sim |
| API filhos | `contracts/openapi.yaml` guardians/children e anamnese | cadastro | sim |
| Relatórios | paths de reports do responsável | tela relatórios | sim se UI relatórios |
| Wizard legado | `front-end/src/pages/Auth/RegisterGuardian/**` | reuso da anamnese | sim |

## Risco de contexto

- medio
- estrategia: não copiar o dashboard profissional inteiro; navegação só com os 4 destinos confirmados

## Observacoes de rastreabilidade

- Substitui o pós-pagamento `/baixar-app` (`resolvePostAuthPath` + `GuardianAppGate`) como destino padrão.
- A página `/baixar-app` pode permanecer como CTA opcional, mas não é mais o gate da conta.

## Progresso das tasks relacionadas

- Task 559 — done
- Task 560 — done
- Task 567 — done (balão de download do app na sidebar apenas do responsável)
- Task 568 — done (balão de download refinado em claymorphism)
- Task 569 — done (CTA e ícones do header agrupados sem largura ociosa da busca)
- Task 570 — done (página Filhos com resumo familiar e composição mais preenchida)
- Task 571 — done (perfil do filho alinhado visualmente ao perfil de paciente)
- Task 572 — done (composição do perfil profissional reproduzida no perfil do filho)
- Task 573 — done (cartão de acesso ao aplicativo removido do perfil do responsável)
- Task 579 — done (parentesco removido do resumo do card de filho)
- Task 580 — done (pesquisa do cabeçalho respeita ações já exibidas)

## Status final

done
