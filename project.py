import pandas as pd
import mysql.connector
import streamlit as st 
from streamlit_option_menu import option_menu  #used for selecting an option from list of options in a menu
import plotly.express as px 
import plotly.graph_objects as go
from tabulate import tabulate
import altair as alt

#each bus we have to filter
#now we have to take route_name from each dataframe and then append to list

#kerala bus
kerala=[]
df_k=pd.read_csv("df_k.csv")
for i,r in df_k.iterrows():  #traverse through each row
    kerala.append(r['Route_name'])   # add that row in new list


#Andhra bus
andhra=[]
df_a=pd.read_csv("df_a.csv")
for i,r in df_a.iterrows():
    andhra.append(r['Route_name'])

#Assam bus
assam=[]
df_as=pd.read_csv("df_as.csv")
for i,r in df_as.iterrows():
    assam.append(r['Route_name'])


#goa bus
goa=[]
df_g=pd.read_csv("df_g.csv")
for i,r in df_g.iterrows():
    goa.append(r['Route_name'])
    
#telungana
telungana=[]
df_t=pd.read_csv("df_t.csv")
for i,r in df_t.iterrows():
    telungana.append(r['Route_name'])

#haryana
haryana=[]
df_h=pd.read_csv("df_h.csv")
for i,r in df_h.iterrows():
    haryana.append(r['Route_name'])

#punjab bus
punjab=[]
df_pb=pd.read_csv("df_pb.csv")
for i,r in df_pb.iterrows():
    punjab.append(r["Route_name"])

#rajasthan bus
rajasthan=[]
df_r=pd.read_csv("df_r.csv")
for i,r in df_r.iterrows():
    rajasthan.append(r['Route_name'])
    
#south bengal bus
sbengal=[]
df_s=pd.read_csv("df_s.csv")
for i,r in df_s.iterrows():
    sbengal.append(r["Route_name"])
    
#uttar pradesh bus
up=[]
df_u=pd.read_csv("df_up.csv")
for i,r in df_u.iterrows():
    up.append(r['Route_name'])

#west bengal bus
wbengal=[]
df_wb=pd.read_csv("df_wb.csv")
for i,r in df_wb.iterrows():
    wbengal.append(r['Route_name'])

###############################################

# ---------------> STREAMLIT PART ------------>

###############################################



#setting streamlit page
st.set_page_config(layout="wide",page_icon=":material/directions_bus:",page_title="RedBus Project",initial_sidebar_state="expanded")
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://images.hdqwalls.com/wallpapers/bus-retro-56.jpg");
        background-size: cover; /* Ensures the image covers the entire container */
        background-position: center; /* Centers the image */
        background-repeat: no-repeat; /* Prevents the image from repeating */
        background-attachment: fixed; /* Fixes the image in place when scrolling */
        height: 100vh; /* Sets the height to 100% of the viewport height */
        width: 100vw; /* Sets the width to 100% of the viewport width */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <style>
    [data-testid="stSidebar"] {{
        background-color: #60191900; /* Replace with your desired color */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    /* Ensure font size does not change on hover */
    .nav-link {
        font-size: 18px !important;
    }
    .nav-link:hover {
        font-size: 18px !important;
        color: #32789e !important; /* Change only the color on hover */
    }
    .nav-link-selected {
        font-size: 20px !important;
    }
    </style>
    """,unsafe_allow_html=True
)




# Theme button in the sidebar



with st.sidebar:
    #THEME CONTROL  OPERATIONAL IN SIDEBAR
    
    
    menu = option_menu(
        "Main Menu", 
        ["Home", 'Bus Routes'], 
        icons=['house', 'map'], 
        menu_icon="cast", 
        default_index=0,
        styles={
            "icon":{"font-size":"21px"},
            # "nav-link-selected": {"background-color": "#0b0bdd","font-size":"20px"}
        }
    )


if menu=="Home":
    st.title(":red[:material/analytics:] :green[Redbus Data Scraping with Selenium  & Dynamic Filtering using Streamlit]")
    st.text("")
    st.subheader(" ")
    st.markdown(""" ### :violet[:material/tooltip:] :red[*Objective of the Project*]

                To Scrape the Data from Redbus Website and to create a user interface and 
     dynamic filtration of data using streamlit and SQL 
    """)
    
    dfbus=pd.read_csv("BusDetails/dfbus.csv")
    
    fig = px.scatter(dfbus, 
                 x='Price', 
                 y='Ratings', 
                 color='Bus_type',
                 size='Seats_Available',
                 hover_name='Bus_name',
                 title='Bus Price vs Ratings',
                 labels={'Price': 'Ticket Price', 'Ratings': 'Bus Ratings'})

    # Display the plot in Streamlit
    st.plotly_chart(fig)
    
    st.markdown("""
                <br><br>""",unsafe_allow_html=True)
    
    labels = dfbus['Seats_Available']
    values = dfbus['Ratings']

    # Create the Pie chart
    fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.1)])
    fig2.update_layout(
        title_text="distribution",
        title_x=0.45
    )
    st.plotly_chart(fig2)
    
    st.markdown("""
                <br><br>""",unsafe_allow_html=True)
    
    
    
    dfbus = pd.read_csv("BusDetails/dfbus.csv")

    # Create an Altair chart
    chart = alt.Chart(dfbus).mark_circle().encode(
        y='Price:Q',               # 'Price' as a quantitative (float) field
        x='Total_duration:N',      # 'total_duration' as a nominal (string) field
        color='Route_name:N',          # Adjust this to the appropriate categorical column in your data
    ).interactive()

        # Display the chart
    st.altair_chart(chart,use_container_width=True)
        
    #altair
    # Top panel is a scatter plot of Total_duration vs Price
    brush = alt.selection_interval(encodings=['x'])

# Define the click selection for interactivity
    click = alt.selection_single(encodings=['y'])

    # Top panel is a scatter plot of Total_duration vs Price
    points = (
        alt.Chart(dfbus)
        .mark_point()
        .encode(
            alt.X("Total_duration:N", title="Total Duration"),
            alt.Y("Price:Q", title="Price"),
            color=alt.condition(brush, "Bus_type:N", alt.value("lightgray")),
            size=alt.Size("Price:Q", scale=alt.Scale(range=[5, 200])),
        )
        .properties(width=550, height=300)
        .add_selection(brush)
        .transform_filter(click)
    )

    # Bottom panel is a bar chart of Bus_type
    bars = (
        alt.Chart(dfbus)
        .mark_bar()
        .encode(
            y="Bus_type:N",
            x="count():Q",
            color=alt.condition(click, alt.Color('Bus_type:N', legend=None), alt.value("lightgray")),
        )
        .transform_filter(brush)
        .properties(width=300, height=700)
        .add_selection(click)
    )
        # Combine the charts
    chart = alt.vconcat(points, bars, title="Bus Data Analysis")

    # Display the chart in Streamlit
    st.altair_chart(chart, use_container_width=True)
    
    
if menu=="Bus Routes":
    
    st.title(":green[:material/filter_alt:]    :blue[Dynamic Filtering of Data]")
    
    
    col1,col2=st.columns(2)
    with col1:
        state=st.selectbox("List of States",["Kerala", "Andhra Pradesh", "Telungana", "Goa", "Rajasthan", "Punjab",
                                          "South Bengal", "Haryana", "Assam", "Uttar Pradesh", "West Bengal"])
    with col2:
        select_type=st.selectbox("choose bus type",["A/C","NON A/C","sleeper","semi-sleeper","seater","others"])
    with col1:
        fare = st.number_input("Enter fare", min_value=40, max_value=5000, value=40, step=50)
        #select_fare = st.number_input("Enter bus fare", min_value=40, max_value=5000, value=40, step=1)
    with col2:
        select_rating = st.slider("Choose rating", min_value=1, max_value=5, value=5, step=1)
    with col1:
        TIME=st.time_input("select the time")  
    #time_str=TIME.strftime("%H:%M:%S")  
    
    #KERALA BUS FILTERATION
    if state=="Kerala":
        with col2:
            k=st.selectbox("List of routes",kerala)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",user="2NWb96BauSzhCfv.root",password="FlKt7G8RKi0SOme7",database="project",port=4000)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
    
    
    #ANDHRA
    if state=="Andhra Pradesh":
        with col2:
            k=st.selectbox("List of routes",andhra)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",user="2NWb96BauSzhCfv.root",password="FlKt7G8RKi0SOme7",database="project",port=4000)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out2=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out2,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result2 = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result2,use_container_width=True)
        
    #PUNJAB 
    
    if state=="Punjab":
        with col2:
            k=st.selectbox("List of routes",punjab)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",user="2NWb96BauSzhCfv.root",password="FlKt7G8RKi0SOme7",database="project",port=4000)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out2=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out2,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result2 = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result2,use_container_width=True)
    
    #ASSAM
    
    if state=="Assam":
        with col2:
           k=st.selectbox("List of routes",assam)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",user="2NWb96BauSzhCfv.root",password="FlKt7G8RKi0SOme7",database="project",port=4000)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
        
        
        #TELUNGANA
    
    if state=="Telungana":
        with col2:
           k=st.selectbox("List of routes",telungana)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",user="2NWb96BauSzhCfv.root",password="FlKt7G8RKi0SOme7",database="project",port=4000)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
    
    
    #HARYANA
    if state=="Haryana":
        with col2:
           k=st.selectbox("List of routes",haryana)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",user="2NWb96BauSzhCfv.root",password="FlKt7G8RKi0SOme7",database="project",port=4000)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
        
        
        #GOA 
        
    if state=="Goa":
        with col2:  
          k=st.selectbox("List of routes",goa)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",user="2NWb96BauSzhCfv.root",password="FlKt7G8RKi0SOme7",database="project",port=4000)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
    
    
    #RAJASTHAN
    if state=="Rajasthan":
        with col2:
           k=st.selectbox("List of routes",rajasthan)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",user="2NWb96BauSzhCfv.root",password="FlKt7G8RKi0SOme7",database="project",port=4000)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
    
    
    #UTTAR PRADESH
    if state=="Uttar Pradesh":
        with col2:
           k=st.selectbox("List of routes",up)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",user="2NWb96BauSzhCfv.root",password="FlKt7G8RKi0SOme7",database="project",port=4000)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
        
    #SOUTH BENGAL 
    if state=="South Bengal":
        with col2:   
           k=st.selectbox("List of routes",sbengal)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",user="2NWb96BauSzhCfv.root",password="FlKt7G8RKi0SOme7",database="project",port=4000)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
    
    
    
    #WEST BENGAL
    if state=="West Bengal":
        with col2:
           k=st.selectbox("List of routes",wbengal)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",user="2NWb96BauSzhCfv.root",password="FlKt7G8RKi0SOme7",database="project",port=4000)
            my_cursor=conn.cursor()
            
            #filtration for rating
            
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)