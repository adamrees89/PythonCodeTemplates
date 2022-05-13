## Credit to Haider Imtiaz

# Proofreading with Pyton
# pip install gingerit
# pip install streamlit
from gingerit.gingerit import GingerIt
import streamlit as webapp
app = GingerIt()
webapp.title('Proofreading in Python')
Text = webapp.text_area("Enter Your Text or Sentence:", value='', height=None, max_chars=None, key=None)
if webapp.button('Correct Sentence'):
    if Text == '':
        webapp.write('Please enter text for proofreading') 
    else: 
        correction = app.parse(Text)
        webapp.markdown('Corrected Text => ' + str(correction["result"]))

#---------------------------------------------------