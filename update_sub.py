import base64
import requests

ips_url = "https://raw.githubusercontent.com/rqzbeh/rqzbeh-wp/refs/heads/main/clean-ips.json"

base_config = "vless://34283924-b06e-4bc8-866a-2bad50ad5c93@{ip}:443?path=%2F&security=tls&encryption=none&insecure=0&host=revecity.pages.dev&fp=chrome&type=ws&allowInsecure=0&sni=revecity.pages.dev#CF%E5%AE%98%E6%96%B9%E4%BC%98%E9%80%89-{index}"

ips = requests.get(ips_url).json()

configs = []
for i, ip in enumerate(ips):
    configs.append(base_config.format(ip=ip, index=i+1))

full_text = "\n".join(configs)
encoded_sub = base64.b64encode(full_text.encode()).decode()

with open("sub", "w") as f:
    f.write(encoded_sub)
