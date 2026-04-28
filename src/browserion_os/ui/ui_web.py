import streamlit as st
import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QProgressBar
from PyQt6.QtWebEngineWidgets import QWebEngineView


def web():
    with st.expander(label="Web Browser", icon="🌐", width="stretch", expanded=True):
        st.iframe("https://google.com/search?igu=1", height=600)