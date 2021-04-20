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

############
# Main App #
############

st.markdown("<div><h1 style='text-align: center; color: #ff7903; font-family: Chewy'> SUVAT Calculator </h1></div>", unsafe_allow_html=True)

st.write('This calculator app will help to calculate the variables of the Newtonian equations of linear motion aka SUVAT equations.')

st.write('Select any 3 known-valued variables:')

opts = [ ('s', 'Displacement'), ('u', 'Initial Velocity'), ('v', 'Final Velocity'), ('a', 'Acceleration'), ('t', 'Time') ]

known_variables = {symbol: st.checkbox(f"{name} ({symbol})") for symbol, name in opts}    # https://codereview.stackexchange.com/a/259505/230104

if sum(known_variables.values()) < 3:
    st.write('Select at least 3 variables.')
elif sum(known_variables.values()) == 3:
   st.write('Enter their values in the same unit system. Accordingly, this calculator will return the values of the remaining 2 variables. ')
elif sum(known_variables.values()) > 3:
    st.write('Select only 3 variables.')

if check_variables(known_variables, ['u', 'v', 't']):    # ['Initial Velocity (u)', 'Final Velocity (v)', 'Time (t)']
    u, v, t = ask('Initial Velocity (u)', 'Final Velocity (v)', 'Time (t)')
    if st.button('Click here to get the values of the rest two variables with equations') is True:
        st.write('The equations which are used to determine the values:\n' +
        '$$\n' +
        's = \\frac{1}{2}(u+v)t, \\quad a = \\frac{v-u}{t}' +
        '$$')
        s = 0.5*(u+v)*t
        try:
            a = (v-u)/t
        except ZeroDivisionError:
            st.write('Here $t=0$ is not allowed.')
            a = None
        st.write('Inserting your given values in these equations, we get: ')
        st.write('Displacement $(s) = \\frac{1}{2}(u+v)t =$ ', s)
        st.write('Acceleration $(a) = \\frac{v-u}{t} =$ ', a)

elif check_variables(known_variables, ['u', 'v', 'a']):   # ['Initial Velocity (u)', 'Final Velocity (v)', 'Acceleration (a)']
    u, v, a = ask('Initial Velocity (u)', 'Final Velocity (v)', 'Acceleration (a)')
    if st.button('Click here to get the values of the rest two variables with equations') is True:
        st.write('The equations which are used to determine the values:\n' +
        '$$\n' +
        's = \\frac{v^2-u^2}{2a}, \\quad t = \\frac{v-u}{a}' +
        '$$')
        try:
            s = (v*v - u*u)/(2*a)
            t = (v - u)/a
        except ZeroDivisionError:
            st.write('Here $a=0$ is not allowed.')
            s = None
            t = None
        st.write('Inserting your given values in these equations, we get: ')
        st.write('Displacement $(s) = \\frac{v^2-u^2}{2a} =$ ', s)
        st.write('Time $(t) = \\frac{v-u}{a} =$ ', t)

elif check_variables(known_variables, ['u', 'a', 't']):  # ['Initial Velocity (u)', 'Acceleration (a)', 'Time (t)']
    u, a, t = ask('Initial Velocity (u)', 'Acceleration (a)', 'Time (t)')
    if st.button('Click here to get the values of the rest two variables with equations') is True:
        st.write('The equations which are used to determine the values:\n' +
        '$$\n' +
        's = ut + \\frac{1}{2}at^2, \\quad v = u + at' +
        '$$')
        s = u*t + 0.5*a*t*t
        v = u + a*t
        st.write('Inserting your given values in these equations, we get: ')
        st.write('Displacement $(s) = ut + \\frac{1}{2}at^2 =$ ', s)
        st.write('Final Velocity $(v) = u + at =$ ', v)

elif check_variables(known_variables, ['v', 'a', 't']):   # ['Final Velocity (v)', 'Acceleration (a)', 'Time (t)']
    v, a, t = ask('Final Velocity (v)', 'Acceleration (a)', 'Time (t)')
    if st.button('Click here to get the values of the rest two variables with equations') is True:
        st.write('The equations which are used to determine the values:\n' +
        '$$\n' +
        's = vt - \\frac{1}{2}at^2, \\quad u= v - at' +
        '$$')
        s = v*t - 0.5*a*t*t
        u = v - a*t
        st.write('Inserting your given values in these equations, we get: ')
        st.write('Displacement $(s) = vt - \\frac{1}{2}at^2 =$ ', s)
        st.write('Initial Velocity $(u) = v - at =$ ', u)

elif check_variables(known_variables, ['s', 'a', 't']):   # ['Displacement (s)', 'Acceleration (a)', 'Time (t)']
    s, a, t = ask('Displacement (s)', 'Acceleration (a)', 'Time (t)')
    if st.button('Click here to get the values of the rest two variables with equations') is True:
        st.write('The equations which are used to determine the values:\n' +
        '$$\n' +
        'u = \\frac{s}{t} - \\frac{1}{2}at, \\quad v = \\frac{s}{t} + \\frac{1}{2}at' +
        '$$')
        try:
            u = (s - 0.5*a*t*t)/t
            v = (s + 0.5*a*t*t)/t
        except ZeroDivisionError:
            st.write('Here $t=0$ is not allowed.')
            u = None
            v = None
        st.write('Inserting your given values in these equations, we get: ')
        st.write('Initial Velocity $(u) = \\frac{s}{t} - \\frac{1}{2}at =$ ', u)
        st.write('Final Velocity $(v) = \\frac{s}{t} + \\frac{1}{2}at =$ ', v)

elif check_variables(known_variables, ['s', 'v', 't']):   # ['Displacement (s)', 'Final Velocity (v)', 'Time (t)']
    s, v, t = ask('Displacement (s)', 'Final Velocity (v)', 'Time (t)')
    if st.button('Click here to get the values of the rest two variables with equations') is True:
        st.write('The equations which are used to determine the values:\n' +
        '$$\n' +
        'u = \\frac{2s}{t} - v, \\quad a = \\frac{2(vt-s)}{t^2}' +
        '$$')
        try:
            u = (2*s)/t - v
            a = 2*(v*t-s)/(t*t)
        except ZeroDivisionError:
            st.write('Here $t=0$ is not allowed.')
            u = None
            a = None
        st.write('Inserting your given values in these equations, we get: ')
        st.write('Initial Velocity $(u) = \\frac{2s}{t} - v =$ ', u)
        st.write('Acceleration $(a)  = \\frac{2(vt-s)}{t^2} =$ ', a)

elif check_variables(known_variables, ['s', 'v', 'a']):   # ['Displacement (s)', 'Final Velocity (v)', 'Acceleration (a)']
    s, v, a = ask('Displacement (s)', 'Final Velocity (v)', 'Acceleration (a)')
    if st.button('Click here to get the values of the rest two variables with equations') is True:
        st.write('The equations which are used to determine the values:\n' +
        '$$\n' +
        'u = \\sqrt{v^2 -2as}, \\quad t = \\frac{v}{a} - \\frac{\\sqrt{v^2 - 2as}}{a}' +
        '$$')
        try:
            u = math.sqrt(v*v - 2*a*s)
            t = v/a - math.sqrt(v*v - 2*a*s)/a
        except ZeroDivisionError:
            st.write('Here $a=0$ is not allowed.')
            t = None
        except ValueError:
            st.write('Here $v^2 < 2as$ is not allowed.')
            u = None
            t = None
        st.write('Inserting your given values in these equations, we get: ')
        st.write('Initial Velocity $(u) = \\sqrt{v^2 -2as} =$ ', u)
        st.write('Time $(t)= \\frac{v}{a} - \\frac{\\sqrt{v^2 - 2as}}{a} =$ ', t)

elif check_variables(known_variables, ['s', 'u', 't']):   # ['Displacement (s)', 'Initial Velocity (u)', 'Time (t)']
    s, u, t = ask('Displacement (s)', 'Initial Velocity (u)', 'Time (t)')
    if st.button('Click here to get the values of the rest two variables with equations') is True:
        st.write('The equations which are used to determine the values:\n' +
        '$$\n' +
        'v = \\frac{2s}{t}-u, \\quad a = \\frac{2(s-ut)}{t^2}' +
        '$$')
        try:
            v = (2*s)/t - u
            a = 2*(s-u*t)/(t*t)
        except ZeroDivisionError:
            st.write('Here $t=0$ is not allowed.')
            v = None
            a = None
        st.write('Inserting your given values in these equations, we get: ')
        st.write('Final Velocity $(v) = \\frac{2s}{t}-u =$ ', v)
        st.write('Acceleration $(a)= \\frac{2(s-ut)}{t^2} =$ ', a)

elif check_variables(known_variables, ['s', 'u', 'a']):   # ['Displacement (s)', 'Initial Velocity (u)', 'Acceleration (a)']
    s, u, a = ask('Displacement (s)', 'Initial Velocity (u)', 'Acceleration (a)')
    if st.button('Click here to get the values of the rest two variables with equations') is True:
        st.write('The equations which are used to determine the values:\n' +
        '$$\n' +
        'v = \\sqrt{u^2 + 2as}, \\quad t = -\\frac{u}{a} + \\frac{\\sqrt{u^2 + 2as}}{a}' +
        '$$')
        try:
            v = math.sqrt(u*u + 2*a*s)
            t = -u/a + math.sqrt(u*u +2*a*s)/a
        except ZeroDivisionError:
            st.write('Here $a=0$ is not allowed.')
            t = None
        except ValueError:
            st.write('Here $v^2 < 2as$ is not allowed.')
            v = None
            t = None
        st.write('Inserting your given values in these equations, we get: ')
        st.write('Final Velocity $(v) = \\sqrt{u^2 + 2as} =$ ', v)
        st.write('Time $(t) = -\\frac{u}{a} + \\frac{\\sqrt{u^2 + 2as}}{a} =$ ', t)

elif check_variables(known_variables, ['s', 'u', 'v']):   # ['Displacement (s)', 'Initial Velocity (u)', 'Final Velocity (v)']
    s, u, v = ask('Displacement (s)', 'Initial Velocity (u)', 'Final Velocity (v)')
    if st.button('Click here to get the values of the rest two variables with equations') is True:
        st.write('The equations which are used to determine the values:\n' +
        '$$\n' +
        'a = \\frac{v^2 - u^2}{2s}, \\quad t = \\frac{2s}{u+v}' +
        '$$')
        try:
            a = (v*v - u*u)/(2*s)
        except ZeroDivisionError:
            st.write('Here $s=0$ is not allowed.')
            a = None
        try:
            t = (2*s)/(u+v)
        except ZeroDivisionError:
            st.write('Here $u+v=0$ is not allowed.')
            t = None
        st.write('Inserting your given values in these equations, we get: ')
        st.write('Acceleration $(a) = \\frac{v^2 - u^2}{2s} =$ ', a)
        st.write('Time $(t) = \\frac{2s}{u+v} =$ ', t)
