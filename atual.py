import yaml
import dataclasses
from collections import defaultdict
from pathlib import Path
from loader import carregar_biblioteca

def calcular_volume_detalhado(lista_treinos):
    # 1. Carrega a biblioteca
    BIBLIOTECA = carregar_biblioteca()
    
    volume_macro = defaultdict(float) # Ex: Peito, Costas
    volume_micro = defaultdict(float) # Ex: Peito_superior, Triceps_longa
    
    # Dicionário para deixar os nomes bonitos
    nomes_bonitos = {
        # Macros
        "posteriorcoxa": "Posterior de Coxa",
        "flexores_do_quadril": "Flexores do Quadril",
        "antebraco": "Antebraço",
        "quadriceps": "Quadríceps",
        "gluteo": "Glúteo",
        "abdomen": "Abdômen",
        "biceps": "Bíceps",
        "triceps": "Tríceps",
        "peito": "Peito",
        "costas": "Costas",
        "ombro": "Ombro",
        "panturrilha": "Panturrilha",
        "lombar": "Lombar",
        "adutores": "Adutores",
        
        # Micros (Tratamento básico de string se não estiver aqui)
        "biceps_femoris_longa": "Bíceps Femoral (Longa)",
        "biceps_femoris_curta": "Bíceps Femoral (Curta)",
        "reto_femoral": "Reto Femoral",
        "vasto_lateral": "Vasto Lateral",
        "vasto_medial": "Vasto Medial",
        "gluteo_maximo": "Glúteo Máximo",
        "gluteo_medio": "Glúteo Médio",
        "triceps_longa": "Tríceps (Longa)",
        "triceps_medial": "Tríceps (Medial)",
        "triceps_curta": "Tríceps (Curta/Lateral)",
        "ombro_anterior": "Ombro Anterior",
        "ombro_lateral": "Ombro Lateral",
        "ombro_posterior": "Ombro Posterior",
        "peito_superior": "Peito Superior",
        "peito_inferior": "Peito Inferior",
        "peito_medial": "Peito Medial",
        "dorsal_superior": "Dorsal Superior",
        "dorsal_inferior": "Dorsal Inferior",
        "redondo_maior": "Redondo Maior"
    }

    print(f"Calculando volume para: {', '.join(lista_treinos)}...")

    # 2. Processa os treinos
    for arquivo_treino in lista_treinos:
        caminho = Path('workouts') / f"{arquivo_treino}.yaml"
        if not caminho.exists():
            print(f"ERRO: Treino '{arquivo_treino}' não encontrado.")
            continue
            
        with open(caminho, 'r', encoding='utf-8') as f:
            dados_treino = yaml.safe_load(f)
            
        for item in dados_treino.get('exercicios', []):
            nome_ex = item['nome']
            sets_feitos = item['series']
            
            exercicio_obj = BIBLIOTECA.get(nome_ex)
            
            if not exercicio_obj:
                print(f"AVISO: '{nome_ex}' não existe na library.")
                continue

            # Itera sobre os grupos musculares (Peito, Costas, etc.)
            for field in dataclasses.fields(exercicio_obj):
                grupo = getattr(exercicio_obj, field.name)
                
                # Verifica se é um grupo muscular válido (tem atributo 'volume')
                if hasattr(grupo, 'volume'):
                    # --- CÁLCULO MACRO ---
                    # Usa a eficiência geral do grupo (efficiency do YAML)
                    if grupo.volume > 0:
                        volume_macro[field.name] += sets_feitos * grupo.volume
                    
                    # --- CÁLCULO MICRO (Sub-ativações) ---
                    # Itera sobre os atributos internos do grupo (ex: Peito_superior)
                    # Exclui métodos e atributos privados ou o próprio 'volume'
                    for sub_nome, sub_valor in vars(grupo).items():
                        if (sub_nome != 'volume' and 
                            isinstance(sub_valor, (int, float)) and 
                            sub_valor > 0):
                            
                            # AQUI ESTÁ A MÁGICA:
                            # Multiplica sets feitos pelo valor da distribuição (Séries Válidas)
                            # Nota: Não multiplica pelo volume macro, pois no YAML tratamos eles como independentes.
                            volume_micro[sub_nome] += sets_feitos * sub_valor

    # 3. Função auxiliar de print
    def imprimir_relatorio(titulo, dados):
        print("\n" + "="*50)
        print(f"{titulo}")
        print("="*50)
        # Ordena crescente pelo valor
        for nome, total in sorted(dados.items(), key=lambda item: item[1]):
            if total > 0.1:
                # Formata o nome (Tenta dicionário, senão Capitalize, senão original)
                nome_formatado = nomes_bonitos.get(nome, 
                                 nomes_bonitos.get(nome.lower(), 
                                 nome.replace('_', ' ').capitalize()))
                
                print(f"{nome_formatado:<25}: {total:.1f} séries")

    # 4. Imprime os Relatórios
    imprimir_relatorio("VOLUME MACRO (Grupos Musculares)", volume_macro)
    imprimir_relatorio("VOLUME MICRO (Porções Específicas)", volume_micro)

if __name__ == "__main__":
    minha_semana = ['fb1', 'fb2', 'upper', 'lower']
    calcular_volume_detalhado(minha_semana)