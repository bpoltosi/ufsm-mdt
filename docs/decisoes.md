# Decisões do projeto

Este documento registra as decisões arquiteturais e de escopo que devem orientar o desenvolvimento do `ufsm-mdt`.

## D-001 — Objetivo principal

O projeto será um **gerador e validador de trabalhos acadêmicos baseado no MDT UFSM 2021**, com foco em reproduzir corretamente a estrutura e a apresentação do modelo de referência e em automatizar apenas regras que possam ser verificadas de forma objetiva.

O projeto não pretende substituir o MDT oficial, regulamentos, editais ou orientação acadêmica.

## D-002 — Prioridade do projeto

A prioridade é, nesta ordem:

1. compreender e mapear o MDT 2021;
2. compreender e preservar o comportamento do template LaTeX de referência;
3. representar corretamente os diferentes tipos de trabalho suportados;
4. gerar projetos LaTeX reproduzíveis;
5. validar regras objetivas;
6. oferecer uma interface simples;
7. oferecer compilação online apenas como conveniência.

A infraestrutura web não pode orientar ou distorcer a implementação das regras acadêmicas.

## D-003 — Fonte normativa

A **UFSM** é a fonte normativa principal.

A página oficial de Normas MDT informa que a MDT 2021 abrange, além de dissertações e teses, trabalhos de conclusão de curso de graduação e pós-graduação e trabalhos de iniciação científica, e que a versão 2021 passou a ser obrigatória a partir de 2022.2.

Fonte: https://www.ufsm.br/orgaos-suplementares/biblioteca/mdt

## D-004 — Template de referência

O ponto de partida técnico será o **MDT UFSM 2021 em LaTeX**, desenvolvido por Eugênio Piveta Pozzobon.

A própria UFSM informa que o modelo foi atualizado conforme a MDT 2021 e revisado/aprovado por unidades de biblioteca da UFSM.

Fontes:
- UFSM: https://www.ufsm.br/orgaos-suplementares/biblioteca/normas-abnt-mdt
- GitHub: https://github.com/Eugenio-Pozzobon/mdt-ufsm-2021-latex
- Overleaf: https://www.overleaf.com/latex/templates/mdt-ufsm-2021/wbmqyzfngtgv

## D-005 — Overleaf

O modelo do Overleaf é considerado uma **distribuição autorizada/referenciada pela própria UFSM**, pois a página oficial da UFSM disponibiliza diretamente o modelo no Overleaf.

O Overleaf informa CC BY 4.0 para essa distribuição e aponta o GitHub como fonte atualizada.

Isso não significa que toda alteração ou código novo do `ufsm-mdt` herde automaticamente essa licença. A política de redistribuição do código incorporado será definida após a conferência dos arquivos e suas licenças.

## D-006 — Não reescrever o template sem necessidade

O `ufsm-mdt` não deve recriar a apresentação do zero.

A classe `ufsm_2021` e os recursos associados serão tratados como a base de apresentação. Alterações serão feitas somente quando necessárias para:

- separar configuração e conteúdo;
- corrigir integração;
- permitir geração automatizada;
- suportar os tipos de trabalho;
- corrigir problemas documentados;
- manter compatibilidade com o MDT adotado.

## D-007 — Tipos de trabalho como perfis

Cada tipo de trabalho será representado por um perfil próprio.

O template de referência expõe, entre outros, comandos para `tese`, `qualificacao`, `dissertacao`, `monografia`, `monografiag`, `tf`, `tfg`, `tcc`, `tccg`, `relatorio` e `generico`.

A lista final de tipos suportados pelo produto não será definida apenas pelos comandos da classe: cada tipo será confrontado com o MDT 2021 e documentado antes de ser considerado suportado.

## D-008 — Modelo interno

O conteúdo do usuário não será tratado diretamente como um grande arquivo LaTeX.

O sistema terá um modelo intermediário contendo, conceitualmente:

```text
Document
├── type
├── metadata
├── pretextual
├── textual
├── posttextual
├── references
└── assets
```

O gerador converte esse modelo para LaTeX.

## D-009 — Interface inicial simples

A interface não será um editor semelhante ao Microsoft Word.

A primeira abordagem deverá privilegiar conteúdo estruturado e simples, mantendo o controle do formato no template.

Não fazem parte do escopo inicial:

- colaboração em tempo real;
- contas de usuários;
- banco de dados;
- armazenamento online permanente;
- IA;
- importação de PDF;
- editor visual complexo.

## D-010 — Dois modos de saída

O usuário terá duas opções:

### A. Download do projeto

O sistema entrega um projeto LaTeX completo para compilação local ou no Overleaf.

### B. PDF sob demanda

O usuário pode solicitar explicitamente a geração do PDF online.

Somente essa solicitação poderá disparar o workflow de compilação do GitHub Actions.

Portanto, a compilação online não é obrigatória para todos os documentos.

## D-011 — Sem backend permanente na primeira versão

A primeira versão não dependerá de VM ou servidor backend 24/7.

A aplicação será prioritariamente estática, com processamento local sempre que possível e GitHub Actions somente para os builds online solicitados.

## D-012 — Validação não é aprovação institucional

O sistema nunca deve apresentar um resultado como "aprovação da UFSM".

A mensagem deve indicar que as regras automatizadas foram verificadas contra uma versão identificada do MDT.

## D-013 — Rastreabilidade das regras

Toda regra automatizada deverá possuir:

- ID;
- severidade;
- fonte;
- versão do MDT;
- seção/página quando disponível;
- descrição;
- implementação;
- teste.

Fluxo obrigatório:

```text
Fonte oficial
   ↓
Regra documentada
   ↓
Implementação
   ↓
Teste
```

## D-014 — Validação incremental

Não tentaremos automatizar todo o MDT de uma vez.

Primeiro serão implementadas regras objetivas e de alto valor. Regras ambíguas serão documentadas antes de serem automatizadas.

## D-015 — Independência do serviço online

O projeto baixado deve continuar útil sem depender do `ufsm-mdt` hospedado.

A saída deverá conter os arquivos necessários para o usuário compilar localmente, respeitadas as licenças e dependências utilizadas.

## D-016 — Mudanças de escopo

Novas funcionalidades somente entram na primeira versão quando forem necessárias para:

- representar corretamente um tipo de trabalho;
- gerar corretamente o documento;
- validar uma regra objetiva;
- testar a geração;
- permitir o uso básico da ferramenta.

Funcionalidades de conveniência ficam para depois.
