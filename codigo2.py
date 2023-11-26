import hashlib

def obter_senha():
    with open("senha.txt", "r") as arquivo:
        return arquivo.read().strip()

def salvar_senha_encriptada(senha):
    senha_encriptada = hashlib.sha256(senha.encode()).hexdigest()
    with open("senha_encriptada.txt", "w") as arquivo:
        arquivo.write(senha_encriptada)

def obter_senha_encriptada():
    with open("senha_encriptada.txt", "r") as arquivo:
        return arquivo.read().strip()

def verificar_senha(senha_digitada, senha_encriptada):
    senha_encriptada_digitada = hashlib.sha256(senha_digitada.encode()).hexdigest()
    return senha_encriptada_digitada == senha_encriptada

def verificar_senha_internamente(senha_digitada, senha_encriptada):
    assert verificar_senha(senha_digitada, senha_encriptada)

def main():
    senha = obter_senha()
    salvar_senha_encriptada(senha)
    senha_encriptada = obter_senha_encriptada()
    senha_digitada = 'pedro1234'

    verificar_senha_internamente(senha_digitada, senha_encriptada)

if __name__ == "__main__":
    main()
