# RSA Алгоритм на Python
Программа реализует алгоритм RSA: генерация ключей, шифрование и дешифрование сообщения. Используется список простых чисел, не превышающих 106106, без необходимости подключения внешних файлов.
## Содержимое проекта
- rsa.py - основной скрипт RSA с вводом через консоль  
- test_rsa.py - юнит-тесты на unittest  
- README.md - инструкция по запуску

## Запуск
- Клонировать репозиторий
``` bash
git clone https://github.com/dariavolnova/rsa
cd rsa
```
- Запустить программу
``` console
python rsa.py
```
- Программа попросит ввести сообщение, затем сгенерирует ключи, зашифрует и расшифрует сообщение.

## Запуск тестов
``` python
python -m unittest test_rsa.py
```
