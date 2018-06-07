
**N way to Transform coordinate**
坐标系统转换的N种方式，因为本人主要立足于互联网应用，比较关注WGS84、gcj02和bd09之间的转换；
## coding

### Python
- [coordTransform_py ](https://github.com/QLWeilcf/coordTransform_py) forked from [wandergis/coordTransform_py](https://github.com/wandergis/coordTransform_py)


### JavaScript

[proj4js](https://github.com/proj4js/proj4js)
[coordtransform js](https://github.com/wandergis/coordtransform)

## using API

**百度WEB服务**：get：http://api.map.baidu.com/geoconv/v1/?coords=114.21892734521,29.575429778924&from=1&to=5&ak=yourak

from:1~8;1：wgs84角度坐标;3：gcj02角度坐标;4：3中对应的米制坐标;;5：百度经纬度坐标;6：百度米制坐标;7：mapbar地图坐标;8：51地图坐标

to:3~6;和from中编号相同

**高德WEB服务**：get：http://restapi.amap.com/v3/assistant/coordinate/convert?locations=116.48,39.99&coordsys=gps&output=xml&key=yourak

原系统：coordsys：gps;mapbar（目前不清楚这是啥）;baidu;autonavi(不进行转换)

输出是gcj02 高德坐标

output有：JSON,XML

### 验证



---

ps:
坐标现状：（参考自[wandergis_coordtransform](https://github.com/wandergis/coordtransform)）

- 从设备获取经纬度（GPS）坐标

  	如果使用的是百度sdk那么可以获得百度坐标（bd09）或者火星坐标（GCJ02),默认是bd09
  	如果使用的是ios的原生定位库，那么获得的坐标是WGS84
  	如果使用的是高德sdk,那么获取的坐标是GCJ02
    
    
    
- 互联网在线地图使用的坐标系

  火星坐标系：
  		iOS 地图（其实是高德）
  		Google国内地图（.cn域名下）
  		搜搜、阿里云、高德地图、腾讯
  百度坐标系：
  		百度地图
  WGS84坐标系：
  		国际标准，谷歌国外地图、osm地图等国外的地图一般都是这个

Google Earth： wgs84

---

















