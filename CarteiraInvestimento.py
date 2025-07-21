import pandas as pd

# Definindo as carteiras
carteiras = {
    "Conservador": [
        ("BBAS3 (Banco do Brasil)", "Brasil", 15),
        ("PETR4 (Petrobras)", "Brasil", 10),
        ("IVVB11 (ETF S&P 500)", "Global", 15),
        ("BOVA11 (ETF Ibovespa)", "Brasil", 10),
        ("INDA (ETF Índia – MSCI)", "Índia", 25),
        ("HDFC Bank", "Índia", 10),
        ("TCS (Tata Consultancy)", "Índia", 15)
    ],
    "Moderado": [
        ("WEGE3 (WEG)", "Brasil", 10),
        ("RADL3 (Raia Drogasil)", "Brasil", 10),
        ("VALE3 (Vale)", "Brasil", 10),
        ("INDA (ETF Índia – MSCI)", "Índia", 20),
        ("Infosys", "Índia", 10),
        ("HDFC Bank", "Índia", 10),
        ("INDY (ETF India 50)", "Índia", 10),
        ("IVVB11 (ETF S&P 500)", "Global", 20)
    ],
    "Agressivo": [
        ("SMAL11 (Small Caps BR)", "Brasil", 15),
        ("VALE3 (Vale)", "Brasil", 10),
        ("Adani Green Energy", "Índia", 10),
        ("Infosys", "Índia", 10),
        ("Reliance Industries", "Índia", 10),
        ("INDA (ETF Índia – MSCI)", "Índia", 20),
        ("IVVB11 (ETF S&P 500)", "Global", 15),
        ("SMIN (Índia Small Cap ETF)", "Índia", 10)
    ]
}

# Criando os DataFrames e salvando em Excel
with pd.ExcelWriter("Carteiras_Brasil_India_2025.xlsx") as writer:
    for perfil, data in carteiras.items():
        df = pd.DataFrame(data, columns=["Ativo", "País", "Peso (%)"])
        df.to_excel(writer, sheet_name=perfil, index=False)

print("Arquivo 'Carteiras_Brasil_India_2025.xlsx' criado com sucesso!")
