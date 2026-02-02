from corpo import criar_exercicio

# ==============================================================================
# TREINO INFERIORES
# ==============================================================================

# 1. RDL (Romanian Deadlift)
rdl = criar_exercicio(
    simples={
        'posteriorcoxa': 8,  # Nome corrigido (era posteriores_coxa)
        'gluteo': 10,        # Nome corrigido (era gluteos)
        'lombar': 5,
        'adutores': 1
    },
    completo={
        'posteriorcoxa': {
            'semitendinoso': 0.30,
            'semimembranoso': 0.25,
            'biceps_femoris_longa': 0.30,  # Nome corrigido (era ...cabeca_longa)
            'biceps_femoris_curta': 0.15   # Nome corrigido
        },
        'gluteo': {
            'gluteo_maximo': 0.70,
            'gluteo_medio': 0.20,
            'gluteo_minimo': 0.10
        },
        'lombar': {
            'eretores': 0.80,        # Nome corrigido (era erector_spinae)
            'multifidus': 0.20,
            'quadrado_lombar': 0.0   # Obrigatório (zero)
        },
        'adutores': {
            'adutor_magnus': 0.75,
            'adutor_longus': 0.25,
            'adutor_brevis': 0.0,    # Obrigatório
            'gracilis': 0.0          # Obrigatório
        }
    }
)

# 2. Cadeira Flexora
cadeira_flexora = criar_exercicio(
    simples={
        'posteriorcoxa': 10,
        'gluteo': 1,
        'panturrilha': 3
    },
    completo={
        'posteriorcoxa': {
            'semitendinoso': 0.35,
            'semimembranoso': 0.30,
            'biceps_femoris_longa': 0.25,
            'biceps_femoris_curta': 0.10
        },
        'gluteo': {
            'gluteo_maximo': 0.80,
            'gluteo_medio': 0.15,
            'gluteo_minimo': 0.05
        },
        'panturrilha': {
            'gastrocnemio_medial': 0.70,
            'gastrocnemio_laterial': 0.0, # Mantido 'laterial' da classe original
            'soleo': 0.30
        }
    }
)

# 3. Back Extension (Hiperextensão)
back_extension = criar_exercicio(
    simples={
        'lombar': 8,
        'gluteo': 10,
        'posteriorcoxa': 6
    },
    completo={
        'lombar': {
            'eretores': 0.80,
            'multifidus': 0.20,
            'quadrado_lombar': 0.0
        },
        'gluteo': {
            'gluteo_maximo': 0.75,
            'gluteo_medio': 0.18,
            'gluteo_minimo': 0.07
        },
        'posteriorcoxa': {
            'semitendinoso': 0.30,
            'semimembranoso': 0.30,
            'biceps_femoris_longa': 0.25,
            'biceps_femoris_curta': 0.15
        }
    }
)

# 4. Leg Press
leg_press = criar_exercicio(
    simples={
        'quadriceps': 10,
        'gluteo': 5,
        'adutores': 3,
        'posteriorcoxa': 1
    },
    completo={
        'quadriceps': {
            'vasto_lateral': 0.4,
            'vasto_medial': 0.3,
            'vasto_intermedio': 0.3,
            'reto_femoral': 0.0
        },
        'gluteo': {
            'gluteo_maximo': 0.60,
            'gluteo_medio': 0.30,
            'gluteo_minimo': 0.10
        },
        'adutores': {
            'adutor_magnus': 0.40,
            'adutor_longus': 0.35,
            'adutor_brevis': 0.15,
            'gracilis': 0.10
        },
        'posteriorcoxa': {
            'semitendinoso': 0.03,
            'semimembranoso': 0.03,
            'biceps_femoris_longa': 0.03,
            'biceps_femoris_curta': 0.91
        }
    }
)

# 5. Sissy Squat
sissy_squat = criar_exercicio(
    simples={
        'quadriceps': 10,
        'gluteo': 1,
        'adutores': 1
    },
    completo={
        'quadriceps': {
            'reto_femoral': 0.4,
            'vasto_medial': 0.2,
            'vasto_lateral': 0.2,
            'vasto_intermedio': 0.2
        },
        'gluteo': {
            'gluteo_maximo': 0.70,
            'gluteo_medio': 0.20,
            'gluteo_minimo': 0.10
        },
        'adutores': {
            'adutor_magnus': 0.45,
            'adutor_longus': 0.35,
            'adutor_brevis': 0.20,
            'gracilis': 0.0
        }
    }
)

# 6. Leg Extension (Cadeira Extensora)
leg_extension = criar_exercicio(
    simples={
        'quadriceps': 10
    },
    completo={
        'quadriceps': {
            'reto_femoral': 0.4,
            'vasto_medial': 0.2,
            'vasto_lateral': 0.2,
            'vasto_intermedio': 0.2
        }
    }
)

# 7. Panturrilha Leg Press
# Nota: 'tibial' foi removido pois a classe Corpo não tem esse grupo.
panturrilha_leg = criar_exercicio(
    simples={
        'panturrilha': 10
    },
    completo={
        'panturrilha': {
            'gastrocnemio_medial': 0.45,
            'gastrocnemio_laterial': 0.35,
            'soleo': 0.20
        }
    }
)

# ==============================================================================
# EXPORTAÇÃO
# ==============================================================================
meus_exercicios = {
    "RDL": rdl,
    "CadeiraFlexora": cadeira_flexora,
    "BackExtension": back_extension,
    "LegPress": leg_press,
    "SissySquat": sissy_squat,
    "LegExtension": leg_extension,
    "PanturrilhaLegPress": panturrilha_leg
}