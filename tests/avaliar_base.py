from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
ARQUIVO = BASE_DIR / "data" / "transacoes.csv"


def main():
    df = pd.read_csv(ARQUIVO)

    entradas = df.loc[df["tipo"] == "entrada", "valor"].sum()
    saidas = df.loc[df["tipo"] == "saida", "valor"].sum()
    saldo = entradas - saidas

    alimentacao = df.loc[
        (df["tipo"] == "saida") & (df["categoria"] == "alimentacao"),
        "valor",
    ].sum()

    resultados = {
        "entradas": (entradas, 5000.00),
        "saidas": (saidas, 2488.90),
        "saldo": (saldo, 2511.10),
        "alimentacao": (alimentacao, 570.00),
    }

    print("=== AVALIAÇÃO DETERMINÍSTICA DA BASE ===")

    falhas = 0

    for nome, (obtido, esperado) in resultados.items():
        correto = abs(obtido - esperado) < 0.01
        status = "OK" if correto else "FALHA"
        print(f"{nome:12} -> obtido={obtido:8.2f} | esperado={esperado:8.2f} | {status}")
        if not correto:
            falhas += 1

    if falhas:
        raise SystemExit(f"\n{falhas} teste(s) falharam.")

    print("\nTodos os testes determinísticos passaram.")


if __name__ == "__main__":
    main()
