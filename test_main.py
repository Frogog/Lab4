from main import port_survival_stat
import pandas as pd

def test_type_of_survival_stat():
    # arrange
    port = "Саутгемптон"
    data = pd.DataFrame({
        'Survived': [1, 0, 1, 1],
        'Embarked': ["S", "S", "Q", "C"]

    })
    expected = type(pd.DataFrame())

    # act
    actual = type(port_survival_stat(port, data))

    # assert
    assert expected == actual

def test_columns_survival_stat():
    # arrange
    port = "Саутгемптон"
    data = pd.DataFrame({
        'Survived': [1, 0, 1, 1],
        'Embarked': ["S", "S", "Q", "C"]

    })
    expected = ["Спасенные", "Умершие"]

    # act
    actual = list(port_survival_stat(port, data).columns)

    # assert
    assert expected == actual

def test_right_port_survival_stat():
    # arrange
    port = "Саутгемптон"
    data = pd.DataFrame({
        'Survived': [1, 0, 1, 1],
        'Embarked': ["S", "S", "Q", "C"]

    })
    expected = pd.DataFrame({
        "Спасенные" :[1],
        "Умершие" : [1]
    })

    # act
    actual = port_survival_stat(port, data)

    # assert
    assert expected.equals(actual)

def test_wrong_port_survival_stat():
    # arrange
    port = "Лондон"
    data = pd.DataFrame({
        'Survived': [1, 0, 1, 1],
        'Embarked': ["S", "S", "Q", "C"]

    })
    expected = pd.DataFrame({
        "Спасенные": [0],
        "Умершие": [0]
    })

    # act
    actual = port_survival_stat(port,data)

    # assert
    assert expected.equals(actual)