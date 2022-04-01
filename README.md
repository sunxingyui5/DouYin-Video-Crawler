## DouYin-Video-Crawler

#### 本项目为抖音视频爬虫的简单实现方法，仅使用requests和re库，在自动保存视频到本地外，还有额外方法如爬取对应视频的标题、点赞数、评论数、精选评论等

### 功能

1. 爬取视频链接对应视频的标题、点赞数、评论数、精选评论  
2. 保存视频到本地  

### 操作方法  

1. 将希望爬取的视频链接url传入DouYin_Downloader(url)类中  
2. 使用下列方法实现你的需求  
#### DY = DouYin_Downloader(url)  
#### 得到标题：DY.getTitle()  
#### 得到精选评论：DY.getComment()  
#### 得到点赞数：DY.getLikeNum()  
#### 得到评论数：DY.getCollectNum()  
#### 保存视频到本地：DY.downloadVideo() #默认保存到当前文件夹下  
