import base64
import requests

ips_url = "https://raw.githubusercontent.com/rqzbeh/rqzbeh-wp/refs/heads/main/clean-ips.json"
base_config = "vless://b9715b66-e4c1-40c2-b130-0ff9822b2adc@{ip}:443?path=%2Fezvs%2Fcf&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=ezvs.ir&fp=random&type=ws&allowInsecure=0&sni=ezvs.ir#ReVeCiTy-{index}"

ips = requests.get(ips_url).json()

configs = []
for i, ip in enumerate(ips):
    configs.append(base_config.format(ip=ip, index=i+1))

full_text = "\n".join(configs)
encoded_sub = base64.b64encode(full_text.encode()).decode()

with open("sub", "w") as f:
    f.write(encoded_sub)
