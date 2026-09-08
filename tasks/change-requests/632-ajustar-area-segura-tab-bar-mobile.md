# Task 632 - Ajustar área segura da tab bar mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile (Expo / React Native)

## Perfil do projeto

- stack web: front-end (React/Vite)
- mobile: sim

## Contrato

Não aplicável; não há alteração de integração cliente-servidor.

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/058-area-segura-tab-bar-mobile.md`

## Objetivo

Evitar que a tab bar cubra os botões nativos do Android, aplicando corretamente a área segura inferior.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/058-area-segura-tab-bar-mobile.md`

## Contexto sob demanda

- `mobile/src/`: localizar o componente de navegação inferior compartilhado.
- `design-system/mobile/Design_System_Evolente_App_Mobile.md`: preservar a referência visual móvel.
- `mobile/docs/ai/{AGENTS,ARCHITECTURE,CODE_STYLE,QA}.md`: implementar e validar conforme a stack.

## Orçamento de contexto

Baixo (até 8 fontes). Estratégia: limitar a leitura ao componente compartilhado, sua configuração de navegação e às diretrizes móveis necessárias.

## Critérios de aceite

- [ ] A tab bar fica acima da área de navegação do sistema no Android.
- [ ] Os itens e as rotas atuais permanecem inalterados.
- [ ] A aparência fica consistente em aparelhos com e sem inset inferior.

## Dependências

- Slice 010 — concluído; fornece a navegação autenticada existente.

## Resultado da execucao

- Removida a margem inferior negativa que estendia a tab bar sobre a área de navegação nativa do Android.
- Mantido o padding inferior calculado por `useAndroidBottomOverlap`, que passa a elevar a barra acima do inset seguro.
- O ajuste foi aplicado aos shells de responsável, telas empilhadas do responsável e master, preservando as abas e rotas existentes.
- Foram iniciadas builds de loja Android e iOS `1.0.0 (5)` com a correção incorporada.

## Contexto utilizado

- Contexto mínimo da raiz, esta task e o Slice 058.
- Referência móvel: seção de navegação em `design-system/mobile/Design_System_Evolente_App_Mobile.md`.
- Diretrizes de `mobile/docs/ai/{AGENTS,ARCHITECTURE,CODE_STYLE,QA}.md`.
- `ShellTabBar`, `useAndroidBottomOverlap` e os três consumidores do shell para localizar a extensão indevida.

## Handoff

- `.agents/state/handoffs/TASK-632.md`

## Arquivos alterados

- `mobile/src/features/shell/components/ResponsavelStackScreenFrame.tsx`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `mobile/src/features/shell/navigators/MasterShellNavigator.tsx`
- `tasks/slices/058-area-segura-tab-bar-mobile.md`
- `tasks/change-requests/632-ajustar-area-segura-tab-bar-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-632.md`

## Validacoes executadas

- `npm run lint` — aprovado.
- `npm run typecheck` — falhou por erros preexistentes em admin, auth, jogos e trilhas, sem relação com os arquivos alterados.
- `npm run test -- --watch=false` — 39 suites passaram; duas falhas preexistentes em `AdminHomeScreen.test.tsx` e `MemoryGameRenderer/index.test.tsx` interromperam a execução.
- EAS Build Android `36ed4de4-6343-4e6d-bc7d-90ad644d6209` e iOS `35680582-ad3b-4e81-9fa6-36a75bb1d993` iniciadas com `versionCode`/`buildNumber` 5.

## Pendencias pos-task

- Baixar as builds concluídas, publicar o Android no teste interno e enviar o iOS ao App Store Connect/TestFlight.

## Status final

done
