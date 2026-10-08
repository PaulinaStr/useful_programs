# Główny Tytuł Dokumentu

## Pierwsza podsekcja

To jest krótki tekst w ramach pierwszej podsekcji. Pokazuje on podstawowe formatowanie tekstu, takie jak **pogrubienie**, *pochylenie* oraz ~~przekreślenie~~. 

W tym miejscu znajdują się również wzory matematyczne w tekście (inline):
- Pierwszy wzór: $E = mc^2$
- Drugi wzór: $a^2 + b^2 = c^2$
- Trzeci wzór: $f(x) = ax + b$

Oto lista punktowana z przydatnymi zasobami:
* Oficjalny edytor do notebooków: [Google Colab](http://colab.research.google.com)
* Dokumentacja języka Python
* Materiały edukacyjne

## Druga podsekcja

Oto krótki tekst w ramach kolejnej podsekcji, w której prezentujemy elementy strukturalne.

### Lista numerowana
1. Krok pierwszy: Przygotowanie środowiska.
2. Krok drugi: Uruchomienie kodu.
3. Krok trzeci: Analiza wyników.

### Checklista
- [x] Stworzenie dokumentu Markdown
- [x] Dodanie wzorów matematycznych
- [no] Weryfikacja wyglądu na GitHubie

### Tabela danych
| Nazwa zmiennej | Typ danych | Opis |
| :--- | :---: | :--- |
| `x` | `int` | Wartość wejściowa |
| `y` | `float` | Wynik obliczeń |
| `label` | `str` | Etykieta punktu |

### Blokowe wzory matematyczne (Display Math)

$$ \int_{a}^{b} f(x) \, dx = F(b) - F(a) $$

$$ \sum_{i=1}^{n} i = \frac{n(n+1)}{2} $$

$$ A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} $$

### Fragment kodu w języku Python

```python
def oblicz_pole_koła(promien):
    pi = 3.14159
    return pi * (promien ** 2)

wynik = oblicz_pole_koła(5)
print(f"Pole koła wynoszenie: {wynik}")
```

### Osadzony obrazek

![Wykres funkcji](wykres.png)
