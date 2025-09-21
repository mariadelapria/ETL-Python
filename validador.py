from datetime import date
from pydantic import BaseModel, Field

###Arquivo de validação feito com Pydentic
###Parametrôs passados diretamente do Pandas

class User(BaseModel):
    Pais: str = Field(..., description="Nome do país")
    Data: date = Field(..., description="Data da observação no formato YYYY-MM-DD")
    PIB: float = Field(..., description="Produto Interno Bruto do país em bilhões de USD")
    Consumo: float = Field(..., description="Consumo privado, valor positivo")
    Investimento: float = Field(..., description="Investimento em capital, valor positivo")
    Gastos_Governo: float = Field(..., description="Gastos do governo, valor positivo")
    Exportacoes: float = Field(..., description="Exportações totais, valor positivo")
    Importacoes: float = Field(..., description="Importações totais, valor positivo")
    Inflacao: float = Field(..., description="Taxa de inflação anual (0 a 1)")
    Desemprego: float = Field(..., description="Taxa de desemprego em %")
    Taxa_Juros: float = Field(..., description="Taxa de juros anual em %")
    Divida_Publica: float = Field(..., description="Dívida pública total, sempre positiva")
    Producao_Industrial: float = Field(..., description="Produção industrial, valor positivo")
    Setor_Agricola: float = Field(..., description="Valor do setor agrícola, positivo")
    Setor_Servicos: float = Field(..., description="Valor do setor de serviços, positivo")
    Balanca_Comercial: float = Field(..., description="Balança comercial (Exportações - Importações), pode ser negativa")
    Crescimento_PIB: float = Field(..., description="Crescimento do PIB, pode ser negativo")

