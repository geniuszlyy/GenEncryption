# GenEncryption
 is a versatile encryption utility designed for securely encrypting and decrypting text data. It supports two encryption algorithms: a custom Simple substitution cipher and the industry-standard Fernet encryption.

# EN
**GenEncryption** is a versatile encryption tool designed to provide secure encryption and decryption of text data. The application supports two main algorithms: a custom Simple substitution cipher and the industry-standard Fernet encryption.

## Features
- **Multiple Encryption Algorithms**: Choose between a custom Simple algorithm and Fernet encryption.
- **Key Generation**: Easily generate and save encryption keys.
- **Key Management**: Load and manage saved keys.
- **User-Friendly Interface**: Intuitive GUI for easy navigation and operation.

## Requirements
- **Python 3.x**
- **Libraries**: `tkinter`, `cryptography`, `os`, `random`, `base64`

## Installation
1. **Clone the repository**:
```bash
git clone https://github.com/geniuszlyy/GenEncryption.git
cd GenEncryption
```
2. **Install dependencies**:\
Install the required Python libraries using pip:
```bash
pip install cryptography
```

## Usage
1. **Run the Application**:\
Start the application by running the `main.py` script:
```bash
python GenEncryption.py
```
2. **Generate Keys**:
- Navigate to the "Keygen" tab.
- Select the desired encryption algorithm (Simple or Fernet).
- Click "Generate" to create a new key.
- Enter a name for the key and save it.
3. **Encrypt/Decrypt Data**:
- Navigate to the "Encrypter" tab.
- Select a saved key or enter a key manually.
- Enter the data to be encrypted or decrypted.
- Click "Encrypt" or "Decrypt" to process the data.

## Key Storage
Generated keys are stored in the `keys/` directory. Ensure that this directory is kept secure to maintain the confidentiality of your encrypted data.

## Example
### Simple:
![image](https://github.com/user-attachments/assets/452d2fc4-9dd7-4d27-b396-8df2072d4018)

![image](https://github.com/user-attachments/assets/37e4199b-b5b3-461c-add6-06625b1a2db5)

![image](https://github.com/user-attachments/assets/230da501-06ab-4578-af79-bec8d45e1f05)

### Fernet:
![image](https://github.com/user-attachments/assets/856de520-b8f6-4619-b54e-3f8cd4c4ece4)

![image](https://github.com/user-attachments/assets/23c7acf8-56dc-4250-aba4-bbe44fffdd8c)

# RU
**GenEncryption** — это универсальный инструмент для шифрования, предназначенный для обеспечения безопасного шифрования и дешифрования текстовых данных. Программа поддерживает два основных алгоритма: собственный алгоритм Simple и стандартизированный шифр Fernet.

## Возможности
- **Множественные алгоритмы шифрования**: Выбор между собственным алгоритмом Simple и шифром Fernet.
- **Генерация ключей**: Легкое создание и сохранение ключей шифрования.
- **Управление ключами**: Загрузка и управление сохраненными ключами.
- **Интуитивный интерфейс**: Удобный графический интерфейс для простоты использования.

## Требования
- **Python 3.x**
- **Библиотеки**: `tkinter`, `cryptography`, `os`, `random`, `base64`

## Установка
1. **Клонирование репозитория**:
```bash
git clone https://github.com/geniuszlyy/GenEncryption.git
cd GenEncryption
```
2. **Установка зависимостей**:\
Установите необходимые библиотеки Python с помощью pip:
```bash
pip install cryptography
```

## Использование
1. **Запуск приложения**:\
Запустите приложение, выполнив скрипт `main.py`:
```bash
python GenEncryption.py
```
2. **Генерация ключей**:
- Перейдите на вкладку "Keygen".
- Выберите желаемый алгоритм шифрования (Simple или Fernet).
- Нажмите "Generate" для создания нового ключа.
- Введите имя для ключа и сохраните его.
3. **Шифрование/Дешифрование данных**:
- Перейдите на вкладку "Encrypter".
- Выберите сохраненный ключ или введите ключ вручную.
- Введите данные для шифрования или дешифрования.
- Нажмите "Encrypt" или "Decrypt" для обработки данных.

## Хранение ключей
Сгенерированные ключи хранятся в каталоге `keys/`. Убедитесь, что этот каталог надежно защищен для сохранения конфиденциальности ваших данных.

## Пример
### Simple:
![image](https://github.com/user-attachments/assets/452d2fc4-9dd7-4d27-b396-8df2072d4018)

![image](https://github.com/user-attachments/assets/37e4199b-b5b3-461c-add6-06625b1a2db5)

![image](https://github.com/user-attachments/assets/230da501-06ab-4578-af79-bec8d45e1f05)

### Fernet:
![image](https://github.com/user-attachments/assets/856de520-b8f6-4619-b54e-3f8cd4c4ece4)

![image](https://github.com/user-attachments/assets/23c7acf8-56dc-4250-aba4-bbe44fffdd8c)


