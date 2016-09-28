import pickle

def save(val, identifier):
    """
    save variable into a file
    :param val: the val you want to save
    :param identifier: str. the identifier of variable
    :return: bool. status of save
    """
    try:
        output = open('data/pickle/' + identifier + '.pkl', 'wb')
        pickle.dump(val, output)
        output.close()
        return True
    except:
        return False


def get(identifier):
    """
    get variable from a file
    :param identifier: str. the identifier of variable
    :return: variable
    """
    pkl_file = open('data/pickle/' + name + '.pkl', 'rb')
    data = pickle.load(pkl_file)
    pkl_file.close()
    return data