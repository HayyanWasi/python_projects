import streamlit as st
import pandas as pd
import os
from io import BytesIO

#set up our app
st.set_page_config(page_title='Data sweeper', layout='wide')
st.title('💿Data Sweeper')
st.write("Tranform ypur files between CSV and Excel formast with built-in data cleaning visualization!")

upload_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsv"], accept_multiple_files=True)

if upload_files:
    for files in upload_files:
        file_ext = os.path.splittext(file.name) [-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xisv":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue

        #Display information about the file 
        st.write(f"**File name: *{file.name}")
        st.write(f"**File Size:**{file.size/1024}")

        #show 5 rows od our df

        st.write("Rreview the Head of the DataFrame")
        st.dataframe(df.head())

        #options for data cleaning 
        st.subheader("Data cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicate from file name"):
                    dp.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed")

            with col2:
                if st.button(f"fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['numbers']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing Values have been Filled")
            
    #Chooose specific Columns to keep or convert
    st.subheader("Select Columns to Convert")
    columns = st.multiselect(f"Choose Columns for {fie.name}", df.columns, default=df.columns)
    df = df[columns]

    #Create same Visualization
    st.subheader("Data Visualization")
    if st.checkbox(f"Show Visualization for file{fule.name}"):
        st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])

    #convert the file --> CSV to Excel
    st.subheader("Convert Options")
    conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
    if st.button(f"Convert {file.name}"):
        buffer = byteIO()
        if conversion_type == "CSV":
            df.to_csv(buffer,index=False)
            file_name = file.name.replace(file_ext, "csv")
            mime_type = "text/csv"




        elif conversion_type == "Excel":
            df.to_excel(buffer,index=False)
            file_name = file.name.replace(file_ext, ".xlsv")
            mime_type = "application/vnd.openxmlformats-officedocument.spreadsheet.sheet"
        buffer.seek(0)

        #Download button
        st.download_button(
        label= f"Download {file.name} as {conversion_type}",
        data=buffer,
        file_name=file_name,  
        mime=mime_type
)
st.sucess("All files processed!")
