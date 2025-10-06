import sys, os [cite: 35]
import pandas as pd [cite: 36]

if len(sys.argv) < 3: [cite: 37, 38]
    print("Uso: transform.py <input_dir> <output_dir>") [cite: 39]
    sys.exit(1) [cite: 39]

inp, outp = sys.argv[1], sys.argv[2] [cite: 40]
os.makedirs(outp, exist_ok=True) [cite: 41]

for f in os.listdir(inp): [cite: 42]
    if f.endswith(".csv"): [cite: 43]
        df = pd.read_csv(os.path.join(inp, f)) [cite: 44]
      
        df = df.dropna() [cite: 47]
        df.columns = [c.strip().lower().replace(" ", "") for c in df.columns] [cite: 48, 49]
        
        
        df_client = df[['order_id', 'amount']] if set(['order_id', 'amount']).issubset(df.columns) else df.copy() [cite: 51, 52]
        
        
        df.to_csv(os.path.join(outp, f"trusted_{f}"), index=False) [cite: 54]
        df_client.to_csv(os.path.join(outp, f"client_{f}"), index=False) [cite: 54, 55]
