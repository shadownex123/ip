import base64
import requests

ips_url = "https://raw.githubusercontent.com/rqzbeh/rqzbeh-wp/refs/heads/main/clean-ips.json"

base_config = "vless://6b1b46fe-c769-4c33-8f5c-c6017805012a@{ip}:443?mode=multi&security=tls&alpn=h2&encryption=none&authority=nl-srv1.z3df1lter.uk&insecure=0&fp=random&type=grpc&serviceName=%2Fgrpc&allowInsecure=0&sni=nl-srv1.z3df1lter.uk#%5B%F0%9F%87%B3%F0%9F%87%B1%5D%20NL1-{index}"

ips = requests.get(ips_url).json()

configs = []
for i, ip in enumerate(ips):
    configs.append(base_config.format(ip=ip, index=i+1))

full_text = "\n".join(configs)
encoded_sub = base64.b64encode(full_text.encode()).decode()

with open("sub", "w") as f:
    f.write(encoded_sub)
