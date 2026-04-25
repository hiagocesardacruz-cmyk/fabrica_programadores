programa {
  funcao inicio() {
    real peso, altura, imc
    real divisao
    real multiplicacao
    cadeia nome
    escreva("Digite o seu nome: ")
    leia(nome)
    escreva("Digite o seu peso: ")
    leia(peso)
    escreva("Digite a sua altura: ")
    leia(altura)
    imc = peso / (altura * altura)
    escreva("---Bem vindo---", nome)
    escreva("\n O resultadodo seu imc é:" , imc)

    
  }
}
