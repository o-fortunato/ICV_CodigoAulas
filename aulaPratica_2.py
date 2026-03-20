import math as m
import numpy as np

u = [32.15, 33.1, 34.05, 36.18, 38.85, 39.14,
        40.72, 42.83, 44.55, 45.91, 44.87, 44.02,
        43.65, 42.96, 42.05, 41.2]

w = [0.35, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0, 0, 0, 0,
        -0.05, -0.1, -0.15, -0.05, 0]

q = [0.05, 0.03, 0.03, 0.02, 0.02, 0.01, 0.01, 0.00, 0.00,
        0.00, 0.00, -0.06, -0.13, -0.19, -0.06, 0.00]

theta = [0.35, 0.36, 0.36, 0.36, 0.36, 0.37, 0.37, 0.37,
            0.37, 0.37, 0.37, 0.37, 0.36, 0.35, 0.33, 0.32]

#### EXERCICIO 1

def media(lista):
    return sum(lista) / len(lista)

def variancia(lista):
    m = media(lista)
    return sum((x - m) ** 2 for x in lista) / (len(lista) - 1)

def desvio_padrao(lista):
    return m.sqrt(variancia(lista))

cv_u = media(u) / desvio_padrao(u)
cv_w = media(w) / desvio_padrao(w)
cv_q = media(q) / desvio_padrao(q)
cv_theta = media(theta) / desvio_padrao(theta)

print(f"Coeficiente de variacao de x = (u w q theta)T: "
      f"[{cv_u:.4f}, {cv_w:.4f}, {cv_q:.4f}, {cv_theta:.4f}]\n")

#### EXERCICIO 2
r_theta_q = np.cov(theta, q)[0][1] / (desvio_padrao(theta) * desvio_padrao(q))
print(f"Coeficiente de correlacao entre theta e q: {r_theta_q:.4f}\n")

### EXERCICIO 3
x = np.array([u, w, q, theta])
cov_x = np.cov(x)
desvioPadrao = np.sqrt(np.diag(cov_x))
corr_x = cov_x / np.outer(desvioPadrao, desvioPadrao)
print(f"Matriz de correlacao de x = (u w q theta):\n{corr_x}\n")

### EXERCICIO 5
mean_x = np.array([media(u), media(w), media(q), media(theta)])
n = len(mean_x)
cv_global = np.sqrt((np.transpose(mean_x) @ np.linalg.inv(cov_x) @ mean_x) / n)

print(f"Coef de variacao global = {cv_global:.4f}")