import streamlit as st
import math

#############
# Functions #
#############

def _ask(variable):
    return st.number_input(f'{variable} :', step=None, format='%f')

############
# Main App #
############

st.markdown("<h1 style='text-align: center; color: #ff7903; font-family: Solaimanlipi'> SUVAT Calculator </h1>", unsafe_allow_html=True)

st.write('This calculator app will help to calculate the variables of the Newtonian equations of linear motion aka SUVAT equations.')

st.write('Select any 3 known-valued variables:')

option_s = st.checkbox('Displacement (s)')
option_u = st.checkbox('Initial Velocity (u)')
option_v = st.checkbox('Final Velocity (v)')
option_a = st.checkbox('Acceleration (a)')
option_t = st.checkbox('Time (t)')
known_variables = option_s + option_u + option_v + option_a + option_t

if known_variables <3:
    st.write('Select at least 3 variables.')
elif known_variables == 3:
   st.write('Enter their values in the same unit system. Accordingly, this calculator will return the values of the remaining 2 variables. ')
elif known_variables >3:
    st.write('Select only 3 variables.')

if (option_s is False and option_u and option_v and option_a is False and option_t):    # ['Initial Velocity (u)', 'Final Velocity (v)', 'Time (t)']
    u = ask('Initial Velocity (u)')
    v = ask('Final Velocity (v)')
    t = ask('Time (t)')
    if st.button('Click here to calculate and check the necessary equations') is True:
        st.write("""        The equations which are used to determine the values::
        $$
        s = \\frac{1}{2}(u+v)t, \\quad a = \\frac{v-u}{t}
        $$      """)
        s = 0.5*(u+v)*t
        try:
            a = (v-u)/t
        except ZeroDivisionError:
            st.write('Here $t=0$ is not allowed.')
            a = None
        st.write('Inserting your given values in these equations, we get: ')
        st.write('Displacement $(s) = \\frac{1}{2}(u+v)t =$ ', s)
        st.write('Acceleration $(a) = \\frac{v-u}{t} =$ ', a)

elif (option_s is False and option_u and option_v and option_a and option_t is False):  # ['Initial Velocity (u)', 'Final Velocity (v)', 'Acceleration (a)']
    u = ask('Initial Velocity (u)')
    v = ask('Final Velocity (v)')
    a = ask('Acceleration (a)')
    if st.button('Click here to calculate and check the necessary equations') is True:
        st.write("""        The equations which are used to determine the values::
        $$
        s = \\frac{v^2-u^2}{2a}, \\quad t = \\frac{v-u}{a}
        $$      """)
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

elif (option_s is False and option_u and option_v is False  and option_a and option_t): # ['Initial Velocity (u)', 'Acceleration (a)', 'Time (t)']
    u = ask('Initial Velocity (u)')
    a = ask('Acceleration (a)')
    t = ask('Time (t)')
    if st.button('Click here to calculate and check the necessary equations') is True:
        st.write("""        The equations which are used to determine the values::
        $$
        s = ut + \\frac{1}{2}at^2, \\quad v = u + at
        $$      """)
        s = u*t + 0.5*a*t*t
        v = u + a*t
        st.write('Inserting your given values in these equations, we get: ')
        st.write('Displacement $(s) = ut + \\frac{1}{2}at^2 =$ ', s)
        st.write('Final Velocity $(v) = u + at =$ ', v)

elif (option_s is False and option_u is False and option_v and option_a and option_t):  # ['Final Velocity (v)', 'Acceleration (a)', 'Time (t)']
    v = ask('Final Velocity (v)')
    a = ask('Acceleration (a)')
    t = ask('Time (t)')
    if st.button('Click here to calculate and check the necessary equations') is True:
        st.write("""        The equations which are used to determine the values::
        $$
        s = vt - \\frac{1}{2}at^2, \\quad u= v - at
        $$      """)
        s = v*t - 0.5*a*t*t
        u = v - a*t
        st.write('Inserting your given values in these equations, we get: ')
        st.write('Displacement $(s) = vt - \\frac{1}{2}at^2 =$ ', s)
        st.write('Initial Velocity $(u) =u - at =$ ', u)

elif (option_s and option_u is False and option_v is False and option_a and option_t):  # ['Displacement (s)', 'Acceleration (a)', 'Time (t)']
    s = ask('Displacement (s)')
    a = ask('Acceleration (a)')
    t = ask('Time (t)')
    if st.button('Click here to calculate and check the necessary equations') is True:
        st.write("""        The equations which are used to determine the values::
        $$
        u = \\frac{s}{t} - \\frac{1}{2}at, \\quad v = \\frac{s}{t} + \\frac{1}{2}at
        $$      """)
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

elif (option_s and option_u is False and option_v and option_a is False and option_t):  # ['Displacement (s)', 'Final Velocity (v)', 'Time (t)']
    s = ask('Displacement (s)')
    v = ask('Final Velocity (v)')
    t = ask('Time (t)')
    if st.button('Click here to calculate and check the necessary equations') is True:
        st.write("""        The equations which are used to determine the values::
        $$
        u = \\frac{2s}{t} - v, \\quad a = \\frac{2(vt-s)}{t^2}
        $$      """)
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

elif (option_s and option_u is False and option_v and option_a and option_t is False):  # ['Displacement (s)', 'Final Velocity (v)', 'Acceleration (a)']
    s = ask('Displacement (s)')
    v = ask('Final Velocity (v)')
    a = ask('Acceleration (a)')
    if st.button('Click here to calculate and check the necessary equations') is True:
        st.write("""        The equations which are used to determine the values::
        $$
        u = \\sqrt{v^2 -2as}, \\quad t = \\frac{v}{a} - \\frac{\\sqrt{v^2 - 2as}}{a}
        $$      """)
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

elif (option_s and option_u and option_v is False and option_a is False and option_t):  # ['Displacement (s)', 'Initial Velocity (u)', 'Time (t)']
    s = ask('Displacement (s)')
    u = ask('Initial Velocity (u)')
    t = ask('Time (t)')
    if st.button('Click here to calculate and check the necessary equations') is True:
        st.write("""        The equations which are used to determine the values::
        $$
        v = \\frac{2s}{t}-u, \\quad a = \\frac{2(s-ut)}{t^2}
        $$      """)
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

elif (option_s and option_u and option_v is False and option_a and option_t is False):  # ['Displacement (s)', 'Initial Velocity (u)', 'Acceleration (a)']
    s = ask('Displacement (s)')
    u = ask('Initial Velocity (u)')
    a = ask('Acceleration (a)')
    if st.button('Click here to calculate and check the necessary equations') is True:
        st.write("""        The equations which are used to determine the values::
        $$
        v = \\sqrt{u^2 + 2as}, \\quad t = -\\frac{u}{a} + \\frac{\\sqrt{u^2 + 2as}}{a}
        $$      """)
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

elif (option_s and option_u and option_v and option_a is False and option_t is False):  # ['Displacement (s)', 'Initial Velocity (u)', 'Final Velocity (v)']
    s = ask('Displacement (s)')
    u = ask('Initial Velocity (u)')
    v = ask('Final Velocity (v)')
    if st.button('Click here to calculate and check the necessary equations') is True:
        st.write("""        The equations which are used to determine the values::
        $$
        a = \\frac{v^2 - u^2}{2s}, \\quad t = \\frac{2s}{u+v}
        $$      """)
        try:
            a = (v*v - u*u)/(2*s)
        except ZeroDivisionError:
            st.write('Here $s=0$ is not allowed.')
            a = None
        try:
            t = (2*s)/(u+v)
        except ZeroDivisionError:
            st.write('Here $u=v=0$ is not allowed.')
            t = None
        st.write('Inserting your given values in these equations, we get: ')
        st.write('Acceleration $(a) = \\frac{v^2 - u^2}{2s} =$ ', a)
        st.write('Time $(t) = \\frac{2s}{u+v} =$ ', t)
