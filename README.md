Установка:
    # Создайте виртуальное окружение
      uv venv

      # Активируйте его
      source .venv/bin/activate  # Linux/Mac
      # или
      .venv\Scripts\activate     # Windows

      
Методы:
    insert(key, value)	Вставляет элемент	tree.insert(10, "A")
    search(key)	Ищет элемент	tree.search(10) → "A"
    delete(key)	Удаляет элемент	tree.delete(10)
    height()	Возвращает высоту	tree.height() → 3
    is_balanced()	Проверяет баланс	tree.is_balanced() → True

Использование:

    # Создание дерева
    tree = BinarySearchTree()

    # Вставка элементов
    tree.insert(10, "десять")
    tree.insert(5, "пять")
    tree.insert(15, "пятнадцать")

    # Поиск
    print(tree.search(10))  # "десять"
    print(tree.search(99))  # None

    # Удаление
    tree.delete(5)

    # Высота дерева
    print(f"Высота: {tree.height()}")

    # Проверка баланса
    print(f"Сбалансировано: {tree.is_balanced()}")


  Запустить тесты:
    uv run pytest tests/ -v