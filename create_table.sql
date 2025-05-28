-- Criar tabela sophia_dashboard
CREATE TABLE sophia_dashboard (
    id SERIAL PRIMARY KEY,
    data DATE,
    hora INTEGER,
    campanha TEXT,
    precisao FLOAT,
    velocidade_processamento FLOAT,
    taxa_erro FLOAT,
    latencia FLOAT,
    tokens INTEGER,
    custo_tokens FLOAT,
    sessoes_chat INTEGER,
    status_finalizacao TEXT,
    duracao_sessao FLOAT,
    consultas_por_sessao INTEGER,
    comprimento_consulta INTEGER,
    nps INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW())
);

-- Criar índices para melhor performance
CREATE INDEX idx_sophia_dashboard_data ON sophia_dashboard(data);
CREATE INDEX idx_sophia_dashboard_campanha ON sophia_dashboard(campanha);
CREATE INDEX idx_sophia_dashboard_hora ON sophia_dashboard(hora);

-- Adicionar comentários na tabela
COMMENT ON TABLE sophia_dashboard IS 'Tabela para armazenar métricas de performance da IA SophIA';
COMMENT ON COLUMN sophia_dashboard.data IS 'Data do registro';
COMMENT ON COLUMN sophia_dashboard.hora IS 'Hora do registro (0-23)';
COMMENT ON COLUMN sophia_dashboard.campanha IS 'Nome da campanha';
COMMENT ON COLUMN sophia_dashboard.precisao IS 'Precisão da IA (0-1)';
COMMENT ON COLUMN sophia_dashboard.velocidade_processamento IS 'Velocidade de processamento em segundos';
COMMENT ON COLUMN sophia_dashboard.taxa_erro IS 'Taxa de erro (0-1)';
COMMENT ON COLUMN sophia_dashboard.latencia IS 'Latência em segundos';
COMMENT ON COLUMN sophia_dashboard.tokens IS 'Quantidade de tokens utilizados';
COMMENT ON COLUMN sophia_dashboard.custo_tokens IS 'Custo dos tokens em USD';
COMMENT ON COLUMN sophia_dashboard.sessoes_chat IS 'Número de sessões de chat';
COMMENT ON COLUMN sophia_dashboard.status_finalizacao IS 'Status da finalização da sessão';
COMMENT ON COLUMN sophia_dashboard.duracao_sessao IS 'Duração da sessão em minutos';
COMMENT ON COLUMN sophia_dashboard.consultas_por_sessao IS 'Número de consultas por sessão';
COMMENT ON COLUMN sophia_dashboard.comprimento_consulta IS 'Comprimento médio das consultas em caracteres';
COMMENT ON COLUMN sophia_dashboard.nps IS 'Net Promoter Score (0-10)'; 