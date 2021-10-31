import os
import psutil
from pywinauto.application import Application
def gethh(name):
    os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})

    name_path=r"D:/NLEMR/RestingECG"
    start_cmd='d: & cd '+name_path+' & start '+name
    you_path_pid=None

    for i in psutil.pids():
        p=psutil.Process(i)
        if str(p.name())==name:
            you_path_pid=i

    if you_path_pid is None:
        os.system(start_cmd)
        p2=psutil.process_iter()
        print(p2)
        for j in p2:
            if j.name()==name:
                you_path_pid=j.pid
                print(you_path_pid)
                you_name_app=Application(backend="uia").connect(process=you_path_pid)

    else:
        you_name_app=Application(backend="uia").connect(process=you_path_pid)
gethh("Aquarium.Ecg.Client.Shell.exe")