# решето Эратосфена (алгоритм простых чисел), проверка на то, является ли число простым/составным в послед-ти до N
# вопрос по 8 строке

N = int(input())
A = [True] * N   # создаем массив длиной N 
A[0] = A[1] = False   # убираем для целей цикла 0 и 1
for k in range(2,N):
    if A[k]:  # подразумевается, если A[k] - True (простое)
        for m in range(2*k, N, k):
            A[m] = False
for k in range(N):
    print(k,'-', 'простое' if A[k] else 'составное')  # тернарный оператор
    
    