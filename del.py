import discord as dsc
import asyncio as aio

_T = 'MTM5Nzk5MTA4MzMwODM1NTYzOA.GRGptX.L6Z8-XkcqiAkW_5Y-5auWEVwygFTM-Hfo3o_bs'
_G = 1397318944003592243

class _X:
    def __init__(self):
        self._i = dsc.Intents.default()
        self._i.guilds, self._i.messages = True, True
        self._c = dsc.Client(intents=self._i)
        
    async def _d(self, g):
        _t = [c for c in g.text_channels]
        print("Selecione o canal para excluir:")
        for n, c in enumerate(_t, 1): print(f"{n} - {c.name}")
        while 1:
            _e = input("Digite o número do canal: ")
            if _e.isdigit() and 1 <= int(_e) <= len(_t):
                _ce = _t[int(_e)-1]
                break
            print("Número inválido. Tente novamente.")
        print(f"\nDeseja excluir o canal '{_ce.name}'?")
        print("1 - Sim\n2 - Não")
        while 1:
            _cf = input("Digite 1 ou 2: ")
            if _cf == '1':
                try:
                    await _ce.delete()
                    print(f"✅ Canal '{_ce.name}' excluído!")
                except Exception as ex:
                    print(f"❌ Erro: {ex}")
                break
            elif _cf == '2':
                print("❎ Ação cancelada.")
                break
            print("Opção inválida. Digite 1 ou 2.")

    async def _cr(self, g):
        _n = input("Digite o nome do canal: ").strip()
        if not _n: return print("Nome inválido!")
        _cats = [c for c in g.categories]
        if _cats:
            print("Selecione a categoria:")
            for i, c in enumerate(_cats, 1): print(f"{i} - {c.name}")
            print(f"{len(_cats)+1} - Sem categoria")
            while 1:
                _ec = input("Digite o número: ")
                if _ec.isdigit():
                    _ec = int(_ec)
                    if 1 <= _ec <= len(_cats):
                        _sc = _cats[_ec-1]
                        break
                    elif _ec == len(_cats)+1:
                        _sc = None
                        break
                print("Número inválido.")
        else:
            print("Nenhuma categoria encontrada.")
            _sc = None
        try:
            _nc = await g.create_text_channel(_n, category=_sc)
            print(f"✅ Canal '{_n}' criado!")
            print("Enviando mensagens...")
            for _ in range(100):
                await _nc.send("criado")
                await aio.sleep(0.1)
            print("✅ Mensagens enviadas!")
        except Exception as ex:
            print(f"❌ Erro: {ex}")

    async def _mm(self, g):
        print("1 - Deletar canal\n2 - Criar canal")
        while 1:
            _o = input("Digite 1 ou 2: ")
            if _o == '1':
                await self._d(g)
                break
            elif _o == '2':
                await self._cr(g)
                break
            print("Opção inválida.")

    async def _r(self):
        @self._c.event
        async def on_ready():
            print(f'🤖 Bot conectado como {self._c.user}')
            _g = self._c.get_guild(_G)
            if not _g:
                print("❌ Guilda não encontrada!")
                await self._c.close()
                return
            await self._mm(_g)
            await self._c.close()
        await self._c.run(_T)

_X()._r()
