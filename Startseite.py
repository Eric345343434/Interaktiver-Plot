import streamlit as st
from function import person,ekgdata
from PIL import Image
import matplotlib.pyplot as plt



st.title("Wilkommen bei  unserer Startseite") 

person_data = person.get_person_data()
person_names_list = person.get_person_names(person_data)




# Eine Überschrift der ersten Ebene
st.write("# EKG APP")

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

current_user_list = person.find_person_data_by_name(st.session_state.current_user) 
current_user_id = int(current_user_list["id"])


# Suche den Pfad zum Bild, aber nur wenn der Name bekannt ist
if st.session_state.current_user in person_names_list:
    image = Image.open(current_user_list["picture_path"])
# Anzeigen eines Bilds mit Caption
    st.image(image, caption=st.session_state.current_user)


st.write("Geburtsjahr =",  current_user_list["date_of_birth"])
st.write(st.session_state.current_user,"wird zurzeit gewählt")

current_ekg_list = current_user_list["ekg_tests"]

st.session_state.current_ekg_list_id = ekgdata.get_ids(current_ekg_list)

st.write("## Ekg-Test auswählen") 
st.session_state.current_ekg_id = st.selectbox( "", options = st.session_state.current_ekg_list_id, key= "ekg_tests")	










st.write("Derzeit ist der Ekg_Test mit der ID", st.session_state.current_ekg_id ,"von", st.session_state.current_user,"ausgewählt")




ekg_dict = ekgdata.load_by_id(st.session_state.current_ekg_id)
st.write("Datum des Ekg-Tests =",ekg_dict["date"])


ekgdata1= ekgdata(ekg_dict)
st.write("Dauer des Ekg-Tests =",ekgdata.calc_duration(ekgdata1)*1000, "Millisekunden = ", ekgdata.calc_duration(ekgdata1), "Sekunden = ", ekgdata.calc_duration(ekgdata1)/60, "Minuten")
peaks = ekgdata1.find_peaks()
st.write("Heartrate:", ekgdata.estimate_hr(peaks))


user_input_ekg_start= int(st.slider("Geben sie den Start Wert des Plots an",0, len(ekgdata1.df["Time in ms"]),0,))
user_input_ekg_end= int(st.slider("Geben sie den End Wert des Plots an",0, len(ekgdata1.df["Time in ms"]),10000))

# Plot EKG data with peaks
st.plotly_chart(ekgdata1.plot_ekg_with_peaks(user_input_ekg_start,user_input_ekg_end))






