import yaml
import dataclasses
from collections import defaultdict
from pathlib import Path

# Importa o carregador que criamos no passo 1
from loader import carregar_biblioteca

def calcular_volume_yaml(lista_treinos):
    # 1. Carrega toda a biomecânica (YAML -> Objetos)
    BIBLIOTECA = carregar_biblioteca()
    
    volume_total = defaultdict(float)
    
    print(f"{'TREINO':<15} | {'EXERCÍCIO':<20} | {'SÉRIES':<6} | {'SÉRIES VÁLIDAS (Efetivas)'}")
    print("-" * 90)

    for arquivo_treino in lista_treinos:
        # Lê o arquivo do treino (ex: workouts/fb1.yaml)
        caminho = Path('workouts') / f"{arquivo_treino}.yaml"
        
        if not caminho.exists():
            print(f"ERRO: Treino '{arquivo_treino}' não encontrado.")
            continue
            
        with open(caminho, 'r', encoding='utf-8') as f:
            dados_treino = yaml.safe_load(f)
            
        nome_sessao = dados_treino.get('treino', arquivo_treino)
        
        for item in dados_treino['exercicios']:
            nome_ex = item['nome']
            sets_feitos = item['series']
            
            # Busca o objeto na biblioteca carregada
            exercicio_obj = BIBLIOTECA.get(nome_ex)
            
            if not exercicio_obj:
                print(f"AVISO: '{nome_ex}' não existe nos arquivos da library.")
                continue
                
            impacto_visual = []

            # Itera sobre os músculos do objeto (Peito, Costas, etc.)
            for field in dataclasses.fields(exercicio_obj):
                grupo = getattr(exercicio_obj, field.name)
                
                # Se o exercício ativa esse grupo (volume > 0)
                if hasattr(grupo, 'volume') and grupo.volume > 0:
                    
                    # CÁLCULO DE SÉRIES VÁLIDAS:
                    # Séries Feitas * Eficiência do Exercício
                    # Ex: 3 séries * 1.0 (Barra) = 3.0 para Costas
                    # Ex: 3 séries * 0.3 (Barra) = 1.0 para Peito (Serrátil)
                    volume_gerado = sets_feitos * grupo.volume
                    
                    volume_total[field.name] += volume_gerado
                    
                    if volume_gerado >= 0.1: # Só mostra se tiver impacto relevante
                        impacto_visual.append(f"{field.name}: {volume_gerado:.1f}")

            print(f"{nome_sessao:<15} | {nome_ex:<20} | {sets_feitos:<6} | {', '.join(impacto_visual)}")

    # === RELATÓRIO FINAL ===
    print("\n" + "="*40)
    print("VOLUME SEMANAL TOTAL (Séries Válidas)")
    print("="*40)
    for musculo, total in sorted(volume_total.items()):
        if total > 0.1:
            print(f"{musculo.capitalize():<20}: {total:.1f} séries")

if __name__ == "__main__":
    # Defina aqui sua semana (nomes dos arquivos na pasta workouts)
    minha_semana = ['fb1', 'fb2', 'fb1', 'fb2']
    
    calcular_volume_yaml(minha_semana)