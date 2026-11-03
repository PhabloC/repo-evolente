# Handoff - Task 791

## Task

- identificador: 791
- título: Card Encontrar profissionais no perfil mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 071
- objetivo de negócio: responsável descobre profissionais a partir do perfil do app
- entrega verificável: card no perfil abre o diretório autenticado

## Decisões preservadas

- decisão: entrada no mobile é um `HomeActionCard` no perfil, não na home
- motivo: pedido humano alinhado aos cards colapsados do perfil
- impacto: CTA **Ver profissionais** navega para `ProfessionalsDirectory`

- decisão: reutilizar `GET /professionals` sem mudar contrato
- motivo: API e comportamento já entregues no Slice 063
- impacto: busca, área, próximos/outros e WhatsApp no app

- decisão: vínculo continua pelo código da criança
- motivo: diretório é só descoberta
- impacto: modal de contato não cria solicitação

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, Task 791, Slice 071

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| OpenAPI `/professionals` | contrato | seções, busca, telefone |
| `ResponsavelProfileScreen` / `HomeActionCard` | UI | card no perfil |
| rotas mobile | navegação | nova tela |
| página web `/profissionais` | comportamento | busca, contato, hint de vínculo |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| backend / OpenAPI write | contrato já existe |
| design-system front | UI mobile |

## Resultado por stack

- mobile: card no perfil + tela de diretório com busca, área, contato WhatsApp

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/routes/params.ts`
- `mobile/src/routes/RootNavigator.tsx`
- `mobile/src/features/professionals/**`
- task 791, slice 071, índice, este handoff

## Validações executadas

- eslint do escopo — passou
- jest 5 suítes / 12 testes — passou
- typecheck do app — erros pré-existentes fora do escopo

## Pendências ou bloqueios

- conferir no Expo o card e o diretório com API real

## Próxima ação sugerida

- abrir Perfil no app, expandir **Encontrar profissionais** e validar a lista

## Próximo contexto recomendado

- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/professionals/screens/ProfessionalsDirectoryScreen.tsx`

## Contexto que não deve ser carregado na próxima etapa

- fonte: backend / IAP / jogos
- motivo: fora desta task
