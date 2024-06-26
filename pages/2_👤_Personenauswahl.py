import streamlit as st
from function import person,ekgdata
from PIL import Image
import matplotlib.pyplot as plt




person_data = person.get_person_data()
person_names_list = person.get_person_names(person_data)






#St.session_state werden abgefragt
if "current-user" not in st.session_state:
    st.session_state.current_user ="None"

if 'picture_path' not in st.session_state:
    st.session_state.picture_path = 'data/pictures/none.jpg'

if "id" not in st.session_state:
    st.session_state.id = "None"





# Eine Überschrift der zweiten Ebene
st.write("## Versuchsperson auswählen")

# Eine Auswahlbox, das Ergebnis wird in current_user gespeichert
st.session_state.current_user = st.selectbox(
    "",
    options = person_names_list, key="sbVersuchspersons")

st.session_state.current_user_list = person.find_person_data_by_name(st.session_state.current_user) 
current_user_id = int(st.session_state.current_user_list["id"])


# Suche den Pfad zum Bild, aber nur wenn der Name bekannt ist
if st.session_state.current_user in person_names_list:
    image = Image.open(st.session_state.current_user_list["picture_path"])
# Anzeigen eines Bilds mit Caption
    st.image(image, caption=st.session_state.current_user)


st.write("Geburtsjahr =",  st.session_state.current_user_list["date_of_birth"])
st.write(st.session_state.current_user,"wird zurzeit gewählt")