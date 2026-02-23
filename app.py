import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Калькулятор")

k = st.number_input("Введите k", value=0)
x_0 = st.number_input("Введите x_0", value=0)
x_1 = st.number_input("Введите x_1", value=0)
y_0 = st.number_input("Введите y_0", value=0)
y_1 = st.number_input("Введите y_1", value=0)
x_val = st.number_input("Введите x", value=0)

def f_left(x, k, y_0, x_0):
  return k*x + (y_0 - k*x_0)

def f_right(x, y_1, a, c):
  return y_1 - a/(x - c)

def draw_plot(x_left, y_left, x_right, y_right, x_0, x_1, y_0, y_1, x_val=None, y_val=None):
    fig = plt.figure(figsize=(8, 8))
    plt.title('График')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.plot(x_left, y_left)
    plt.plot(x_right, y_right)
    plt.axvline(x=x_0, color='red', linestyle='--', label='x_0')
    plt.axvline(x=x_1, color='red', linestyle='--', label='x_1')
    plt.axhline(y=y_0, color='blue', linestyle='--', label='y_0')
    plt.axhline(y=y_1, color='blue', linestyle='--', label='y_1')
    if x_val:
        plt.axvline(x=x_val, color='green', linestyle='--', label='x')
        plt.axhline(y=y_val, color='green', linestyle='--', label='y')
        plt.title('График с точкой')
    plt.grid(True)
    # plt.xticks([x_0, x_1])#, ['x_0', 'x_1'])
    # plt.yticks([y_0, y_1])#, ['y_0', 'y_1'])
    # plt.show()
    st.pyplot(fig)

@st.fragment
def show_plot():
    if st.button("Показать график"):
        if k*x_1 + (y_0 - k*x_0) >= y_1:
            st.write('Неккоректные значения параметров: значение линейной функции в точке x1 больше y1. Измените параметры')
        else:
          a = (y_1 - y_0 + k * (x_0 - x_1)) ** 2 / k
          c = (y_0 - y_1 - k * (x_0 - 2 * x_1)) / k
          x_left = np.linspace(0, x_1, 100)
          y_left = f_left(x_left, k, y_0, x_0)
          x_right = np.linspace(x_1, 3*x_1, 100)
          y_right = f_right(x_right, y_1, a, c)
          draw_plot(x_left, y_left, x_right, y_right, x_0, x_1, y_0, y_1)

@st.fragment
def show_value():
    if st.button("Рассчитать значение в точке"):
        if k*x_1 + (y_0 - k*x_0) >= y_1:
            st.write('Неккоректные значения параметров: значение линейной функции в точке x1 больше y1. Измените параметры')
        else:
          a = (y_1 - y_0 + k * (x_0 - x_1)) ** 2 / k
          c = (y_0 - y_1 - k * (x_0 - 2 * x_1)) / k
          x_left = np.linspace(0, x_1, 100)
          y_left = f_left(x_left, k, y_0, x_0)
          x_right = np.linspace(x_1, 3*x_1, 100)
          y_right = f_right(x_right, y_1, a, c)
          if x_val < x_1:
              y_val = k*x_val + (y_0 - k*x_0)
          else:
              y_val = y_1 - a/(x_val - c)
          draw_plot(x_left, y_left, x_right, y_right, x_0, x_1, y_0, y_1, x_val, y_val)
          st.write(f'Значение **y** в точке **x = {x_val}** равно **{y_val}**')


show_plot()
show_value()
