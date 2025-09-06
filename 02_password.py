SECRET = "13"  # ← тут меняешь пароль на любой текст

pwd = input("Введите пароль: ").strip()
if pwd == SECRET:
    print("Доступ разрешён")
else:
    print("Неверный пароль")
