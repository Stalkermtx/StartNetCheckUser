
import os
import subprocess
import sys
import socket
import urllib.request
import json

cor_vermelha = "\033[91m"
cor_verde = "\033[92m"
cor_amarela = "\033[93m"
cor_azul = "\033[94m"
cor_reset = "\033[0m"

def adicionar_ao_cache(chave, valor):
    cache = carregar_cache()  
    cache[chave] = valor
    salvar_cache(cache)  

def remover_do_cache(chave):
    cache = carregar_cache()  
    if chave in cache:
        del cache[chave]
        salvar_cache(cache) 

def obter_do_cache(chave):
    cache = carregar_cache()  
    return cache.get(chave)

def carregar_cache():
    try:
        with open('/root/StartNet/cache.json', 'r') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {} 
    
def salvar_cache(cache):
    with open('/root/UlekCheckUser/cache.json', 'w') as arquivo:
        json.dump(cache, arquivo)


def get_public_ip():
    try:
        url = "https://ipinfo.io"
        response = urllib.request.urlopen(url)
        if response.status == 200:
            data = json.loads(response.read().decode("utf-8"))
            if 'ip' in data:
                return data['ip']
            else:
                print("Endereço IP público não encontrado na resposta.")
                return None
        else:
            print("Falha na Solicitação ao servidor.")
            return None
    except Exception as e:
        print("Não Foi Possível Obter o Endereço IP Público:", str(e))
        return None




def verificar_processo(nome_processo):
    try:
        resultado = subprocess.check_output(["ps", "aux"]).decode()
        linhas = resultado.split('\n')
        for linha in linhas:
            if nome_processo in linha and "python" in linha:
                return True
    except subprocess.CalledProcessError as e:
        print(f"Erro ao Verificar o Processo: {e}")
    return False


nome_do_script = "/root/StartNet/checkuser.py"




if __name__ == "__main__":
    while True:
        os.system('clear')


        if verificar_processo(nome_do_script):
            status = f'{cor_verde}ativo{cor_reset} - porta em uso: {obter_do_cache("porta")}'
        else:
            status = f'{cor_vermelha}parado{cor_reset} - porta que será usada: {obter_do_cache("porta")}'
       
        print(f"Status: {status}")

        print(f"")

        print(f"Selecione Uma Opção:")
        print(f" 1 - Iniciar Checkuser")
        print(f" 2 - Parar Checkuser")
        print(f" 3 - Verificar Links")
        print(f" 4 - Sobre")
        print(f" 0 - Sair do Menu")

        option = input("Digite a Opção: ")

        if option == "1":

            print(f"Observação: Para Funcionar Com Security Apenas Se Usar a Porta 5454 !")
            
            adicionar_ao_cache('porta', input("\nDigite a Porta Que Deseja Usar !"))

            os.system('clear')
            print(f'Porta Escolhida: {obter_do_cache("porta")}')

            os.system(f'nohup python3 {nome_do_script} --port {obter_do_cache("porta")} & ')

            input(f"\nPressione a Tecla Enter Para Voltar ao Menu\n\n")
        elif option == "2":
            if verificar_processo(nome_do_script):

                try:
                    subprocess.run(f'pkill -9 -f "/root/StartNet/checkuser.py"', shell=True)

                        
                except subprocess.CalledProcessError:
                    print("Erro ao Executar o Comando.")
                remover_do_cache("porta")
            else: 
                print("O Checkuser Não Está Ativo.")
            


            input(f"Pressione a tecla enter para voltar ao menu")
        elif option == "3":
            os.system('clear')
            if verificar_processo(nome_do_script):
                print("Abaixo os Apps, e os Links Para Cada Um: ")
                print("")
                ip = get_public_ip()
                porta = obter_do_cache("porta")
                print(f" DtunnelMod - http://{ip}:{porta}/dtmod  ")
                print(f" GltunnelMod - http://{ip}:{porta}/gl ")
                print(f" AnyVpnMod - http://{ip}:{porta}/anymod ")
                print(f" Conecta4g - http://{ip}:{porta}/checkUser ")
                print(f" AtxTunnel - http://{ip}:{porta}/atx ")
                print("")

                print("Para usar com security (por favor, use apenas esses links com security e conexões que não usam cloudflare para não sobrecarregar nossos servidores)")
                print("")
                print(f" DtunnelMod - http://proxy.ulekservices.shop/api.php?url=http://{ip}:{porta}/dtmod  ")
                print(f" GltunnelMod - http://proxy.ulekservices.shop/api.php?url=http://{ip}:{porta}/gl ")
                print(f" AnyVpnMod - http://proxy.ulekservices.shop/api.php?url=http://{ip}:{porta}/anymod ")
                print(f" Conecta4g - http://proxy.ulekservices.shop/api.php?url=http://{ip}:{porta}/checkUser ")
                print(f" AtxTunnel - http://proxy.ulekservices.shop/api.php?url=http://{ip}:{porta}/atx ")
                print("")

            else:
                print("\nInicie o Serviço Primeiro\n")
            input(f"Pressione a Tecla Enter Para Voltar ao Menu")
                  

        elif option == "4":
            os.system('clear')
            print(f"Olá, esse é um multi-checkuser Editado por @StartNetOfc")
            print(f"Com esse Checkuser Venho Trazendo a Possibilidade de Usar em Diversos Apps")
            print(f"Apps Como: ")
            print(f" - DtunnelMod")
            print(f" - GlTunnelMod")
            print(f" - AnyVpnMod")
            print(f" - Conecta4g")
            print(f"")
            input(f"Pressione a Tecla Enter Para Voltar ao Menu")
        elif option == "0":
            sys.exit(0)
        else:
            os.system('clear')
            print(f"Selecionado Uma Opção Invalida, Tente Novamente !")
            input(f"Pressione a Tecla Enter Para Voltar ao Menu")
