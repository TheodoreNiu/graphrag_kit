from datetime import datetime
import logging
import sys
import tracemalloc
import streamlit as st
import os
from dotenv import load_dotenv
from libs.save_env import set_envs
from  libs.common import restart_component
import libs.config as config
from libs.create_version import create_version
from libs.versions_manage import versions_manage
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

tracemalloc.start()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

load_dotenv()

notebook_dir = os.path.abspath("")
parent_dir = os.path.dirname(notebook_dir)
grandparent_dir = os.path.dirname(parent_dir)

sys.path.append(grandparent_dir)


def page():
    st.markdown(f"GraphRAG Kit:`{config.app_version}` GraphRAG:`{config.graphrag_version}`")
    if config.manage_tip:
        st.write(config.manage_tip)

    # if st.button("Refresh Page", icon="🔄"):
    #     st.success(f"Refresh Page at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
    restart_component()
    
    set_envs()

    create_version()

    versions_manage()


if __name__ == "__main__":
    try:
        page_title = "GraphRAG Manage"
        st.set_page_config(
            page_title=page_title,
                            page_icon="avatars/favicon.ico",
                            layout="wide",
                            initial_sidebar_state='expanded')
        st.image("avatars/logo.svg", width=100)
        st.title(page_title)
        
        if not os.path.exists('./config.yaml'):
            page()
        else:
            with open('./config.yaml') as file:
                yaml_config = yaml.load(file, Loader=SafeLoader)
                authenticator = stauth.Authenticate(
                    yaml_config['credentials'],
                    yaml_config['cookie']['name'],
                    yaml_config['cookie']['key'],
                    yaml_config['cookie']['expiry_days'],
                )
                
                authenticator.login()

                if st.session_state['authentication_status']:
                    st.write(f'Welcome `{st.session_state["name"]}`')
                    authenticator.logout()
                    st.markdown("-----------------")
                    page()
                elif st.session_state['authentication_status'] is False:
                    st.error('Username/password is incorrect')
                elif st.session_state['authentication_status'] is None:
                    st.warning('Please enter your username and password')
    except Exception as e:
        st.error(e)
