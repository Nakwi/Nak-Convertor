from markdown_to_html import markdown_to_html
from html_to_markdown import html_to_markdown

def main():
    choix = input("1. Markdown ➜ HTML\n2. HTML ➜ Markdown\nChoix : ")
    fichier = input("Chemin du fichier à convertir : ")
    with open(fichier, "r") as f:
        contenu = f.read()

    if choix == "1":
        result = markdown_to_html(contenu)
        output = fichier.replace(".md", ".html")
    else:
        result = html_to_markdown(contenu)
        output = fichier.replace(".html", ".md")

    with open(output, "w") as f:
        f.write(result)
    print(f"Conversion terminée ! Fichier généré : {output}")

if __name__ == "__main__":
    main()
