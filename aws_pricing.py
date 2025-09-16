import requests
import pandas as pd

url = "https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/US%20East%20%28Ohio%29/Linux/index.json"


resp = requests.get(url)
data = resp.json()

rows = []

# Iterate through all regions
for region, instances in data.get("regions", {}).items():
    for name, details in instances.items():
        rows.append({
            "Region": region,
            "InstanceKey": name,
            "InstanceType": details.get("Instance Type"),
            "InstanceFamily": details.get("Instance Family"),
            "vCPU": details.get("vCPU"),
            "Memory": details.get("Memory"),
            "Storage": details.get("Storage"),
            "Network": details.get("Network Performance"),
            "OperatingSystem": details.get("Operating System"),
            "PriceUSD": details.get("price"),
        })

df = pd.DataFrame(rows)

df["IsGPU"] = df["InstanceFamily"].str.contains("GPU|Accelerated", case=False, na=False)


df["PricePerGPU"] = df.apply(lambda x: float(x["PriceUSD"]) if x["IsGPU"] else None, axis=1)

# Save to Excel
output_file = "aws_ec2_ohio_linux.xlsx"
df.to_excel(output_file, index=False)

print(f" Data saved to {output_file}")
print("Sample rows:")
print(df.head())
