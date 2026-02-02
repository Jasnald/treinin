from corpo import criar_exercicio

# ==============================================================================
# TREINO CORE (Abdômen e Lombar)
# ==============================================================================

# 1. Abdominal Máquina
# Volume original: 10 séries Abdomen + 2 séries Oblíquos = 12 Total
# Cálculo da nova distribuição:
# - Reto Superior: (10 * 0.6) / 12 = 0.50
# - Reto Inferior: (10 * 0.4) / 12 = 0.33
# - Oblíquo Ext:   (2 * 0.55) / 12 = 0.09
# - Oblíquo Int:   (2 * 0.45) / 12 = 0.08
abs_maquina = criar_exercicio(
    simples={
        'abdomen': 12
    },
    completo={
        'abdomen': {
            'reto_superior': 0.50,
            'reto_inferior': 0.333,
            'obliquo_externo': 0.092,
            'obliquo_interno': 0.075
        }
    }
)

# 2. Abdominal Infra
# Volume original: 10 Abdomen + 2 Oblíquos = 12 Total (Flexores separado com 4)
# Cálculo da nova distribuição do Abdomen:
# - Reto Inf: (10 * 0.70) / 12 = 0.583
# - Reto Sup: (10 * 0.30) / 12 = 0.250
# - Oblíquos: (2 * 0.50) / 12  = 0.083 (cada)
abs_infra = criar_exercicio(
    simples={
        'abdomen': 12,
        'flexores_do_quadril': 4  # Nome corrigido (era flexores_quadril)
    },
    completo={
        'abdomen': {
            'reto_inferior': 0.583,
            'reto_superior': 0.250,
            'obliquo_externo': 0.083,
            'obliquo_interno': 0.084
        },
        'flexores_do_quadril': {
            'iliopsoas': 0.50,
            'reto_femoral': 0.30,
            'sartorio': 0.20
        }
    }
)

# ==============================================================================
# EXPORTAÇÃO
# ==============================================================================
meus_exercicios = {
    "AbdominalMaquina": abs_maquina,
    "AbdominalInfra": abs_infra
}