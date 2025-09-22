# 📊 Carteiras de Investimento Brasil–Índia 2025

Este projeto Python gera automaticamente um arquivo Excel com três perfis de carteiras de investimento — **Conservador**, **Moderado** e **Agressivo** — com foco em ativos do **Brasil**, **Índia** e mercado **global**.
As carteiras são organizadas em abas separadas no Excel, com seus respectivos ativos, países de origem e pesos percentuais.
---
## 🧠 Objetivo
O projeto tem como objetivo:
- Simular carteiras diversificadas para diferentes perfis de risco
- Promover o entendimento de alocação internacional (Brasil + Índia + Global)
- Automatizar a exportação das carteiras para um formato acessível (Excel)
---
## ⚙️ Como funciona
O script utiliza a biblioteca **Pandas** para:
1. Definir os ativos e suas alocações para cada perfil de investidor
2. Organizar os dados em DataFrames
3. Exportar cada carteira para uma aba distinta no arquivo `Carteiras_Brasil_India_2025.xlsx`
---
## 📁 Estrutura das Carteiras

Cada carteira é composta por:
- **Nome do ativo** (ex: VALE3, IVVB11, Infosys)
- **País de origem** (Brasil, Índia ou Global)
- **Peso (%)** no portfólio

### 🟢 Conservador
Foco em ativos sólidos, com maior presença de ETFs e bancos.

### 🟡 Moderado
Balanceamento entre ações brasileiras, ETFs e empresas indianas.

### 🔴 Agressivo
Mais exposição a small caps e empresas de crescimento, especialmente da Índia.

---
## 🖥️ Como executar

1. Certifique-se de ter o Python instalado (versão 3.7+)
2. Instale o `pandas`, se ainda não tiver:
   ```bash
   pip install pandas

Execute o script:
python nome_do_arquivo.py
Um arquivo chamado Carteiras_Brasil_India_2025.xlsx será gerado no mesmo diretório.

📦 Exemplo de saída (Excel)

O arquivo final conterá:
🗂️ 3 abas: Conservador, Moderado e Agressivo

📋 Tabela com colunas:
Ativo
País
Peso (%)

📚 Tecnologias utilizadas
Python 3

Pandas
 – para manipulação e exportação de dados

👤 Autor
Desenvolvido por Cintia Sedenho Dias.
💼 Interesse em análise de dados e automações com Python.

📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e compartilhar.
