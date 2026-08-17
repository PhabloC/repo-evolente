# 003 — Requisitos não funcionais

## 1. Segurança e privacidade

- Atender política de privacidade e exigências da **LGPD**.
- Credenciais de acesso baseadas em e-mail e senha.
- Recuperação de senha via link enviado por e-mail.
- Controle de acesso por perfil (master, profissional, responsável), com isolamento de dados entre profissionais.

## 2. Auditoria e rastreabilidade

- Registrar **histórico de alterações** feitas por cada usuário.
- Manter **logs** do sistema acessíveis ao master.
- Registrar evolução da criança a cada atividade concluída.

## 3. Armazenamento de mídia

- Conteúdos (áudio, vídeo) e imagens devem ficar em **storage**.
- Não persistir arquivos de mídia no banco de dados.

## 4. Plataformas e experiência

- Web para cadastro, pagamento e dashboards (master, profissional e responsável).
- Mobile para master e responsável/paciente, com capacidades do master equivalentes à web e interface adaptada.
- Notificações push no mobile para o responsável (provedor **a definir**).

## 5. Exportação de dados

- Relatórios exportáveis em **PDF** e **CSV** pelo profissional.

## 6. Disponibilidade de acesso

- Acesso completo à plataforma condicionado à confirmação de pagamento da assinatura (profissional ou responsável).

## Documentos relacionados

- `001-escopo-produto.md`
- `002-regras-de-negocio.md`
