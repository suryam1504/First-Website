import streamlit as st

st.title('Hello Ayushi!')
st.write('Yo this is Suryam and Kaushik. We are supposed to study Abstract Algebra now but welp.')

st.header("You are lame")

st.subheader("You are lame in sub-header")

st.write('')

Host_Celeb = st.selectbox('Who is your favourite celebrity:', ('Chris Evans', 'Andrew Scott', 'Harry Styles'))
st.write('You selected:', Host_Celeb)

st.write('')

# Add selectbox in streamlit
option = st.selectbox(
    'Who is the best person in the class?',
    ('Suryam', 'Suryam', 'Suryam'))

st.write('You selected:', option)

st.write('')

st.button('Chinese Button (obv does nothing)')

st.write('')

if st.button('Tap to reveal crush'):   
    st.write('Sangeeth') #displayed when the button is clicked
else:
    st.write('') #displayed when the button is unclicked

# Display Images
 
# import Image from pillow to open images
from PIL import Image
img = Image.open(r"C:\Users\surya\OneDrive\Pictures\Screenshots\Sangeeth.jpeg")
 
# display image using streamlit
# width is used to set the width of an image
if st.button("Tap to reveal crush's photo"): 
    st.image(img, width=200)

st.write('')

level = st.slider("Rate Suryam's humor level", 10000, 99999)
st.text('Selected: {}'.format(level))

st.write('')

# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Select for surprise"):
   
  # display the text if the checkbox returns True value
  st.text("Jaa na be nautanki")

st.write('')