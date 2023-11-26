import pytest
from codigo2 import obter_senha, salvar_senha_encriptada, obter_senha_encriptada, verificar_senha

# Fixture para obter a senha do arquivo
@pytest.fixture
def senha_fixture():
    return obter_senha()

# Fixture para salvar a senha encriptada
@pytest.fixture
def senha_encriptada_fixture(senha_fixture):
    salvar_senha_encriptada(senha_fixture)
    return obter_senha_encriptada()

# Teste para verificar se a senha é correta
def test_verificar_senha(senha_fixture, senha_encriptada_fixture):
    assert verificar_senha(senha_fixture, senha_encriptada_fixture)

# Teste para verificar se a função interna com assert funciona corretamente
def test_verificar_senha_internamente(senha_fixture, senha_encriptada_fixture):
    verificar_senha_internamente(senha_fixture, senha_encriptada_fixture)

# Teste para verificar que a senha encriptada não é igual à senha original
def test_senha_encriptada_diferente(senha_fixture, senha_encriptada_fixture):
    senha_encriptada = obter_senha_encriptada()
    assert senha_fixture != senha_encriptada

# Adicione mais testes conforme necessário

# Main
if __name__ == "__main__":
    pytest.main()