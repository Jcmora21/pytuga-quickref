# PyTuga – A Linguagem de Programação Tuga Meme

PyTuga é uma linguagem de programação 100% portuguesa, criada por mim (**José Carlos (@Jcmora0201)**) nos Açores.  
Inspirada no BIRL, mas cheia de alma tuga: gírias do dia a dia, realidade show, funil, saudade açoriana e um grande “Bora lá pá!”.

É interpretada em Python e serve para aprender programação de forma clara e fácil.

**Última atualização:** Janeiro 2026  
**Versão atual:** 1.0 (cores RGB, rainbow degrade suave na frase inteira, listas normais e associativas, proteção contra erros, percorrer chaves/valores/pares, ordenação, remoção segura e mais)

## Como instalar e usar

1. Clona o repositório:
   ```bash
   git clone https://github.com/Jcmora0201/pytuga.git
   cd pytuga
   ```
   
2. como mostrar (print):
   ```pytuga
   mostrar ("Alguma coisa")
   ```
   
O texto sempre dentro de parênteses: ("...")

Sem cor especificada → branco padrão (255 255 255)

Cores pré-definidas (100% intensidade por default): vermelho, verde, azul, amarelo, branco, rosa, laranja, roxo

Se quiseres outra cor → usa formato RGB direto [R G B] entre 0 e 255. 
Ex.: 
  ```pytuga
  mostrar com cor [100 149 237]
  ```

Transparência/intensidade em % (opcional, depois da cor): 
Ex.:
  ```pytuga
  mostrar com cor [verde] a [70%] ("....")
  ```

Modificadores (negrito, sublinhado, fundo) antes da cor. Com cores respetivamente. 
Ex.: 
  ```pytuga
  mostrar negrito sublinhado fundo [azul] [255 234 0] [255 255 255] com cor [vermelho] a [85%] ("...") (negrito a azul | sublinhado a 255 234 0 | fundo a 255 255 255 | com cor da letra vermelho)
  ```
## Sintaxe Rápida
Início e fim:
```pytuga
  Bora
  //codigo aqui
  Oh desligou!
  ```
Variáveis:
  ```pytuga
  definir nome como "José Carlos"
  definir idade como 33
  definir altura como 1.75
  definir tem_bi como verdadeiro
  definir saldo como 45.50
  ```
Input:
  ```pytuga
  perguntar: ("Qual é o teu nome?") guardar em nome
  ```
Condições:
  ```pytuga
  se idade >= 18 então
    mostrar verde: ("Maior de idade!")
senão se idade >= 13 então
    mostrar amarelo: ("Adolescente!")
senão
    mostrar vermelho: ("Criança!")
então pronto
  ```
Ciclos Enquanto:
  ```pytuga
  definir cont como 0
enquanto cont < 5 
    mostrar str(cont)
    aumenta cont em 1
então acaba
  ```
Para cada (chaves / valores / pares):
   ```pytuga
   para cada chave em chaves da lista idades 
    mostrar chave
fim para cada

para cada valor em valores da lista idades 
    mostrar str(valor)
fim para cada

para cada par em pares da lista idades 
    mostrar par.chave + " tem " + str(par.valor) + " anos"
fim para cada
   ```
## Listas 
   ```pytuga
criar lista 
   ```
