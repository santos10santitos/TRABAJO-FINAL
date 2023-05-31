
#Esta algo inspirada en un algoritmo pero no se me ocurrio mucho y tuve que investigar :C 
def ordenamientobinario(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            left = mid
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    arr.insert(left, target)


def binariosimprimir(arr):
    sorted_arr = []
    for num in arr:
        ordenamientobinario(sorted_arr, num)
        print("Paso:", sorted_arr)

    return sorted_arr


# Ejemplo de uso
numeros = [16, 4, 10, 6, 8, 14, 2, 20, 12, 18, 23, 12, 43, 41]

print("Lista original:", numeros)
print()

numeros_ordenados = binariosimprimir(numeros)

print()
print("Lista ordenada:", numeros_ordenados)