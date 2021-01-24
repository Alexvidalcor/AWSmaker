from src.gui import LoginGui, MainGui
from src.ConfigAWS import *

userCredentials = LoginGui()

if userCredentials:
    MainGui()