import yaml
import os
from pathlib import Path
from corpo import criar_exercicio

def carregar_biblioteca():
    """Lê todos os YAMLs na pasta library/ e cria o dicionário de objetos."""
    biblioteca = {}
    
    # Caminho para a pasta 'library'
    base_dir = Path(__file__).parent / 'library'
    
    # Pega todos os arquivos .yaml
    for arquivo in base_dir.glob('*.yaml'):
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados_yaml = yaml.safe_load(f) or {}
            
        for nome_exercicio, specs in dados_yaml.items():
            # A MÁGICA: Converte YAML -> Objeto Corpo
            biblioteca[nome_exercicio] = criar_exercicio(
                simples=specs['efficiency'],    # No YAML chamamos de efficiency
                completo=specs['distribution']  # No YAML chamamos de distribution
            )

    return biblioteca