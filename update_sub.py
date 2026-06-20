import base64
import requests

ips_url = "https://raw.githubusercontent.com/rqzbeh/rqzbeh-wp/refs/heads/main/clean-ips.json"

base_config = "vless://9ba99b6f-c7a4-44da-a298-d0e883a4b40e@{ip}:443?mode=auto&path=%2F&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&insecure=0&host=ezvs.ir&fp=random&type=xhttp&allowInsecure=0&sni=ezvs.ir#ReVeCiTy-{index}"

ips = requests.get(ips_url).json()

configs = []
for i, ip in enumerate(ips):
    configs.append(base_config.format(ip=ip, index=i+1))

full_text = "\n".join(configs)
encoded_sub = base64.b64encode(full_text.encode()).decode()

with open("sub", "w") as f:
    f.write(encoded_sub)
