# EVOLENTE

## Design System App Mobile

Plataforma para profissionais de fonoaudiologia, criancas e responsaveis.

## Objetivo

Documentar a base visual, os principios de experiencia e os componentes do app mobile da Evolente para orientar uma interface terapeutica, guiada e consistente.

## 1. Essencia da marca

No mobile, a Evolente deve parecer segura, acolhedora e motivadora. A identidade continua clinicamente confiavel, mas a traducao visual precisa ser mais calorosa, leve e orientada a interacao.

### Atributos centrais

- acolhimento
- ludicidade
- clareza
- incentivo ao progresso

## 2. Fundamentos visuais

### Fonte da paleta

Paleta oficial do **Evo brandbook** (mesma base do desktop). Artefatos:

- `design-system/front/brandbook/paleta-resumo-bege.png`
- `design-system/front/brandbook/paleta-laranja-rosa.png`
- `design-system/front/brandbook/paleta-verde-vermelho.png`
- `design-system/front/brandbook/paleta-azul-amarelo.png`

### Paleta principal

| Cor | Atributo | Papel | Hex |
|---|---|---|---|
| Laranja Impulso | Impulso | botoes de acao e energia positiva | `#F48700` |
| Rosa Acolhimento | Acolhimento | apoio emocional e suavizacao visual | `#F38DB3` |
| Verde Evolucao | Evolucao | sucesso, conquista e avancos | `#47945E` |
| Vermelho Vitalidade | Vitalidade | atencao, erro e correcoes com cuidado | `#D53924` |
| Azul Confianca | Confianca | orientacao, navegacao e apoio | `#2978BB` |
| Amarelo Descoberta | Descoberta | celebracao, curiosidade e recompensa | `#F5AF01` |
| Bege Equilibrio | Equilibrio | base calma para equilibrar elementos vivos | `#F4E4C3` |

Escalas de tons completas (RGB/CMYK/Pantone): ver `design-system/front/Design_System_Evolente_Desktop.md`.

### Regras de uso da cor

- Misture tons vivos com bastante respiro para evitar sobrecarga sensorial.
- Use amarelo, laranja e verde em momentos de progresso, resposta positiva e recompensa.
- Preserve contraste alto em instrucoes, botoes e mensagens.
- Evite telas com muitos acentos cromaticos competindo ao mesmo tempo.
- Bege Equilibrio e a base; tons claros das familias servem para pastilhas e fundos suaves.

### Tipografia

- Familia principal: `Nunito`.
- Titulos: `Nunito ExtraBold` ou `Bold`.
- Corpo de texto: `Nunito Regular` ou `SemiBold`.
- O texto deve ser curto, direto e facil de entender em primeira leitura.

### Elementos graficos

- formas organicas e cantos arredondados
- ilustracoes amigaveis e inclusivas
- confetes, medalhas e pequenos elementos de celebracao
- uso equilibrado de personagem, audio e imagem como apoio pedagogico

## 3. Principios da experiencia mobile

O app mobile e a experiencia cotidiana da crianca e do responsavel. Ele deve reduzir friccao, guiar a acao e reforcar progresso com linguagem visual positiva.

### Principios de interface

- Menos texto, mais orientacao visual e sonora.
- Poucas escolhas por tela.
- Fluxo previsivel, com proximo passo sempre evidente.
- Feedback imediato para toque, resposta, acerto e tentativa.

### Distincao de publico

| Publico | Caracteristicas esperadas |
|---|---|
| Crianca | interface colorida, guiada, com reforco positivo, avatar e instrucoes curtas |
| Responsavel | interface mais calma, objetiva e informativa, com menos ornamentacao |

Dados clinicos, acompanhamento e orientacoes ficam na area do responsavel, sem expor linguagem tecnica para a crianca.

## 4. Estrutura esperada do app

### Telas principais

- login ou acesso por convite ou codigo
- tela inicial da crianca com avatar, progresso e atividades do dia
- lista de atividades planejadas
- tela de atividade ou jogo
- tela de conquistas e recompensas
- area do responsavel com acompanhamento, orientacoes e notificacoes

### Navegacao

- Para o responsavel, usar navegacao simples e previsivel, preferencialmente inferior quando fizer sentido.
- Para a crianca, priorizar fluxo guiado: iniciar, interagir, receber feedback e continuar.
- Evitar menus profundos; o ideal e no maximo dois niveis antes da tarefa principal.
- Botoes de voltar e sair devem ser claros para evitar perda de contexto ou progresso.

## 5. Sistema de componentes

| Componente | Uso principal | Diretriz visual |
|---|---|---|
| Botao principal | comecar atividade, responder, continuar | grande, arredondado, colorido, com texto curto e icone quando util |
| Card de atividade | atividades do dia ou da semana | ilustrado, com status, tempo estimado e chamada simples |
| Card de recompensa | medalhas, estrelas, sequencias e conquistas | forte apelo visual, com amarelo e laranja como apoio |
| Avatar ou personagem | companhia visual da crianca | expressivo, amigavel e coerente com o tom terapeutico |
| Bloco de instrucao | explicar a proxima acao | texto curto, audio opcional, imagem grande e uma tarefa por tela |
| Feedback | acerto, tentativa, erro e conclusao | animacao leve, som opcional e mensagem positiva |

### Estados obrigatorios

- inicio: deixar claro o que fazer agora
- progresso: mostrar avancos sem poluir a tela
- sucesso: celebrar com leveza e objetividade
- erro ou nova tentativa: corrigir sem punicao visual
- carregando: transicoes curtas e placeholders suaves
- offline ou rede instavel: comunicar impacto e o que ainda pode ser feito

## 6. Gamificacao

- Use estrelas, medalhas, barras de progresso, sequencias e desafios curtos.
- Recompensas devem incentivar constancia, nao comparacao com outras criancas.
- Evite linguagem de fracasso; prefira convites como "vamos tentar de novo".
- Ao concluir uma atividade, mostrar claramente o que foi conquistado e qual e o proximo passo.

## 7. Acessibilidade infantil e uso assistido

- Alvos de toque com minimo de `44 px`; ideal entre `48 px` e `56 px`.
- Tipografia grande e contraste alto em instrucoes, respostas e botoes.
- Audio, imagem e animacao devem apoiar a compreensao, nunca substitui-la de forma obrigatoria.
- Evite piscadas rapidas, excesso de movimento e sons automaticos invasivos.
- A interface deve funcionar tanto para uso autonomo da crianca quanto para uso mediado por um adulto.

## 8. Tokens recomendados

Manter tokens compartilhados com a base da marca para:

- cores
- tipografia
- espacamento
- raio de borda
- sombras
- estados semanticos

No mobile, esses tokens podem ganhar variacoes especificas para toque, gamificacao e leitura infantil, sem quebrar a consistencia com o ecossistema da Evolente.

## 9. Boas praticas de implementacao

- Criar componentes reutilizaveis para `Button`, `Card`, `ActivityCard`, `RewardBadge`, `ProgressBar` e `ScreenContainer`.
- Separar os fluxos de crianca e responsavel em modulos ou navegadores distintos.
- Prever resiliencia de rede e uso parcial offline, quando atividades precisarem continuar em casa.
- Tratar imagens, audios e ilustracoes como assets versionados e organizados por dominio.
- Validar sempre se o reforco visual ajuda a tarefa ou apenas adiciona ruido.

## 10. Resumo

A experiencia mobile da Evolente deve parecer uma brincadeira terapeutica guiada: simples, positiva, segura e visualmente encantadora, sem perder clareza nem acessibilidade.
