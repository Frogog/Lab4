import streamlit as st
import pandas as pd
from names import ports_names

df = pd.read_csv("../Lab4/data.csv", encoding="utf-8")


st.image("1_1300734.jpg")
st.title("Вариант №2: Данные пассажиров титаника")
st.write("Для просмотра данных о выживших и умерших пассажирах выберите соответствующий пункт посадки")

port = st.selectbox(
"Выберите пункт посадки:",
("Пункт посадки не выбран",'Саутгемптон', 'Квинстаун', 'Шербур')
)

def port_survival_stat (port_name):
    statistic = {
        'Спасенные': [0],
        'Умершие': [0]
    }
    results = pd.DataFrame(statistic)
    if port_name in ports_names:
        st.header("Статистика по пункту посадки "+port_name)
        statistic["Спасенные"] = [len(df[(df["Embarked"] == ports_names[port_name]) & (df["Survived"] == 1)])]
        statistic["Умершие"] = [len(df[(df["Embarked"] == ports_names[port_name]) & (df["Survived"] == 0)])]
        results = pd.DataFrame(statistic)

    return results

st.dataframe(port_survival_stat(port))