from main import port_survival_stat
import pandas as pd

def test_type_of_survival_stat():
    # arrange
    port = "Саутгемптон"
    expected = type(pd.DataFrame())

    # act
    actual = type(port_survival_stat(port))

    # assert
    assert expected == actual

def test_columns_survival_stat():
    # arrange
    port = "Саутгемптон"
    expected = ["Спасенные", "Умершие"]

    # act
    actual = list(port_survival_stat(port).columns)

    # assert
    assert expected == actual

def test_right_port_survival_stat():
    # arrange
    port = "Саутгемптон"
    expected = pd.DataFrame({
        "Спасенные" :[217],
        "Умершие" : [427]
    })

    # act
    actual = port_survival_stat(port)

    # assert
    assert expected.equals(actual)

def test_wrong_port_survival_stat():
    # arrange
    port = "Лондон"
    expected = pd.DataFrame({
        "Спасенные": [0],
        "Умершие": [0]
    })

    # act
    actual = port_survival_stat(port)

    # assert
    assert expected.equals(actual)