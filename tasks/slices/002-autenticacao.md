# Slice 002 - Autenticacao e recuperacao de senha

## Status

done

## Objetivo de negocio

Permitir login por e-mail/senha e recuperacao de senha por link de e-mail na web e no mobile.

## Entrega verificavel

Usuario autenticado acessa a area do perfil; recovery envia link e permite redefinir senha.

## Fora de escopo

- Cadastro de contas
- Pagamento
- Dashboards de negocio

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- front-end
- backend
- mobile

## Contrato

- `contracts/openapi.yaml#/paths` de auth

## Referencia visual por stack

### Web

- tipo: artefato de design system
- fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md` (login, inputs, estados)

### Mobile

- tipo: artefato de design system
- fonte primaria: `design-system/mobile/Design_System_Evolente_App_Mobile.md` (login/acesso)

## Permissoes e atores

- Qualquer perfil cadastrado (master, profissional, responsavel)

## Casos de erro e borda

- Credenciais invalidas
- Recovery nao enumeravel
- Token reset expirado
- Conta inativa

## Decisoes humanas confirmadas

- Stack web: React/Vite; Mobile: sim; Profissional multi-especialidade; Inativar (nao excluir); Gamificacao/jogos fora do escopo

## Premissas adotadas

- Gateway, valores e push a definir — abstrair
- DS documental governa tokens; sem prints nesta fase
- Conflito DS mobile (gamificacao/UI crianca) vs requisitos — prevalece requisito

## Tasks relacionadas

- `tasks/005-api-autenticacao.md` - API auth
- `tasks/006-telas-auth-web.md` - Auth web
- `tasks/007-telas-auth-mobile.md` - Auth mobile
- `tasks/change-requests/093-refinar-auth-mobile-placeholders-visualizacao-senha.md` - refino visual incremental das telas auth mobile
- `tasks/change-requests/094-login-mobile-fiel-ao-print-sem-cadastro.md` - fidelidade visual do login mobile por print concreto
- `tasks/change-requests/096-refinar-fidelidade-login-mobile-print.md` - refino de fidelidade com nuvem SVG real e print versionado
- `tasks/change-requests/097-ajustar-menina-nuvem-e-shapes-login-mobile.md` - menina atras da nuvem e shapes mais espaçados
- `tasks/change-requests/098-ajustar-nuvem-input-e-shapes-login-mobile.md` - nuvem, input e-mail, emoji e shapes fora do texto
- `tasks/change-requests/099-corrigir-camada-menina-atras-nuvem-login-mobile.md` - menina atras da nuvem com SVG de onda
- `tasks/change-requests/100-restaurar-login-mobile-fiel-ao-print.md` - restauracao fiel ao print apos regressao
- `tasks/change-requests/101-login-mobile-asset-menina-nuvem.md` - asset unico menina+nuvem no login
- `tasks/change-requests/102-ajustar-copy-e-shapes-logo-login-mobile.md` - copy e shapes ao lado da logo
- `tasks/change-requests/109-background-animado-login-recuperacao-mobile.md` - fundo animado suave no login e na recuperacao mobile
- `tasks/change-requests/110-fundo-auth-mobile-lava-lamp.md` - refino do fundo animado auth mobile para movimento lava lamp
- `tasks/change-requests/111-goo-lava-auth-mobile.md` - aproximacao do fundo auth mobile ao goo do sidebar web
- `tasks/change-requests/112-remover-fundo-auth-mobile.md` - remocao do fundo animado no auth mobile
- `tasks/change-requests/113-modal-erro-login-mobile.md` - erro de login em modal central no mobile
- `tasks/change-requests/114-elevar-login-com-teclado-mobile.md` - login mobile sobe ao abrir teclado
- `tasks/change-requests/115-reduzir-subida-login-teclado-mobile.md` - reduzir amplitude da subida no login mobile
- `tasks/change-requests/116-remover-encolhimento-lateral-nuvem-login-mobile.md` - remover margem lateral da nuvem no login mobile
- `tasks/change-requests/117-elevar-recuperacao-com-teclado-mobile.md` - recuperacao mobile sobe ao abrir teclado
- `tasks/change-requests/118-restaurar-subtitulo-recuperacao-mobile.md` - restaurar subtitulo da recuperacao mobile
- `tasks/change-requests/119-restaurar-copy-auth-mobile.md` - restaurar a copy completa no login e na recuperacao mobile
- `tasks/change-requests/120-corrigir-login-mobile-api-local.md` - corrigir acesso local da API no login mobile em Expo
- `tasks/change-requests/054-renovacao-automatica-sessao-web.md` - renovacao transparente da sessao web
- `tasks/change-requests/073-endurecer-auth-refresh-e-hidratacao-web.md` - endurecimento incremental do refresh, segredo e hidratacao legada
- `tasks/change-requests/127-refresh-automatico-sessao-mobile.md` - refresh automatico da sessao no mobile
- `tasks/change-requests/491-limpar-sessao-perfil-nao-suportado-no-boot-mobile.md` - boot limpa sessao de perfil sem shell mobile e abre login
- `tasks/change-requests/492-elevar-campos-login-esconder-menina-nuvem-teclado.md` - eleva campos do login e esconde menina/nuvem com teclado
- `tasks/change-requests/493-esconder-hero-login-subir-form-teclado.md` - esconde logo/bem-vindo/subtitulo e sobe o form ao topo
- `tasks/change-requests/494-corrigir-overshoot-login-samsung-pass-pan.md` - evita overshoot com Samsung Pass mantendo form ancorado
- `tasks/change-requests/495-login-resize-form-topo-acima-teclado.md` - resize Android + form no topo; reduz Samsung Pass no login
- `tasks/change-requests/496-estabilizar-elevacao-login-baixar-form.md` - mesma elevação e-mail/senha; restore só ao fechar teclado
- `tasks/change-requests/549-login-mobile-autofill-so-no-compacto.md` - autofill só desligado no estado compacto
- `tasks/change-requests/607-recovery-mobile-aplicar-lift-do-login.md` - recovery aplica a elevação de teclado do login
- `tasks/change-requests/608-fundo-liquid-glass-auth-mobile.md` - fundo liquid glass com bolhas no login e recuperação mobile
- `tasks/change-requests/609-transparencia-painel-auth-teclado-mobile.md` - painel do formulário transparente com teclado aberto no login e recuperação mobile

## Dependencias do slice

- Slice 001

## Contexto minimo recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Requisitos | `requirements/001-escopo-produto.md`, `requirements/002-regras-de-negocio.md` | regras do slice | sim |
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | UI web | sim se UI web |
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | UI mobile | sim se UI mobile |
| API | `contracts/openapi.yaml` | API | sim se API |
| Front-end | `front-end/docs/ai/` | front envolvido | sim se front |
| Backend | `backend/docs/ai/` | back envolvido | sim se back |
| Mobile | `mobile/docs/ai/` | mobile envolvido | sim se mobile |

## Risco de contexto

- baixo
- estrategia: carregar apenas secoes/paths citados nas tasks

## Observacoes de rastreabilidade

- API auth: Task 005 done
- Telas auth web: Task 006 done
- Telas auth mobile: Task 007 done
- Task 093 concluiu o refino visual incremental de login e recovery no mobile com branding, placeholders e visualizacao de senha no login.
- Task 094 concluiu a substituicao do login mobile por uma versao fiel ao print anexado pelo usuario, sem CTA de cadastro.
- Task 788 adicionou CTA “Criar conta” no login mobile abrindo `https://evolente.com.br/cadastro/responsavel` (desvio documentado do print; sem cadastro in-app).
- Task 096 refinou a fidelidade com nuvem SVG real (`SignInCloud`), print em `design-system/mobile/prints/login-mobile.png` e sem cadastro.
- Task 097 ajustou a menina sutilmente atras da nuvem e espaçou shapes top/bottom.
- Task 098 subiu a nuvem, corrigiu corte do e-mail, removeu emoji e afastou shapes do texto.
- Task 099 corrigiu stacking da menina atras da nuvem com SVG de onda dedicado.
- Task 100 restaurou o login ao print original com camadas estaveis e SVG oficial da nuvem.
- Task 101 adotou `menina_nuvem.png` e ajustou texto/logo do login.
- Task 102 desceu o bem-vindo, quebrou o subtitulo e posicionou shapes ao lado da logo.
- Task 104 alinhou o formulario da recuperacao de senha ao padrao visual do login.
- Task 109 adiciona uma camada de background animado suave sobre o shell auth mobile consolidado.
- Task 110 refina essa camada para um movimento mais viscoso e irregular, em estilo lava lamp.
- Task 111 aproxima esse fundo do comportamento goo do sidebar web com massas SVG filtradas.
- Task 112 remove esse fundo e restaura o auth mobile sem efeito decorativo.
- Task 113 substitui o erro inline do login por um modal central com acao explicita de fechamento.
- Task 114 faz a composicao do login recolher o topo e elevar nuvem+form quando o teclado e aberto.
- Task 115 reduz a altura dessa elevacao para um deslocamento mais contido.
- Task 116 remove o encolhimento da nuvem durante a animacao para preservar a largura visual da imagem.
- Task 117 replica o mesmo comportamento de recolhimento/subida na recuperacao de senha mobile.
- Task 118 ajusta a altura do topo da recuperacao para não cortar o subtitulo.
- Task 119 amplia o topo do login e da recuperacao para voltar a exibir toda a copy sem corte inferior.
- Task 120 corrige a resolucao de `localhost` no mobile para permitir login contra a API local via Expo, Android Emulator e dispositivo fisico.
- Task 054 concluiu a renovacao automatica da sessao web por refresh token.
- Task 073 endureceu o fluxo de refresh e a compatibilidade de hidratacao sem reabrir mobile.
- Task 127 estende ao mobile a renovacao automatica da sessao ao receber `401` com `refreshToken` valido.
- Task 607 reutiliza o hook de elevação do login na recuperação, preservando o debounce de fechamento do teclado.
- Task 608 reintroduz no auth mobile bolhas ascendentes e camada liquid glass por solicitação explícita do usuário.
- Task 609 torna transparente o painel claro do formulário enquanto o teclado está aberto no login e na recuperação mobile.
- Slice 002 concluido.

## Progresso das tasks relacionadas

- `tasks/005-api-autenticacao.md` — done
- `tasks/006-telas-auth-web.md` — done
- `tasks/007-telas-auth-mobile.md` — done
- `tasks/change-requests/093-refinar-auth-mobile-placeholders-visualizacao-senha.md` — done
- `tasks/change-requests/094-login-mobile-fiel-ao-print-sem-cadastro.md` — done
- `tasks/change-requests/096-refinar-fidelidade-login-mobile-print.md` — done
- `tasks/change-requests/097-ajustar-menina-nuvem-e-shapes-login-mobile.md` — done
- `tasks/change-requests/098-ajustar-nuvem-input-e-shapes-login-mobile.md` — done
- `tasks/change-requests/099-corrigir-camada-menina-atras-nuvem-login-mobile.md` — done
- `tasks/change-requests/100-restaurar-login-mobile-fiel-ao-print.md` — done
- `tasks/change-requests/101-login-mobile-asset-menina-nuvem.md` — done
- `tasks/change-requests/102-ajustar-copy-e-shapes-logo-login-mobile.md` — done
- `tasks/change-requests/109-background-animado-login-recuperacao-mobile.md` — done
- `tasks/change-requests/110-fundo-auth-mobile-lava-lamp.md` — done
- `tasks/change-requests/111-goo-lava-auth-mobile.md` — done
- `tasks/change-requests/112-remover-fundo-auth-mobile.md` — done
- `tasks/change-requests/113-modal-erro-login-mobile.md` — done
- `tasks/change-requests/114-elevar-login-com-teclado-mobile.md` — done
- `tasks/change-requests/115-reduzir-subida-login-teclado-mobile.md` — done
- `tasks/change-requests/116-remover-encolhimento-lateral-nuvem-login-mobile.md` — done
- `tasks/change-requests/117-elevar-recuperacao-com-teclado-mobile.md` — done
- `tasks/change-requests/118-restaurar-subtitulo-recuperacao-mobile.md` — done
- `tasks/change-requests/119-restaurar-copy-auth-mobile.md` — done
- `tasks/change-requests/120-corrigir-login-mobile-api-local.md` — done
- `tasks/change-requests/054-renovacao-automatica-sessao-web.md` — done
- `tasks/change-requests/073-endurecer-auth-refresh-e-hidratacao-web.md` — done
- `tasks/change-requests/127-refresh-automatico-sessao-mobile.md` — done
- `tasks/change-requests/456-template-email-recuperacao-senha-logo-s3.md` — done
- `tasks/change-requests/457-evitar-timeout-password-recovery-smtp.md` — done
- `tasks/change-requests/458-logo-png-email-recuperacao-senha.md` — done
- `tasks/change-requests/607-recovery-mobile-aplicar-lift-do-login.md` — done
- `tasks/change-requests/608-fundo-liquid-glass-auth-mobile.md` — done
- `tasks/change-requests/609-transparencia-painel-auth-teclado-mobile.md` — done
- `tasks/change-requests/788-botao-criar-conta-login-mobile.md` — done (CTA web para cadastro do responsável)
- `tasks/change-requests/789-versao-sempre-visivel-login-mobile.md` — done (versão fixa no rodapé do login)
- `tasks/change-requests/790-manter-ctas-visiveis-erro-login-mobile.md` — done

## Status final

done
