# Slice 052 - Dashboard analítico web do responsável

## Status

done

## Objetivo de negocio

O responsável, na web, acompanha a evolução do filho com o mesmo tipo de painel do profissional: indicadores, gráfico diário e demais gráficos da rotina — filtrados pelos filhos da conta, sem virar um clone clínico da carteira profissional.

## Entrega verificavel

- `/dashboard` do responsável deixa de ser só a grade de cards de filhos
- Com filhos cadastrados: KPIs, gráfico de evolução diária (7 dias), gráfico de evolução geral, atividades por área, atividades de hoje e relatórios disponibilizados
- Com 2+ filhos: seletor de filho no próprio dashboard; gráficos e atividades do dia usam o `childId` escolhido
- Com 0 filhos: empty state atual (CTA cadastrar) permanece
- Reuso dos componentes/builders do dashboard profissional (Tasks 439/554), sem novos endpoints

## Fora de escopo

- Copiar CTAs clínicos (criar planejamento, biblioteca, cadência profissional)
- Editar trilha na web
- Jogos e execução da trilha na web
- Dashboard mobile do responsável
- Novos endpoints de summary exclusivo do responsável
- Relatórios gerados pelo responsável (continua só os disponibilizados)

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- front-end

## Contrato

- `GET /guardians/me/children`
- `GET /patients/{patientId}/trails`
- `GET /patients/{patientId}/progress`
- paths de reports já liberados ao responsável (somente disponibilizados)

## Referencia visual por stack

### Web

- tipo: artefato de design system + linguagem do dashboard profissional existente
- fonte primaria: `front-end/src/pages/Main/ShellHome/` (composição: KPIs, DailyEvolutionChart, EvolutionLineChart, ActivitiesByAreaChart, TodayActivitiesCard, WeeklyReportsCard)
- tokens: `design-system/front/Design_System_Evolente_Desktop.md`
- lacuna: **não há print** do dashboard analítico do responsável; não inventar um produto visual novo — reutilizar cards/gráficos do ShellHome, com copy de família (não “painel clínico”)

### Mobile

- tipo: nao se aplica

## Permissoes e atores

- Responsável com `accessGranted=true`
- Isolamento: só filhos da própria conta

## Casos de erro e borda

- Zero filhos (empty state, sem gráficos)
- Um filho (sem seletor, dados desse filho)
- Vários filhos (seletor; filho inválido volta ao primeiro da lista)
- Filho sem trilha/progresso (estados vazios dos gráficos)
- Falha parcial ao carregar trilha/progresso/relatórios
- Relatório ainda não disponibilizado não aparece

## Decisoes humanas confirmadas

- Dashboard do responsável deve ficar parecido com o do profissional
- Precisa ter gráfico de evolução do filho cadastrado e outras informações/gráficos

## Premissas adotadas

- A Task 559 limitou o dashboard a listagem; esta demanda **substitui o conteúdo** da home do responsável, não a navegação (Dashboard, Filhos, Relatórios, Configuração)
- Dados montados no cliente a partir das APIs já usadas (como `getDashboardSummary` do profissional, mas com `GET /guardians/me/children` no lugar de `listPatients`)
- “Relatórios pendentes” do profissional vira “Relatórios disponibilizados” (o responsável não gera relatório)
- Carrossel “maior progresso” da carteira profissional não se aplica; a lista de filhos pode permanecer como atalho abaixo dos gráficos, se couber sem poluir
- CTA do header continua “Cadastrar filho”, não “Criar planejamento”

## Tasks relacionadas

- `tasks/change-requests/562-dashboard-analitico-responsavel-web.md`
- `tasks/change-requests/563-remover-cards-filhos-dashboard-responsavel.md`
- `tasks/change-requests/564-ajustar-acoes-cabecalho-dashboard-responsavel.md`
- `tasks/change-requests/565-remover-cta-dashboard-responsavel-reduzir-espacamento.md`
- `tasks/change-requests/566-dashboard-responsavel-visao-consolidada-filhos.md`

## Dependencias do slice

- Slice 050 (área web do responsável)
- Slice 019 / Tasks 439 e 554 (composição e gráfico diário do profissional)
- Slice 011 (relatórios já existentes)

## Contexto minimo recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice
- `tasks/change-requests/559-area-web-responsavel-shell-dashboard.md` (o que não copiar: menu/CTAs clínicos)

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Layout profissional | `front-end/src/pages/Main/ShellHome/**` | composição | sim |
| Gráfico diário | `DailyEvolutionChart`, `buildDailyEvolutionSeries` | série 7 dias | sim |
| Summary profissional | `getDashboardSummary.ts`, `buildDashboardPanels.ts` | o que reusar vs adaptar | sim |
| Filhos | `useGuardianChildren`, trails/progress | dados | sim |
| A11y | `front-end/docs/ai/ACCESSIBILITY.md` | gráficos e seletor | sim |

## Risco de contexto

- medio
- estrategia: reusar builders/componentes; não reabrir jogos, planejamento nem dashboard master

## Observacoes de rastreabilidade

- Slice 050 entregou a home como listagem. O pedido humano de “parecer o dashboard do profissional” é o Slice 052.

## Progresso das tasks relacionadas

- Task 562 — done
- Task 563 — done (grade de cards de filhos removida do dashboard; seletor e empty state preservados)
- Task 564 — done (CTA do header sem quebra de texto; sino com retorno acessível sobre notificações no app)
- Task 565 — done (CTA removido do dashboard; CTA de Filhos preservado; espaçamento do dashboard reduzido)
- Task 566 — done (visão padrão agregada de todos os filhos e filtro individual)

## Status final

done

## Correcoes posteriores

- Task 592 - done (respostas obsoletas do summary ignoradas).
