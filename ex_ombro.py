from corpo import criar_exercicio

# 1. Elevação Lateral Máquina
elevacao_lateral = criar_exercicio(
    simples={
        'ombro': 10,
        'costas': 2,   # Trapézio é parte das costas na nossa classe
        'peito': 2     # Serrátil é parte do peito na nossa classe
    },
    completo={
        'ombro': {
            'ombro_anterior': 0.15,
            'ombro_medial': 0.70,
            'ombro_posterior': 0.15
        },
        'costas': {
            # Trapézio (Repassando seus dados antigos)
            'trapezio_superior': 0.60,
            'trapezio_medio': 0.30,
            'trapezio_inferior': 0.10,
            
            # Zeros Obrigatórios (Outros músculos das costas)
            'dorsal_superior': 0.0,
            'dorsal_medial': 0.0,
            'dorsal_inferior': 0.0,
            'redondo_maior': 0.0,
            'romboide': 0.0
        },
        'peito': {
            # Serrátil (Sua classe Peito tem apenas 'Serratil' geral, sem divisão)
            # Então jogamos 100% do volume alocado de peito (2 séries) para ele.
            'Serratil': 1.0, 

            # Zeros Obrigatórios
            'Peito_superior': 0.0,
            'Peito_medial': 0.0,
            'Peito_inferior': 0.0
        }
    }
)

# ==============================================================================
# EXPORTAÇÃO
# ==============================================================================
meus_exercicios = {
    "ElevacaoLateralMaquina": elevacao_lateral
}