import pandas as pd
import streamlit
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.datframe(my_fruit_list)

   


