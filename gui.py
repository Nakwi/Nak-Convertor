from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit,
    QPushButton, QFileDialog, QLabel, QMessageBox, QComboBox, QSplitter, QFrame
)
from PyQt6.QtCore import Qt
from markdown_to_html import markdown_to_html
from html_to_markdown import html_to_markdown
import sys
import os

class MarkdownHTMLConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Convertisseur Markdown ⇄ HTML")
        self.resize(1280, 720)
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: #dcdcdc;
                font-family: Consolas, monospace;
                font-size: 14px;
            }
            QPushButton {
                background-color: #0078d7;
                color: white;
                border-radius: 6px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
            QComboBox {
                background-color: #2d2d30;
                color: white;
                padding: 4px;
            }
            QTextEdit {
                background-color: #252526;
                border: 1px solid #3c3c3c;
                padding: 8px;
                color: #dcdcdc;
            }
            QLabel {
                color: #dcdcdc;
            }
        """)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        # Barre supérieure avec options
        top_bar = QHBoxLayout()

        self.load_button = QPushButton("Ouvrir un fichier")
        self.convert_button = QPushButton("Convertir")
        self.save_button = QPushButton("Enregistrer")
        self.info_button = QPushButton("Info")
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Markdown ➞ HTML", "HTML ➞ Markdown"])

        for btn in [self.load_button, self.convert_button, self.save_button, self.info_button]:
            btn.setCursor(Qt.CursorShape.PointingHandCursor)

        top_bar.addWidget(QLabel("Mode de conversion :"))
        top_bar.addWidget(self.mode_selector)
        top_bar.addStretch()
        top_bar.addWidget(self.load_button)
        top_bar.addWidget(self.convert_button)
        top_bar.addWidget(self.save_button)
        top_bar.addWidget(self.info_button)

        layout.addLayout(top_bar)

        # Ligne de séparation
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        layout.addWidget(separator)

        # Zones d'édition
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Collez ici votre Markdown ou HTML...")
        self.output_text = QTextEdit()
        self.output_text.setPlaceholderText("Le résultat apparaîtra ici...")
        self.output_text.setReadOnly(True)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(self.input_text)
        splitter.addWidget(self.output_text)
        splitter.setSizes([640, 640])
        layout.addWidget(splitter)

        # Connexions
        self.load_button.clicked.connect(self.load_file)
        self.convert_button.clicked.connect(self.convert_content)
        self.save_button.clicked.connect(self.save_file)
        self.info_button.clicked.connect(self.show_info)

    def load_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Charger un fichier", "", "Markdown/HTML (*.md *.html)")
        if path:
            try:
                with open(path, "r", encoding="utf-8", errors="replace") as f:
                    content = f.read()
                self.input_text.setPlainText(content)
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Impossible de charger le fichier :\n{e}")

    def convert_content(self):
        input_data = self.input_text.toPlainText()
        if not input_data.strip():
            QMessageBox.warning(self, "Attention", "Le champ d'entrée est vide.")
            return

        mode = self.mode_selector.currentText()
        try:
            if mode == "Markdown ➞ HTML":
                result = markdown_to_html(input_data)
            else:
                result = html_to_markdown(input_data)
            self.output_text.setPlainText(result)
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Une erreur est survenue :\n{e}")

    def save_file(self):
        content = self.output_text.toPlainText()
        if not content.strip():
            QMessageBox.warning(self, "Attention", "Aucun contenu à enregistrer.")
            return

        path, _ = QFileDialog.getSaveFileName(self, "Enregistrer sous", "", "Texte (*.txt);;Tous les fichiers (*)")
        if path:
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                QMessageBox.information(self, "Succès", "Fichier enregistré avec succès !")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Impossible d'enregistrer le fichier :\n{e}")

    def show_info(self):
        QMessageBox.information(
            self,
            "À propos",
            "Convertisseur Markdown ⇄ HTML\n\nCette application permet de convertir du texte Markdown en HTML et inversement.\n\nCréé par Corsyn Ryan."
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MarkdownHTMLConverter()
    window.show()
    sys.exit(app.exec())
