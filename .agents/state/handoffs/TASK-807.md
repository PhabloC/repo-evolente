# Handoff - Task 807

## Task

- identificador: 807
- título: Corrigir avisos Play Console (DEX + edge-to-edge)
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 073
- objetivo de negócio: reduzir avisos de qualidade Android na Play Console
- entrega verificável: R8 ligado no release + modais edge-to-edge; próximo AAB deve melhorar ofuscação DEX

## Decisões preservadas

- decisão: habilitar R8 via `expo-build-properties` + plugin local `withAndroidR8Optimize` (preset optimize)
- motivo: template Expo/RN ainda usa `proguard-android.txt` com `-dontoptimize`
- impacto: próximo `eas build` production Android regenera nativo com minify/shrink/optimize

- decisão: não setar `android.edgeToEdgeEnabled` em `app.json`
- motivo: no SDK 57 o prebuild avisa que a customização não existe mais (edge-to-edge mandatório)
- impacto: aviso residual de APIs descontinuadas pode continuar por `react-native`/`expo-image-picker` internos

- decisão: tornar todos os `<Modal>` translucent nas system bars
- motivo: mitigação app-level do aviso de experiência edge-to-edge
- impacto: UI de modal alinhada ao desenho sob status/nav bar no Android

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `tasks/000-index.md`
- `tasks/change-requests/807-corrigir-avisos-play-console-dex-edge-to-edge.md`
- `tasks/slices/073-play-console-qualidade-android.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `mobile/app.json` | plugin R8 / navigation-bar | config de build |
| `mobile/package.json` | instalar `expo-build-properties` | dependência |
| Modais em `mobile/src` | edge-to-edge | props translucent |
| Docs Play/Expo R8 | aceite DEX | estratégia R8 |

### Contexto evitado

- front-end, backend, requirements, design-system

## Arquivos alterados

- `mobile/app.json`
- `mobile/package.json` / lockfile
- `mobile/plugins/withAndroidR8Optimize.js`
- Modais (SignIn, AppConfirm, ProfessionalContact, AdminUserDetail, WordSearch)
- task/slice/índice/handoff

## Validacoes executadas

- Confirmação local (gitignored): `android.enableMinifyInReleaseBuilds=true`, preset `proguard-android-optimize.txt`, keep Expo Modules
- Instalação `expo-build-properties@~57.0.22`

## Pendencias

- Submit do AAB 1.0.4 (versionCode 27) à Play Console e validar % DEX no App bundle explorer
- Smoke test no dispositivo (R8)
- Aviso edge-to-edge pode persistir por APIs internas do RN até update upstream

## Build produção gerado

- versão: `1.0.4` / versionCode `27`
- build: https://expo.dev/accounts/phabloc/projects/mobile/builds/0ec1e225-a35b-4349-b530-35aef3a92a5f
- AAB: https://expo.dev/artifacts/eas/wDK0wkQY0R9Mw_iJo7lZoBoVftYfa9Otj0utacte4Ck.aab

## Próxima ação sugerida

- `eas submit --platform android --profile production` (ou upload manual) e conferir ofuscação na Play

## Próximo contexto recomendado

- `mobile/app.json` (`expo.version`)
- `mobile/eas.json`
- Slice 061 (deploy lojas), se for o fluxo de publicação
