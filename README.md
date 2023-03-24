# Analiza algorytmów rozwiązujących problem kolorowania wierzchołków grafu

### Opis programu
Program pomaga w określeniu złożoności algorytmu dokładnego, oraz algorytmu heurystycznego LF (Large First) kolorowania wierzchołków grafu, podając czasy działania dla zadanych danych wejściowych.

### Kroki alogrytmu dokładnego
1. Wyznaczenie wszystkich maksymalnych zbiorów wewnętrznie stabilnych \[[1](#przypisy)\]:

$$W_1, W_2, ..., W_k$$

2. Utworzenie macierzy $B=[b_{ij}]_{n \times K}$ gdzie:            

$$\textbullet \quad b_{ij}=\\begin{cases} 1,\\; gdy \quad w_i \in W_j \\\ 0,\\; gdy \quad w_i \notin W_j \end{cases} \quad w_i - i \\text{-ty wierzchołek grafu}$$

3. Dla zmiennych binarnych $v_j(j=\overline{1,K})$ tworzony jest WAK \[[2](#przypisy)\] gdzie:

$$\textbullet \quad v_{j}=\\begin{cases} 1,\\;  j-ty \\; zbiór \\; wewn. \\; stab. \\; należy \\; do \\; pokrycia \\\ 0,\\;  w \\; przeciwnym \\; wypadku \\end{cases}$$

$$\textbullet \quad \prod_{i=1}^n \sum_{j=1}^K b_{ij} \times v_i \Leftrightarrow \\text{Pokrycie elementów zbioru wierzchołków grafu G}$$

$$\\text{przez elementy zbiorów wewnętrznie stabilnych.}$$

4. Przekształcenie WAK do postaci mfa\[[3](#przypisy)\]:

$$ \sum_r\prod^r(v^K) $$

5. Wybranie nakrótszego iloczynu z mfa
6. Utworzenie rodziny $A_1 \times A_2 \times ... \times A_p$ podzbiorów:

$$\textbullet \quad A_1=W_{i_1}, \quad W_{i_p} \backslash \left(\bigcup_{i=1}^{p-1}A_i\right),\quad p=\overline{2,\textbf{P}}$$

7. Optymalne pokolorowanie:

$$\textbullet \quad f^*(x)=p\Leftrightarrow x\in A_p, p=\overline{1,\textbf{P}}\\text{ gdzie P - liczba chromatyczna grafu}$$

$$\\text{(minimalna liczba kolorów jaką można pokolorować graf).}$$


### Kroki alogrytmu heurystycznego LF (Largest First)
1. Uporządkowanie wierzchołków grafu malejąco według ich stopnia
2. Kolorowanie wierzchołków zachłannie zgodnie z ustaloną kolejnością <br />
    2.1 Wybranie wierzchołka<br />
    2.2 Sprawdzenie wszystkich sąsiadujących wierzchołków <br />
    2.3 Wykreślenie koloru który został już użyty<br />
    3.4 Wybranie dostępnego koloru

### Złożoności czasowe

Zakładając wielkości danych wejściowych jako:

$$\textbullet \quad n \\text{ - liczba krawędzi,}$$

$$\textbullet \quad m \\text{ - liczba wierzchołków.}$$

<br />

Teoretyczna pesymistyczna złożoność czasowa **algorytmu dokładnego** w ogólności wyniosła:
$$O \left(n+n^2+n+nlogn+m+2n+n^2+n+2^n \times n+2^n \times 2^n+2^n+m \times 2^n+m^2+m+2^nlog2^n+2^n+m*2^{n-1}+{1 \over 8}m^2+{5 \over 4}m+m+{1 \over 4}(m^2+2m) \right)$$

Natomiast po uproszczeniu:
$$O(2^{2n}+m*2^n+m^2)$$

<br />

Teoretyczna pesymistyczna złożoność czasowa **algorytmu heurystycznego** w ogólności wyniosła:
$$O \left(m+n+mlogm+m+m \times (m-1)+{m \times (m+1) \over 2} \right)$$

Natomiast po uproszczeniu:
$$O(m^2+n)$$

<br />

<br />

Okazuje się, że analiza działania algorytmów i zmierzone czasy, odpowiadają obliczonym wartościom.
<br />
<p align="center">
<kbd><img style="border:1px solid black;" src="https://github.com/k-golen/algorithm-analysis/blob/main/images/alg_dokladny.jpg?raw=true"/></kbd>
</p>

<sub> Rysunek 1. Czasy wykonywania algorytmu dokładnego przy pesymistycznych danych wejściowych. </sub>

<br />

Istnieją takie stałe parametry, które przy dodaniu do obliczonej złożoności, pozwalają ograniczyć zmierzone czasy od góry oraz od dołu. Oznacza to, że pesymistyczna złożoność czasowa **algorytmu dokładnego** została prawdopodobnie wyznaczona poprawnie.

<br />

<br />

<p align="center">
<kbd><img src="https://github.com/k-golen/algorithm-analysis/blob/main/images/alg_heurystyczny.jpg?raw=true" /></kbd>
</p>

<sub> Rysunek 2. Czasy wykonywania algorytmu heurystycznego przy losowych danych wejściowych. </sub>

<br />

Podobnie jak w poprzednim algorytmie, tutaj także istnieje możliwość wyznaczenia górnej i dolnej granicy. Co także oznacza, że pesymistyczna złożoność czasowa **algorytmu heurystycznego** została prawdopodobnie wyznaczona poprawnie.

### Przypisy

1. Zbiór wewnętrznie stabilny, to zbiór wierzchołków grafu $G$, które tworzą podgraf pusty grafu $G$.
2. WAK - Wyrażenie Alternatywno-Koniunkcyjne opisywane jako $\prod\sum$ np.: $(x_1+x_2)\times(x_2+x_3)$
3. mfa - minimalna formuła alternatywna opisywana jako $\sum\prod$ np.: (przekształcenie z przypisu 2)  $(x_1+x_2)\times(x_2+x_3)=x_2+(x_1\times x_3)$
