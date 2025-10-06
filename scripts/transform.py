import sys, os
import pandas as pd

if len(sys.argv) < 3:
print("Uso: transform.py <input_dir> <output_dir>")
sys.exit(1)

inp, outp = sys.argv[1], sys.argv[2]
os.makedirs(outp, exist_ok=True)

for f in os.listdir(inp):
if f.endswith(".csv"):
df = pd.read_csv(os.path.join(inp, f))

    # Limpa dados
    df = df.dropna()
    df.columns = [c.strip().lower().replace(" ", "") for c in df.columns]

    # Gera dataframe de clientes se colunas existirem
    if set(['order_id', 'amount']).issubset(df.columns):
        df_client = df[['order_id', 'amount']]
    else:
        df_client = df.copy()

    # Salva arquivos transformados
    df.to_csv(os.path.join(outp, f"trusted_{f}"), index=False)
    df_client.to_csv(os.path.join(outp, f"client_{f}"), index=False)
