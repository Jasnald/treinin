from corpo import criar_exercicio

# ==============================================================================
# TREINO SUPERIORES
# ==============================================================================

# 1. Dips (Mergulho)
dips = criar_exercicio(
    simples={'peito': 3, 'ombro': 1, 'triceps': 2},
    completo={
        'peito': {
            'Peito_inferior': 1.00,
            'Peito_medial'  : 0.60, 
            'Peito_superior': 0.20,
            'Serratil'      : 0.10 
        },
        'ombro': {
            'ombro_anterior'    : 1.00,
            'ombro_medial'      : 0.60,
            'ombro_posterior'   : 0.20 
        },
        'triceps': {
            'triceps_longa' : 0.00,
            'triceps_medial': 1.00,
            'triceps_curta' : 1.00 
        }
    }
)

# 2. Crossover
crossover = criar_exercicio(
    simples={'peito': 3, 'ombro': 1, 'biceps': 1},
    completo={
        'peito': {
            'Peito_superior': 0.4,
            'Peito_medial'  : 0.6,
            'Peito_inferior': 1.0,
            'Serratil': 0.0
        },
        'ombro': {
            'ombro_anterior' : 1.0,
            'ombro_medial'   : 0.6,
            'ombro_posterior': 0.2
        },
        'biceps': {
            'biceps_longa': 1.0,
            'biceps_curta': 1.0,
            'braquial': 0.0
        }
    }
)

# 3. Crucifixo Máquina
crucifixo_maquina = criar_exercicio(
    simples={'peito': 3, 'ombro': 1, 'biceps': 1},
    completo={
        'peito': {
            'Peito_superior': 0.5,
            'Peito_medial'  : 1.0,
            'Peito_inferior': 0.5,
            'Serratil': 0.0
        },
        'ombro': {
            'ombro_anterior' : 1.0,
            'ombro_medial'   : 0.6,
            'ombro_posterior': 0.2
        },
        'biceps': {
            'biceps_longa': 0.5,
            'biceps_curta': 0.5,
            'braquial': 0.0
        }
    }
)

# 4. Barra Fixa
barra_fixa = criar_exercicio(
    simples={'costas': 3, 'biceps': 1, 'peito': 1, 'antebraco': 1, 'ombro': 1},
    completo={
        'costas': {
            'dorsal_superior'   : 0.60,
            'dorsal_medial'     : 0.80,
            'dorsal_inferior'   : 1.00,
            'romboide'          : 0.50,
            'trapezio_superior' : 0.20,
            'trapezio_medio'    : 0.40,
            'trapezio_inferior' : 1.00,
            'redondo_maior'     : 0.80
        },
        'peito': {
            'Peito_superior'    : 0.20,
            'Peito_medial'      : 0.50,
            'Peito_inferior'    : 1.00,
            'Serratil'          : 0.90
        },
        'ombro': {
            'ombro_anterior'    : 0.5,
            'ombro_medial'      : 0.7,
            'ombro_posterior'   : 1.0
        },
        'biceps': {
            'biceps_longa'      : 1.0,
            'biceps_curta'      : 1.0,
            'braquial'          : 1.0
        },
        'antebraco': {
            'antebraco_extensores'  : 0.40,
            'antebraco_fletores'    : 0.60,
            'braquiorradial'        : 1.0
        }
    }
)

# 5. Lat Pullover Machine
lat_pullover = criar_exercicio(
    simples={'costas': 3, 'peito': 1, 'triceps': 1, 'ombro': 1},
    completo={
        'costas': {
            'dorsal_superior': 0.20,
            'dorsal_medial': 0.25,
            'dorsal_inferior': 0.25,
            'romboide': 0.10,
            'trapezio_superior': 0.0,
            'trapezio_medio': 0.07,
            'trapezio_inferior': 0.05,
            'redondo_maior': 0.06
        },
        'peito': {
            'Peito_superior': 0.20,
            'Peito_medial': 0.20,
            'Peito_inferior': 0.60,
            'Serratil': 0.0
        },
        'ombro': {
            'ombro_anterior': 0.2,
            'ombro_medial': 0.2,
            'ombro_posterior': 0.6
        },
        'triceps': {
            'triceps_longa': 0.60,
            'triceps_medial': 0.2,
            'triceps_curta': 0.2
        }
    }
)

# 6. Lat Pulldown Machine
lat_pulldown = criar_exercicio(
    simples={'costas': 10, 'biceps': 3, 'peito': 2, 'ombro': 2, 'antebraco': 2},
    completo={
        'costas': {
            'dorsal_superior': 0.15,
            'dorsal_medial': 0.25,
            'dorsal_inferior': 0.25,
            'romboide': 0.10,
            'trapezio_superior': 0.0,
            'trapezio_medio': 0.08,
            'trapezio_inferior': 0.05,
            'redondo_maior': 0.08
        },
        'peito': {
            'Peito_superior': 0.25,
            'Peito_medial': 0.35,
            'Peito_inferior': 0.40,
            'Serratil': 0.0
        },
        'biceps': {
            'biceps_longa': 0.55,
            'biceps_curta': 0.45,
            'braquial': 0.0
        },
        'ombro': {
            'ombro_anterior': 0.2,
            'ombro_medial': 0.2,
            'ombro_posterior': 0.6
        },
        'antebraco': {
            'antebraco_extensores': 0.40,
            'antebraco_fletores': 0.60,
            'braquiorradial': 0.0
        }
    }
)

# ==============================================================================
# EXPORTAÇÃO (Essencial para o atual.py não quebrar)
# ==============================================================================
meus_exercicios = {
    "Dips": dips,
    "Crossover": crossover,
    "CrucifixoMaquina": crucifixo_maquina,
    "BarraFixa": barra_fixa,
    "LatPullover": lat_pullover,
    "LatPulldown": lat_pulldown
}