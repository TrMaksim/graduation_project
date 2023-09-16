<strong>Проект "Система розподілу витрат на зустрічі з друзями"</strong>
### Опис проекту
Проект "Система розподілу витрат на зустрічі з друзями" розроблений для автоматизації розподілу витрат між учасниками зустрічей. Кожен тиждень група друзів зустрічається у закладі, щоб випити чаю та поспілкуватися. Програмне рішення допомагає автоматично розрахувати, скільки кожен учасник повинен внести грошей, щоб вирівняти загальні витрати.

### Основні функціональні можливості:

# Реєстрація користувачів: Користувачі можуть зареєструвати свої облікові записи, вказавши свій email, пароль, телефон та ім'я користувача.
# Авторизація користувачів: Зареєстровані користувачі можуть авторизуватися за допомогою свого email та паролю.
# Створення зустрічей: Користувачі можуть створювати нові зустрічі, вказуючи місце та дату зустрічі.
# Додавання учасників до зустрічі: Користувачі можуть додавати інших користувачів до своїх зустрічей, вказуючи їх ідентифікатори.
# Створення покупок: Під час зустрічі користувачі можуть створювати записи про покупки, вказуючи суму, опис та учасників, які спільно сплатили за цю покупку.
# Розрахунок боргів: Система автоматично розраховує, скільки кожен учасник зустрічі повинен іншим учасникам, щоб вирівняти загальні витрати.
# Коментарі до витрат: Користувачі можуть додавати коментарі до кожної покупки, щоб вказати, за що саме були зроблені витрати.
# Захист даних: Проект забезпечує безпеку даних користувачів, використовуючи аутентифікацію та авторизацію, а також шифрування паролів.

## Інструкція з встановлення і запуску
## Склонуйте репозиторій проекту з GitHub:
```
git clone https://github.com/your-repository.git
cd your-repository
```
## Встановіть необхідні залежності за допомогою pip:
```
pip install -r requirements.txt
```
## Запустіть сервер за допомогою uvicorn:
```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
## Після запуску, ваше веб-застосування буде доступним за адресою:
```
http://localhost:8000
```
## Використані технології
# Python та фреймворк FastAPI для розробки веб-застосунку.
# SQLAlchemy для роботи з базою даних.
# JWT для аутентифікації та авторизації користувачів.
# База даних для зберігання даних користувачів, зустрічей, покупок та боргів.
![Модель базы данных]![Blank diagram (3)](https://github.com/TrMaksim/graduation_project/assets/127137829/db2c3b0e-3188-428f-a6f6-afbd7d752db3)

## Автори
# Проект розроблений [Trachuk Maksym].

## Ліцензія
Этот проект распространяется под лицензией [MIT]([[ссылка-на-лицензию](https://opensource.org/licenses/MIT)](https://opensource.org/license/mit/)).

Цей проект створений для зручного та справедливого розподілу витрат під час зустрічей з друзями та може бути використаний для обліку спільних витрат між будь-якою групою людей. Насолоджуйтесь вашими зустрічами та нехай ця система полегшить вам життя!
