

class Calculator:


    def add(self,a,b):

        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def dev(self, a, b):
        return a / b


import yaml



def get_datas():

    with open("./data.yaml","r",encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        #print(datas)

        data_add = datas["add"]
        data_subtract = datas["subtract"]
        data_ride = datas["ride"]
        data_divide = datas["divide"]
        add_ids = datas["myid"]
        #datas = datas["add"]

        #return [datas]

        return [data_add,add_ids,data_subtract,data_ride,data_divide]

print(get_datas()[2])






