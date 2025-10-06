import sys
import os
import pandas as pd

def main(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".csv"):
            input_path = os.path.join(input_dir, filename)
            df = pd.read_csv(input_path)
            
            df = df.dropna()
            df.columns = [col.strip().lower().replace(" ", "") for col in df.columns]

            if {'order_id', 'amount'}.issubset(df.columns):
                df_client = df[['order_id', 'amount']]
            else:
                df_client = df.copy()

            trusted_path = os.path.join(output_dir, f"trusted_{filename}")
            df.to_csv(trusted_path, index=False)
            
            client_path = os.path.join(output_dir, f"client_{filename}")
            df_client.to_csv(client_path, index=False)

    print("Processamento concluído com sucesso!")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python transform.py <diretorio_de_entrada> <diretorio_de_saida>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]
    
    main(input_directory, output_directory)
