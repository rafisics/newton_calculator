import streamlit as st


#############
# Variables #
#############
def ask_u():
    u = st.number_input('আদিবেগ (u) :')
    return u

def ask_v():
    u = st.number_input('অন্তবেগ (v) :')
    return u

def ask_a():
    u = st.number_input('ত্বরণ (a) :')
    return u

def ask_t():
    u = st.number_input('সময় (t) :')
    return u



############
# Main App #
############
st.title('গতিসূত্র ক্যালকুলেটর')

st.write('v=u+at গতিসূত্রের হিসাব বের করতে এই ক্যালকুলেটরটি আপনাকে সাহায্য করবে।')

option = st.selectbox('কোন চলকের মান বের করতে চান? নিচের ড্রপডাউন থেকে নির্ধারণ করুন:', ['চলক সনাক্ত করুন', 'আদিবেগ (u)', 'অন্তবেগ (v)', 'ত্বরণ (a)', 'সময় (t)'])

if option == 'আদিবেগ (u)':
    v = ask_v()
    a = ask_a()
    t = ask_t()
    u = v - (a*t)
    st.write('u, আদিবেগ = ', u)
elif option == 'অন্তবেগ (v)':
    a = ask_a()
    t = ask_t()
    u = ask_u()
    v = u + (a*t)
    st.write('v, শেষবেগ = ', v)
elif option == 'ত্বরণ (a)':
    t = ask_t()
    u = ask_u()
    v = ask_v()
    a = (v-u)/t
    st.write('a, ত্বরণ = ', a)
elif option == 'সময় (t)':
    a = ask_a()
    u = ask_u()
    v = ask_v()
    t = (v - u) / a
    st.write('t, সময় = ', t)
else:
    st.write('উপরে কোন চলকের মান গণনা করতে চান সেটা ঠিক করলে বাকি চলকগুলো এখানে নিচে চলে আসবে')
