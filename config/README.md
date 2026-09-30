# Configuração

A configuração representa **metadados e opções do trabalho**, não o conteúdo acadêmico.

## Separação

```text
configuração -> dados do trabalho
template     -> aparência e composição
conteúdo     -> texto acadêmico
validator    -> verificações
```

## Campos previstos

- versão do MDT;
- tipo de trabalho;
- idioma;
- instituição;
- centro;
- curso;
- autor;
- orientador/coorientador;
- banca;
- título/subtítulo;
- área;
- datas;
- elementos pré-textuais opcionais;
- paginação.

## Exemplo conceitual

```yaml
mdt_version: "2021"
document_type: "tcc"
language: "pt-BR"

institution:
  name: "Universidade Federal de Santa Maria"
  center: ""
  center_acronym: ""
  course: ""
  course_level: "Graduação"
  city: "Santa Maria"
  state: "RS"

work:
  title: ""
  subtitle: ""
  english_title: ""
  english_subtitle: ""
  area: ""

author:
  name: ""
  sex: ""
  email: ""

advisor:
  name: ""
  title: ""
  institution: ""
  sex: ""

options:
  dedication: false
  acknowledgements: false
  epigraph: false
  errata: false
  catalog_card: false
  abbreviations: false
  acronyms: false
  symbols: false
```

O schema ainda é preliminar. Antes de congelá-lo, devemos mapear os comandos de metadados da classe `ufsm_2021.cls` e classificá-los como obrigatórios, opcionais, condicionais ou obsoletos.

Textos longos devem permanecer em arquivos de conteúdo. O YAML/TOML não deve virar um editor de texto disfarçado.
