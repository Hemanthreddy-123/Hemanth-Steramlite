
import streamlit as st
from streamlit_option_menu import option_menu

page = option_menu(
    menu_title=None,
    options=['Home', 'Projects', 'Resume', 'Feedback'],
    default_index=0,
    orientation='horizontal'
)

st.divider()
name,photo = st.columns([2,1])
st.write('\n')
name.title('Mukkamalla Hemanth Reddy')
photo.image('https://res.cloudinary.com/dzvzvj8nd/image/upload/v1706625422/IMG_2556_vkrkb5.jpg')
if page=='Home':
    if st.button('Show Details'):
        with st.expander('Personal Details'):
            st.write('Name : Mukkamalla Hemanth Reddy')
            st.caption('Software Engineering Student - pursuing b.tech 2nd year')
            st.caption('In Audisankara college of engineering and technology')
            st.write('Address : Depur, Atmakur, Nellore 524322')
            st.write('Phone : 9347591702')
            st.write('Mail : hemanthreddymukkamalla@gmail.com')

        with st.expander('Educational Details'):
            st.write('Education : B.Tech, Intermediate, 10th')
            st.write('Course : CSE,MPC,Regular')
            st.write('College Name : Audisankara college of engineering and technology ,')

            st.write('Percentage : 75%,57%,86%')

        with st.expander('Family Details'):
            st.write('Mother Name: Mukkamalla Vengamma')
            st.caption('Domestic engineer')
            st.write('Father Name: Mukkamalla YellaReddy')
            st.caption('Former')

            st.caption('')
    st.divider()
    st.header('My Skills')

    if st.button('Show skills'):
        st.subheader('Technical Skills :')

        with st.expander('C'):
            st.write('I posses very good skills in C')

        with st.expander('Java'):
            st.write('I have very good skills in Java')
            st.write('Including GUI , Graphics')

        with st.expander('SQL'):
            st.write('I can work on databases with SQL')

        with st.expander('DSA'):
            st.write('I can implement data structures using C & JAVA')

        with st.expander('Problem Solving'):
            st.write('I have a good problem solving ability')

        st.subheader('Personal Skills :')

        with st.expander('Communication skills'):
            st.write('Telugu')

            st.write('English')

            st.write('Hindi')


        with st.expander('LeaderShip Skills'):
             st.write('I have good leadership Skills')

    st.divider()
    st.header('Certificates')

    rad = st.selectbox('Select Option To View', ['Default', 'Java', 'Data Science', 'Python For Data Science'], index=0)

    if rad == 'Java':
        st.markdown("*java* Certification From *codesoft*\n\n")
        st.markdown("Sololearn is an application\n"
"we can learn many programing languages from it\n"
"While I am learning java certification it was very fun to learn in sololearn")

        st.link_button('See Java certificate', 'https://www.linkedin.com/posts/hemanth-reddy-mukkamalla-3b6491269_codesoft-java-internship-activity-7147076927743213568-R1vi?utm_source=share&utm_medium=member_desktop')

    if rad == 'Data Science':
        st.markdown("*Data Science* Certification From *codesoft*\n\n"
        "codesoft is well known platform to everyone.\n"
        "Learning Data Science in codesoft is very challenging and exciting")

        st.link_button('See Data Science Certificate', 'https://www.linkedin.com/posts/hemanth-reddy-mukkamalla-3b6491269_codsoft-newbeginnings-activity-7121495855471202304-s87Q?utm_source=share&utm_medium=member_desktop')

    if rad == 'Python For Data Science':
        st.markdown("*Python For Data Science* certification from *IBM*\n\n"
        "While learning Python For Data Science from IBM\n"
   "It was very challenging and difficult to learn\n"
 "But i would like to learn more difficult courses in future")
        st.link_button('See P&S certificate', 'https://www.linkedin.com/posts/hemanth-reddy-mukkamalla-3b6491269_ibm-pythonfordatascience-activity-7089784711048278016-ilhz?utm_source=share&utm_medium=member_desktop')

if page == 'Projects':
    st.header('Projects :')
    project = st.selectbox('select project',['Default','Garbage Collector','College Students Study Materials','Bus Tracking'])

    if project== 'Default':
       st.caption('Select a project from above menu')
    if project == 'Garbage Collector':
        st.write('Garbage Collector')

        with st.expander('Detailed Description'):
            st.markdown("Garbage Collection Project")
            st.markdown("Hackathon Garbage Collection Project")

        st.write('*Check Out Project*')
        st.link_button('Visit Page','www.google.com')

    if project == 'College Students Study Materials':
        st.write('COllege Students')


        st.write('*Check out Source Code here :*')
        st.link_button('Source Code','https://sites.google.com/view/audisankara/home')
    if project == 'Bus Tracking':
        st.write('Live Bus Tracking Application')

        with st.expander('Detailed Description'):
            st.markdown("Bus Tracking Project")

if page == 'Feedback':
    feed = st.slider('Please rate this page (0-10)', min_value=0, max_value=10, value=5)

    if feed < 3:
        st.info('I apologize for any disappointment. Share your suggestions:')
        st.markdown('\n\n\n\n*Please share your suggestions to help Me to improve the webpage:*')
        with st.form('Form1'):
             subm = st.text_area('Submit your suggestion')
             but1 = st.form_submit_button('Submit')
             if subm == "" and but1:
                st.warning("Please Fill the Text Field")
             elif but1:
                st.success('Your feedback is noted. Thank you for sharing your suggestions.')
    elif feed <= 5:
        st.markdown('\n\n\n\n*Please share your suggestions to help Me to improve the webpage:*')
        with st.form('Form2'):
             sub = st.text_area('Submit your suggestion')
             but2 = st.form_submit_button('Submit')
             if sub == "" and but2:
                st.warning('Please Fill the Text Field')
             elif but2:
                st.success('Your feedback is noted. Thank you for sharing your suggestions.')

    elif feed > 7:
        st.success('Thank you for providing your Positive rating!')
    elif feed > 5:
        suggestion = st.chat_input('Any suggestions to enhance the site?')
        if suggestion:
           st.success('Your feedback is noted. Thank you for sharing your suggestions.')
if page == 'Resume':
   st.header('Resume :')
   st.link_button('See Resume', 'https://res.cloudinary.com/dzvzvj8nd/image/upload/v1706630876/Screenshot_2024-01-30_213406_bmu7yp.png')
   st.markdown('### Dowload Resume Here :')