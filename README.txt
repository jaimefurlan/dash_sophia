# Documentação dos Dashboards SophIA

## 📊 Dashboard IA 🤖

O Dashboard IA monitora o desempenho técnico e operacional da inteligência artificial, fornecendo insights sobre performance, qualidade e impacto nos negócios.

### Conceitos Fundamentais
- **Token**: Unidade básica de processamento de texto. Cada token representa aproximadamente 4 caracteres ou 0.75 palavras em português.
- **Latência**: Tempo entre o envio da pergunta e recebimento da resposta. Crucial para experiência do usuário.
- **NPS (Net Promoter Score)**: Métrica de satisfação que varia de -100 a 100, calculada pela diferença entre promotores e detratores.
- **CSAT (Customer Satisfaction Score)**: Medida de satisfação do cliente em escala de 1 a 5.

### Métricas de Performance Técnica
- **Tokens por sessão**: Quantidade média de tokens processados por sessão
  - Impacto: Afeta custos e tempo de resposta
  - Meta: Otimizar para máximo de 1000 tokens/sessão
  - Alerta: Acima de 2000 tokens/sessão

- **Tokens por resposta**: Quantidade média de tokens por resposta gerada
  - Impacto: Influencia qualidade e custo
  - Meta: Manter entre 50-200 tokens
  - Alerta: Respostas muito curtas (<30) ou longas (>300)

- **Latência média**: Tempo médio de resposta em milissegundos
  - Impacto: Experiência do usuário
  - Meta: < 500ms
  - Alerta: > 1000ms

- **Tempo de processamento**: Duração média do processamento em segundos
  - Impacto: Eficiência operacional
  - Meta: < 2s
  - Alerta: > 5s

- **Custo por sessão**: Custo médio em dólares por sessão
  - Impacto: Eficiência financeira
  - Meta: < $0.05
  - Alerta: > $0.10

- **Chamadas/dia**: Número total de chamadas à API por dia
  - Impacto: Volume de uso
  - Meta: Aumentar 10% mês a mês
  - Alerta: Quedas > 20%

### Métricas de Uso e Engajamento
- **Sessões/dia**: Número total de sessões iniciadas
  - Impacto: Volume de interações
  - Meta: Crescimento 15% mês a mês
  - Alerta: Quedas > 10%

- **Sessões sucesso**: Sessões concluídas com sucesso
  - Impacto: Efetividade
  - Meta: > 90% das sessões
  - Alerta: < 70%

- **Taxa abandono**: Percentual de sessões abandonadas
  - Impacto: Engajamento
  - Meta: < 20%
  - Alerta: > 30%

- **Duração média**: Tempo médio de duração das sessões
  - Impacto: Engajamento
  - Meta: 3-5 minutos
  - Alerta: < 1 minuto

- **Interações/sessão**: Número médio de interações por sessão
  - Impacto: Profundidade do engajamento
  - Meta: 5-10 interações
  - Alerta: < 3 interações

- **Usuários únicos/dia**: Quantidade de usuários únicos por dia
  - Impacto: Base de usuários
  - Meta: Crescimento 20% mês a mês
  - Alerta: Quedas > 15%

### Métricas de Qualidade
- **Precisão**: Taxa de acerto das respostas
  - Impacto: Confiabilidade
  - Meta: > 95%
  - Alerta: < 85%

- **Confiabilidade**: Nível de confiabilidade das respostas
  - Impacto: Qualidade
  - Meta: > 90%
  - Alerta: < 80%

- **Erros críticos**: Percentual de erros críticos
  - Impacto: Qualidade
  - Meta: < 1%
  - Alerta: > 5%

- **Relevância**: Score de relevância das respostas (1-5)
  - Impacto: Satisfação
  - Meta: > 4.5
  - Alerta: < 3.5

- **NPS IA**: Net Promoter Score da IA
  - Impacto: Satisfação
  - Meta: > 50
  - Alerta: < 0

### Métricas de Linguagem
- **Comprimento resposta**: Tamanho médio das respostas
  - Impacto: Clareza
  - Meta: 100-200 caracteres
  - Alerta: < 50 ou > 300

- **Linguagem ofensiva**: Ocorrências de linguagem inadequada
  - Impacto: Qualidade
  - Meta: 0 ocorrências
  - Alerta: > 0

- **Repetições**: Quantidade de repetições nas respostas
  - Impacto: Qualidade
  - Meta: 0 repetições
  - Alerta: > 2

### Métricas de Negócio
- **Conversões**: Número de conversões geradas
  - Impacto: Resultado
  - Meta: Aumentar 20% mês a mês
  - Alerta: Quedas > 10%

- **Eficiência operacional**: Índice de eficiência operacional
  - Impacto: Custo
  - Meta: > 0.8
  - Alerta: < 0.6

- **Redução de custo**: Percentual de redução de custos
  - Impacto: Financeiro
  - Meta: > 30%
  - Alerta: < 10%

## 💰 Dashboard Cobrança

O Dashboard Cobrança monitora o desempenho do canal automatizado de cobrança, focando em resultados financeiros, engajamento e qualidade do atendimento.

### Conceitos Fundamentais
- **Ticket Médio**: Valor médio dos acordos fechados
- **CAC**: Custo de Aquisição de Cliente
- **ROI**: Retorno sobre Investimento
- **Taxa de Conversão**: Percentual de contatos que resultam em acordo

### Métricas Financeiras
- **Valor negociado total**: Soma dos valores negociados
  - Impacto: Resultado financeiro
  - Meta: Aumentar 15% mês a mês
  - Alerta: Quedas > 10%

- **Acordos fechados**: Quantidade de acordos realizados
  - Impacto: Volume de negócios
  - Meta: Aumentar 20% mês a mês
  - Alerta: Quedas > 15%

- **Ticket médio**: Valor médio por acordo
  - Impacto: Eficiência
  - Meta: > R$ 1.000
  - Alerta: < R$ 500

- **% Acordos pagos**: Percentual de acordos efetivamente pagos
  - Impacto: Efetividade
  - Meta: > 80%
  - Alerta: < 60%

- **% Recuperação carteira**: Percentual da carteira recuperada
  - Impacto: Eficácia
  - Meta: > 25%
  - Alerta: < 15%

- **Valor recuperado/sessão**: Valor médio recuperado por sessão
  - Impacto: Eficiência
  - Meta: > R$ 100
  - Alerta: < R$ 50

### Funil de Conversão
- **Abertura 1º contato**: Taxa de abertura do primeiro contato
  - Impacto: Engajamento inicial
  - Meta: > 70%
  - Alerta: < 50%

- **Resposta 1º contato**: Taxa de resposta ao primeiro contato
  - Impacto: Interação
  - Meta: > 60%
  - Alerta: < 40%

- **Entrada negociação**: Taxa de entrada em negociação
  - Impacto: Conversão
  - Meta: > 40%
  - Alerta: < 25%

- **Conclusão negociação**: Taxa de conclusão de negociações
  - Impacto: Fechamento
  - Meta: > 30%
  - Alerta: < 20%

- **Abandono fluxo**: Taxa de abandono durante o fluxo
  - Impacto: Eficiência
  - Meta: < 20%
  - Alerta: > 30%

- **Tempo até decisão**: Tempo médio até a decisão
  - Impacto: Eficiência
  - Meta: < 5 minutos
  - Alerta: > 10 minutos

### Qualidade da IA
- **Acerto proposta**: Taxa de acerto nas propostas
  - Impacto: Eficiência
  - Meta: > 90%
  - Alerta: < 75%

- **% Sem intervenção**: Percentual de casos resolvidos sem humano
  - Impacto: Automação
  - Meta: > 80%
  - Alerta: < 60%

- **NPS/CSAT**: Score de satisfação
  - Impacto: Qualidade
  - Meta: > 70
  - Alerta: < 50

- **Taxa erros conversa**: Percentual de erros na conversa
  - Impacto: Qualidade
  - Meta: < 5%
  - Alerta: > 10%

- **Comprimento sessão**: Duração média das sessões
  - Impacto: Eficiência
  - Meta: 3-5 minutos
  - Alerta: > 10 minutos

### Métricas Operacionais
- **Custo por sessão**: Custo médio por sessão
  - Impacto: Eficiência
  - Meta: < R$ 2
  - Alerta: > R$ 5

- **CAC**: Custo de Aquisição de Cliente
  - Impacto: Eficiência
  - Meta: < R$ 50
  - Alerta: > R$ 100

- **Call center**: Custo por acordo via call center
  - Impacto: Comparativo
  - Meta: 50% menor que call center
  - Alerta: > 80% do call center

### Recorrência
- **Retentativa**: Número de retentativas
  - Impacto: Persistência
  - Meta: < 3 por cliente
  - Alerta: > 5 por cliente

- **Reengajamento**: Taxa de reengajamento pós-lembrete
  - Impacto: Efetividade
  - Meta: > 40%
  - Alerta: < 20%

- **Renegociações**: Número de renegociações
  - Impacto: Flexibilidade
  - Meta: < 2 por acordo
  - Alerta: > 3 por acordo

## 🛍️ Dashboard Vendas

O Dashboard Vendas monitora o desempenho do chatbot de vendas, focando em conversões, funil de vendas e satisfação do cliente.

### Conceitos Fundamentais
- **Lead**: Potencial cliente que demonstrou interesse
- **Funil de Vendas**: Etapas que o cliente percorre até a compra
- **CTR**: Click-Through Rate (Taxa de Cliques)
- **CAC**: Custo de Aquisição de Cliente

### Métricas Comerciais
- **Vendas realizadas**: Número total de vendas
  - Impacto: Resultado
  - Meta: Aumentar 20% mês a mês
  - Alerta: Quedas > 10%

- **Valor total vendas**: Soma dos valores vendidos
  - Impacto: Receita
  - Meta: Aumentar 25% mês a mês
  - Alerta: Quedas > 15%

- **Ticket médio**: Valor médio por venda
  - Impacto: Eficiência
  - Meta: > R$ 500
  - Alerta: < R$ 200

- **Conversão/sessão**: Taxa de conversão por sessão
  - Impacto: Eficiência
  - Meta: > 15%
  - Alerta: < 5%

- **Conversão/lead**: Taxa de conversão por lead
  - Impacto: Qualidade
  - Meta: > 30%
  - Alerta: < 15%

- **CAC**: Custo de Aquisição de Cliente
  - Impacto: Eficiência
  - Meta: < R$ 100
  - Alerta: > R$ 200

- **Tempo fechamento**: Tempo médio até fechamento
  - Impacto: Eficiência
  - Meta: < 24 horas
  - Alerta: > 48 horas

### Funil de Vendas
- **Qualificação leads**: Taxa de qualificação
  - Impacto: Qualidade
  - Meta: > 60%
  - Alerta: < 40%

- **Abandono funil**: Taxa de abandono no funil
  - Impacto: Eficiência
  - Meta: < 30%
  - Alerta: > 50%

- **Agendamento reunião**: Taxa de agendamentos
  - Impacto: Conversão
  - Meta: > 40%
  - Alerta: < 20%

- **Cliques oferta**: Taxa de cliques em ofertas
  - Impacto: Interesse
  - Meta: > 25%
  - Alerta: < 10%

- **Leads 2ª sessão**: Taxa de retorno para segunda sessão
  - Impacto: Engajamento
  - Meta: > 50%
  - Alerta: < 30%

- **Leads totais**: Número total de leads
  - Impacto: Volume
  - Meta: Aumentar 30% mês a mês
  - Alerta: Quedas > 20%

### Performance Chatbot
- **Latência resposta**: Tempo médio de resposta
  - Impacto: Experiência
  - Meta: < 1 segundo
  - Alerta: > 3 segundos

- **Interações/sessão**: Número médio de interações
  - Impacto: Engajamento
  - Meta: 5-10 interações
  - Alerta: < 3 interações

- **Finalização automática**: Taxa de finalização automática
  - Impacto: Automação
  - Meta: > 80%
  - Alerta: < 60%

- **Fallback**: Taxa de transferência para humano
  - Impacto: Eficiência
  - Meta: < 20%
  - Alerta: > 40%

- **Empatia/naturalidade**: Score de empatia (1-5)
  - Impacto: Experiência
  - Meta: > 4.5
  - Alerta: < 3.5

### Satisfação Cliente
- **CSAT**: Customer Satisfaction Score
  - Impacto: Satisfação
  - Meta: > 4.5
  - Alerta: < 3.5

- **NPS IA**: Net Promoter Score
  - Impacto: Recomendação
  - Meta: > 70
  - Alerta: < 50

- **Elogios**: Taxa de elogios recebidos
  - Impacto: Satisfação
  - Meta: > 20%
  - Alerta: < 10%

- **Tempo sessão**: Duração média das sessões
  - Impacto: Engajamento
  - Meta: 3-5 minutos
  - Alerta: < 1 minuto

### Retenção
- **Retorno nova compra**: Taxa de retorno para compra
  - Impacto: Fidelização
  - Meta: > 40%
  - Alerta: < 20%

- **Up-sell/cross-sell**: Taxa de vendas adicionais
  - Impacto: Valor
  - Meta: > 30%
  - Alerta: < 15%

- **Recompra no mês**: Taxa de recompra mensal
  - Impacto: Fidelização
  - Meta: > 25%
  - Alerta: < 10%

## 🎧 Dashboard SAC

O Dashboard SAC monitora o atendimento automatizado, focando em resolução, qualidade e satisfação do cliente.

### Conceitos Fundamentais
- **Resolução 1ª Interação**: Problemas resolvidos sem transferência
- **Fallback**: Transferência para atendente humano
- **Loops**: Conversas que não avançam ou se repetem
- **SLA**: Service Level Agreement (Acordo de Nível de Serviço)

### Resolução
- **Resolução 1ª interação**: Taxa de resolução na primeira interação
  - Impacto: Eficiência
  - Meta: > 80%
  - Alerta: < 60%

- **Resolução sem transferência**: Taxa de resolução sem humano
  - Impacto: Automação
  - Meta: > 70%
  - Alerta: < 50%

- **Transferências para humano**: Taxa de transferências
  - Impacto: Eficiência
  - Meta: < 30%
  - Alerta: > 50%

- **Reabertura chamado**: Taxa de reabertura
  - Impacto: Qualidade
  - Meta: < 10%
  - Alerta: > 20%

- **Chamados resolvidos/dia**: Número de resoluções diárias
  - Impacto: Volume
  - Meta: Aumentar 15% mês a mês
  - Alerta: Quedas > 10%

### Qualidade
- **Score relevância**: Nível de relevância das respostas
  - Impacto: Qualidade
  - Meta: > 4.5
  - Alerta: < 3.5

- **Respostas incorretas**: Taxa de respostas incorretas
  - Impacto: Qualidade
  - Meta: < 5%
  - Alerta: > 10%

- **Loops**: Taxa de loops na conversa
  - Impacto: Eficiência
  - Meta: < 2%
  - Alerta: > 5%

- **Score clareza**: Nível de clareza das respostas
  - Impacto: Compreensão
  - Meta: > 4.5
  - Alerta: < 3.5

### Operacionais
- **Latência média**: Tempo médio de resposta
  - Impacto: Experiência
  - Meta: < 1 segundo
  - Alerta: > 3 segundos

- **Falhas técnicas**: Taxa de falhas
  - Impacto: Estabilidade
  - Meta: < 1%
  - Alerta: > 3%

- **Tempo atendimento**: Duração média do atendimento
  - Impacto: Eficiência
  - Meta: < 5 minutos
  - Alerta: > 10 minutos

- **Tokens/sessão**: Quantidade de tokens por sessão
  - Impacto: Custo
  - Meta: < 500 tokens
  - Alerta: > 1000 tokens

### Satisfação
- **CSAT**: Customer Satisfaction Score
  - Impacto: Satisfação
  - Meta: > 4.5
  - Alerta: < 3.5

- **NPS IA**: Net Promoter Score
  - Impacto: Recomendação
  - Meta: > 70
  - Alerta: < 50

- **Feedback positivo**: Taxa de feedback positivo
  - Impacto: Satisfação
  - Meta: > 80%
  - Alerta: < 60%

- **Reclamações pós**: Taxa de reclamações
  - Impacto: Qualidade
  - Meta: < 5%
  - Alerta: > 10%

### Volume
- **Sessões/dia**: Número de sessões diárias
  - Impacto: Volume
  - Meta: Aumentar 20% mês a mês
  - Alerta: Quedas > 10%

- **Sessões/mês**: Número de sessões mensais
  - Impacto: Volume
  - Meta: Aumentar 20% mês a mês
  - Alerta: Quedas > 10%

- **Simultâneas máx**: Máximo de sessões simultâneas
  - Impacto: Capacidade
  - Meta: > 100
  - Alerta: < 50

- **Sessões WhatsApp/Web**: Distribuição por canal
  - Impacto: Canais
  - Meta: 60% WhatsApp, 40% Web
  - Alerta: Desbalanceamento > 20%

## 📱 Dashboard WhatsApp

O Dashboard WhatsApp monitora o desempenho das campanhas no WhatsApp, focando em entregabilidade, engajamento e ROI.

### Conceitos Fundamentais
- **Template**: Modelo de mensagem pré-aprovado
- **Custo Meta**: Custo por mensagem do WhatsApp Business API
- **Custo Gupshup**: Custo do provedor de mensagens
- **ROI**: Retorno sobre Investimento

### Performance Campanha
- **Mensagens Enviadas**: Total de mensagens enviadas
  - Impacto: Volume
  - Meta: Aumentar 30% mês a mês
  - Alerta: Quedas > 15%

- **Taxa de Entrega**: Percentual de mensagens entregues
  - Impacto: Efetividade
  - Meta: > 95%
  - Alerta: < 90%

- **Taxa de Leitura**: Percentual de mensagens lidas
  - Impacto: Engajamento
  - Meta: > 80%
  - Alerta: < 60%

- **Taxa de Resposta**: Percentual de respostas recebidas
  - Impacto: Interação
  - Meta: > 40%
  - Alerta: < 20%

- **Taxa de Clique**: Percentual de cliques em links
  - Impacto: Conversão
  - Meta: > 25%
  - Alerta: < 10%

- **Conversões**: Número total de conversões
  - Impacto: Resultado
  - Meta: Aumentar 20% mês a mês
  - Alerta: Quedas > 10%

- **Conversões/1K msgs**: Taxa de conversão por mil mensagens
  - Impacto: Eficiência
  - Meta: > 50
  - Alerta: < 20

- **ROI**: Retorno sobre investimento
  - Impacto: Eficiência
  - Meta: > 200%
  - Alerta: < 100%

### Custos
- **Custo Total Meta**: Custo com Meta Ads
  - Impacto: Investimento
  - Meta: < 30% do orçamento
  - Alerta: > 50% do orçamento

- **Custo Total Gupshup**: Custo com provedor
  - Impacto: Operacional
  - Meta: < 10% do orçamento
  - Alerta: > 20% do orçamento

- **Custo Total Geral**: Soma dos custos
  - Impacto: Financeiro
  - Meta: < 40% do orçamento
  - Alerta: > 60% do orçamento

### Templates
- **Marketing**: Template para campanhas de marketing
  - Uso: Campanhas promocionais
  - Custo: USD 0.0625 por mensagem
  - Meta: Conversão > 5%

- **Marketing (Lite)**: Versão simplificada
  - Uso: Campanhas menores
  - Custo: USD 0.05625 por mensagem
  - Meta: Conversão > 3%

- **Utility**: Template para mensagens utilitárias
  - Uso: Informações importantes
  - Custo: USD 0.008 por mensagem
  - Meta: Entrega > 95%

- **Authentication**: Template para autenticação
  - Uso: Códigos de verificação
  - Custo: USD 0.0315 por mensagem
  - Meta: Entrega > 98%

- **Service**: Template para atendimento
  - Uso: Suporte ao cliente
  - Custo: USD 0.001 por mensagem
  - Meta: Resposta > 80%

- **Ads Click to WhatsApp**: Template para anúncios
  - Uso: Campanhas pagas
  - Custo: USD 0.001 por mensagem
  - Meta: CTR > 2%

- **Sessão (resposta)**: Template para respostas
  - Uso: Respostas a mensagens
  - Custo: USD 0.001 por mensagem
  - Meta: Resposta < 1 minuto

## 📈 Fórmulas Importantes

### Taxas e Percentuais
- Taxa de Conversão = (Conversões / Total de Interações) * 100
- ROI = ((Receita - Custo) / Custo) * 100
- NPS = % Promotores - % Detratores
- CSAT = (Satisfeitos / Total de Avaliações) * 100

### Médias e Totais
- Ticket Médio = Valor Total / Número de Vendas
- CAC = Custo Total de Aquisição / Número de Clientes
- Duração Média = Soma das Durações / Número de Sessões

## 💡 Dicas de Uso

1. **Filtros**: Utilize os filtros de data e hora para análises específicas
2. **Comparativos**: Compare períodos diferentes para identificar tendências
3. **Detalhamento**: Clique nas métricas para ver mais detalhes
4. **Exportação**: Use o botão de exportação para análises externas

## ❓ FAQs

### Como são calculados os indicadores?
Todos os indicadores são calculados em tempo real com base nos dados do banco de dados.

### Qual a frequência de atualização?
Os dados são atualizados a cada 5 minutos.

### Como interpretar o NPS?
- 70+ Excelente
- 50-70 Bom
- 0-50 Precisa melhorar
- Negativo Crítico

## 📞 Suporte

Para suporte técnico ou dúvidas sobre os indicadores, entre em contato:
- Email: suporte@sophia.ai
- Telefone: (11) 9999-9999
- Horário: Seg-Sex, 9h-18h 