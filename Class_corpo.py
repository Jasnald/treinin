import dataclasses
from Class_musculatura import *

# --- Função Auxiliar ---
def fac(function):
    """
    Função de atalho para dataclasses.field(default_factory=...).
    """
    return dataclasses.field(default_factory=function)

# --- Classe Principal ---
@dataclasses.dataclass
class Corpo:
    """
    Agrega todas as classes de grupos musculares em uma única estrutura,
    representando o corpo humano completo para análise de treino.
    """
    # --- Membros Superiores e Tronco ---
    peito:     Peito     = fac(Peito)
    costas:    Costas    = fac(Costas)
    ombro:     Ombro     = fac(Ombro)
    manguito:  Manguito  = fac(Manguito)

    # --- Braços ---
    biceps:    Biceps    = fac(Biceps)
    triceps:   Triceps   = fac(Triceps)
    antebraco: Antebraco = fac(Antebraco)

    # --- Core (Núcleo) ---
    abdomen: Abdomen = fac(Abdomen)
    lombar:  Lombar  = fac(Lombar)

    # --- Membros Inferiores ---
    gluteo:              Gluteo            = fac(Gluteo)
    quadriceps:          Quadriceps        = fac(Quadriceps)
    posteriorcoxa:       PosteriorCoxa     = fac(PosteriorCoxa)
    adutores:            Adutores          = fac(Adutores)
    panturrilha:         Panturrilha       = fac(Panturrilha)
    flexores_do_quadril: FlexoresDoQuadril = fac(FlexoresDoQuadril)
    
    def set_corpo_simples(self, **volumes):
        """Assume que todos os métodos seguem padrão set_{musculo}_simples"""
        for musculo, volume in volumes.items():
            if hasattr(self, musculo):
                grupo = getattr(self, musculo)
                metodo_nome = f'set_{musculo}_simples'
                if hasattr(grupo, metodo_nome):
                    metodo = getattr(grupo, metodo_nome)
                    metodo(volume)
        return self
    
    def set_corpo_completo(self, **volumes):
        """Assume que todos os métodos seguem padrão set_{musculo}_simples"""
        for musculo, detalhes in volumes.items():
            if hasattr(self, musculo):
                grupo = getattr(self, musculo)
                metodo_nome = f'set_{musculo}_completo'
                if hasattr(grupo, metodo_nome):
                    metodo = getattr(grupo, metodo_nome)
                    metodo(**detalhes)
        return self


    def __str__(self):
        """Mostra apenas campos não-zero de forma automática"""
        partes = []
        
        # Pega todos os campos do Corpo automaticamente
        for field in dataclasses.fields(self):
            grupo = getattr(self, field.name)
            
            # Pega campos não-zero do grupo automaticamente  
            campos_ativos = []
            for subfield in dataclasses.fields(grupo):
                valor = getattr(grupo, subfield.name)
                if valor != 0.0:
                    campos_ativos.append(f"{subfield.name}={valor}")
            
            # Se tem algo ativo, mostra
            if campos_ativos:
                partes.append(f"{field.name.title()}: {', '.join(campos_ativos)}")
        
        return "\n".join(partes) if partes else "Corpo vazio"
    
    def resumo(self):
        """Só os valores principais (primeiro campo de cada grupo)"""
        ativos = []
        
        for field in dataclasses.fields(self):
            grupo = getattr(self, field.name)
            # Pega o primeiro campo (valor principal)
            primeiro_campo = dataclasses.fields(grupo)[0]
            valor = getattr(grupo, primeiro_campo.name)
            
            if valor != 0.0:
                ativos.append(f"{field.name}: {valor}")
        
        return " | ".join(ativos)
        
    # Dentro da classe Corpo
    def detalhado(self):
        """Mostra TODOS os campos não-zero, incluindo frações"""
        partes = []
        
        for field in dataclasses.fields(self):
            grupo = getattr(self, field.name)
            
            # Pega TODOS os campos não-zero do grupo
            campos_ativos = []
            for subfield in dataclasses.fields(grupo):
                valor = getattr(grupo, subfield.name)
                if valor != 0.0:
                    campos_ativos.append(f"   {subfield.name} = {valor}")
            
            if campos_ativos:
                partes.append(f"{field.name}:\n{', \n'.join(campos_ativos)}\n")
        
        return "\n".join(partes)