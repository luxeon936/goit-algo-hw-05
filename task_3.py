import timeit

# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1


    skip = {}

    for k in range(m - 1):
        skip[pattern[k]] = m - k - 1

    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            return i + 1
        k += skip.get(text[k], m)
    return -1


# Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    def build_lps(pattern):
        lps = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j
            else:
                if j != 0:
                    j = lps[j - 1]
                    i -= 1
                else:
                    lps[i] = 0
        return lps

    n = len(text)
    m = len(pattern)
    lps = build_lps(pattern)
    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = t = 0
    h = 1
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1

text1 = open("стаття 1.txt", "r", encoding="windows-1251").read()
text2 = open("стаття 2.txt", "r", encoding="windows-1251").read()

# Вибираємо підрядки
pattern_existing = "алгоритм"  # існуючий підрядок
pattern_non_existing = "неіснуючийпідрядок"  # неіснуючий підрядок

# Вимірювання часу виконання
def run_tests():
    for alg_name, alg in [("Алгоритм Боєра-Мура:", boyer_moore), ("Алгоритм Кнута-Морріса-Пратта:", kmp_search), ("Алгоритм Рабіна-Карпа:", rabin_karp)]:
        print(f"\n{alg_name}:")
        for text, text_name in [(text1, "Стаття 1"), (text2, "Стаття 2")]:
            print(f"\n{text_name}:")
            time_existing = timeit.timeit(lambda: alg(text, pattern_existing), number=100)
            time_non_existing = timeit.timeit(lambda: alg(text, pattern_non_existing), number=100)
            print(f"Час пошуку існуючого підрядка: {time_existing:.5f} сек")
            print(f"Час пошуку неіснуючого підрядка: {time_non_existing:.5f} сек")

if __name__ == "__main__":
    run_tests()