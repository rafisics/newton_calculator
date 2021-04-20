import streamlit as st
import math

#############
# Functions #
#############

def _ask(variable):
    return st.number_input(f'{variable} :', step=None, format='%f')

def ask(*variables):                    #  https://codereview.stackexchange.com/a/259470/230104
    return [_ask(variable) for variable in variables]

def check_variables(variables, values):    #  https://codereview.stackexchange.com/a/259505/230104
    for variable, flag in variables.items():
        if flag != (variable in values):
            return False
    return True

##############
# Dictionary #
##############

strings = {
  'বাংলা': {
    'title': "<div><h1 style='text-align: center; color: #ff7903; font-family: Solaimanlipi'> গতি-সমীকরণ ক্যালকুলেটর </h1></div>",
    'about': 'নিউটনিয়ান গতি-সমীকরণগুলো (SUVAT সমীকরণ) দিয়ে সমত্বরণে চলমান বস্তুর গতীয় চলকগুলো হিসাব করতে এই ক্যালকুলেটরটি আপনাকে সাহায্য করবে।',
    'select': 'যে চলক তিনটির মান আপনি জানেন, তাদেরকে নির্বাচন করুন:',
    's': 'সরণ',
    'u': 'আদিবেগ',
    'v': 'শেষবেগ',
    'a': 'ত্বরণ',
    't': 'সময়',
    'min3': 'কমপক্ষে যেকোন তিনটি চলক নির্বাচন করুন যাদের মান আপনার জানা আছে।',
    'insert': 'আপনার নির্বাচিত ৩টা চলকের মান একই ইউনিট সিস্টেমে লিখুন। সেই অনুযায়ী এই ক্যালকুলেটর বাকি ২টা চলকের মান হিসাব করে জানিয়ে দিবে।',
    'max3': 'সর্ব্বোচ্চ যেকোন তিনটি চলক নির্বাচন করুন যাদের মান আপনার জানা আছে।',
    'button': 'বাকি দুই চলকের অজানা মান সমীকরণসহ জানতে এখানে ক্লিক করুন',
    'eqns': 'মান নির্ণয়ে ব্যবহৃত সমীকরণদ্বয়:\n',
    'here': 'এখানে',
    'notallow': 'বসালে চলবে না।',
    'inserting': 'আপনার দেওয়া মানগুলো উক্ত সমীকরণদ্বয়ে বসিয়ে পাই:',
  },
  'English': {
    'title': "<div><h1 style='text-align: center; color: #ff7903; font-family: Chewy'> SUVAT Calculator </h1></div>",
    'about': 'This calculator app will help to calculate the variables of the Newtonian equations of linear motion aka SUVAT equations.',
    'select': 'Select any 3 known-valued variables:',
    's': 'Displacement',
    'u': 'Initial Velocity',
    'v': 'Final Velocity',
    'a': 'Acceleration',
    't': 'Time',
    'min3': 'Select at least 3 variables.',
    'insert': 'Enter their values in the same unit system. Accordingly, this calculator will return the values of the remaining 2 variables.',
    'max3': 'Select only 3 variables.',
    'button': 'Click here to get the values of the rest two variables with equations',
    'eqns': 'The equations which are used to determine the values:\n',
    'here': 'Here',
    'notallow': 'is not allowed.',
    'inserting': 'Inserting your given values in these equations, we get:',
  }
}

############
# Main App #
############

def app(strs):
    st.markdown(strs['title'], unsafe_allow_html=True)
    st.write(strs['about'])
    st.write(strs['select'])
    opts = [ ('s', strs['s']), ('u', strs['u']), ('v', strs['v']), ('a', strs['a']), ('t', strs['t']) ]
    known_variables = {symbol: st.checkbox(f"{name} ({symbol})") for symbol, name in opts}    # https://codereview.stackexchange.com/a/259472/230104

    if sum(known_variables.values()) <3:
        st.write(strs['min3'])
    elif sum(known_variables.values()) == 3:
        st.write(strs['insert'])
    else:
        st.write(strs['max3'])

    if check_variables(known_variables, ['u', 'v', 't']):    # [u, v, t]
        u, v, t = ask(strs['u']+' (u)', strs['v']+' (v)', strs['t']+' (t)')
        if st.button(strs['button']) is True:
            st.write(strs['eqns'] +
            '$$\n' +
            's = \\frac{1}{2}(u+v)t, \\quad a = \\frac{v-u}{t}' +
            '$$')
            s = 0.5*(u+v)*t
            try:
                a = (v-u)/t
            except ZeroDivisionError:
                st.write(strs['here']+' $t=0$ '+strs['notallow'])
                a = None
            st.write(strs['inserting'])
            st.write(strs['s']+' $(s) = \\frac{1}{2}(u+v)t =$ ', s)
            st.write(strs['a']+' $(a) = \\frac{v-u}{t} =$ ', a)

    elif check_variables(known_variables, ['u', 'v', 'a']):  # [u, v, a]
        u, v, a = ask(strs['u']+' (u)', strs['v']+' (v)',  strs['a']+' (a)')
        if st.button(strs['button']) is True:
            st.write(strs['eqns'] +
            '$$\n' +
            's = \\frac{v^2-u^2}{2a}, \\quad t = \\frac{v-u}{a}' +
            '$$')
            try:
                s = (v*v - u*u)/(2*a)
                t = (v - u)/a
            except ZeroDivisionError:
                st.write(strs['here']+' $a=0$ '+strs['notallow'])
                s = None
                t = None
            st.write(strs['inserting'])
            st.write( strs['s']+' $(s) = \\frac{v^2-u^2}{2a} =$ ', s)
            st.write( strs['t']+' $(t) = \\frac{v-u}{a} =$ ', t)

    elif check_variables(known_variables, ['u', 'a', 't']): # [u, a, t]
        u, a, t = ask(strs['u']+' (u)',  strs['a']+' (a)',  strs['t']+' (t)')
        if st.button(strs['button']) is True:
            st.write(strs['eqns'] +
            '$$\n' +
            's = ut + \\frac{1}{2}at^2, \\quad v = u + at' +
            '$$')
            s = u*t + 0.5*a*t*t
            v = u + a*t
            st.write(strs['inserting'])
            st.write( strs['s']+' $(s) = ut + \\frac{1}{2}at^2 =$ ', s)
            st.write( strs['v']+' $(v) = u + at =$ ', v)

    elif check_variables(known_variables, ['v', 'a', 't']):  # [v, a, t]
        v, a, t = ask(strs['v']+' (v)',  strs['a']+' (a)',  strs['t']+' (t)')
        if st.button(strs['button']) is True:
            st.write(strs['eqns'] +
            '$$\n' +
            's = vt - \\frac{1}{2}at^2, \\quad u= v - at' +
            '$$')
            s = v*t - 0.5*a*t*t
            u = v - a*t
            st.write(strs['inserting'])
            st.write( strs['s']+' $(s) = vt - \\frac{1}{2}at^2 =$ ', s)
            st.write( strs['u']+' $(u) = v - at =$ ', u)

    elif check_variables(known_variables, ['s', 'a', 't']):  # [s, a, t]
        s, a, t = ask( strs['s']+' (s)',  strs['a']+' (a)',  strs['t']+' (t)')
        if st.button(strs['button']) is True:
            st.write(strs['eqns'] +
            '$$\n' +
            'u = \\frac{s}{t} - \\frac{1}{2}at, \\quad v = \\frac{s}{t} + \\frac{1}{2}at' +
            '$$')
            try:
                u = (s - 0.5*a*t*t)/t
                v = (s + 0.5*a*t*t)/t
            except ZeroDivisionError:
                st.write(strs['here']+' $t=0$ '+strs['notallow'])
                u = None
                v = None
            st.write(strs['inserting'])
            st.write( strs['u']+' $(u) = \\frac{s}{t} - \\frac{1}{2}at =$ ', u)
            st.write( strs['v']+' $(v) = \\frac{s}{t} + \\frac{1}{2}at =$ ', v)

    elif check_variables(known_variables, ['s', 'v', 't']):  # [s, v, t]
        s, v, t = ask( strs['s']+' (s)', strs['v']+' (v)',  strs['t']+' (t)')
        if st.button(strs['button']) is True:
            st.write(strs['eqns'] +
            '$$\n' +
            'u = \\frac{2s}{t} - v, \\quad a = \\frac{2(vt-s)}{t^2}' +
            '$$')
            try:
                u = (2*s)/t - v
                a = 2*(v*t-s)/(t*t)
            except ZeroDivisionError:
                st.write(strs['here']+' $t=0$ '+strs['notallow'])
                u = None
                a = None
            st.write(strs['inserting'])
            st.write( strs['u']+' $(u) = \\frac{2s}{t} - v =$ ', u)
            st.write( strs['a']+' $(a)  = \\frac{2(vt-s)}{t^2} =$ ', a)

    elif check_variables(known_variables, ['s', 'v', 'a']):  # [s, v, a]
        s, v, a = ask( strs['s']+' (s)', strs['v']+' (v)',  strs['a']+' (a)')
        if st.button(strs['button']) is True:
            st.write(strs['eqns'] +
            '$$\n' +
            'u = \\sqrt{v^2 -2as}, \\quad t = \\frac{v}{a} - \\frac{\\sqrt{v^2 - 2as}}{a}' +
            '$$')
            try:
                u = math.sqrt(v*v - 2*a*s)
                t = v/a - math.sqrt(v*v - 2*a*s)/a
            except ZeroDivisionError:
                st.write(strs['here']+' $a=0$ '+strs['notallow'])
                t = None
            except ValueError:
                st.write(strs['here']+' $v^2 < 2as$ '+strs['notallow'])
                u = None
                t = None
            st.write(strs['inserting'])
            st.write( strs['u']+' $(u) = \\sqrt{v^2 -2as} =$ ', u)
            st.write( strs['t']+'  $(t)= \\frac{v}{a} - \\frac{\\sqrt{v^2 - 2as}}{a} =$ ', t)

    elif check_variables(known_variables, ['s', 'u', 't']):  # [s, u, t]
        s, u, t = ask( strs['s']+' (s)', strs['u']+' (u)',  strs['t']+' (t)')
        if st.button(strs['button']) is True:
            st.write(strs['eqns'] +
            '$$\n' +
            'v = \\frac{2s}{t}-u, \\quad a = \\frac{2(s-ut)}{t^2}' +
            '$$')
            try:
                v = (2*s)/t - u
                a = 2*(s-u*t)/(t*t)
            except ZeroDivisionError:
                st.write(strs['here']+' $t=0$ '+strs['notallow'])
                v = None
                a = None
            st.write(strs['inserting'])
            st.write( strs['v']+' $(v) = \\frac{2s}{t}-u =$ ', v)
            st.write( strs['a']+' $(a)= \\frac{2(s-ut)}{t^2} =$ ', a)

    elif check_variables(known_variables, ['s', 'u', 'a']):  # [s, u, a]
        s, u, a = ask( strs['s']+' (s)', strs['u']+' (u)',  strs['a']+' (a)')
        if st.button(strs['button']) is True:
            st.write(strs['eqns'] +
            '$$\n' +
            'v = \\sqrt{u^2 + 2as}, \\quad t = -\\frac{u}{a} + \\frac{\\sqrt{u^2 + 2as}}{a}' +
            '$$')
            try:
                v = math.sqrt(u*u + 2*a*s)
                t = -u/a + math.sqrt(u*u +2*a*s)/a
            except ZeroDivisionError:
                st.write(strs['here']+' $a=0$ '+strs['notallow'])
                t = None
            except ValueError:
                st.write(strs['here']+' $v^2 < 2as$ '+strs['notallow'])
                v = None
                t = None
            st.write(strs['inserting'])
            st.write( strs['v']+' $(v) = \\sqrt{u^2 + 2as} =$ ', v)
            st.write( strs['t']+' $(t) = -\\frac{u}{a} + \\frac{\\sqrt{u^2 + 2as}}{a} =$ ', t)

    elif check_variables(known_variables, ['s', 'u', 'v']):  # [s, u, v]
        s, u, v = ask( strs['s']+' (s)', strs['u']+' (u)', strs['v']+' (v)')
        if st.button(strs['button']) is True:
            st.write(strs['eqns'] +
            '$$\n' +
            'a = \\frac{v^2 - u^2}{2s}, \\quad t = \\frac{2s}{u+v}' +
            '$$')
            try:
                a = (v*v - u*u)/(2*s)
            except ZeroDivisionError:
                st.write(strs['here']+' $s=0$ '+strs['notallow'])
                a = None
            try:
                t = (2*s)/(u+v)
            except ZeroDivisionError:
                st.write(strs['here']+' $u+v=0$ '+strs['notallow'])
                t = None
            st.write(strs['inserting'])
            st.write( strs['a']+' $(a) = \\frac{v^2 - u^2}{2s} =$ ', a)
            st.write( strs['t']+' $(t) = \\frac{2s}{u+v} =$ ', t)

lang = st.sidebar.radio('Select Language:', ['বাংলা', 'English'], index=0)
app(strings[lang])
