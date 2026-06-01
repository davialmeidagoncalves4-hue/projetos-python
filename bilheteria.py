#aluno1: formato nome do filme
def formatar (nome):
    return nome.uper()
#aluno2: verificaçao de acesso
def verificador (idade):
    if idade >=18:
        return "autorizado"
 else:
        return "não autorizado"
#aluno3:mensagem de retorno 
def gerar_mensagem (status)
if status == "autorizado"
     return "tenha uma otims sessão"
else:
    return "Sinto muito, idade não autorizada"
#aluno4: integrador do projeto 
nome_filme = input ("Digite o nome do filme:")
idade_filme = int(input("Digite sua idade:"))
idade_filme = formatar (nome_filme)
status_final = verificador (idade_filme)
mensagem = gerar-mensagem(status_final)
print(f"\nfilme:{filme}")
Print(f"status:{status_final}")
print(f"aviso:{mensagem}")