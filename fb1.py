from corpo import criar_exercicio

# ==============================================================================
# TREINO FULLBODY 1 (Corrigido com todos os argumentos obrigatórios)
# ==============================================================================

# 1. Crucifixo Máquina
crucifixo = criar_exercicio(
    simples={'peito': 2, 'ombro': 0.5},
    completo={
        'peito': {
            'Peito_medial': 1.0, 
            'Peito_inferior': 0.5, 
            'Peito_superior': 0.5,
            'Serratil': 0.0          # Adicionado (Obrigatório)
        },
        'ombro': {
            'ombro_anterior': 1.0,
            'ombro_medial': 0.0,     # Adicionado
            'ombro_posterior': 0.0   # Adicionado
        }
    }
)

# 2. Barra Fixa
barra_fixa = criar_exercicio(
    simples={'costas': 2, 'biceps': 1, 'antebraco': 1},
    completo={
        'costas': {
            'dorsal_inferior': 1.0, 
            'dorsal_medial': 0.8, 
            'dorsal_superior': 0.6,
            'redondo_maior': 0.8,
            # Obrigatórios que faltavam:
            'romboide': 0.0,
            'trapezio_superior': 0.0,
            'trapezio_medio': 0.0,
            'trapezio_inferior': 0.0
        },
        'biceps': {
            'biceps_longa': 1.0, 
            'biceps_curta': 1.0,
            'braquial': 0.0          # Adicionado
        }
    }
)

# 3. Cadeira Extensora
cadeira_extensora = criar_exercicio(
    simples={'quadriceps': 2},
    completo={
        'quadriceps': {
            'reto_femoral': 1.0,
            'vasto_medial': 0.8,
            'vasto_lateral': 0.8,
            'vasto_intermedio': 0.8
        }
    }
)

# 4. Mesa Flexora
mesa_flexora = criar_exercicio(
    simples={'posteriorcoxa': 2, 'panturrilha': 0.5},
    completo={
        'posteriorcoxa': {
            'semitendinoso': 1.0,
            'semimembranoso': 1.0,
            'biceps_femoris_longa': 0.8,  # Nome corrigido (conforme seu arquivo posterior.py)
            'biceps_femoris_curta': 0.8   # Nome corrigido
        }
    }
)

# 5. Rosca Scott Máquina
rosca_scott = criar_exercicio(
    simples={'biceps': 2},
    completo={
        'biceps': {
            'biceps_curta': 1.0,
            'braquial': 0.8,
            'biceps_longa': 0.4
        }
    }
)

# 6. Rosca Inversa
rosca_inversa = criar_exercicio(
    simples={'biceps': 2, 'antebraco': 2},
    completo={
        'biceps': {
            'braquial': 1.0,
            'biceps_longa': 0.2,
            'biceps_curta': 0.2
        },
        'antebraco': {
            'braquiorradial': 1.0,
            'antebraco_extensores': 0.8,
            'antebraco_fletores': 0.0  # Adicionado
        }
    }
)

# ==============================================================================
# EXPORTAÇÃO
# ==============================================================================
meus_exercicios = {
    "Crucifixo": crucifixo,
    "BarraFixa": barra_fixa,
    "CadeiraExtensora": cadeira_extensora,
    "MesaFlexora": mesa_flexora,
    "RoscaScott": rosca_scott,
    "RoscaInversa": rosca_inversa
}