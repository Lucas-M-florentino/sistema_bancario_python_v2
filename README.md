# 💰 Desafio: Sistema Bancário em Python

Este projeto implementa um sistema bancário básico em Python, onde o usuário pode realizar operações como depósito, saque, visualizar extrato, criar novos usuários e contas, listar usuários e contas, além de sair da aplicação. O sistema também inclui validações de limite de saques diários e saldo disponível.

## 🚀 Funcionalidades

- **Depósito**: O usuário pode realizar depósitos em sua conta.
- **Saque**: Limite de 3 saques diários, com valor máximo de R$ 500 por operação.
- **Extrato**: Exibe o histórico de transações realizadas, incluindo depósitos e saques, além do saldo atual.
- **Criação de Usuário**: Permite cadastrar novos usuários com CPF único.
- **Criação de Conta**: Associa um novo usuário a uma conta bancária.
- **Listar Usuários**: Exibe a lista de todos os usuários cadastrados no sistema.
- **Listar Contas**: Mostra todas as contas criadas com seus respectivos titulares.
- **Limitações**: Não é possível sacar mais do que o saldo disponível na conta.

## 🛠️ Como o Sistema Funciona

Ao iniciar o programa, o usuário verá um menu com as seguintes opções:

```bash
[d]   Depositar
[s]   Sacar
[e]   Extrato
[nu]  Novo usuário
[nc]  Nova conta
[lu]  Listar usuários
[lc]  Listar contas
[q]   Sair
```

1. Depósito (d): Permite que o usuário deposite um valor positivo na conta. Se o valor inserido for inválido (menor ou igual a zero), a operação será cancelada.

2. Saque (s): Limite de 3 saques por dia, com valor máximo de R$ 500 por operação. Se o saldo for insuficiente, o saque não será permitido.

3. Extrato (e): Exibe o histórico de todas as transações realizadas (depósitos e saques) e o saldo atual da conta. Se não houver transações, uma mensagem indicará que não houve movimentações.

4. Novo Usuário (nu): Cadastra um novo usuário no sistema solicitando CPF, nome completo, data de nascimento e endereço.

5. Nova Conta (nc): Cria uma nova conta bancária associada a um usuário já cadastrado.

6. Listar Usuários (lu): Exibe todos os usuários cadastrados, mostrando nome, CPF, data de nascimento e endereço.

7. Listar Contas (lc): Mostra todas as contas criadas, incluindo o número da agência, número da conta e o nome do titular.

8. Sair (q): Encerra o programa.

# 💻 Exemplo de Uso
```bash
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo usuário
[nc] Nova conta
[lu] Listar usuários
[lc] Listar contas
[q] Sair

Escolha uma opção: nu
Informe o CPF (somente números): 12345678900
Informe o nome completo: João Silva
Informe a data de nascimento (dd-mm-aaaa): 10-04-1980
Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): Rua das Flores, 123 - Centro - São Paulo/SP
Usuário criado com sucesso!

Escolha uma opção: nc
Informe o CPF do usuário: 12345678900
Conta criada com sucesso!

Escolha uma opção: d
Informe o valor do depósito: 200
Depósito realizado com sucesso!

Escolha uma opção: s
Informe o valor do saque: 100
Saque realizado com sucesso!
Saques restantes: 2

Escolha uma opção: e
Extrato
----------------------
Depósito: + R$ 200.00
Saque: - R$ 100.00
----------------------
Saldo: R$ 100.00
----------------------
```

# 📜 Instruções de Execução
1. Clone este repositório:
```bash
git clone https://github.com/Lucas-M-florentino/sistema_bancario_python_v2.git
```
2. Navegue até o diretório do projeto:

```bash
cd sistema_bancario_python_v2
```
3. Execute o script:
```bash
python3 sistema_bancario.py
```
# 📋 Regras de Negócio
- Um usuário pode ter várias contas, mas uma conta só pode ter um titular.
- O número máximo de saques diários é de 3 por conta.
- O valor máximo permitido por saque é de R$ 500,00.
- Não é possível cadastrar dois usuários com o mesmo CPF.
- O saldo da conta deve ser suficiente para realizar um saque.