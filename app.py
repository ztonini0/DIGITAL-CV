from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Matheus Tonini"
PAGE_ICON = ":wave:"
NAME = "Matheus Tonini"
DESCRIPTION = """
Analista Geoespacial | Capacitado na interpretação de dados espaciais para apoiar decisões estratégicas.
"""
EMAIL = "matheustonini.co@gmail.com"
SOCIAL_MEDIA = {
    "Instagram": "https://www.instagram.com/pydatalab.co?utm_source=qr&igsh=MXFoN202OTd5aWd0dw==",
    "LinkedIn": "https://linkedin.com/in/matheus-tonini-3a05791b6",
    "GitHub": "https://github.com/ztonini0"
}
PROJECTS = {
    "🏆 Automação de Processo - Automação da Coleta de Dados do IBGE com Python": {
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7262175958906900480/",
        "description": "Script automatizado com Selenium para acessar o site do IBGE, baixar estimativas populacionais e organizar arquivos para análise."
    },
    "🏆 Automação de Processo - Automação para Notificar Clientes com Pendências": {
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7253085812274176001/",
        "description": "O script filtra a base de dados e dispara e-mails automaticamente, otimizando processos e trazendo mais agilidade ao dia a dia."
    },
    "🏆 Geoespacial com Folium - National Obesity By State": {
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7252732129027969024/",
        "description": "Mapa interativo para análise de taxas de obesidade nos EUA, utilizando Folium para visualização e GeoPandas para manipulação de dados geográficos."
    },
    "🏆 dashboard interativo - Manipulação de dados (Pandas & Plotly)": {
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7115248992929656832/",
        "description": "O dashboard apresenta total de vendas, classificação média e vendas médias por transação, com manipulação de dados realizada via Pandas e gráficos interativos construídos com Plotly para melhor visualizaçã."
    }
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Currículo",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS (Centralizado) ---
st.write('\n')
if len(SOCIAL_MEDIA) == 2:
    col1, col2, spacer = st.columns([2, 2, 1])
    with col1:
        platform1, link1 = list(SOCIAL_MEDIA.items())[0]
        st.write(f"[{platform1}]({link1})")
    with col2:
        platform2, link2 = list(SOCIAL_MEDIA.items())[1]
        st.write(f"[{platform2}]({link2})")
else:
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experiência & Qualificações")
st.write(
    """
- ✔️ 4 anos transformando dados em insights estratégicos  
- ✔️ Forte experiência prática e conhecimento em Python, Excel e SQL  
- ✔️ Sólida habilidade para resolver problemas complexos com dados
- ✔️ Excelente trabalho em equipe e iniciativa forte na execução de tarefas  
"""
)


# --- HARD SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programação: Python (Pandas, NumPy, GeoPandas), SQL, VBA  
- 📊 Visualização de Dados: MS Excel, Plotly, Folium (Mapas), Dash  
- 🔗 APIs & Backend: Flask, Integração com APIs  
- 🗄️ Bancos de Dados: Postgres, MySQL  
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Trajetória Profissional")
st.write("---")

# --- JOB 1
st.write("🚧", "**Analista Geoespacial | Geografia de Mercado**")
st.write("12/2023 - Atual")
st.write(
    """
- ► Gerenciamento de bases de dados públicas e privadas para estruturação de ferramentas de geomarketing, permitindo análises geoespaciais detalhadas  
- ► Suporte e treinamento em ferramentas de Geomarketing e Inteligência de Mercado  
- ► Segmentação e clusterização de consumidores para definição de público-alvo e estratégias de marketing  
- ► Estudos de localização para abertura, realocação e encerramento de PDVs  
"""
)


# --- JOB 2 ---
st.write('\n')
st.write("🚧", "**Estágio em Operações | Votorantim Cimentos**")
st.write("10/2022 - 11/2023")
st.write(
    """
- ► Gestão, análise e governança dos KPIs de operações logísticas (CDM, TMAC)  
- ► Suporte às áreas de interface, incluindo Cimentos, Argamassa, Agregados, Viter e Comercial  
- ► Atuação como PMO em projetos estratégicos de logística  
- ► Desenvolvimento de relatórios logísticos e otimização de processos  
"""
)


# --- JOB 3 ---
st.write('\n')
st.write("🚧", "**Estágio em Operações | Almaria**")
st.write("03/2023 - 08/2023")
st.write(
    """
- ► Desenvolvimento de relatórios operacionais, incluindo fluxo de mercadorias expedidas e entregues  
- ► Atualização de relatório de quebras de estoque para monitoramento de perdas  
- ► Análise de motivos de contato do SAC para otimização de atendimento  
- ► Levantamento e estruturação de processos operacionais para melhoria contínua  
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projetos")
st.write("---")
for project, details in PROJECTS.items():
    st.write(f"[{project}]({details['link']})")
    st.write(details["description"])
