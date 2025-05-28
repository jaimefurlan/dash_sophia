import os
from dotenv import load_dotenv
from supabase import create_client, Client
import pandas as pd
from datetime import datetime

def setup_supabase():
    # Verificar se o arquivo .env existe
    if not os.path.exists('.env'):
        print("⚠️ Arquivo .env não encontrado!")
        print("\nPor favor, siga estes passos:")
        print("1. Crie uma conta no Supabase (https://supabase.com)")
        print("2. Crie um novo projeto")
        print("3. No painel do projeto, vá em 'Project Settings' > 'API'")
        print("4. Copie a 'Project URL' e 'anon public' key")
        print("\nCrie um arquivo .env com o seguinte conteúdo:")
        print("SUPABASE_URL=sua_url_do_projeto")
        print("SUPABASE_KEY=sua_chave_anon_public")
        return False

    # Carregar variáveis de ambiente
    load_dotenv()
    
    # Verificar se as variáveis estão definidas
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    
    if not supabase_url or not supabase_key:
        print("⚠️ Variáveis de ambiente não configuradas!")
        print("Por favor, verifique se o arquivo .env contém SUPABASE_URL e SUPABASE_KEY")
        return False
    
    try:
        # Testar conexão com o Supabase
        print("🔄 Testando conexão com o Supabase...")
        supabase: Client = create_client(supabase_url, supabase_key)
        
        # Verificar se a tabela existe
        response = supabase.table('sophia_dashboard').select("count").execute()
        print("✅ Conexão com o Supabase estabelecida com sucesso!")
        
        # Carregar dados mock se existir
        if os.path.exists('mock_data.csv'):
            print("\n🔄 Carregando dados mock para o Supabase...")
            df = pd.read_csv('mock_data.csv')
            
            # Converter dados para o formato correto
            df['data'] = pd.to_datetime(df['data']).dt.strftime('%Y-%m-%d')
            
            # Inserir dados em lotes
            batch_size = 100
            for i in range(0, len(df), batch_size):
                batch = df.iloc[i:i+batch_size]
                data = batch.to_dict('records')
                supabase.table('sophia_dashboard').insert(data).execute()
            
            print(f"✅ {len(df)} registros carregados com sucesso!")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao conectar com o Supabase: {str(e)}")
        return False

if __name__ == "__main__":
    setup_supabase() 