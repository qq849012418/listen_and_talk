# Listen_and_talk

简单整合了一个ros_demo软件包，满足单节点双Topic的要求. python版本。

## 功能介绍

假设Topic的发布者为GPS模块，它以**1HZ**的频率向**/gps_info**这个topic上发布消息，消息格式要包括坐标(x,y)和工作状态(state)。

Topic的接受者会订阅**/gps_info**，并计算每次GPS位置到原点的距离，在屏幕上显示。

本例需要自定义msg文件，见[msg/gps.msg](./msg/gps.msg)。

Python版本代码见`scripts/`下。


## 运行方法

启动发布与接收者

```sh
$ rosrun listen_and_talk node_template.py   
```


