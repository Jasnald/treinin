from typing import List, Tuple, Dict

class Peito:
    exercicios = [
        ("Dips", 3),
        ("Crossover", 3), 
        ("Crucifixo Máquina", 3)
    ]

class Costas:
    exercicios = [
        ("Barra Fixa", 3),
        ("Lat Pullover Machine", 3),
        ("Lat Pulldown Machine", 3)
    ]

class Posterior:
    exercicios = [
        ("RDL", 3),
        ("Cadeira Flexora", 3),
        ("Back Extension", 3)
    ]

class Quads:
    exercicios = [
        ("Leg Press", 3),
        ("Sissy Squat", 3),
        ("Leg Extension", 3)
    ]

class Biceps:
    exercicios = [
        ("Cable Curl", 3),
        ("Rosca Martelo", 3)
    ]

class Triceps:
    exercicios = [
        ("Triceps Pulldown", 3)
    ]

class Abdomen:
    exercicios = [
        ("Abdominal Máquina", 3),
        ("Abdominal Infra", 3)
    ]

class Panturrilha:
    exercicios = [
        ("Panturrilha Leg Press", 4)
    ]

class Ombro:
    exercicios = [
        ("Ombro", 3)
    ]

class GruposMaiores:
    def __init__(self):
        self.peito = Peito()
        self.costas = Costas()
        self.posterior = Posterior()
        self.quads = Quads()
        
        self.grupos = {
            'peito': self.peito,
            'costas': self.costas,
            'posterior': self.posterior,
            'quads': self.quads
        }

class GruposMenores:
    def __init__(self):
        self.biceps = Biceps()
        self.triceps = Triceps()
        self.abdomen = Abdomen()
        self.panturrilha = Panturrilha()
        self.ombro = Ombro()
        
        self.grupos = {
            'biceps': self.biceps,
            'triceps': self.triceps,
            'abdomen': self.abdomen,
            'panturrilha': self.panturrilha,
            'ombro': self.ombro
        }

class GeradorTreinoAutomatico:
    def __init__(self):
        self.grupos_maiores = GruposMaiores()
        self.grupos_menores = GruposMenores()
        
        # Metas semanais
        self.series_restantes = {
            'peito': 12, 'costas': 12, 'posterior': 9, 'quads': 9,
            'biceps': 6, 'triceps': 3, 'abdomen': 6, 'panturrilha': 4, 'ombro': 3
        }
        
        # Exercícios usados
        self.exercicios_usados = {grupo: [] for grupo in self.series_restantes}
        
        # Apenas as prioridades - tudo mais é automático
        self.prioridades = {
            'A': 'peito',
            'B': 'costas', 
            'C': 'posterior',
            'D': 'quads'
        }
    
    def reset_semana(self):
        self.series_restantes = {
            'peito': 12, 'costas': 12, 'posterior': 9, 'quads': 9,
            'biceps': 6, 'triceps': 3, 'abdomen': 6, 'panturrilha': 4, 'ombro': 3
        }
        for grupo in self.exercicios_usados:
            self.exercicios_usados[grupo].clear()
    
    def get_exercicio_disponivel(self, grupo: str) -> Tuple[str, int]:
        # Determinar se é grupo maior ou menor
        if grupo in self.grupos_maiores.grupos:
            exercicios_grupo = self.grupos_maiores.grupos[grupo].exercicios
        else:
            exercicios_grupo = self.grupos_menores.grupos[grupo].exercicios
        
        # Pegar exercício não usado
        exercicios_disponiveis = [ex for ex in exercicios_grupo 
                                if ex not in self.exercicios_usados[grupo]]
        
        if not exercicios_disponiveis:
            self.exercicios_usados[grupo].clear()
            exercicios_disponiveis = exercicios_grupo
        
        exercicio_escolhido = exercicios_disponiveis[0]
        self.exercicios_usados[grupo].append(exercicio_escolhido)
        return exercicio_escolhido
    
    def alocar_exercicio(self, grupo: str) -> Tuple[str, int]:
        if self.series_restantes[grupo] <= 0:
            return None
            
        nome, series = self.get_exercicio_disponivel(grupo)
        self.series_restantes[grupo] -= series
        return (nome, series)
    
    def distribuir_grupos_automaticamente(self, letra_treino: str) -> Tuple[List[str], List[str]]:
        """Distribui grupos automaticamente baseado na prioridade"""
        prioridade = self.prioridades[letra_treino]
        
        # Todos os grupos maiores
        todos_grupos_maiores = ['peito', 'costas', 'posterior', 'quads']
        
        # Coloca prioridade em 2º lugar, outros em ordem padrão  
        grupos_maiores = []
        outros_grupos = [g for g in todos_grupos_maiores if g != prioridade]
        
        grupos_maiores.append(outros_grupos[0])  # 1º exercício
        grupos_maiores.append(prioridade)        # 2º exercício (PRIORIDADE)
        grupos_maiores.extend(outros_grupos[1:]) # Resto
        
        # Distribuição automática de grupos menores por dia
        distribuicao_menores = {
            'A': ['panturrilha', 'triceps'],  # Panturrilha antes do leg press
            'B': ['biceps', 'abdomen'],
            'C': ['abdomen'],  # Só 1 grupo menor
            'D': ['biceps']    # Só 1 grupo menor
        }
        
        grupos_menores = distribuicao_menores[letra_treino]
        
        return grupos_maiores, grupos_menores
    
    def gerar_treino_dia(self, letra_treino: str) -> List[Tuple[str, int]]:
        """Gera treino para um dia específico"""
        grupos_maiores, grupos_menores = self.distribuir_grupos_automaticamente(letra_treino)
        treino = []
        
        # 4 exercícios de grupos maiores
        for grupo in grupos_maiores:
            exercicio = self.alocar_exercicio(grupo)
            if exercicio:
                treino.append(exercicio)
        
        # Grupos menores  
        for grupo in grupos_menores:
            exercicio = self.alocar_exercicio(grupo)
            if exercicio:
                treino.append(exercicio)
        
        return treino
    
    def gerar_semana_completa(self) -> Dict[str, List[Tuple[str, int]]]:
        self.reset_semana()
        treinos = {}
        for letra in ['A', 'B', 'C', 'D']:
            treinos[letra] = self.gerar_treino_dia(letra)
        return treinos
    
    def imprimir_treino_completo(self):
        treinos = self.gerar_semana_completa()
        
        print("=" * 60)
        print("TREINO FULL BODY 4 DIAS POR SEMANA - GERAÇÃO AUTOMÁTICA")
        print("=" * 60)
        
        dias = {'A': 'Segunda-feira', 'B': 'Terça-feira', 'C': 'Quinta-feira', 'D': 'Sexta-feira'}
        
        # Contadores para verificação
        series_realizadas = {grupo: 0 for grupo in self.series_restantes}
        
        for letra, exercicios in treinos.items():
            prioridade = self.prioridades[letra].upper()
            print(f"\n## TREINO {letra} ({dias[letra]})")
            print(f"**Prioridade: {prioridade}** (2º exercício)")
            print("-" * 40)
            
            total_series_treino = 0
            for i, (nome, series) in enumerate(exercicios, 1):
                marca_prioridade = " ⭐ *PRIORIDADE*" if i == 2 else ""
                tipo = "MAIOR" if i <= 4 else "MENOR"
                print(f"{i}. **{nome}** - {series} séries [{tipo}]{marca_prioridade}")
                total_series_treino += series
                
                # Contar para resumo
                self._contar_series_por_grupo(nome, series, series_realizadas)
            
            print(f"\n**Total do treino: {total_series_treino} séries**")
        
        # Resumo semanal
        print("\n" + "=" * 60)
        print("RESUMO SEMANAL:")
        print("=" * 60)
        for grupo, realizado in series_realizadas.items():
            meta = 12 if grupo in ['peito', 'costas'] else (9 if grupo in ['posterior', 'quads'] else (6 if grupo in ['biceps', 'abdomen'] else (4 if grupo == 'panturrilha' else 3)))
            status = "✅" if realizado >= meta else "⚠️"
            print(f"{status} {grupo.capitalize()}: {realizado}/{meta} séries")
    
    def _contar_series_por_grupo(self, nome_exercicio: str, series: int, contador: Dict[str, int]):
        # Mapeamento de exercícios para grupos
        mapeamento = {}
        
        # Grupos maiores
        for grupo_nome, grupo_obj in self.grupos_maiores.grupos.items():
            for ex_nome, _ in grupo_obj.exercicios:
                mapeamento[ex_nome] = grupo_nome
        
        # Grupos menores
        for grupo_nome, grupo_obj in self.grupos_menores.grupos.items():
            for ex_nome, _ in grupo_obj.exercicios:
                mapeamento[ex_nome] = grupo_nome
        
        if nome_exercicio in mapeamento:
            grupo = mapeamento[nome_exercicio]
            contador[grupo] += series

if __name__ == "__main__":
    gerador = GeradorTreinoAutomatico()
    gerador.imprimir_treino_completo()