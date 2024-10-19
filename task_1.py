import heapq

def min_cost_to_connect_cables(cable_lengths):
    # Створюємо мін-купу зі списку довжин кабелів
    heapq.heapify(cable_lengths)
    total_cost = 0
    # Поки в купі більше ніж один елемент
    while len(cable_lengths) > 1:
        # Витягуємо два найкоротших кабелі
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths) 
        # Витрати на з'єднання цих двох кабелів
        cost = first + second
        total_cost += cost
        # Додаємо з'єднаний кабель назад до купи
        heapq.heappush(cable_lengths, cost)
    return total_cost

# Приклад використання
cable_lengths = [7, 1, 4, 3, 2, 6]
result = min_cost_to_connect_cables(cable_lengths)
print(f"Мінімальні витрати на з'єднання кабелів: {result}")
