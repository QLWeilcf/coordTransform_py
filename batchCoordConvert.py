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

#处理csv列数据
def coordConvertCsvCol():
    import pandas as pd
    #目前不支持含中文目录
    g_path="D:/DigitalC_data/xiaoxueWgs84.csv" #原先坐标csv数据
    s_path="D:/DigitalC_data/xiaoxuebd09_1.csv" #之后保存的位置
    gridLst=pd.read_csv(g_path,encoding='utf-8')
    gridLst['bdlng']=0 #增加两列
    gridLst['bdlat']=0
    
    idx=[2,3,4,5]#[原先lng,原先lat,转换后lng,转换后lat]
    for i in range(len(gridLst)):
        lst=gridLst.iloc[i,]
        bdc=wgs84_to_bd09(gridLst.iloc[i,idx[0]],gridLst.iloc[i,idx[1]])
        gridLst.iloc[i,idx[2]]=bdc[0]
        gridLst.iloc[i,idx[3]]=bdc[1]
    gridLst.to_csv(s_path,index=False)
    print('save at',s_path)
        
        
        
        
        

