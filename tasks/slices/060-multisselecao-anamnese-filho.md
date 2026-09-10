# Slice 060 - Multisseleção na anamnese do filho

## Status

done

## Objetivo de negocio

Permitir que o responsável registre mais de um motivo principal e mais de uma forma de comunicação durante o cadastro de um filho, mantendo a mesma informação consistente na web e no mobile.

## Entrega verificavel

- Web e mobile exibem controles de seleção múltipla para `Motivo principal` e `Comunicação`.
- É possível marcar, desmarcar e revisar várias opções antes de avançar.
- O payload enviado continua compatível com `POST /guardians/me/children` e preserva todas as escolhas.

## Fora de escopo

- Alterar categorias disponíveis, contrato da API ou regras de sugestão de trilha.
- Alterar outras perguntas da anamnese.

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- front-end
- mobile

## Contrato

- Preserva `POST /guardians/me/children`; validar o formato já aceito para listas de respostas de anamnese.

## Referencia visual por stack

- Web: `design-system/front/Design_System_Evolente_Desktop.md`, reutilizando o padrão de campos do wizard existente.
- Mobile: `design-system/mobile/Design_System_Evolente_App_Mobile.md`, reutilizando componentes de seleção existentes.
- Não há print específico desses estados.

## Contexto minimo recomendado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta slice e a Task 650
- handoffs das implementações web/mobile do cadastro de filho

## Contexto sob demanda recomendado

| Gatilho | Fonte | Uso |
|---|---|---|
| UI web | `front-end/src/pages/Auth/RegisterGuardian/**` e cadastro autenticado de filho | localizar perguntas e estado dos campos |
| UI mobile | `mobile/src/features/children/**` | localizar perguntas, estado e componentes |
| Payload | `contracts/openapi.yaml`, path `POST /guardians/me/children` | confirmar compatibilidade do array |
| Acessibilidade | `front-end/docs/ai/ACCESSIBILITY.md` e docs equivalentes do mobile | garantir grupos nomeados e estado selecionado |

## Risco de contexto

- medio; limitar a leitura aos arquivos do formulário, schemas/types e serviço/payload de cada stack.

## Tasks relacionadas

- Task 560 — cadastro autenticado de filho na web — done
- Task 621 — cadastro de filho no perfil mobile — done
- Task 623 — refinamento do formulário mobile — done

## Status final

done



