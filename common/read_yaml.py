import yaml
def open_yaml(path):
    with open(path,"rb") as  f:
        data=yaml.load(f,Loader=yaml.FullLoader)
        f.close()
    return data
if __name__=="__main__":

    open_yaml("path")