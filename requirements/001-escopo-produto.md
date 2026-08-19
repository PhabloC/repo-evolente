# 001 — Escopo do produto

## 1. Visão

O **Evolente** é uma plataforma de acompanhamento do desenvolvimento infantil voltada a profissionais da saúde e da educação, e a responsáveis por crianças.

O sistema oferece:

- acompanhamento de pacientes por profissionais de diferentes áreas (individuais ou clínicas);
- trilhas de aprendizado semanais para a criança treinar;
- conteúdos criados pelo usuário master e reutilizados pelos profissionais;
- personalização automática da trilha com base na anamnese;
- versão **web (desktop)** e **aplicativo mobile**.

## 2. Plataformas

| Plataforma | Público inicial |
| --- | --- |
| Web | Master, profissional e responsável (cadastro, pagamento e dashboards) |
| Mobile | Master e responsável/paciente |

> No mobile, após o login o responsável escolhe o filho e acessa home, perfil, trilha e notificações. O master acessa as mesmas capacidades da web, adaptadas à interface mobile.

## 3. Perfis de usuário

| Perfil | Descrição |
| --- | --- |
| **Master** | Administra a plataforma: usuários, planos, conteúdos, relatórios e logs |
| **Profissional** | Profissional da saúde ou educação (ex.: fonoaudiólogo, psicólogo, terapeuta ocupacional, psicopedagogo, entre outros); atua de forma individual ou como clínica e acompanha pacientes vinculados a ele |
| **Responsável / acompanhante** | Adulto que cria a conta e acessa a plataforma em nome da criança |
| **Paciente / criança** | Pessoa acompanhada; não faz login próprio — o acesso é do responsável |

### 3.1 Tipos de profissional

O perfil **profissional** não se restringe a fonoaudiologia. Pode incluir, entre outros:

- fonoaudiólogo;
- psicólogo;
- terapeuta ocupacional;
- fisioterapeuta;
- psicopedagogo;
- outras especialidades informadas no cadastro.

No cadastro, o profissional também informa se atua como:

- **Individual**, ou
- **Clínica** (com os dados cadastrais típicos de clínica).

## 4. Capacidades por perfil

### 4.1 Master (web e mobile)

- visualizar métricas: profissionais ativos, pacientes cadastrados, atividades realizadas, pagamentos, evolução geral;
- visualizar todos os profissionais e seus pacientes;
- cadastrar, editar e inativar profissionais e responsáveis;
- criar contas e definir permissão: master, profissional ou responsável;
- gerenciar planos/assinaturas e status de pagamento;
- criar e organizar o catálogo de conteúdos das trilhas;
- acessar relatórios de evolução, logs e histórico de alterações.

### 4.2 Profissional (web)

- listar pacientes/responsáveis vinculados;
- criar login de criança/responsável;
- vincular paciente pelo código único;
- editar e inativar pacientes sob sua gestão;
- abrir perfil do paciente (dados + anamnese);
- montar trilha semanal com conteúdos do master;
- acompanhar planos terapêuticos e evolução no app;
- gerar e gerenciar relatórios (PDF e CSV).

### 4.3 Responsável / paciente

**Web**

- cadastro só do responsável e pagamento (assinatura por conta, não por filho);
- após pagamento: dashboard com os filhos cadastrados, cadastro de um ou mais filhos (dados + anamnese), relatórios disponibilizados e configuração de perfil;
- cada filho tem perfil, código único de paciente e trilha individualizada (categorias da anamnese).

**Mobile**

- após o login, selecionar qual filho gerenciar;
- home, perfil, trilha e notificações do filho selecionado;
- cadastro de novo filho nesta fase ocorre na web.

## 5. Conteúdos e atividades (fase atual)

Tipos de conteúdo:

- áudio;
- vídeo.

Atividades classificadas por:

- categoria;
- idade;
- dificuldade;
- objetivo terapêutico.

## 6. Fora de escopo nesta fase

- exclusão definitiva de profissionais ou pacientes (usar inativação);
- criação de atividades personalizadas pelo profissional;
- jogos como tipo de conteúdo (previsto para o futuro);
- gamificação, pontuação e medalhas.

## 7. Fluxos principais

```text
Profissional
  Cadastro → Pagamento → Dashboard web
  → Vincular/criar pacientes → Montar trilha semanal → Acompanhar evolução → Relatórios

Responsável
  Cadastro (só responsável) → Pagamento
  → Web: dashboard / cadastrar filhos (anamnese, código, trilha) / relatórios / perfil
  → App: selecionar filho → Seguir trilha → Receber notificações

Master
  Gestão de usuários, planos, conteúdos, métricas, relatórios e logs
  (web e mobile)
```

## 8. Decisões de produto

### Confirmadas — pagamento e assinatura

| Tema | Decisão |
| --- | --- |
| Gateway de pagamento | **Asaas** |
| Valor profissional | **R$ 79,00** / mês (`7900` centavos) |
| Valor responsável | **R$ 49,00** / mês (`4900` centavos) |
| Periodicidade | **Mensal** |
| Meios de pagamento | **Cartão, PIX e boleto** |
| Master | **Isento** de pagamento |
| Ciclo de estados | `PENDING` → `ACTIVE` → `OVERDUE` → `SUSPENDED` → `CANCELED` |
| Atraso | `ACTIVE` → `OVERDUE` (carência 3 dias); depois → `SUSPENDED` (**inativa a conta**) |
| Cancelamento | → `CANCELED` com **bloqueio imediato** do acesso |
| Reembolso | Até **3 dias de uso** após 1º pagamento; → `CANCELED` e **bloqueia na hora** |
| Inadimplência aberta | **Não** — sem período prolongado além de `OVERDUE` (3 dias) |

### Em aberto

| Tema | Status |
| --- | --- |
| Provedor/biblioteca de notificações push | A definir |
| Jogos como tipo de conteúdo | Futuro |
| Gamificação (pontos/medalhas) | Fora do escopo atual |

## Documentos relacionados

- `002-regras-de-negocio.md`
- `003-requisitos-nao-funcionais.md`
