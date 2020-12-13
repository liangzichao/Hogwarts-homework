import pytest

def get_data():
    l = [1,2,3]
    return l

@pytest.fixture(params=get_data(),scope="module")
def myfixture(request):
    print("参数为：{}".format(request.param))

    print("执行myfixture")




def pytest_collection_modifyitems(session, config, items):
    print(type(items))
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        if "add" in item._nodeid:
            item.add_marker(pytest.mark.add)
        if "div" in item._nodeid:
            item.add_marker(pytest.mark.div)
