# Arquitetura da experiência web

## Objetivo

A interface web do UFSM-MDT é uma camada de apresentação sobre o núcleo Python. Ela não deve reproduzir regras da MDT nem assumir responsabilidades que pertencem aos perfis, ao modelo, ao validador ou ao gerador.

## Princípios

- **Núcleo como fonte de verdade:** perfis, metadados, regras, validação e geração permanecem no código/configuração do projeto.
- **UI como consumidora:** a interface coleta dados, apresenta estado e dispara operações do núcleo.
- **Rastreabilidade:** toda exigência normativa exibida deve poder ser relacionada ao perfil/regra/documentação correspondente.
- **Progressive disclosure:** mostrar primeiro o essencial e revelar detalhes conforme o usuário avança.
- **Minimalismo editorial:** hierarquia tipográfica clara, espaços generosos, poucos componentes e identidade visual coerente com a UFSM.
- **Acessibilidade por padrão:** HTML semântico, foco visível, teclado, labels explícitos, mensagens associadas aos campos e comportamento responsivo.
- **Sem persistência remota na primeira versão:** rascunhos podem existir no navegador, mas não haverá conta ou banco como requisito.
- **Baixa dependência operacional:** preferir HTML/CSS/JS simples quando atender ao contrato; evitar dependências que aumentem custo de manutenção ou CI.
- **Validação antes da geração:** o usuário deve conseguir entender e corrigir problemas antes de solicitar uma saída.
- **Build sob demanda:** PDF online não deve ser acionado por cada alteração de formulário.

## Camadas e contratos

```text
┌─────────────────────────────────────────────┐
│                  Site / UI                  │
│ seleção · formulário · conteúdo · feedback  │
└──────────────────────┬──────────────────────┘
                       │ dados do documento
                       ▼
┌─────────────────────────────────────────────┐
│              Modelo / Perfis                │
│ Document · metadata · sections · assets     │
└───────────────┬─────────────────┬───────────┘
                │                 │
                ▼                 ▼
        ┌──────────────┐  ┌─────────────────┐
        │  Validador   │  │    Gerador      │
        │ findings     │  │ projeto LaTeX   │
        └──────────────┘  └────────┬────────┘
                                    │
                                    ▼
                            projeto LaTeX / PDF
```

### Contrato mínimo do documento

O estado editável da UI deve ser serializável para o modelo existente:

- `type`
- `metadata`
- `sections`
- `references`
- `assets`

A UI pode manter estado transitório de navegação, mas esse estado não deve virar requisito do núcleo.

### Contrato de perfil

Cada perfil deve continuar sendo a autoridade para:

- identificação e nome do tipo;
- comando/base LaTeX;
- metadados necessários;
- informações descritivas usadas pelo catálogo;
- diferenças estruturais conhecidas.

A UI não deve manter uma segunda lista manual de requisitos.

### Contrato de validação

O resultado do validador é uma coleção de findings com:

- `rule_id`;
- `severity`;
- `message`.

A apresentação web deve distinguir ERROR, WARNING e INFO sem alterar sua semântica.

### Contrato de geração

A UI entrega um `Document` válido ao gerador. O gerador permanece responsável por criar o projeto LaTeX e por aplicar o perfil selecionado.

## Arquitetura de navegação

A experiência final será organizada em quatro áreas funcionais:

1. **Início** — proposta, princípios e acesso rápido.
2. **Perfis** — catálogo navegável dos tipos suportados e suas características.
3. **Criador** — fluxo guiado para preencher um documento.
4. **Regras e fontes** — exploração das regras automatizadas e das evidências que as sustentam.

A implementação pode permanecer em uma aplicação estática enquanto isso reduzir complexidade. Rotas, páginas ou componentes só devem ser separados quando trouxerem benefício real de manutenção ou UX.

## Fluxo principal

```text
Início
  ↓
Escolher perfil
  ↓
Preencher metadados
  ↓
Escrever/organizar conteúdo
  ↓
Validar
  ├─ corrigir
  └─ continuar
       ↓
Exportar projeto LaTeX
       └─ opcionalmente solicitar PDF
```

## Responsabilidades por camada

| Necessidade | Responsável |
|---|---|
| listar perfis | catálogo/perfis |
| explicar requisitos | perfil + documentação |
| coletar metadados | UI |
| representar documento | `Document` |
| validar regras | `validator.py` |
| gerar LaTeX | `generator.py` |
| compilar PDF | workflow sob demanda |
| persistir rascunho local | camada web |
| registrar fonte normativa | documentação de regras |

## O que deliberadamente não entra na UI

- regras normativas hard-coded;
- exigências inventadas por conveniência visual;
- validação duplicada em JavaScript quando o núcleo já possui a regra;
- autenticação;
- banco de dados;
- colaboração;
- editor WYSIWYG complexo;
- geração automática de PDF a cada mudança.

## Estratégia de implementação

Os próximos blocos devem evoluir a interface de forma incremental:

1. catálogo baseado nos perfis existentes;
2. explorador de regras e evidências;
3. criador guiado;
4. validação integrada;
5. exportação;
6. integração completa com o núcleo;
7. persistência local;
8. auditoria de acessibilidade, responsividade e UX.

Cada etapa deve reutilizar contratos já definidos e produzir mudanças pequenas o suficiente para revisão e validação local antes de consumir GitHub Actions.

## Definition of Done desta arquitetura

- A UI não é fonte de verdade para regras institucionais.
- O modelo `Document` é o contrato central de dados.
- Perfis são a fonte para catálogo e requisitos.
- O validador é a fonte para findings.
- O gerador é a fonte para exportação LaTeX.
- PDF online é uma operação explícita e separada.
- A estrutura permite evolução sem introduzir backend permanente.
