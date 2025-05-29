# 💻 Convertisseur Markdown ⇄ HTML – Interface PyQt6

---

## 📝 Introduction

Ce projet est une application graphique développée avec **PyQt6** permettant de convertir du **texte Markdown en HTML** et inversement, sans utiliser de bibliothèques de conversion toutes faites.

🎯 Objectif : Permettre aux utilisateurs de tester, visualiser et convertir facilement du contenu Markdown ou HTML via une interface moderne et minimaliste.

---

## ⚙️ Fonctionnalités

- ✅ Chargement de fichiers `.md` ou `.html`
- ✅ Conversion bidirectionnelle Markdown ⇄ HTML
- ✅ Interface **sombre et ergonomique**
- ✅ Bouton Info avec une présentation du projet
- ✅ Compatible avec Python 3.9+

---

## 📦 Installation

### 🔧 Prérequis

- Python 3.9 ou supérieur
- PyQt6

### 🔁 Installation des dépendances

```bash
pip install PyQt6
```

---

## 🚀 Lancer l'application

```bash
python gui.py
```

L'interface graphique s'ouvrira et vous pourrez :
- Ouvrir un fichier `.md` ou `.html`
- Convertir le texte
- Visualiser le résultat dans une autre zone
- Sauvegarder le fichier converti

---

## 🧱 Architecture du projet

```
markdown_converter/
│
├── gui.py               # Interface graphique principale PyQt6
├── markdown_to_html.py # Fonctions de conversion Markdown vers HTML
├── html_to_markdown.py # Fonctions de conversion HTML vers Markdown
├── article_astronomie.md  # Exemple de fichier Markdown
└── README.md            # Documentation du projet
```

---

## 🛠️ Détails Techniques

### 🎨 Construction de l'interface PyQt6

L'interface est conçue avec `QVBoxLayout`, `QHBoxLayout`, `QSplitter` et des composants comme :
- `QTextEdit` pour saisir et afficher les textes
- `QPushButton` pour les actions (ouvrir, convertir, enregistrer, info)
- `QComboBox` pour choisir le sens de conversion
- `QMessageBox` pour afficher les erreurs ou informations

Le thème sombre est appliqué via une feuille de style CSS intégrée (style VS Code).  
L’interface est totalement **responsive** et redimensionnable grâce au `QSplitter`.

---

### 🔁 Fonctionnement de la conversion Markdown ⇄ HTML

Les fichiers `markdown_to_html.py` et `html_to_markdown.py` utilisent principalement **des expressions régulières** (regex) pour parser et transformer le texte :

#### Markdown → HTML

- `# Titre` → `<h1>`, `##` → `<h2>`, etc.
- `**gras**` → `<strong>`, `*italique*` → `<em>`
- `[lien](url)` → `<a href="url">lien</a>`
- `- Élément` → `<li>Élément</li>`

#### HTML → Markdown

- `<h1>` → `#`, `<strong>` → `**`, `<em>` → `*`
- `<a href="...">` → `[texte](url)`
- `<li>` → `- Élément`

L’approche est simple, claire et **sans dépendances externes**. Elle peut être étendue pour supporter les tableaux, citations, blocs de code multi-lignes, etc.

---

## 🎥 Démonstration

[![Image](https://i.goopics.net/dfveuc.gif)](https://goopics.net/i/dfveuc)

---

## 👤 À propos

Développé par **Corsyn Ryan** dans le cadre d’un projet pédagogique.  
Ce projet vise à renforcer les compétences en **interface graphique**, **manipulation de fichiers** et **conversion de formats texte**.

---

## 📜 Licence

Ce projet est distribué sous licence libre à des fins pédagogiques.
