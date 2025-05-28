# Dashboard SophIA

Dashboard interativo para monitoramento de métricas de IA, cobrança, vendas, SAC e WhatsApp.

## 🚀 Funcionalidades

- Dashboard de IA com métricas de performance e qualidade
- Dashboard de Cobrança com indicadores financeiros
- Dashboard de Vendas com métricas comerciais
- Dashboard SAC com métricas de atendimento
- Dashboard WhatsApp com métricas de campanhas
- Visualização geográfica de usuários por DDD
- Integração com APIs públicas para testes

## 📋 Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/dash_sophia.git
cd dash_sophia
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
- Crie um arquivo `.env` na raiz do projeto
- Adicione suas credenciais:
```
SUPABASE_URL=sua_url_supabase
SUPABASE_KEY=sua_chave_supabase
```

## 🎮 Como Usar

1. Execute o aplicativo:
```bash
streamlit run app.py
```

2. Acesse o dashboard em seu navegador:
```
http://localhost:8501
```

## 📊 Estrutura do Projeto

```
dash_sophia/
├── app.py              # Aplicação principal
├── assets/            # Arquivos estáticos
│   └── style.css      # Estilos CSS
├── requirements.txt   # Dependências
├── .env              # Variáveis de ambiente
└── README.md         # Documentação
```

## 🔐 Segurança

- Não compartilhe suas credenciais
- Mantenha o arquivo `.env` no .gitignore
- Use variáveis de ambiente para dados sensíveis

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📧 Contato

Seu Nome - [@seu_twitter](https://twitter.com/seu_twitter) - email@exemplo.com

Link do Projeto: [https://github.com/seu-usuario/dash_sophia](https://github.com/seu-usuario/dash_sophia) 