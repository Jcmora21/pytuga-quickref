import sys
import re

def interpretar_pytuga(codigo):
    # Remover comentários (# ...)
    linhas = [linha for linha in codigo.split('\n') if not linha.strip().startswith('#')]
    codigo = '\n'.join(linhas)

    # Início: Bora
    codigo = codigo.replace('Bora', 'if __name__ == "__main__":')

    # Fim: Oh desligou!
    codigo = codigo.replace('Oh desligou!', '')

    # Mostrar texto com cores e efeitos
    # (insere o bloco completo de mostrar com a implementação anterior)

    # Variáveis: definir nome como valor
    codigo = re.sub(
        r'definir\s+([a-zA-Z_]\w*)\s+como\s+(.+?)(?=\s*(?:\n|$))',
        lambda m: f'{m.group(1)} = {m.group(2)}',
        codigo,
        flags=re.DOTALL
    )

    # Perguntar input
    codigo = re.sub(
        r'perguntar\s*:\s*\("([^"]*)"\)\s*guardar em\s*([a-zA-Z_]\w*)',
        r'\2 = input("\1\n> ")',
        codigo
    )

    # Conversões
    codigo = re.sub(
        r'converte\s+([a-zA-Z_]\w*)\s+para\s+n[úu]mero',
        r'\1 = int(\1)',
        codigo
    )

    # Condições
    codigo = re.sub(
        r'se\s+(.+?)\s+então',
        r'if \1:',
        codigo,
        flags=re.DOTALL
    )
    codigo = re.sub(
        r'senão se\s+(.+?)\s+então',
        r'elif \1:',
        codigo,
        flags=re.DOTALL
    )
    codigo = re.sub(
        r'senão',
        r'else:',
        codigo
    )
    codigo = codigo.replace('então pronto', '')

    # Ciclos enquanto
    codigo = re.sub(
        r'enquanto\s+(.+?)\s*\n((?:\s{4}.+\n?)+)então acaba',
        r'while \1:\n\2',
        codigo,
        flags=re.DOTALL | re.MULTILINE
    )

    # Ciclos para cada
    codigo = re.sub(
        r'para cada\s+([a-zA-Z_]\w*)\s+em\s+chaves da lista\s+([a-zA-Z_]\w*)',
        r'for \1 in \2.keys():',
        codigo
    )
    codigo = re.sub(
        r'para cada\s+([a-zA-Z_]\w*)\s+em\s+valores da lista\s+([a-zA-Z_]\w*)',
        r'for \1 in \2.values():',
        codigo
    )
    codigo = re.sub(
        r'para cada\s+([a-zA-Z_]\w*)\s+em\s+pares da lista\s+([a-zA-Z_]\w*)',
        r'for \1 in [{"chave": k, "valor": v} for k, v in \2.items()]:',
        codigo
    )
    codigo = codigo.replace('par.chave', 'par["chave"]')
    codigo = codigo.replace('par.valor', 'par["valor"]')
    codigo = codigo.replace('fim para cada', '')

    # Listas normais (só strings)
    codigo = re.sub(
        r'criar lista\s+([a-zA-Z_]\w*)\s+com\s+((?:"[^"]*"(?:\s*,\s*"[^"]*")*))',
        r'\1 = [\2]',
        codigo
    )

    # Listas de números
    codigo = re.sub(
        r'criar lista de numeros\s+([a-zA-Z_]\w*)\s+com\s+((?:\d+(?:\.\d+)?(?:\s*,\s*\d+(?:\.\d+)?)*))',
        r'\1 = [\2]',
        codigo
    )

    # Listas mista (de coisas)
    codigo = re.sub(
        r'criar lista de coisas\s+([a-zA-Z_]\w*)\s+com\s+(.+?)(?=\s*(?:\n|$))',
        r'\1 = [\2]',
        codigo,
        flags=re.DOTALL
    )

    # Adicionar a lista normais
    codigo = re.sub(
        r'adicionar\s+"([^"]*)"\s+a lista\s+([a-zA-Z_]\w*)',
        r'\2.append("\1")',
        codigo
    )

    # Listas associativas
    codigo = re.sub(
        r'criar lista\s+([a-zA-Z_]\w*)\s+com\s+((?:"[^"]*"\s*-\s*(?:"[^"]*"|\d+(?:\.\d+)?|verdadeiro|falso)\s*(?:,\s*(?:"[^"]*"\s*-\s*(?:"[^"]*"|\d+(?:\.\d+)?|verdadeiro|falso)\s*)*))',
        lambda m: f'\1 = {{{m.group(2).replace(" - ", ": ")}}}',
        codigo,
        flags=re.DOTALL
    )

    # Valor da chave (sem fallback)
    codigo = re.sub(
        r'valor da chave\s+"([^"]*)"\s+da lista\s+([a-zA-Z_]\w*)(?!\s+ou)',
        r'\2.get("\1", None)',
        codigo
    )

    # Valor da chave com fallback
    codigo = re.sub(
        r'valor da chave\s+"([^"]*)"\s+ou\s+([^,]+?)\s+da lista\s+([a-zA-Z_]\w*)',
        r'\3.get("\1", \2)',
        codigo
    )

    # Chaves com valor X
    codigo = re.sub(
        r'chaves com valor\s+([^,]+?)\s+da lista\s+([a-zA-Z_]\w*)',
        r'[k for k, v in \2.items() if v == \1]',
        codigo
    )

    # Se lista tem chave "X"
    codigo = re.sub(
        r'se lista\s+([a-zA-Z_]\w*)\s+tem chave\s+"([^"]*)"\s+então',
        r'if "\2" in \1:',
        codigo
    )

    # Ordenar por chaves / valores
    codigo = re.sub(
        r'ordenar lista\s+([a-zA-Z_]\w*)\s+por chaves',
        r'\1 = dict(sorted(\1.items(), key=lambda item: item[0]))',
        codigo
    )
    codigo = re.sub(
        r'ordenar lista\s+([a-zA-Z_]\w*)\s+por valores',
        r'\1 = dict(sorted(\1.items(), key=lambda item: item[1]))',
        codigo
    )

    # Remover chave (uma ou múltiplas) - seguro
    codigo = re.sub(
        r'remover chave\s+((?:"[^"]*"(?:,\s*"[^"]*")*))\s+da lista\s+([a-zA-Z_]\w*)',
        lambda m: '; '.join([f'if "{k.strip('"')}" in {m.group(2)}: del {m.group(2)}["{k.strip('"')}"]' for k in m.group(1).split(',')]),
        codigo
    )

    # Remover valor (pôr None) - seguro
    codigo = re.sub(
        r'remover valor com chave\s+((?:"[^"]*"(?:,\s*"[^"]*")*))\s+da lista\s+([a-zA-Z_]\w*)',
        lambda m: '; '.join([f'if "{k.strip('"')} " in {m.group(2)}: {m.group(2)}["{k.strip('"')}"] = None' for k in m.group(1).split(',')]),
        codigo
    )

    # Aumenta / diminui
    codigo = re.sub(
        r'aumenta\s+([a-zA-Z_]\w*)\s+em\s+(.+)',
        r'\1 += \2',
        codigo
    )
    codigo = re.sub(
        r'diminui\s+([a-zA-Z_]\w*)\s+em\s+(.+)',
        r'\1 -= \2',
        codigo
    )

    # Dorme
    codigo = re.sub(
        r'dorme\s+(\d+)\s+segundos',
        r'import time; time.sleep(\1)',
        codigo
    )

    # Escolhe aleatorio
    codigo = re.sub(
        r'escolhe aleatorio entre\s+(\d+)\s+e\s+(\d+)\s+guarda em\s+([a-zA-Z_]\w*)',
        r'import random; \3 = random.randint(\1, \2)',
        codigo
    )

    # Verificação de estrutura
    linhas = codigo.strip().split('\n')
    if not linhas or linhas[0].strip() != "Bora":
        print("Erro: O programa deve começar com 'Bora'")
        return

    if not linhas or linhas[-1].strip() != "Oh desligou!":
        print("Erro: O programa deve terminar com 'Oh desligou!'")
        return

    corpo = '\n'.join(linhas[1:-1])
    python_code = f"""if __name__ == "__main__":
{corpo}
"""

    print("\n" + "="*50)
    print("CÓDIGO PYTHON GERADO:")
    print("="*50)
    print(python_code.strip())
    print("="*50)
    print("\nA executar...\n")

    try:
        exec(python_code, globals())
    except Exception as e:
        print(f"Erro ao executar: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            codigo = f.read()
        interpretar_pytuga(codigo)
    else:
        print("Cole o teu código PyTuga abaixo (Ctrl+D ou Ctrl+Z para terminar):")
        codigo = sys.stdin.read()
        interpretar_pytuga(codigo)
