import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_mock_data(num_records=500):
    # Datas
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    dates = [start_date + timedelta(days=x) for x in range((end_date - start_date).days)]
    
    # Campanhas
    campanhas = ['Campanha A', 'Campanha B', 'Campanha C', 'Campanha D']
    
    # Status de finalização
    status = ['Concluído', 'Abandonado', 'Erro', 'Em Progresso']
    
    data = {
        'data': np.random.choice(dates, num_records),
        'hora': np.random.randint(0, 24, num_records),
        'campanha': np.random.choice(campanhas, num_records),
        'precisao': np.random.uniform(0.7, 1.0, num_records),
        'velocidade_processamento': np.random.uniform(0.1, 2.0, num_records),
        'taxa_erro': np.random.uniform(0, 0.3, num_records),
        'latencia': np.random.uniform(0.1, 1.0, num_records),
        'tokens': np.random.randint(100, 1000, num_records),
        'custo_tokens': np.random.uniform(0.01, 0.5, num_records),
        'sessoes_chat': np.random.randint(1, 100, num_records),
        'status_finalizacao': np.random.choice(status, num_records),
        'duracao_sessao': np.random.uniform(1, 60, num_records),
        'consultas_por_sessao': np.random.randint(1, 20, num_records),
        'comprimento_consulta': np.random.randint(10, 500, num_records),
        'nps': np.random.randint(0, 10, num_records)
    }
    
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    # Gerar dados mock
    df = generate_mock_data()
    
    # Salvar em CSV
    df.to_csv('mock_data.csv', index=False)
    print("Dados mock gerados e salvos em 'mock_data.csv'") 