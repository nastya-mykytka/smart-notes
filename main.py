from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPlainTextEdit, QHBoxLayout, QPushButton

app = QApplication([])

window = QWidget()

window.setWindowTitle("Розумні замітки")
width = 800
height = 500
window.resize(width, height)
window.show()

# білий квадратік
notesText = QPlainTextEdit("1111111111111111111")
notesTextLayout = QHBoxLayout() #
notesTextLayout.addWidget(notesText) #


# верхній леяут для нотаток
titleNotes = QLabel("Список заміток")
titleNotesLayout = QHBoxLayout()
titleNotesLayout.addWidget(titleNotes)

notesItem = QLabel("Нотатка 1")
notesListLayout = QVBoxLayout()
notesListLayout.addWidget(notesItem)

createNote = QPushButton("Створити нотатку")
deleteNote = QPushButton("Видалити замітку")
saveNote = QPushButton("Зберегти замітку")

topNotesButtonLayout = QHBoxLayout()
topNotesButtonLayout.addWidget(createNote)
topNotesButtonLayout.addWidget(deleteNote)

saveNoteLayout = QHBoxLayout()
saveNoteLayout.addWidget(saveNote)

notesButtonLayout = QVBoxLayout()
notesButtonLayout.addLayout(topNotesButtonLayout)
notesButtonLayout.addLayout(saveNoteLayout)

mainNotesLayout = QVBoxLayout()
mainNotesLayout.addLayout(titleNotesLayout)
mainNotesLayout.addLayout(notesListLayout)
mainNotesLayout.addLayout(notesButtonLayout)

# нижній леяут для тегів
titleTags = QLabel("Список тегів")
titleTagsLayout = QHBoxLayout()
titleTagsLayout.addWidget(titleTags)

tagsItem = QLabel("Нотатка 1")
tagsListLayout = QVBoxLayout()
tagsListLayout.addWidget(tagsItem)

addToNote = QPushButton("Додати до замітки")
unpinFromNote = QPushButton("Відкріпити від замітки")
searchNoteByTags = QPushButton("Шукати нотатки то тегу")

topTagsButtonLayout = QHBoxLayout()
topTagsButtonLayout.addWidget(addToNote)
topTagsButtonLayout.addWidget(unpinFromNote)

searchNotesByTagLayout = QHBoxLayout()
searchNotesByTagLayout.addWidget(searchNoteByTags)

tagsButtonLayout = QVBoxLayout()
tagsButtonLayout.addLayout(topTagsButtonLayout)
tagsButtonLayout.addLayout(searchNotesByTagLayout)

mainTagsLayout = QVBoxLayout()
mainTagsLayout.addLayout(titleTagsLayout)
mainTagsLayout.addLayout(tagsListLayout)
mainTagsLayout.addLayout(tagsButtonLayout)


leftLayout = QVBoxLayout()
leftLayout.addLayout(notesTextLayout)


rightLayout = QVBoxLayout()
rightLayout.addLayout(mainNotesLayout)
rightLayout.addLayout(mainTagsLayout)


mainLayout = QHBoxLayout()
mainLayout.addLayout(leftLayout)
mainLayout.addLayout(rightLayout)


window.setLayout(mainLayout)

app.exec()