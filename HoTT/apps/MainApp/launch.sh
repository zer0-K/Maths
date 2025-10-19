
PATH_PROJECT="/home/adrien/Programmation/Projets/Maths"
PATH_MAIN_APP="HoTT/apps/MainApp"

path_file="${PATH_PROJECT}/${PATH_MAIN_APP}/mainapp.py"

streamlit run "${path_file}" --server.headless=true
