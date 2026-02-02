from corpo import Corpo, criar_exercicio

# ==============================================================================
# TREINO FULLBODY 2
# ==============================================================================

# 1. Panturrilha no Leg Press (2 Séries)
# Foco: Gastrocnêmio (joelho estendido favorece ele sobre o sóleo)
panturrilha_leg = criar_exercicio(
    simples={'panturrilha': 2},
    completo={
        'panturrilha': {
            'gastrocnemio_medial': 0.45,
            'gastrocnemio_laterial': 0.35, # Ajuste conforme a grafia na sua classe (laterial/lateral)
            'soleo': 0.20
        }
    }
)

# 2. Agachamento Pêndulo (2 Séries)
# Foco: Quadríceps (ênfase total devido à estabilidade e profundidade) e Glúteo
agacho_pendulo = criar_exercicio(
    simples={'quadriceps': 2, 'gluteo': 1},
    completo={
        'quadriceps': {
            'vasto_lateral': 0.3,
            'vasto_medial': 0.3,
            'vasto_intermedio': 0.3,
            'reto_femoral': 0.1  # Menor ativação que na extensora, mas presente
        },
        'gluteo': {
            'gluteo_maximo': 0.8,
            'gluteo_medio': 0.15,
            'gluteo_minimo': 0.05
        }
    }
)

# 3. Flexão Nórdica (2 Séries)
# Foco: Posterior de Coxa (fase excêntrica brutal)
flexao_nordica = criar_exercicio(
    simples={'posteriorcoxa': 2, 'gluteo': 0.5},
    completo={
        'posteriorcoxa': {
            'semitendinoso': 0.4,
            'semimembranoso': 0.3,
            'biceps_femoris_cabeca_longa': 0.2, # Bi-articular
            'biceps_femoris_cabeca_curta': 0.1
        }
    }
)

# 4. Supino Inclinado (2 Séries)
# Foco: Peito Superior e Ombro Anterior
supino_inclinado = criar_exercicio(
    simples={'peito': 2, 'ombro': 1.5, 'triceps': 1},
    completo={
        'peito': {
            'Peito_superior': 0.7,  # Ênfase principal
            'Peito_medial': 0.2,
            'Peito_inferior': 0.1,
            'Serratil': 0.0
        },
        'ombro': {
            'ombro_anterior': 0.8,
            'ombro_medial': 0.2,
            'ombro_posterior': 0.0
        },
        'triceps': {
            'triceps_curta': 0.4,   # Lateral
            'triceps_medial': 0.4,
            'triceps_longa': 0.2
        }
    }
)

# 5. Tríceps Corda (2 Séries)
# Foco: Cabeça Lateral (Curta) e Medial. Maior contração de pico.
triceps_corda = criar_exercicio(
    simples={'triceps': 2},
    completo={
        'triceps': {
            'triceps_curta': 0.5,   # Foco na cabeça lateral
            'triceps_medial': 0.3,
            'triceps_longa': 0.2
        }
    }
)

# 6. Abdominal Infra (2 Séries)
# Foco: Reto Abdominal Inferior e Flexores do Quadril
abs_infra = criar_exercicio(
    simples={'abdomen': 2, 'flexores_do_quadril': 1.5},
    completo={
        'abdomen': {
            'reto_abdominal_inferior': 0.7,
            'reto_abdominal_superior': 0.3,
            'obliquo_externo': 0.0,
            'obliquo_interno': 0.0
        },
        'flexores_do_quadril': {
            'iliopsoas': 0.6,
            'reto_femoral': 0.3,
            'sartorio': 0.1
        }
    }
)

# ==============================================================================
# EXPORTAÇÃO
# ==============================================================================
meus_exercicios = {
    "PanturrilhaLeg": panturrilha_leg,
    "AgachoPendulo": agacho_pendulo,
    "FlexaoNordica": flexao_nordica,
    "SupinoInclinado": supino_inclinado,
    "TricepsCorda": triceps_corda,
    "AbsInfra": abs_infra
}