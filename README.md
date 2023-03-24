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
5. Wybranie nakrótszy iloczyn z mfa
6. Utworzenie rodziny $A_1 \times A_2 \times ... \times A_p$ podzbiorów:
$$\textbullet \quad A_1=W_{i_1}, \quad W_{i_p} \backslash \left(\bigcup_{i=1}^{p-1}A_i\right),\quad p=\overline{2,\textbf{P}}$$
7. Optymalne pokolorowanie:
$$\textbullet \quad f^*(x)=p\Leftrightarrow x\in A_p, p=\overline{1,\textbf{P}}\\text{ gdzie P - liczba chromatyczna grafu}$$
$$\\text{(minimalna liczba kolorów jaką można pokolorować graf).}$$

### Przypisy
