import discord
import asyncio

TOKEN = 'MTM5Nzk5MTA4MzMwODM1NTYzOA.GYE9qb.eBkDZubFFwinLC8tjoOUM4nsfuVXIKWMxNIQ9Y'         # 🟡 Substitua pelo token do seu bot
GUILD_ID = 1397318944003592243    # 🟡 Substitua pelo ID do seu servidor (como número)

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True

client = discord.Client(intents=intents)

# Função para deletar canal escolhido
async def deletar_canal(guild):
    canais_texto = [c for c in guild.text_channels]

    print("Selecione o canal para excluir:")
    for i, canal in enumerate(canais_texto, start=1):
        print(f"{i} - {canal.name}")

    while True:
        escolha = input("Digite o número do canal: ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(canais_texto):
            canal_escolhido = canais_texto[int(escolha) - 1]
            break
        else:
            print("Número inválido. Tente novamente.")

    print(f"\nDeseja excluir o canal '{canal_escolhido.name}'?")
    print("1 - Sim")
    print("2 - Não")

    while True:
        confirm = input("Digite 1 ou 2: ")
        if confirm == '1':
            try:
                await canal_escolhido.delete()
                print(f"✅ Canal '{canal_escolhido.name}' excluído com sucesso!")
            except Exception as e:
                print(f"❌ Erro ao excluir canal: {e}")
            break
        elif confirm == '2':
            print("❎ Ação cancelada.")
            break
        else:
            print("Opção inválida. Digite 1 ou 2.")

# Função para criar canal e enviar 100 mensagens "criado"
async def criar_canal(guild):
    nome = input("Digite o nome do canal para criar: ").strip()
    if not nome:
        print("Nome inválido!")
        return

    categorias = [c for c in guild.categories]
    if categorias:
        print("Selecione a categoria para o canal:")
        for i, cat in enumerate(categorias, start=1):
            print(f"{i} - {cat.name}")
        print(f"{len(categorias)+1} - Nenhuma categoria (sem categoria)")

        while True:
            escolha_cat = input("Digite o número da categoria: ")
            if escolha_cat.isdigit():
                escolha_cat = int(escolha_cat)
                if 1 <= escolha_cat <= len(categorias):
                    categoria_escolhida = categorias[escolha_cat - 1]
                    break
                elif escolha_cat == len(categorias) + 1:
                    categoria_escolhida = None
                    break
            print("Número inválido. Tente novamente.")
    else:
        print("Nenhuma categoria encontrada. O canal será criado sem categoria.")
        categoria_escolhida = None

    try:
        canal = await guild.create_text_channel(nome, category=categoria_escolhida)
        print(f"✅ Canal '{nome}' criado com sucesso!")

        # Enviar 100 mensagens "criado"
        print("Enviando 100 mensagens no canal novo...")
        for _ in range(100):
            await canal.send("criado")
            await asyncio.sleep(0.1)  # Recomendado para evitar bloqueio por spam

        print("✅ Mensagens enviadas!")

    except Exception as e:
        print(f"❌ Erro ao criar canal: {e}")

# Menu principal
async def main_menu(guild):
    print("Escolha uma opção:")
    print("1 - Deletar canal")
    print("2 - Criar canal")

    while True:
        opcao = input("Digite 1 ou 2: ")
        if opcao == '1':
            await deletar_canal(guild)
            break
        elif opcao == '2':
            await criar_canal(guild)
            break
        else:
            print("Opção inválida. Digite 1 ou 2.")

# Quando o bot estiver pronto
@client.event
async def on_ready():
    print(f'🤖 Bot conectado como {client.user}')
    guild = client.get_guild(GUILD_ID)
    if guild is None:
        print("❌ Guilda não encontrada! Verifique o GUILD_ID.")
        await client.close()
        return

    await main_menu(guild)
    await client.close()

# Iniciar o bot
client.run(TOKEN)
