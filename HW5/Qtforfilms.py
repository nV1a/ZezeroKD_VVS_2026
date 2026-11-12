import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox, QCheckBox

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle('Tonight we will watch...???')
window.resize(800, 650)
label = QLabel('Name:')
name_input = QLineEdit()
name_input.setPlaceholderText('For example, Ivan')
add_button = QPushButton('Add')
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(name_input)
layout.addWidget(add_button)
central = QWidget()
central.setLayout(layout)
window.setCentralWidget(central)
friends = {}
def add_friend():
    name = ' '.join(name_input.text().split())
    wishes = [box.text() for box in genre_boxes if box.isChecked()]
    if not name:
        QMessageBox.warning(window, 'Incorrect input', 'Enter a name')
        return
    if name in friends:
        QMessageBox.warning(window, 'Incorrect input', f'{name} is already added, try {name}2')
        return
    if not wishes:
        QMessageBox.warning(window, 'Incorrect input', 'Select at least one genre')
        return
    friends[name] = wishes
    friends_list.addItem(name + ': ' + ', '.join(wishes))
    name_input.clear()
    for box in genre_boxes:
        box.setChecked(False)
    
friends_list = QListWidget()
add_button.clicked.connect(add_friend)
layout.addWidget(friends_list)
# movies = [
#     {"title": "Интерстеллар", "genres": ["фантастика", "драма", "приключения"]},
#     {"title": "Начало", "genres": ["фантастика", "боевик", "триллер"]},
#     {"title": "Матрица", "genres": ["фантастика", "боевик"]},
#     {"title": "Парк Юрского периода", "genres": ["приключения", "фантастика", "триллер"]},
#     {"title": "Побег из Шоушенка", "genres": ["драма", "криминал"]},
#     {"title": "Зелёная миля", "genres": ["драма", "фэнтези", "криминал"]},
#     {"title": "Крёстный отец", "genres": ["драма", "криминал"]},
#     {"title": "Форрест Гамп", "genres": ["драма", "комедия", "мелодрама"]},
#     {"title": "Один дома", "genres": ["комедия", "приключения"]},
#     {"title": "Маска", "genres": ["комедия", "фэнтези"]},
#     {"title": "Тёмный рыцарь", "genres": ["боевик", "криминал", "триллер"]},
#     {"title": "Джон Уик", "genres": ["боевик", "триллер", "криминал"]},
#     {"title": "Сияние", "genres": ["ужасы", "триллер"]},
#     {"title": "Крик", "genres": ["ужасы", "триллер", "комедия"]},
#     {"title": "Молчание ягнят", "genres": ["триллер", "ужасы", "криминал"]},
#     {"title": "Властелин колец: Братство кольца", "genres": ["фэнтези", "приключения", "драма"]},
#     {"title": "Гарри Поттер и философский камень", "genres": ["фэнтези", "приключения"]},
#     {"title": "Титаник", "genres": ["мелодрама", "драма"]},
#     {"title": "Дневник памяти", "genres": ["мелодрама", "драма"]},
#     {"title": "Шрек", "genres": ["мультфильм", "комедия", "фэнтези"]},
#     {"title": "Король Лев", "genres": ["мультфильм", "драма", "приключения"]},
#     {"title": "Холодное сердце", "genres": ["мультфильм", "фэнтези", "приключения"]},
# ]
#фильмы собраны нейросетью, сверху вариант на русском языке
movies = [
    {"title": "Interstellar", "genres": ["sci-fi", "drama", "adventure"]},
    {"title": "Inception", "genres": ["sci-fi", "action", "thriller"]},
    {"title": "The Matrix", "genres": ["sci-fi", "action"]},
    {"title": "Jurassic Park", "genres": ["adventure", "sci-fi", "thriller"]},
    {"title": "The Shawshank Redemption", "genres": ["drama", "crime"]},
    {"title": "The Green Mile", "genres": ["drama", "fantasy", "crime"]},
    {"title": "The Godfather", "genres": ["drama", "crime"]},
    {"title": "Forrest Gump", "genres": ["drama", "comedy", "romance"]},
    {"title": "Home Alone", "genres": ["comedy", "adventure"]},
    {"title": "The Mask", "genres": ["comedy", "fantasy"]},
    {"title": "The Dark Knight", "genres": ["action", "crime", "thriller"]},
    {"title": "John Wick", "genres": ["action", "thriller", "crime"]},
    {"title": "The Shining", "genres": ["horror", "thriller"]},
    {"title": "Scream", "genres": ["horror", "thriller", "comedy"]},
    {"title": "The Silence of the Lambs", "genres": ["thriller", "horror", "crime"]},
    {"title": "The Lord of the Rings: The Fellowship of the Ring", "genres": ["fantasy", "adventure", "drama"]},
    {"title": "Harry Potter and the Sorcerer's Stone", "genres": ["fantasy", "adventure"]},
    {"title": "Titanic", "genres": ["romance", "drama"]},
    {"title": "The Notebook", "genres": ["romance", "drama"]},
    {"title": "Shrek", "genres": ["animation", "comedy", "fantasy"]},
    {"title": "The Lion King", "genres": ["animation", "drama", "adventure"]},
    {"title": "Frozen", "genres": ["animation", "fantasy", "adventure"]},
]
all_genres = sorted({genre for m in movies for genre in m["genres"]})
def pick_movie(movies, friends):
    def score_of(movie):
        scores = [len(set(movie["genres"]) & set(genres)) for genres in friends.values()]
        return (min(scores), sum(scores))
    picked = max(movies, key=score_of)
    return picked, score_of(picked)

genre_boxes = []
for genre in all_genres:
    box = QCheckBox(genre)
    layout.addWidget(box)
    genre_boxes.append(box)
pick_button = QPushButton('Pick a movie')
layout.addWidget(pick_button)
def on_pick():
    if not friends:
        QMessageBox.warning(window, 'Warning', 'Add at least one friend')
        return
    picked, score = pick_movie(movies, friends)
    if score[0] > 0:
        QMessageBox.information(window, 'Picked', f'Tonight we will watch {picked["title"]}')
    else:
        QMessageBox.information(window, 'Different points of view...', f'Most suitable is {picked["title"]}')
pick_button.clicked.connect(on_pick)


window.show()

sys.exit(app.exec())
