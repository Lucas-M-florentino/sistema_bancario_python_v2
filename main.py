import textwrap
def menu():
  
  menu = """
  ============== MENU ===============

  [d]\tDepositar
  [s]\tSacar
  [e]\tExtrato
  [nu]\tNovo usuário
  [nc]\tNova conta
  [lu]\tListar usuários
  [lc]\tListar contas
  [q]\tSair

  ->"""
  return input(menu)

# receber os argumentos apenas por posição
def depositar(saldo, valor, extrato, /):
  if valor > 0:
    # digitar a conta
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    print("\n=== Depósito realizado com sucesso! ===")
  else:
    print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
  return saldo, extrato
  
# receber argumentos apenas por nome
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
  excedeu_saldo = valor > saldo
  excedeu_limite = valor > limite
  excedeu_saques = numero_saques >= limite_saques

  if excedeu_saldo:
    print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
  elif excedeu_limite:
    print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
  elif excedeu_saques:
    print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
  elif valor > 0:
    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    numero_saques += 1
    print("\n=== Saque realizado com sucesso! ===")
  else:
    print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
  return saldo, extrato

def extrato(saldo, /, *, extrato):
  print("\n================ EXTRATO ================")
  print("Não foram realizadas movimentações." if not extrato else extrato)
  print(f"\nSaldo: R$ {saldo:.2f}")
  print("=========================================")

  
# Criar conta Corrente
## O programa deve armazenar contas em uma lista, uma conta é composta por: agência, nro. da conta, nome do usuário. O número da conta é sequencial iniciando em 1. O número da agência é fixo: '0001'. O usuário pode ter mais de uma conta, mas uma conta pode ter apenas um usuário.
def criar_usuario(usuarios):
  cpf = input("Informe o CPF (somente número): ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("\n@@@ Já existe usuário com esse CPF! @@@")
    return

  nome = input("Informe o nome completo: ")
  data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
  endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

  usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

  print("=== Usuário criado com sucesso! ===")

# Para vincular um usuário a uma conta filtre a lista de usuários buscando o número de CPF informado para cada usuário da lista.
def filtrar_usuario(cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None

# Criar Usuário
## O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, CPF e endereço. O endereço é uma string contendo o logradouro, o nro, o bairro, a cidade/sigla do estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.
def criar_conta(agencia, numero_conta, usuarios):
  cpf = input("Informe o CPF do usuário: ")
  usuario = filtrar_usuario(cpf, usuarios)

  if not usuario:
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    return

  print("\n=== Conta criada com sucesso! ===")
  return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

def listar_usuarios(usuarios):
  for usuario in usuarios:
    linha = f"""\
      Nome: {usuario['nome']}
      Data de nascimento: {usuario['data_nascimento']}
      CPF: {usuario['cpf']}
      Endereço: {usuario['endereco']}
    """
    print("=" * 100)
    print(textwrap.dedent(linha))

def listar_contas(contas):
  for conta in contas:
    linha = f"""\
      Agência:\t{conta['agencia']}
      C/C:\t\t{conta['numero_conta']}
      Titular:\t{conta['usuario']['nome']}
    """
    print("=" * 100)
    print(textwrap.dedent(linha))


def main():
  LIMITE_SAQUES = 3
  AGENCIA = "0001"

  saldo = 0
  limite = 500
  extrato = ""
  numero_saques = 0
  usuarios = []
  contas = []

  while True:
    opcao = menu()

    if opcao == "d":
      valor = float(input("Informe o valor do depósito: "))
      saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
      valor = float(input("Informe o valor do saque: "))
      saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
      extrato(saldo, extrato=extrato)

    elif opcao == "nu":
      criar_usuario(usuarios)

    elif opcao == "nc":
      conta = criar_conta(AGENCIA, len(contas) + 1, usuarios)
      if conta:
        contas.append(conta)

    elif opcao == "lu":
      listar_usuarios(usuarios)

    elif opcao == "lc":
      listar_contas(contas)

    elif opcao == "q":
      break

    else:
      print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
  main()