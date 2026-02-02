from corpo import criar_exercicio

# ==============================================================================
# TREINO FULLBODY 2 (Corrigido: Nomes exatos e zeros obrigatórios)
# ==============================================================================

# 1. Panturrilha no Leg Press
panturrilha_leg = criar_exercicio(
    simples={'panturrilha': 2},
    completo={
        'panturrilha': {
            'gastrocnemio_medial': 0.45,
            'gastrocnemio_laterial': 0.35, # Mantido 'laterial' conforme erro de grafia na classe original
            'soleo': 0.20
        }
    }
)

# 2. Agachamento Pêndulo
agacho_pendulo = criar_exercicio(
    simples={'quadriceps': 2, 'gluteo': 1},
    completo={
        'quadriceps': {
            'vasto_lateral': 0.3,
            'vasto_medial': 0.3,
            'vasto_intermedio': 0.3,
            'reto_femoral': 0.1
        },
        'gluteo': {
            'gluteo_maximo': 0.8,
            'gluteo_medio': 0.15,
            'gluteo_minimo': 0.05
        }
    }
)

# 3. Flexão Nórdica
# CORREÇÃO AQUI: removido "_cabeca_" dos nomes para bater com posterior.py
flexao_nordica = criar_exercicio(
    simples={'posteriorcoxa': 2, 'gluteo': 0.5},
    completo={
        'posteriorcoxa': {
            'semitendinoso': 0.4,
            'semimembranoso': 0.3,
            'biceps_femoris_longa': 0.2,  # Nome corrigido (era biceps_femoris_cabeca_longa)
            'biceps_femoris_curta': 0.1   # Nome corrigido
        },
        'gluteo': {
            'gluteo_maximo': 1.0,
            'gluteo_medio': 0.0,    # Obrigatório
            'gluteo_minimo': 0.0    # Obrigatório
        }
    }
)

# 4. Supino Inclinado
# CORREÇÃO: Adicionado Serratil e completado Ombro/Tríceps
supino_inclinado = criar_exercicio(
    simples={'peito': 2, 'ombro': 1.5, 'triceps': 1},
    completo={
        'peito': {
            'Peito_superior': 0.7,
            'Peito_medial': 0.2,
            'Peito_inferior': 0.1,
            'Serratil': 0.0         # Obrigatório
        },
        'ombro': {
            'ombro_anterior': 0.8,
            'ombro_medial': 0.2,
            'ombro_posterior': 0.0  # Obrigatório
        },
        'triceps': {
            'triceps_curta': 0.4,
            'triceps_medial': 0.4,
            'triceps_longa': 0.2
        }
    }
)

# 5. Tríceps Corda
triceps_corda = criar_exercicio(
    simples={'triceps': 2},
    completo={
        'triceps': {
            'triceps_curta': 0.5,
            'triceps_medial': 0.3,
            'triceps_longa': 0.2
        }
    }
)

# 6. Abdominal Infra
# CORREÇÃO: Nomes dos argumentos de abdomen alterados para bater com core.py (reto_superior, etc)
abs_infra = criar_exercicio(
    simples={'abdomen': 2, 'flexores_do_quadril': 1.5},
    completo={
        'abdomen': {
            'reto_inferior': 0.7,   # Nome corrigido (era reto_abdominal_inferior)
            'reto_superior': 0.3,   # Nome corrigido
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