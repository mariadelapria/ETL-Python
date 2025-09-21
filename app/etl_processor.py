import pandas as pd
from datetime import datetime
from pydantic import ValidationError
from validador import User
import logging

class ETLProcessor:
    def __init__(self):
        self.validation_errors = []
        self.processed_data = []
        self.stats = {
            'total_rows': 0,
            'valid_rows': 0,
            'invalid_rows': 0,
            'errors': []
        }
    
    def process_csv(self, file_path):
        """
        Processa arquivo CSV validando cada linha com o modelo Pydantic
        """
        try:
            # 1. Ler arquivo CSV
            df = pd.read_csv(file_path, sep=';')
            
            # 2. Converter coluna Data para datetime
            df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
            
            # 3. Inicializar contadores
            self.stats['total_rows'] = len(df)
            self.validation_errors = []
            self.processed_data = []
            
            # 4. Percorrer cada linha
            for index, row in df.iterrows():
                try:
                    # 5. Converter linha para dicionário
                    row_dict = row.to_dict()
                    
                    # 6. Validar com Pydantic
                    user = User(**row_dict)
                    
                    # 7. Adicionar à lista de dados válidos
                    self.processed_data.append(user.dict())
                    self.stats['valid_rows'] += 1
                    
                except ValidationError as e:
                    # 8. Registrar erro
                    error_info = {
                        'row': index + 1,
                        'data': row_dict,
                        'error': str(e),
                        'error_details': e.errors()
                    }
                    self.validation_errors.append(error_info)
                    self.stats['invalid_rows'] += 1
                    self.stats['errors'].append(str(e))
                    
                except Exception as e:
                    # 9. Registrar outros erros
                    error_info = {
                        'row': index + 1,
                        'data': row.to_dict(),
                        'error': f"Erro inesperado: {str(e)}",
                        'error_details': []
                    }
                    self.validation_errors.append(error_info)
                    self.stats['invalid_rows'] += 1
                    self.stats['errors'].append(str(e))
            
            return self.get_results()
            
        except Exception as e:
            return {
                'error': f"Erro ao processar arquivo: {str(e)}",
                'processed_data': [],
                'validation_errors': [],
                'stats': self.stats,
                'success_rate': 0
            }
    
    def get_results(self):
        """
        Retorna resultados do processamento
        """
        success_rate = 0
        if self.stats['total_rows'] > 0:
            success_rate = (self.stats['valid_rows'] / self.stats['total_rows']) * 100
        
        return {
            'processed_data': self.processed_data,
            'validation_errors': self.validation_errors,
            'stats': self.stats,
            'success_rate': success_rate
        }
    
    def get_summary_stats(self):
        """
        Retorna estatísticas resumidas
        """
        return {
            'total_rows': self.stats['total_rows'],
            'valid_rows': self.stats['valid_rows'],
            'invalid_rows': self.stats['invalid_rows'],
            'success_rate': self.stats['valid_rows'] / self.stats['total_rows'] * 100 if self.stats['total_rows'] > 0 else 0
        }

