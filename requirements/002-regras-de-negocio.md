# 002 — Regras de negócio

## 1. Autenticação e conta

### 1.1 Login

Campos:

- e-mail
- senha

Ações auxiliares:

- ir para cadastro
- ir para recuperação de senha

### 1.2 Recuperação de senha

1. O usuário solicita recuperação informando o e-mail.
2. O sistema envia um link por e-mail.
3. Ao abrir o link, o usuário define a nova senha.

### 1.3 Cadastro — escolha de tipo

Na criação de conta, o usuário escolhe:

- **Profissional**, ou
- **Responsável / paciente**.

---

## 2. Cadastro de profissional

| Campo | Obrigatório | Observação |
| --- | --- | --- |
| Nome | Sim | — |
| E-mail | Sim | Credencial de acesso |
| Telefone | Sim | — |
| Especialidade | Sim | Ex.: fonoaudiologia, psicologia, TO, etc. |
| Registro profissional | Não | Opcional (ex.: CRFa, CRP, CREFITO — conforme a área) |
| Tipo de atuação | Sim | Individual ou clínica |
| Dados da clínica | Condicional | Exigidos quando o tipo for clínica |
| Senha | Sim | — |

Após o cadastro, o profissional é direcionado ao **pagamento**. O acesso completo só é liberado após a confirmação do pagamento.

---

## 3. Cadastro de responsável e criança

O fluxo ocorre em etapas. O **responsável** é quem faz login. A **criança** é quem recebe o acompanhamento.

### 3.1 Etapa 1 — Dados do responsável

| Campo | Obrigatório | Observação |
| --- | --- | --- |
| Nome completo | Sim | — |
| Data de nascimento | Sim | Validar maioridade |
| CPF | Sim | — |
| Telefone | Sim | — |
| Sexo | Sim | — |
| Grau de parentesco | Sim | Relação com a criança |
| E-mail | Sim | Credencial de acesso à plataforma |
| Senha | Sim | Credencial de acesso à plataforma |

### 3.2 Etapa 2 — Dados da criança

| Campo | Obrigatório |
| --- | --- |
| Nome completo | Sim |
| Data de nascimento | Sim |
| CPF | Sim |
| Sexo | Sim |

Cada criança recebe um **código único de paciente**, usado depois pelo profissional para vínculo.

### 3.3 Etapa 3 — Anamnese

#### Pergunta 1 — Motivo principal de uso do Evolente

Seleção (permitir “Outro” com texto livre):

- Atraso na fala
- Dificuldade de linguagem
- Aprendizagem escolar
- Atenção
- Memória
- Comportamento
- Emoções
- Outro: ________

#### Pergunta 2 — Diagnóstico

- Não
- Sim. Qual? ________

#### Pergunta 3 — Acompanhamento profissional

- Não
- Sim, com:
  - Fonoaudiólogo
  - Psicólogo
  - Terapeuta ocupacional
  - Fisioterapeuta
  - Psicopedagogo
  - Outro: ________

#### Pergunta 4 — Comunicação da criança

- Adequada
- Fala pouco
- Não fala
- Dificuldade para compreender
- Dificuldade para se expressar

#### Pergunta 5 — Desempenho escolar

- Adequado
- Apresenta dificuldades
- Ainda não frequenta a escola

#### Pergunta 6 — Áreas com dificuldade (múltipla escolha)

Esta pergunta **define a personalização automática da trilha**.

- Linguagem
- Fala
- Atenção
- Memória
- Raciocínio
- Emoções
- Socialização
- Leitura
- Escrita
- Matemática

#### Pergunta 7 — Desenvolvimento geral (escala 1 a 5)

1. Muito abaixo do esperado  
2. Abaixo do esperado  
3. Dentro do esperado  
4. Bom  
5. Excelente  

#### Pergunta 8 — Expectativa de uso

Campo aberto: o que se espera alcançar com o aplicativo.

---

## 4. Personalização automática da trilha

Após a anamnese:

1. O sistema gera uma trilha personalizada com base nas áreas marcadas na **pergunta 6**.
2. As categorias de conteúdo da trilha correspondem a essas áreas.
3. Os conteúdos sugeridos são montados automaticamente a partir do catálogo criado pelo master.

---

## 5. Pagamento e liberação de acesso

Regra geral:

1. Cadastro concluído.
2. Pagamento obrigatório (profissional ou responsável).
3. Somente após pagamento o acesso completo é liberado.
4. **Master é isento** de pagamento (`accessGranted=true`, sem checkout).

### 5.1 Planos e gateway

| Audience | Valor mensal | Gateway |
| --- | --- | --- |
| Profissional | R$ 79,00 | Asaas |
| Responsável | R$ 49,00 | Asaas |

- Periodicidade: **mensal**.
- Meios aceitos: **cartão, PIX e boleto**.

### 5.2 Responsável que se cadastra por conta própria

1. Conclui cadastro + anamnese.
2. É direcionado à tela de pagamento.
3. Após o pagamento, é instruído a **baixar o app mobile** e acessar por lá.

### 5.3 Ciclo de estados da assinatura

Fluxo canônico:

`PENDING` → `ACTIVE` → `OVERDUE` → `SUSPENDED` → `CANCELED`

| Estado | Significado | `accessGranted` |
| --- | --- | --- |
| `PENDING` | Checkout iniciado; aguarda confirmação de pagamento | `false` |
| `ACTIVE` | Pagamento confirmado; assinatura em dia | `true` |
| `OVERDUE` | Pagamento em atraso dentro da carência de **3 dias** | `true` (acesso mantido) |
| `SUSPENDED` | Carência esgotada; conta **inativada** e acesso bloqueado | `false` |
| `CANCELED` | Cancelamento ou reembolso; acesso bloqueado | `false` |

Caminhos laterais:

- `PENDING` → `refused` quando o pagamento é recusado no checkout (sem liberar acesso).
- `ACTIVE` → `CANCELED` em cancelamento voluntário ou reembolso (bloqueio imediato).
- `OVERDUE` → `ACTIVE` se o pagamento atrasado for regularizado dentro da carência.

### 5.4 Atraso, cancelamento e reembolso

| Evento | Comportamento |
| --- | --- |
| Pagamento em atraso | Entra em `OVERDUE`; após **3 dias** sem regularização → `SUSPENDED` (inativa a conta) |
| Cancelamento | `ACTIVE`/`OVERDUE` → `CANCELED` com **bloqueio imediato** |
| Reembolso | Permitido até **3 dias de uso** após confirmação do 1º pagamento; ao reembolsar → `CANCELED` e **bloqueia na hora** |
| Inadimplência prolongada | **Não** — sem estado além de `OVERDUE` (3 dias) e `SUSPENDED` |

---

## 6. Conteúdos, atividades e trilhas

| Papel | Regra |
| --- | --- |
| **Master** | Cria, edita e organiza atividades/conteúdos da plataforma |
| **Profissional** | Usa apenas as atividades disponibilizadas pelo master |
| **Profissional** | Monta rotinas/trilhas semanais para a criança |
| **Profissional** | **Não** pode criar atividades personalizadas próprias |

As categorias das atividades correspondem às áreas da pergunta 6 da anamnese.

O profissional monta, no perfil do paciente, uma **rotina semanal** de atividades com base no catálogo do master.

---

## 7. Controle de acesso e vínculo

### 7.1 Profissional

- vê **apenas** pacientes vinculados a ele;
- **não** acessa pacientes de outros profissionais;
- **não** acessa dados de outros profissionais;
- vincula paciente pelo **código único** do paciente.

### 7.2 Inativação (sem exclusão)

Nesta fase:

- master pode **inativar** profissionais e responsáveis — **não excluir**;
- profissional pode **inativar** pacientes sob sua gestão — **não excluir**.

---

## 8. Relatórios e evolução

1. Sempre que uma atividade for concluída, o sistema registra dados de evolução da criança.
2. O profissional gera relatórios em **PDF** e **CSV**.
3. O responsável acessa relatórios **somente após** o profissional disponibilizá-los.

---

## Documentos relacionados

- `001-escopo-produto.md`
- `003-requisitos-nao-funcionais.md`
