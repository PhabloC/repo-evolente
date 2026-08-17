# Slice 008 - Refinamento do design system web e mobile

## Status

done

## Objetivo de negocio

Melhorar a qualidade e a clareza dos artefatos documentais do design system da Evolente para que web e mobile tenham referencia visual mais consistente e acionavel.

## Entrega verificavel

Os documentos `design-system/front/Design_System_Evolente_Desktop.md` e `design-system/mobile/Design_System_Evolente_App_Mobile.md` passam a usar estrutura editorial consistente, com principios, tokens, componentes, estados e recomendacoes de uso mais claras.

## Fora de escopo

- Criar telas novas de produto.
- Alterar codigo em `front-end/`, `next-js/`, `backend/` ou `mobile/`.
- Definir requisitos funcionais fora do escopo documental.

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- raiz

## Contrato

- nao se aplica

## Referencia visual por stack

### Web

- tipo: artefato documental
- fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md`

### Mobile

- tipo: artefato documental
- fonte primaria: `design-system/mobile/Design_System_Evolente_App_Mobile.md`

## Permissoes e atores

- nao se aplica

## Casos de erro e borda

- Estrutura desigual entre os documentos de web e mobile, dificultando consulta cruzada.
- Excesso de HTML e tabelas simples, reduzindo legibilidade e manutencao.
- Diretrizes visuais validas, mas pouco operacionais para uso futuro.

## Decisoes humanas confirmadas

- O usuario pediu reformulacao dos dois documentos de design system, sem solicitacao de mudanca de produto ou implementacao de codigo.

## Premissas adotadas

- O escopo e editorial/documental.
- A paleta e o tom de marca atuais devem ser preservados.
- O objetivo principal e melhorar organizacao, clareza e consistencia entre plataformas.

## Tasks relacionadas

- `tasks/change-requests/008-refinamento-design-system-web-mobile.md` - executa a reformulacao documental.

## Dependencias do slice

- Nenhuma

## Contexto minimo recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice
- task relacionada

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Revisao documental web | `design-system/front/Design_System_Evolente_Desktop.md` | para reestruturar o design system desktop | sim |
| Revisao documental mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | para reestruturar o design system mobile | sim |

## Risco de contexto

- baixo
- estrategia de fatiamento ou reducao de contexto: limitar a leitura aos dois arquivos-alvo e ao backlog raiz.

## Observacoes de rastreabilidade

- A execucao atua somente sobre a documentacao fonte do design system.

## Status final

done
