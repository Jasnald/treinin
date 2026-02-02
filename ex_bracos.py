from corpo import criar_exercicio

# ==============================================================================
# TREINO DE BRAÇOS (Bíceps, Tríceps e Antebraço)
# ==============================================================================

# 1. Cable Curl (Rosca na Polia)
cable_curl = criar_exercicio(
    simples={
        'biceps': 10,
        'antebraco': 4
    },
    completo={
        'biceps': {
            'biceps_longa': 0.4,
            'biceps_curta': 0.4,
            'braquial': 0.2
        },
        'antebraco': {
            'braquiorradial': 0.6,
            'antebraco_fletores': 0.2,
            'antebraco_extensores': 0.2
        }
    }
)

# 2. Rosca Martelo
rosca_martelo = criar_exercicio(
    simples={
        'biceps': 10,
        'antebraco': 8
    },
    completo={
        'biceps': {
            'biceps_longa': 0.45,
            'biceps_curta': 0.25,
            'braquial': 0.30
        },
        'antebraco': {
            'braquiorradial': 0.80,
            'antebraco_fletores': 0.10,
            'antebraco_extensores': 0.10
        }
    }
)

# 3. Tríceps Pulldown (Corda/Polia)
triceps_pulldown = criar_exercicio(
    simples={
        'triceps': 10,
        'ombro': 1
    },
    completo={
        'triceps': {
            'triceps_longa': 0.40,
            'triceps_medial': 0.35,  # Nome corrigido (era triceps_media)
            'triceps_curta': 0.25
        },
        'ombro': {
            'ombro_anterior': 0.4,
            'ombro_medial': 0.3,
            'ombro_posterior': 0.2
        }
    }
)

# ==============================================================================
# EXPORTAÇÃO
# ==============================================================================
meus_exercicios = {
    "CableCurl": cable_curl,
    "RoscaMartelo": rosca_martelo,
    "TricepsPulldown": triceps_pulldown
}