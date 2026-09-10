# TASK-652

- Slice: `047-trilha-self-serve-responsavel-mobile`
- Status final: done
- Decisão: Biblioteca abre a tela existente em modo preview; conclusão fica indisponível nesse modo.
- Correção: wrapper do item preserva a largura da célula do grid; botão fica dentro da mesma coluna.
- Refinamento: ação virou pill com ícone de olho e área de toque mobile.
- Arquivos: `TrailLibraryPane`, `TrailActivityScreen`, navegação e params mobile.
- Validação: typecheck executado; bloqueado por erros globais preexistentes, sem erro novo do fluxo após correção.
- Próximo contexto: Biblioteca/trilha mobile apenas se houver novo refinamento.
