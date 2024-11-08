# Funções de uso geral no aplicativo

def remove_prefixo(d):
    """
    Remove o prefixo das chaves de um dicionário.
    :param d: dicionário original com prefixo nas chaves
    :return: novo dicionário com as chaves sem o prefixo
    """
    # Obtém o prefixo a partir da primeira chave do dicionário
    first_key = next(iter(d))
    prefix = first_key.split('_')[0] + '_'

    # Cria um novo dicionário com as chaves sem o prefixo
    new_dict = {key[len(prefix):]: value for key, value in d.items()}
    return new_dict
