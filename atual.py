import dataclasses
from collections import defaultdict

# Importa os arquivos de treino que criamos
import fb1
import fb2

def calcular_volume_semanal():
    # ==========================================================================
    # 1. DEFINA SUA ROTINA AQUI
    # Basta repetir os módulos na lista quantas vezes fizer na semana.
    # ==========================================================================
    semana = [
        ("Fullbody 1", fb1),
        ("Fullbody 2", fb2),
        ("Fullbody 1", fb1),
        ("Fullbody 2", fb2),
    ]
    
    # Acumuladores
    volume_total = defaultdict(float)
    
    print(f"{'TREINO':<12} | {'EXERCÍCIO':<20} | {'GRUPOS ATIVADOS (Séries)'}")
    print("-" * 75)

    for nome_treino, modulo in semana:
        # Pega o dicionário exportado 'meus_exercicios' de cada arquivo
        for nome_ex, exercicio in modulo.meus_exercicios.items():
            
            grupos_ativos = []
            
            # Varre automaticamente todos os grupos musculares do objeto Corpo
            for field in dataclasses.fields(exercicio):
                grupo = getattr(exercicio, field.name)
                
                # Se o grupo tiver volume > 0, contabiliza
                # (O 'getattr' garante que funciona pra qualquer músculo que tenha .volume)
                if hasattr(grupo, 'volume') and grupo.volume > 0:
                    volume_total[field.name] += grupo.volume
                    grupos_ativos.append(f"{field.name}: {grupo.volume:g}")

            print(f"{nome_treino:<12} | {nome_ex:<20} | {', '.join(grupos_ativos)}")

    # ==========================================================================
    # RELATÓRIO FINAL
    # ==========================================================================
    print("\n" + "="*40)
    print("VOLUME SEMANAL TOTAL (Séries por Grupo)")
    print("="*40)
    
    # Ordena alfabeticamente para facilitar leitura
    for musculo, total in sorted(volume_total.items()):
        print(f"{musculo.capitalize():<20}: {total:>5.1f} séries")

if __name__ == "__main__":
    calcular_volume_semanal()