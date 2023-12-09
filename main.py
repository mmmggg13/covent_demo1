from API_KEY import API_KEY
import streamlit as st
import openai as oai
# from PIL import Image

# print(API_KEY)
# selected_options = {
#     'TOPIC': None,
#     'SUBTOPIC': None,
#     'DOMAIN': None,
#     'AGE': None,
#     'Expertise': None,
#     'Responsibility': None,
#     'TITLE': None
# }
st.session_state.age = None
st.session_state.exp = None
st.session_state.res = None

selected_options = {}
st.title("Birdhaus Book Writing Online Platform Powered by AI")
# mode_topic = None
st.sidebar.image('logo.jpg')
mode_topic = st.sidebar.selectbox('Topic', ['IT', 'Marketing', 'Medecine', 'Sport', 'Culture'])
selected_options['TOPIC'] = mode_topic

select_subtopic = None
if mode_topic == 'Marketing':
    select_subtopic = st.sidebar.selectbox('Marketing', ['Traditional', 'Internet', 'Interactive'])
    selected_options['SUBTOPIC'] = select_subtopic
else:
    st.sidebar.write('Marketing not selected :)')

# select_domain = None
if select_subtopic == 'Internet':
    select_domain = st.sidebar.radio('Select a domain of your topic',
                            ['Search Engine Marketing', 'Social Media Marketing', 'Email Marketing',
                             'Content Marketing', 'Affiliate Marketing', 'Video Marketing', 'Mobile Marketing']
    )
    selected_options['DOMAIN'] = select_domain

else:
    st.write('Select TOPIC for your book!!!')

mode_brand = st.sidebar.selectbox('Brand', ['values', 'vision', 'voice', 'visuals'])

# st.sidebar.write('Audience')
# mode_audience = st.sidebar.selectbox('Audience', ['Age', 'Expertise', 'Responsibility'])
# if mode_audience == 'Age':
#     mode_audience_age = st.sidebar.radio('Select AGE of your audience',
#                                  ['18-25', '26-40', '41-60', '61+'])
#     selected_options['AGE'] = mode_audience_age
#     st.session_state.age = mode_audience_age
#
# if mode_audience == 'Expertise':
#     mode_audience_exp = st.sidebar.radio('Select Expertise of your audience in selected or satelite topic',
#                                      ['switcher', 'newcomer', 'average', 'expert'])
#     selected_options['Expertise'] = mode_audience_exp
#     st.session_state.exp = mode_audience_exp
#
#
# if mode_audience == 'Responsibility':
#     mode_audience_resp = st.sidebar.radio('Select Responsibility of your audience',
#                                      ['opearation level', 'tactic level', 'strategic level', 'top level'])
#     selected_options['Responsibility'] = mode_audience_resp
#     st.session_state.res = mode_audience_resp
#
#
# selected_options['AGE'] = st.session_state.age
# selected_options['Expertise'] = st.session_state.exp
# selected_options['Responsibility'] = st.session_state.res

mode_audience_age = st.sidebar.selectbox('Audience: AGE',
                                 ['18-25', '26-40', '41-60', '61+'])
selected_options['AGE'] = mode_audience_age

mode_audience_exp = st.sidebar.selectbox('Audience: Expertise',
                                     ['switcher', 'newcomer', 'average', 'expert'])
selected_options['Expertise'] = mode_audience_exp

mode_audience_resp = st.sidebar.selectbox('Audience: Responsibility',
                                     ['opearation level', 'tactic level', 'strategic level', 'top level'])
selected_options['Responsibility'] = mode_audience_resp

mode_style = st.sidebar.selectbox('Text style', ['scientific', 'official business', 'journalistic', 'art', 'colloquial'])
selected_options['Text style'] = mode_style

options = st.sidebar.button('Show selected options')

if options:
    st.write('Selected options: ', selected_options)
# image = Image.open('logo.jpg')
#
# st.image(image, width=700)

# with st.form('santiment form'):
#     text = st.text_area('Text to analyze')
#
#     submited = st.form_submit_button('Submit')
#     if submited:
#         # prediction = model(text=text)
#         # label = maping[prediction]
#         st.write(f'Done')
