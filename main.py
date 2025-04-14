from risk_calculator import calcular_risco
from protection_level import determinar_nivel_protecao

def main():
    print("Bem-vindo ao programa de análise de risco de SPDA!")

    # Entrada de parâmetros do usuário
    parametros = {
        'probabilidade': float(input("Digite a probabilidade de ocorrência (0-100): ")),
        'impacto': float(input("Digite o impacto esperado (0-100): "))
    }

    # Cálculos
    risco = calcular_risco(parametros)
    nivel_protecao = determinar_nivel_protecao(risco)

    # Exibir resultados
    print(f"\nAnálise de Risco concluída:")
    print(f"Risco calculado: {risco:.2f}")
    print(f"Nível de proteção recomendado: {nivel_protecao}")

if __name__ == "__main__":
    main()
