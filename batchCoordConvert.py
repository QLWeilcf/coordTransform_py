#coding=utf-8

#**封装一些应用coordTransform_py进行批处理一些转换需求**，例如批量处理geojson中的坐标

## Geojson batch process

# 一个不太自由的geojson内坐标转换
def geojsonCConvert(cin,cout):
    """
    :param cin:输入geojson文件路径
    :param cout:输出路径
    :return: none
    """
    with open(cin,'r+',encoding='utf-8') as fr:
        gtj = json.load(fr)

    try:
        coorlst=gtj["features"][0]["geometry"]["coordinates"]
        outlst=[[]]
        for ik in coorlst[0]:
            ouw=wgs84_to_bd09(ik[1],ik[0])
            ow=[ouw[1],ouw[0]]
            outlst[0].append(ow)

        gtj["features"][0]["geometry"]["coordinates"]=outlst
        otxt=(json.dumps(gtj)) #.encode('utf-8')
        with open(cout,'w+') as fw:
            fw.write(otxt)

    except Exception as exp:
        print(exp)



