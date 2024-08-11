import tkinter as tk
from tkinter import ttk, messagebox
from cryptography.fernet import Fernet
import os
import random
import base64

# Определение базового набора символов для символьного шифрования
base_charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+|-=/{}[]`~;:.,<>1234567890?"

# Папка для хранения ключей
KEY_FOLDER = "keys"
if not os.path.exists(KEY_FOLDER):
    os.makedirs(KEY_FOLDER)

# Функции шифрования и дешифрования
def simple_encrypt(text, key):
    if len(key) != len(base_charset):
        raise ValueError("Ключ шифрования некорректной длины.")
    result = []
    for char in text:
        if char in base_charset:
            result.append(key[base_charset.index(char)])
        elif char == '\n':
            result.append('\n')
        else:
            raise ValueError(f"Недопустимый символ в данных: {char}")
    return "".join(result)

def simple_decrypt(text, key):
    if len(key) != len(base_charset):
        raise ValueError("Ключ шифрования некорректной длины.")
    result = []
    for char in text:
        if char in key:
            result.append(base_charset[key.index(char)])
        elif char == '\n':
            result.append('\n')
        else:
            raise ValueError(f"Недопустимый символ в данных: {char}")
    return "".join(result)

def fernet_encrypt(text, key):
    try:
        cipher_suite = Fernet(key.encode())  # Преобразование ключа в байты
        return cipher_suite.encrypt(text.encode()).decode()
    except ValueError:
        raise ValueError("Ошибка шифрования: Некорректный ключ Fernet.")

def fernet_decrypt(text, key):
    try:
        cipher_suite = Fernet(key.encode())  # Преобразование ключа в байты
        return cipher_suite.decrypt(text.encode()).decode()
    except ValueError:
        raise ValueError("Ошибка дешифрования: Некорректный ключ Fernet.")

def generate_key():
    selected_algorithm = algorithm_choice.get()
    if selected_algorithm == "Simple":
        shuffled_charset = list(base_charset)
        random.shuffle(shuffled_charset)
        key = "".join(shuffled_charset)
    elif selected_algorithm == "Fernet":
        key = Fernet.generate_key().decode()
    key_output.delete("1.0", tk.END)
    key_output.insert(tk.END, key)

def save_key():
    key = key_output.get("1.0", tk.END).strip()
    key_name = key_name_entry.get().strip()
    if not key_name:
        messagebox.showerror("Ошибка", "Имя ключа не может быть пустым.")
        return
    if not os.path.exists(KEY_FOLDER):
        os.makedirs(KEY_FOLDER)
    key_path = os.path.join(KEY_FOLDER, f"{key_name}.key")
    try:
        with open(key_path, "w", encoding="utf-8") as file:
            file.write(key)
        messagebox.showinfo("Сохранение", f"Ключ сохранен в файл {key_path}")
    except (UnicodeEncodeError, ValueError) as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить ключ: {str(e)}")

def load_keys():
    keys = []
    if not os.path.exists(KEY_FOLDER):
        os.makedirs(KEY_FOLDER)
    for filename in os.listdir(KEY_FOLDER):
        if filename.endswith(".key"):
            keys.append(filename.replace(".key", ""))
    key_dropdown['values'] = keys

def select_key(event):
    key_name = key_dropdown.get()
    key_path = os.path.join(KEY_FOLDER, f"{key_name}.key")
    try:
        with open(key_path, "r", encoding="utf-8") as file:
            key = file.read().strip()
        # Только проверка ключа Fernet, если выбран алгоритм Fernet
        if algorithm_choice.get() == "Fernet":
            if not is_valid_fernet_key(key):
                raise ValueError("Ключ Fernet некорректной длины или формата.")
        key_entry.delete(0, tk.END)
        key_entry.insert(0, key)
    except (UnicodeDecodeError, ValueError) as e:
        messagebox.showerror("Ошибка", f"Ошибка загрузки ключа: {str(e)}")

def perform_encryption():
    key = key_entry.get().strip()
    data = input_text.get("1.0", tk.END)
    try:
        if algorithm_choice.get() == "Simple":
            result = simple_encrypt(data, key)
        elif algorithm_choice.get() == "Fernet":
            if not is_valid_fernet_key(key):
                raise ValueError("Ключ Fernet некорректной длины или формата.")
            result = fernet_encrypt(data, key)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка шифрования: {str(e)}")

def perform_decryption():
    key = key_entry.get().strip()
    data = input_text.get("1.0", tk.END)
    try:
        if algorithm_choice.get() == "Simple":
            result = simple_decrypt(data, key)
        elif algorithm_choice.get() == "Fernet":
            if not is_valid_fernet_key(key):
                raise ValueError("Ключ Fernet некорректной длины или формата.")
            result = fernet_decrypt(data, key)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось расшифровать данные: {str(e)}")

def is_valid_fernet_key(key):
    try:
        decoded_key = base64.urlsafe_b64decode(key.encode())
        return len(decoded_key) == 32
    except Exception:
        return False

def on_tab_change(event):
    selected_tab = event.widget.tab(event.widget.index("current"))["text"]
    if selected_tab == 'Keygen':
        root.geometry("450x400")
    else:
        root.geometry("650x600")
    load_keys()

# Создание основного окна и вкладок
root = tk.Tk()
root.title("GenEncryption")

tab_control = ttk.Notebook(root)
tab_control.bind("<<NotebookTabChanged>>", on_tab_change)

# Установка иконки программы
root.iconbitmap('logo_geniusz.ico') # Замените 'path_to_icon.ico' на путь к вашему файлу иконки


# Вкладка генерации ключа
keygen_tab = ttk.Frame(tab_control)
tab_control.add(keygen_tab, text='Keygen')

algorithm_choice_label = tk.Label(keygen_tab, text="Выберите алгоритм шифрования:")
algorithm_choice_label.pack(pady=10)
algorithm_choice = ttk.Combobox(keygen_tab, values=["Simple", "Fernet"])
algorithm_choice.current(0)
algorithm_choice.pack(pady=5)

key_label = tk.Label(keygen_tab, text="Сгенерировать новый ключ шифрования:")
key_label.pack(pady=10)

key_output = tk.Text(keygen_tab, height=2, width=50)
key_output.pack(pady=5)

generate_button = tk.Button(keygen_tab, text="Сгенерировать", command=generate_key)
generate_button.pack(pady=5)

key_name_label = tk.Label(keygen_tab, text="Введите имя ключа:")
key_name_label.pack(pady=10)
key_name_entry = tk.Entry(keygen_tab, width=50)
key_name_entry.pack(pady=5)

save_button = tk.Button(keygen_tab, text="Сохранить ключ", command=save_key)
save_button.pack(pady=5)

# Вкладка шифрования/дешифрования
encrypt_tab = ttk.Frame(tab_control)
tab_control.add(encrypt_tab, text='Encrypter')

key_dropdown_label = tk.Label(encrypt_tab, text="Выберите ключ из сохранённых:")
key_dropdown_label.pack(pady=10)
key_dropdown = ttk.Combobox(encrypt_tab, postcommand=load_keys)
key_dropdown.pack(pady=5)
key_dropdown.bind("<<ComboboxSelected>>", select_key)

key_entry_label = tk.Label(encrypt_tab, text="Введите ключ шифрования:")
key_entry_label.pack(pady=10)
key_entry = tk.Entry(encrypt_tab, width=50)
key_entry.pack(pady=5)

input_label = tk.Label(encrypt_tab, text="Введите данные:")
input_label.pack(pady=10)
input_text = tk.Text(encrypt_tab, height=10, width=50)
input_text.pack(pady=5)

encrypt_button = tk.Button(encrypt_tab, text="Зашифровать", command=perform_encryption)
encrypt_button.pack(pady=5)
decrypt_button = tk.Button(encrypt_tab, text="Расшифровать", command=perform_decryption)
decrypt_button.pack(pady=5)

output_label = tk.Label(encrypt_tab, text="Результат:")
output_label.pack(pady=10)
output_text = tk.Text(encrypt_tab, height=10, width=50)
output_text.pack(pady=5)

# Добавление вкладок в окно
tab_control.pack(expand=1, fill='both')

root.mainloop()
