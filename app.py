import streamlit as st 
import mysql.connector 

conn=mysql.connector.connect(
        # host="localhost",
        user="root",
        password="root",
        database="mydbfromlocal"
    )


def userregister(u,e,p):
    cur=conn.cursor()

    query="""insert into login values(%s,%s,%s)"""
    value=(u,e,p)

    cur.execute(query,value)
    conn.commit()
    conn.close()

    return "success"

def userlogin(u,p):
    cursor=conn.cursor()
    try:
        query="select * from login where email=%s and password=%s"
        value=(u,p)
        # print(query)
        cursor.execute(query,value)
        obj=cursor.fetchone()
        return obj
    except Exception as e:
        print("an error occured")

def dashboard():
    st.title("welcome to dashboard...")
    st.write(f"welcome{st.session_state.user}")
    if st.button("logout"):
        st.session_state.logged_in=False
        st.session_state.user=None
        st.rerun()

def main():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.user = None

    # If user is logged in, show dashboard only
    if st.session_state.logged_in:
        dashboard()
    else:
        menu=["login","register"]

        c=st.sidebar.selectbox("Menu",menu)

        if c=="register":
            username=st.text_input("enter username here.")
            Email=st.text_input("enter Email here.")
            password=st.text_input("enter password here.")
            if st.button("submit"):
                val=userregister(username,Email,password)
                st.success(f"registered successfulll")
        elif c=="login":
            Email=st.text_input("enter Email here.")
            password=st.text_input("enter password here.")
            if st.button("submit"):
                val1=userlogin(Email,password)
                if val1:
                    st.session_state.logged_in=True
                    st.session_state.user=Email
                    st.rerun()
                
                    # print(val1)
                else:
                    st.error("failed")

if __name__=='__main__':
    main()


