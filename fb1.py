from corpo import criar_exercicio

# ==============================================================================
# TREINO FULLBODY 1
# ==============================================================================

# 1. Crucifixo Máquina (2 Séries)
# Foco: Peito Medial e alongamento
crucifixo = criar_exercicio(
    simples={'peito': 2, 'ombro': 0.5},
    completo={
        'peito': {
            'Peito_medial': 1.0, 
            'Peito_inferior': 0.5, 
            'Peito_superior': 0.5
        },
        'ombro': {'ombro_anterior': 1.0}
    }
)

# 2. Barra Fixa (2 Séries)
# Foco: Latíssimo (Dorsal) e Bíceps
barra_fixa = criar_exercicio(
    simples={'costas': 2, 'biceps': 1, 'antebraco': 1},
    completo={
        'costas': {
            'dorsal_inferior': 1.0, 
            'dorsal_medial': 0.8, 
            'dorsal_superior': 0.6,
            'redondo_maior': 0.8
        },
        'biceps': {'biceps_longa': 1.0, 'biceps_curta': 1.0}
    }
)

# 3. Cadeira Extensora (2 Séries)
# Foco: Quadríceps (Reto Femoral isolado)
cadeira_extensora = criar_exercicio(
    simples={'quadriceps': 2},
    completo={
        'quadriceps': {
            'reto_femoral': 1.0,      # A extensora é ótima para o reto
            'vasto_medial': 0.8,
            'vasto_lateral': 0.8,
            'vasto_intermedio': 0.8
        }
    }
)

# 4. Mesa Flexora (2 Séries)
# Foco: Posterior de Coxa (Isquiotibiais)
mesa_flexora = criar_exercicio(
    simples={'posteriorcoxa': 2, 'panturrilha': 0.5},
    completo={
        'posteriorcoxa': {
            'semitendinoso': 1.0,     # Trabalha bem todas as porções
            'semimembranoso': 1.0,
            'biceps_femoris_cabeca_curta': 0.8,
            'biceps_femoris_cabeca_longa': 0.8
        }
    }
)

# 5. Rosca Scott Máquina (2 Séries)
# Foco: Bíceps (Ênfase na Cabeça Curta e Braquial devido à flexão de ombro)
rosca_scott = criar_exercicio(
    simples={'biceps': 2},
    completo={
        'biceps': {
            'biceps_curta': 1.0,      # Mais ativada na posição Scott
            'braquial': 0.8,
            'biceps_longa': 0.4       # Menos ativa (insuficiência ativa)
        }
    }
)

# 6. Rosca Inversa (2 Séries)
# Foco: Antebraço e Braquial (Bíceps "desativado" mecanicamente)
rosca_inversa = criar_exercicio(
    simples={'biceps': 2, 'antebraco': 2},
    completo={
        'biceps': {
            'braquial': 1.0,          # Motor primário aqui
            'biceps_longa': 0.2,
            'biceps_curta': 0.2
        },
        'antebraco': {
            'braquiorradial': 1.0,    # O rei da rosca inversa
            'antebraco_extensores': 0.8
        }
    }
)

# ==============================================================================
# EXPORTAÇÃO (Para o atual.py ler)
# ==============================================================================
meus_exercicios = {
    "Crucifixo": crucifixo,
    "BarraFixa": barra_fixa,
    "CadeiraExtensora": cadeira_extensora,
    "MesaFlexora": mesa_flexora,
    "RoscaScott": rosca_scott,
    "RoscaInversa": rosca_inversa
}