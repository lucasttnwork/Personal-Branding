# Agent Copywriter — Knowledge Base

> Base de conhecimento estruturada para agente de IA especializado em roteiros de vídeos curtos.
> Structured knowledge base for an AI agent specialized in short-form video scripts.

---

## Sobre / About

Esta base de conhecimento contém prompts, exemplos e estruturas para alimentar um agente de IA copywriter focado em criação de roteiros para Reels, TikTok e conteúdo de vídeo curto.

This knowledge base contains prompts, examples, and structures to power an AI copywriter agent focused on creating scripts for Reels, TikTok, and short-form video content.

---

## Estrutura de Diretórios / Directory Structure

```
Agent_copywriter/
│
├── Prompts/                          # System prompts para o agente
│   ├── PT-BR/
│   │   └── System_Prompt.md          # Prompt principal em português
│   └── EN-US/
│       └── System_Prompt.md          # Main prompt in English
│
├── Examples/                         # Biblioteca de exemplos categorizados
│   ├── PT-BR/
│   │   ├── Hooks/
│   │   │   ├── Infotainment.md       # 60 hooks de infotenimento
│   │   │   ├── Storytelling.md       # 40 hooks de storytelling
│   │   │   └── Ads.md                # 30 hooks de anúncios
│   │   ├── Transitions/
│   │   │   ├── Impact.md             # 20 transições de impacto
│   │   │   ├── Didactic.md           # 20 transições didáticas
│   │   │   ├── Story.md              # 20 transições narrativas
│   │   │   └── CTA.md                # 20 transições para CTA
│   │   ├── CTAs/
│   │   │   ├── Standard.md           # 20 CTAs padrão
│   │   │   ├── Pre-CTA.md            # 15 pré-CTAs
│   │   │   └── Looping.md            # 15 CTAs de looping
│   │   ├── Punchlines/
│   │   │   └── Printables.md         # 50 frases printáveis
│   │   ├── Objections/
│   │   │   └── Objections_Responses.md  # 25 objeções + respostas
│   │   ├── QPVs/
│   │   │   └── Visual_Patterns.md    # 46 quebras de padrão visual
│   │   └── Scripts/
│   │       ├── Infotainment/
│   │       │   └── 01_Teste_Rapido.md
│   │       ├── Storytelling/
│   │       │   └── 01_Confissao_Vergonha.md
│   │       └── Mini-Doc/
│   │           └── 01_Case_Numeros.md
│   │
│   └── EN-US/                        # Versões localizadas em inglês
│       ├── Hooks/
│       │   ├── Infotainment.md
│       │   ├── Storytelling.md
│       │   └── Ads.md
│       ├── Transitions/
│       │   ├── Impact.md
│       │   ├── Didactic.md
│       │   ├── Story.md
│       │   └── CTA.md
│       ├── CTAs/
│       │   ├── Standard.md
│       │   ├── Pre-CTA.md
│       │   └── Looping.md
│       ├── Punchlines/
│       │   └── Printables.md
│       ├── Objections/
│       │   └── Objections_Responses.md
│       ├── QPVs/
│       │   └── Visual_Patterns.md
│       └── Scripts/
│           ├── Infotainment/
│           │   └── 01_Quick_Test.md
│           ├── Storytelling/
│           │   └── 01_Shame_Confession.md
│           └── Mini-Doc/
│               └── 01_Case_Numbers.md
│
├── Structures/                       # Templates de estrutura de roteiros
│   ├── PT-BR/
│   │   ├── Infotainment_Structure.md
│   │   ├── Storytelling_Structure.md
│   │   ├── Series_Structure.md
│   │   └── Ad_Structure.md
│   └── EN-US/
│       ├── Infotainment_Structure.md
│       ├── Storytelling_Structure.md
│       ├── Series_Structure.md
│       └── Ad_Structure.md
│
├── Examples_raw.md                   # [DEPRECATED] Arquivo original
├── Prompt_raw.md                     # [DEPRECATED] Arquivo original
└── README.md                         # Este arquivo
```

---

## Como Usar / How to Use

### Para alimentar um agente de IA:

1. **System Prompt**: Use o arquivo `Prompts/[LANG]/System_Prompt.md` como prompt de sistema
2. **Exemplos como RAG**: Indexe os arquivos de `Examples/` para retrieval
3. **Estruturas como referência**: Use `Structures/` para templates de formato

### Para consulta manual:

1. Escolha o idioma (`PT-BR` ou `EN-US`)
2. Navegue até a categoria desejada (Hooks, Transitions, CTAs, etc.)
3. Substitua os colchetes `[X]` pelo conteúdo específico do seu nicho

---

## Categorias de Conteúdo / Content Categories

### Hooks (Ganchos)
- **Infotainment**: Dicas rápidas, myth-busting, testes
- **Storytelling**: Confissões, vulnerabilidade, cenas específicas
- **Ads**: Anúncios diretos, objeções chamadas

### Transitions (Transições)
- **Impact**: Marcam momentos-chave
- **Didactic**: Organizam informação educativa
- **Story**: Criam imersão narrativa
- **CTA**: Preparam para ação final

### CTAs (Chamadas para Ação)
- **Standard**: CTAs de fechamento padrão
- **Pre-CTA**: CTAs intermediários no meio do vídeo
- **Looping**: CTAs que conectam ao início para rewatch

### Punchlines (Frases Printáveis)
- Afirmações densas que valem screenshot
- Ideais para pontos de virada e takeaways

### Objections (Objeções)
- Resistências comuns do público
- Formato: objeção → resposta curta

### QPVs / VPBs (Quebras de Padrão Visual)
- Técnicas visuais por cenário (cozinha, escritório, rua)
- Objetos como metáfora
- Técnicas de edição simples

### Scripts (Roteiros)
- Exemplos completos por formato
- Com direção visual e timing

### Structures (Estruturas)
- Templates de estrutura por formato
- Timelines sugeridas
- Checklists de validação

---

## Convenções / Conventions

### Símbolos de Notação
- 🎦 = Direção de câmera/cena
- 🗣 = Fala do apresentador
- 🟨 = Texto na tela
- 🔊 = Efeito sonoro
- ✂️ = Corte/transição

### Placeholders
- `[X]` = Substituir por conteúdo específico
- `[NICHO]` = Inserir nicho do criador
- `[DOR]` = Inserir dor do público
- `[RESULTADO]` = Inserir resultado prometido
- `[GANCHO]` = Inserir frase do hook (para looping)

---

## Extensibilidade / Extensibility

### Para adicionar novos exemplos:

1. Crie o arquivo na categoria apropriada
2. Siga o formato existente (título, descrição, lista numerada)
3. Adicione notas de uso quando relevante
4. Crie versão localizada no outro idioma

### Para adicionar novas estruturas:

1. Crie arquivo em `Structures/[LANG]/`
2. Inclua: fórmula base, timeline, elementos obrigatórios, variações, checklist
3. Crie versão localizada

### Para adicionar novos scripts de exemplo:

1. Crie em `Examples/[LANG]/Scripts/[FORMATO]/`
2. Use numeração incremental (`02_`, `03_`, etc.)
3. Inclua: diagnóstico, hooks, roteiro completo, estrutura aplicada, "por que funciona"

---

## Arquivos Deprecados / Deprecated Files

Os arquivos `Examples_raw.md` e `Prompt_raw.md` são os arquivos originais não-organizados. Eles foram mantidos como referência, mas a nova estrutura organizada deve ser usada.

---

## Próximos Passos / Next Steps

- [ ] Adicionar mais scripts de exemplo por categoria
- [ ] Criar variações de estrutura por duração (15s, 30s, 60s, 90s)
- [ ] Adicionar exemplos específicos por nicho
- [ ] Criar templates de série por tema
- [ ] Adicionar biblioteca de analogias visuais

---

## Licença / License

Este material é propriedade de Lucas Nogueira e faz parte do projeto de Personal Branding.
