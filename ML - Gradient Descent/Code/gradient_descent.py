#! python3

x = [60, 63, 65, 70, 70, 70, 80, 90, 80, 80, 85, 89, 90, 90, 90, 90, 94, 100, 100, 100]
y = [1, 0, 1, 2, 5, 1, 4, 6, 2, 3, 5, 4, 6, 8, 4, 5, 7, 9, 7, 6]

def gradient_descent(m_now, b_now, learning_rate):
    m_gradient = sum(y) / sum(x)
    b_gradient = (max(y) - min(y)) / (max(x) - min(x))

    n = len(x) 

    for i in range(n):
        x_1 = x[i]
        y_1 = y[i]

        m_gradient += -(2/n) * x_1 * (y_1 - (m_now * x_1 + b_now))
        b_gradient += -(2/n) * (y_1 - (m_now * x_1 + b_now))

    m = m_now - m_gradient * learning_rate
    b = b_now - b_gradient * learning_rate
    return m, b


m = 0
b = 0
L = 0.0001
epochs = 100000

for i in range(epochs):
    m, b = gradient_descent(m, b, L)


print(f'The slope is {m}.\nThe intercept is {b}\nTHe value of blood pressure for 97db is {(m*97+b)}.')    