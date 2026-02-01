import dataclasses

from corpo import Corpo
# No final do seu arquivo da classe Corpo, ou onde preferir:

#====
dips = Corpo()

dips.set_corpo_simples(
    peito=3, ombro=1, triceps=2)

dips.set_corpo_completo(
    peito={
        'Peito_inferior': 1.00,
        'Peito_medial'  : 0.60, 
        'Peito_superior': 0.20,
        'Serratil'      : 0.10 },
    ombro={
        'ombro_anterior'    : 1.00,
        'ombro_medial'      : 0.60,
        'ombro_posterior'   : 0.20 },
    triceps={
        'triceps_longa' : 0.00,
        'triceps_medial': 1.00,
        'triceps_curta' : 1.00 }
)

#====
crossover = Corpo()

crossover.set_corpo_simples(
    peito=3, ombro=1, biceps=1)

crossover.set_corpo_completo(
    peito={
        'Peito_superior': 0.4,
        'Peito_medial'  : 0.6,
        'Peito_inferior': 1.0,
        'Serratil': 0.0
    },
    ombro={
        'ombro_anterior' : 1.0,
        'ombro_medial'   : 0.6,
        'ombro_posterior': 0.2
    },
    biceps={
        'biceps_longa': 1,
        'biceps_curta': 1,
        'braquial': 0.0
    }
)

#====
crucifixo_maquina = Corpo()

crucifixo_maquina.set_corpo_simples(
    peito=3, ombro=1, biceps=1)

crucifixo_maquina.set_corpo_completo(
    peito={
        'Peito_superior': 0.5,
        'Peito_medial'  : 1.0,
        'Peito_inferior': 0.5,
        'Serratil': 0.0
    },
    ombro={
        'ombro_anterior' : 1.0,
        'ombro_medial'   : 0.6,
        'ombro_posterior': 0.2
    },
    biceps={
        'biceps_longa': 0.5,
        'biceps_curta': 0.5,
        'braquial': 0.0
    }
)

#====
barra_fixa = Corpo()

barra_fixa.set_corpo_simples(
    costas=3, biceps=1, peito=1, antebraco=1, ombro=1
)

barra_fixa.set_corpo_completo(
    costas={
        'dorsal_superior'   : 0.60,
        'dorsal_medial'     : 0.80,
        'dorsal_inferior'   : 1.00,
        'romboide'          : 0.50,
        'trapezio_superior' : 0.20,
        'trapezio_medio'    : 0.40,
        'trapezio_inferior' : 1.00,
        'redondo_maior'     : 0.80
    },
    peito={
        'Peito_superior'    : 0.20,
        'Peito_medial'      : 0.50,
        'Peito_inferior'    : 1.00,
        'Serratil'          : 0.90
    },
    ombro={
        'ombro_anterior'    : 0.5,
        'ombro_medial'      : 0.7,
        'ombro_posterior'   : 1.0
    },
    biceps={
        'biceps_longa'      : 1.0,
        'biceps_curta'      : 1.0,
        'braquial'          : 1.0
    },
    antebraco={
        'antebraco_extensores'  : 0.40,
        'antebraco_fletores'    : 0.60,
        'braquiorradial'        : 1.0
    }
)


#====
lat_pullover = Corpo()

lat_pullover.set_corpo_simples(
    costas=3, peito=1, triceps=1, ombro=1
)

lat_pullover.set_corpo_completo(
    costas={
        'dorsal_superior': 0.20,
        'dorsal_medial': 0.25,
        'dorsal_inferior': 0.25,
        'romboide': 0.10,
        'trapezio_superior': 0.0,
        'trapezio_medio': 0.07,
        'trapezio_inferior': 0.05,
        'redondo_maior': 0.06
    },
    peito={
        'Peito_superior': 0.20,
        'Peito_medial': 0.20,
        'Peito_inferior': 0.60,
        'Serratil': 0.0
    },
    ombro={
        'ombro_anterior': 0.2,
        'ombro_medial': 0.2,
        'ombro_posterior': 0.6
    },
    triceps={
        'triceps_longa': 0.60,
        'triceps_medial': 0.2,
        'triceps_curta': 0.2
    }
)

#====
lat_pulldown = Corpo()

lat_pulldown.set_corpo_simples(
    costas=10, biceps=3, peito=2, ombro=2, antebraco=2
)

lat_pulldown.set_corpo_completo(
    costas={
        'dorsal_superior': 0.15,
        'dorsal_medial': 0.25,
        'dorsal_inferior': 0.25,
        'romboide': 0.10,
        'trapezio_superior': 0.0,
        'trapezio_medio': 0.08,
        'trapezio_inferior': 0.05,
        'redondo_maior': 0.08
    },
    peito={
        'Peito_superior': 0.25,
        'Peito_medial': 0.35,
        'Peito_inferior': 0.40,
        'Serratil': 0.0
    },
    biceps={
        'biceps_longa': 0.55,
        'biceps_curta': 0.45,
        'braquial': 0.0
    },
    ombro={
        'ombro_anterior': 0.2,
        'ombro_medial': 0.2,
        'ombro_posterior': 0.6
    },
    antebraco={
        'antebraco_extensores': 0.40,
        'antebraco_fletores': 0.60,
        'braquiorradial': 0.0
    }
)
"""
# =========================================================
print("=== DIPS ===")
print(dips.resumo())    
print(dips.detalhado())    

print("=== CROSSOVER ===")
print(crossover.resumo())
print(crossover.detalhado())

print("\n=== BARRA FIXA ===") 
print(barra_fixa.resumo())
print(barra_fixa.detalhado())

print("\n=== LAT PULLDOWN ===")
print(lat_pulldown.resumo())
print(lat_pulldown.detalhado())
"""

