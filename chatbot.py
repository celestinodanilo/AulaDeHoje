import random


def saudacoes(nome):
    frases = [
        f"Bom dia! Meu nome é {nome}. Como vai você?",
        "Olá!",
        "Oi, tudo bem?"
    ]
    print(frases[random.randint(0, 2)])


def recebeTexto():
    resposta = input("Cliente: ")
    palavrasProibidas = ["bocó"]
    for p in palavrasProibidas:
        if p in resposta.lower():
            print("Não vem não! Me respeite!")
            return recebeTexto()
    return "Cliente: " + resposta


def buscaResposta(nome, texto):
    pergunta = texto.strip()

    # Verifica despedida ANTES de mexer no arquivo,
    # assim funciona mesmo que a base esteja vazia/curta
    if texto.replace("Cliente: ", "").strip().lower() == "tchau":
        return "fim"

    with open("BaseDeConhecimento.txt", "a+", encoding="utf-8") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()

            if viu == "":
                # chegou ao fim do arquivo e não achou a pergunta
                print("Me desculpe, não sei o que falar")
                resposta_user = input("O que esperava?\n")
                conhecimento.write("\n" + pergunta)
                conhecimento.write("\n" + "Chatbot: " + resposta_user)
                # já responde com o que acabou de aprender
                return "Chatbot: " + resposta_user

            if viu.strip() == pergunta:
                proximalinha = conhecimento.readline().strip()
                # comparação sem diferenciar maiúsc/minúsc (Chatbot / ChatBot)
                if proximalinha.lower().startswith("chatbot:"):
                    resposta = proximalinha.split(":", 1)[1].strip()
                    return "Chatbot: " + resposta
                # se a linha seguinte não for uma resposta válida,
                # continua procurando a partir da próxima linha


def exibeResposta(resposta, nome):
    if resposta == "fim":
        print(nome + ": volte sempre!")
        return "fim"
    print(resposta.replace("Chatbot", nome))
    return "continua"


if __name__ == "__main__":
    nome_maquina = "Maria"
    saudacoes(nome_maquina)
    while True:
        texto = recebeTexto()
        resposta = buscaResposta(nome_maquina, texto)
        if exibeResposta(resposta, nome_maquina) == "fim":
            break