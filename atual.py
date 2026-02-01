# pressupõe que TODAS as suas dataclasses já estão importadas
# (Dips, LatPulloverMachine, CrucifixoMaquina, etc.)

from collections import defaultdict
import pprint

import dataclasses

from exercicios_inferiores import (
    RDL,CadeiraFlexora, BackExtension,
    LegExtension,LegPress,SissySquat,
    PanturrilhaLegPress
    )

from exercicios_superiores import (
    Dips, Crossover, CrucifixoMaquina,
    LatPulldownMachine,LatPulloverMachine,BarraFixa
    )

from exercicios_bracos import (
    CableCurl, RoscaMartelo, TricepsPulldown
    )

from exercicios_core import (
    AbdominalInfra,AbdominalMaquina
)

from exercicios_ombro import (
    ElevacaoLateralMaquina
)
# Mapeamento dos exercícios para suas dataclasses
exercicios_map = {
    # Treino A
    "Dips": Dips(),
    "Lat Pullover Machine": LatPulloverMachine(),
    "Leg Extension": LegExtension(),
    "RDL": RDL(),
    "Triceps Pulldown": TricepsPulldown(),
    
    # Treino B
    "Crucifixo Máquina": CrucifixoMaquina(),
    "Barra Fixa": BarraFixa(),
    "Back Extension": BackExtension(),
    "Cable Curl": CableCurl(),
    "Abdominal Infra": AbdominalInfra(),
    
    # Treino C
    "Crossover": Crossover(),
    "Lat Pulldown Machine": LatPulldownMachine(),
    "Cadeira Flexora": CadeiraFlexora(),
    "Panturrilha Leg Press": PanturrilhaLegPress(),
    "Leg Press": LegPress(),
    
    # Treino D
    # "Crucifixo Máquina": já mapeado acima
    # "Lat Pulldown Machine": já mapeado acima
    "Sissy Squat": SissySquat(),
    "Ombro": ElevacaoLateralMaquina(),  # assumindo que "Ombro" é elevação lateral
    "Abdominal Máquina": AbdominalMaquina(),
}

# Definição dos treinos
treinos = {
    "A": ["Dips", "Lat Pullover Machine", "Leg Extension", "RDL", "Triceps Pulldown"],
    "B": ["Crucifixo Máquina", "Barra Fixa", "Back Extension", "Cable Curl", "Abdominal Infra"],
    "C": ["Crossover", "Lat Pulldown Machine", "Cadeira Flexora", "Panturrilha Leg Press", "Leg Press"],
    "D": ["Crucifixo Máquina", "Lat Pulldown Machine", "Sissy Squat", "Ombro", "Abdominal Máquina"]
}


def calcular_series_semanais(treinos, exercicios_map, series_por_exercicio=3/10):
    """
    Calcula o total de séries semanais por grupo muscular
    """
    # Dicionário para acumular as séries
    series_totais = {}
    
    # Para cada treino
    for treino_nome, exercicios in treinos.items():
        print(f"\n=== TREINO {treino_nome} ===")
        
        # Para cada exercício no treino
        for exercicio in exercicios:
            if exercicio in exercicios_map:
                dataclass_exercicio = exercicios_map[exercicio]
                
                print(f"{exercicio}:")
                
                # Pegar todos os atributos que representam músculos (não são distribuições)
                for attr_name in dir(dataclass_exercicio):
                    if not attr_name.startswith('_') and not callable(getattr(dataclass_exercicio, attr_name)):
                        attr_value = getattr(dataclass_exercicio, attr_name)
                        
                        # Só considerar atributos numéricos que não sejam distribuições (que somam 1.0)
                        if isinstance(attr_value, (int, float)) and attr_value > 1:
                            series_grupo = attr_value * series_por_exercicio
                            
                            if attr_name not in series_totais:
                                series_totais[attr_name] = 0
                            series_totais[attr_name] += series_grupo
                            
                            print(f"  {attr_name}: {series_grupo} séries")
            else:
                print(f"⚠️ Exercício '{exercicio}' não encontrado no mapeamento")
    
    # Imprimir totais semanais
    print("\n" + "="*50)
    print("SÉRIES SEMANAIS TOTAIS:")
    print("="*50)
    
    for grupo, total in sorted(series_totais.items()):
        print(f"{grupo.capitalize()}: {total} séries")
    
    return series_totais

# Executar o cálculo
series_semanais = calcular_series_semanais(treinos, exercicios_map)