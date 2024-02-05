from pathlib import Path

import streamlit as st
from PIL import Image
import pandas as pd
from bokeh.plotting import figure 



current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "c (1).pdf"
profile_pic = current_dir / "assets" / "WhatsApp Image 2024-01-25 à 05.00.44_856a817e.jpg"

PAGE_TITLE = "CV | MOUNIROU wahab"
PAGE_ICON = ":wave:"
NAME = "MOUNIROU wahab"
DESCRIPTION = """
Etudiant en seconde Année de Bachelor informatique, à Paris Ynov Campus,
à la recherche d'un STAGE EN DATA ENGINEERING
"""
EMAIL = "wahab.mounirou@ynov.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/wahab-mounirou-161786253/",
    "GitHub": "https://github.com/MOUNIROUWAHAB23",
}
# PROJECTS = {
#     "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
#     "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
#     "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
#     "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
# } 
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write("#")
st.subheader("infomations personnelles")
st.write("Age: 17ans")
st.write ( "Nationalité: Bénin")

st.subheader("Competénces")
st.write(
    """
- ✔️ CAPACITES D’ANALYSE
- ✔️ ESPRIT DE RESPONSABILITE
- ✔️ TRAVAIL EN EQUIPE
- ✔️ CAPACITE D’ADAPTATION
- ✔️ PERSEVERANT

"""
)

st.write("#")
st.subheader("Competénces en informatiques")
st.write(
    """
Java | Php | Python (POO, bibliothèques de
Data) | Golang | C# | Javascript |
HTML | CSS | Git |
| SQL |
Maths DataScience | Docker | UX/UI | La gestion de reseaux, (windows server,
ubuntu, debian)

"""
)


st.write("#")
st.subheader("Data Skills")
st.write(
    """
- 👩‍💻 Programmation: Python (numpy, Pandas), SQL
- 📊 Data Visualisation: matplotlib
- 📚 Modelation: Logistic regression, linear regression, decition trees
- 🗄️ Databases: MongoDB, MySQL
"""
)

st.write("#")
st.subheader("🌍 Langues")

# Load the CSV data into a Pandas DataFrame
data = pd.DataFrame({'Language': ['Anglais', 'Français'], 'Scores': [6,  10]})

# Create a Bokeh figure
p = figure(y_range=data['Language'], height = 300, width=600, title="Language Scores")
p.hbar(y=data['Language'], right=data['Scores'], height=0.9)

# Show the Bokeh figure in Streamlit
st.bokeh_chart(p)

# st.write("#")
st.write("---")
# st.write("#")

st.subheader("Formations")

st.write(" - 📚 Baccalauréat (Physique, Mathématiques et biologie)")
st.write("Cours catholique saint-Augustin, Bénin - 10.2016 / 06.2022")
st.write(" - 📙 Mastère Informatique")
st.write("Paris Ynov Campus, Nanterre - 09.2022 / 04.2027")

# st.write("\n")
st.write("---")
# st.write("\n")

st.subheader("Expérience étudiant")

st.write("🏴 Data projects")

st.write("- ➖ Scraping des données de quotesToScrapp et les affichage dans MongoDB utilisation de FAStAPI pour automatiser les requêtes CRUD")
st.write("- - 🛠 Technologies: Selenium, Streamlit, MongoDb,pandas")



st.write("🏴 Les jeux:")

st.write("- ➖ Pacman Web")
st.write("- - 🛠 Technologies: Pure JS, POO en JS")
st.write("- - 🛠 Technologies: POO Java, Gestion de sockets, BDD")

st.write("- ➖ Hangman Web")
st.write("- - 🛠 Technologies: Pure JS, POO en JS")
st.write("- - 🛠 Technologies: POO Java, Gestion de sockets, BDD")


st.write("🏴 Web développement:")

st.write("- ➖ La réalisation des projets tels que hangman ")
st.write("- - 🛠 Technologies: Golang")
st.write("- ➖ Le site Forum")
st.write("- - 🛠 Technologies: javascript, sql")
st.write("- ➖ L'affichage des données mongodb sur une page Web et les filtrer, la barre de recherche")
st.write("- - 🛠 Technologies: HTML, CSS, JS, Express, NoSql")

# st.write("#")
st.write("---")
# st.write("#")

st.subheader("Expériences professionelles")
st.write("Aucune")
# st.write("- Ynov Campus, Nanterre - Depuis 07.2022")
# st.write("- - 📐 Le travail avec les élèves B1 et B2, enseignements pédagogiques, aide à la réalisation de leurs projets selon le cursus")

# st.write("#")
st.write("---")
# st.write("#")

st.subheader("Intérêts")
st.write("- ⚽️ | 🏀 | 🥊 | 🦾 | 🎧 | 🎵")

 