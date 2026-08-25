from fastapi import APIRouter

router = APIRouter()


@router.get("/mensagem")
def mensagem():
    """Rota para uma mensagem de boas vindas"""
    return {"mensagem": "Olá mundo"}


# Query params: numero1 numero2
# http://localhost:8000/calculadora/somar?numero1=2&numero2=5
@router.get("/calculadora/somar")
def somar(numero1: int , numero2: int):
    soma = numero1 + numero2
    return {
        "resultado": soma
    }


# http://localhost:8000/calculadora/imc?peso=70&altura=1.50
@router.get("/calculadora/imc")
def calcular_imc(peso: float, altura: float):
    imc = peso / altura ** 2

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"

    return {
        "peso": peso,
        "altura": altura,
        "imc": round(imc, 2),
        "classificacao": classificacao
    }
# 0. Criar endpoint /concatenar
#       Recebe nome e sobrenome
#       Retorna o nome completo do usuário 
# 1. Criar endpoint /calcular/desconto
#       Recebe preco e percentual como query param
#       Calcular o valor do desconto
#       Retornar o preço, percentual, valor do desconto e valor com desconto
# 2. Criar endpoint /calcular/media
#       Recebe nota 1, nota 2, nota 3 e nota 4
#       Calcular a média
#       Retornar as notas e a média