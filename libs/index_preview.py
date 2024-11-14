import pandas as pd
import streamlit as st
import os
from libs.common import check_rag_complete
import libs.config as config


def index_preview(rag_version: str):
    if st.button('Preview Index', key=f"index_preview_{rag_version}", icon="🔍"):
    
        # check_rag_complete(rag_version)
        artifacts_path = f"/app/projects/{rag_version}/output"
        with st.spinner(f'Reading ...'):
            hasIndex = False
            
            for root, dirs, files in os.walk(f"{artifacts_path}/"):
                for file in files:
                    hasIndex = True
                    file_path = os.path.join(root, file)
                    file_size_bytes = os.path.getsize(file_path)
                    file_size_mb = file_size_bytes / (1024 * 1024)
                    
                    try:
                        if file_path.endswith(".parquet"):
                            df = pd.read_parquet(file_path)
                            st.markdown(f"### {file}")
                            st.write(f"{len(df)} items ({file_size_mb:.4f}MB)")
                            st.write(df.head(n=20000))
                    except Exception as e:
                        st.error(f"Error reading {file}: {e}")

            if not hasIndex:
                st.error("Please index first.")
