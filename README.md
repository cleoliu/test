# 相關環境設定

一、安裝 python (下載python : http://www.python.org/download/releases/2.6.6/)
 
  - 安裝Python : 下載 python-2.6.6.msi 後，直接執行使用預設設定

        [設定環境變數]  
         PYTHON_HOME ：C:\Python26\
         PATH： ;%PYTHON_HOME%

  - 測試：cmd下 python看到以下畫面，表示安裝成功

         Last login: Thu Jul 21 15:31:14 on ttys002
         Jeffreys-Mac-mini:~ cleo$ python
         Python 2.7.10 (default, Oct 23 2015, 19:19:21)
         [GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.5)] on darwin
         Type "help", "copyright", "credits" or "license" for more information.
         >>>


二、安裝 pip 

 - 到 https://pip.pypa.io/en/latest/installing/ 下載連結 https://bootstrap.pypa.io/get-pip.py)

        $  python pip.py install

        [設定環境變數] 
        PATH： c:\Pthon26\Script

        $ pip install requests


三、安裝 selenium

        $ pip install -U selenium


四、安裝 purl (optional): purl 是 python 功能強大方便使用的 url builder 模組，在 web automation test 時建立 url 建議安裝

        $ pip install purl


五、selenium 下載瀏覽器相關的 WebDriver (運行在本機端時使用)

  - 可依照需求下載：
  
    [IE 32-bit WebDriver] http://code.google.com/p/selenium/downloads/detail?name=IEDriverServer_Win32_2.25.2.zip
    
    [IE 64-bit WebDriver] http://code.google.com/p/selenium/downloads/detail?name=IEDriverServer_x64_2.25.2.zip

    [chromedriver_win_23.0.1240.0.zip] http://code.google.com/p/chromedriver/downloads/detail?name=chromedriver_win_23.0.1240.0.zip


六、安裝OpenCV (2016.10增加)

1.安裝在win上：（安裝包：https://drive.google.com/drive/folders/0B7RNHrsqW0YeNkRQREpEdTNmSmM?usp=sharing）

  - opencv-2.4.13.exe

        [設定環境變數]
        PATH：  ;C:\opencv\build\x64\vc12\bin;C:\opencv\build\x86\vc12\bin

  - matplotlib-1.5.0rc3.win32-py2.7.exe

  - matplotlib-1.5.0-cp27-none-win32.whl

  - numpy-1.10.2-win32-superpack-python2.7.exe



2.安裝在linux centos上：（安裝包：https://drive.google.com/open?id=0B7RNHrsqW0YeMWYwWFdXVVItQms）

  - python升級（opencv僅支援py2.7以上版本）
  
    1.下載Python2.7並安裝 （教學：https://ruter.github.io/2015/12/03/Update-python/）

        $ wget http://www.python.org/ftp/python/2.7.10/Python-2.7.10.tar.xz

        $ unxz Python-2.7.10.tar.xz

        $ tar -vxf Python-2.7.10.tar

        $ cd Python-2.7.10

        $ ./configure --with-png=/usr/local --with-jpeg=/usr/local --without-x --with-freetype=/usr/local CXXFLAGS=-fPIC CFLAGS=-fPIC LDFLAGS=-fPIC CPPFLAGS=-fPIC

        $ vi ./Modules/Setup

        $ make

        $ sudo make install  

        
    2.Python2.6進行備份，Python2.7創建鏈結（Python2.7之後我們需要先把Python2.6備份起來，然後再對yum的配置進行修改，如果不進行這一步操作的話，執行yum命令將會提示你Python的版本不對。）
    
        $ mv /usr/bin/python /usr/bin/python2.6.6

        $ ln -s /usr/local/bin/python2.7 /usr/bin/python
            然後編輯/usr/bin/yum，將第一行的#!/usr/bin/python修改成#!/usr/bin/python2.6.6
        
    3.執行python -V查看版本信息，如果出現錯誤"error while loading shared libraries: libpython2.7.so.1.0: cannot open shared object file: No such file or directory"，編輯配置文件：
    
        $ vi /etc/ld .so .conf
            在檔案內寫入 /usr/local/lib 後存檔

        $ sudo ldconfig

    4.將需要的東西移動至Python2.7
    
        [pip]
        $ ln -s /usr/ local /bin/ pip2. 7  /usr/ bin /pip

        [selenium]
        $ cp /usr/lib/python2.6/site-packages/selenium /usr/local/lib/python2.7/site-package

        
- 安装Matplotlib，安装包下载：http://matplotlib.org/downloads.html

        $ tar zxvf matplotlib-1.4.3.tar.gz  

        $ cd matplotlib-1.4.3

        $ python setup.py install  
        
- 安裝opencv 

>參考資料
>http://techieroop.com/install-opencv-in-centos/
>http://hanmajor.blogspot.tw/2013/10/linux-ubuntu-opencv.html
>https://gist.github.com/mitmul/9253702#file-install_opencv2-4-8-sh


    1.Install opencv from yum repo
    
        $ sudo yum install python-devel python-nose python-setuptools gcc gcc-gfortran gcc-c++ blas-devel lapack-devel atlas-devel

        $ sudo easy_install pip

        $ sudo pip install numpy==1.6.1
            or安装包下载numpy：http://sourceforge.net/projects/numpy/files/

        $ yum install opencv
        
    2.Installing Opencv from Source
    
        $ yum install cmake

        $ yum install python-devel numpy

        $ yum install gcc gcc-c++

        $ yum install gtk2-devel

        $ yum install libdc1394-devel

        $ yum install libv4l-devel

        $ yum install ffmpeg-devel

        $ yum install gstreamer-plugins-base-devel

        $ yum install libpng-devel libjpeg-turbo-devel jasper-devel openexr-devel libtiff-devel libwebp-devel

    3.donwload opencv from git & install

        $ yum install git

        $ mkdir opencv-build

        $ cd opencv-build

        $ git clone https://github.com/Itseez/opencv.git

        $ cd opencv

        $ git checkout tags/2.4.8.2

        $ mkdir build

        $ cd build

        $ cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..

        $ make

        $ sudo make install

        $ sudo vim /etc/ld.so.conf.d/opencv.conf
            修改設定檔，打開新檔案，把下面這行加上去/usr/local/lib。完成後按「:wq」儲存離開

        $ sudo ldconfig
            
    4.設定環境變數
    
        $ sudo vim /etc/bash.bashrc
            把下面兩行加到文件的最後
            PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig
            export PKG_CONFIG_PATH



        
    4.copy cv2.so to site-packages
    
        $ cp /usr/local/lib/python2.7/site-packages/cv2.so /usr/lib/python2.7/site-packages




    





# SELENIUM AUTOTEST PICOWORK 文件說明
一、資料夾

1.PIC

  - PIC/normal : 存放比對用圖片

  - PIC/u3d.picowork.com_2016-10-11 : 存放自動測試之結果截圖

2.ppp2

  - 存放測試用各種檔案類型


二、依照SOP製作每個selenium webdirver case,每個CASE為獨立的檔案:

1.[Login.py]

  - 正常登錄*，桌面/聯絡人正常顯示 *(桌面 hard to indicate)

2.[Cowork.py]

  - 建立並開啟雲書

  - 開啟home任一matter

3.[Invite4ConntactsInCowork.py]

  - 上傳cowork封面

  - 建立並邀請四人加入cowork

4.[FilesInCowork.py]

  - 使用檔案名稱驗證上傳檔案是否存在於聊天室及互動空間（支援1.23以上版本）

  - 在cowork上傳支援檔案，都可以開啟(截圖比較)  

5.[PudlicChat.py]

  - 在公開聊天室傳送訊息

  - 在公開聊天室上傳matter

  - 在公開聊天室新增連結

  - 在公開聊天室從home新增matter

6.[PrivateChat.py]

  - 在私人聊天室傳送訊息

  - 在私人聊天室上傳matter

  - 在私人聊天室新增連結

  - 在私人聊天室從home新增matter

7.[MinifyCowork.py]

  - cowork視窗能縮小與還原

8.[FilesInDesk.py]

  - desk 上傳支援檔案，都可以開啟(截圖比較) 

  - opencv的運作

9.[InviteNewContacts.py]

  - 邀請新的使用者

10.[ChangePw.py]

  - 修改密碼

11.[Pbc.py] >只適用在alpha

  - 從PBC建立帳號，帳號能註冊

  - 建立組織

  - 匯入帳號，組織能這常顯示

  - suspend user不能登陸

12.[DelDeskFile.py]

  - 刪除測試所新增的桌面檔案 
 
 
三、將所有case import為一包:

1.[config.py]

  - browserstack瀏覽器設定

  - import所需要執行的case


四、用來接收cmd所key的參數，將參數記起來

1.[you.py]

  - 記住寫入的參數，並輸出到命令提示視窗

  - 執行[config.py]，並將結果輸出到命令提示視窗

五、其他紀錄

1.[cmd.txt]

  - 寫入cmd傳入參數

2.[stocks.csv]

  - pbc csv上傳用

3.[version.txt]

  - 紀錄Domain版本編號











# CMD下指令執行自動化測試
>指令產生小工具(google dos):
https://docs.google.com/a/unispace3d.com/spreadsheets/d/1KFEh3Xr88Ol7r0pl7nmljmFi_YuHxS2vEFK-HNjMZmM/edit?usp=sharing

一、到檔案根目錄

-
        $ cd C:\Users\momo\workspace\py_autotest selenium\general

二、寫入參數

  - 結構 :
 
         $ python you.py 網域 使用者帳號 密碼 瀏覽器 瀏覽器版本 browserstack使用者 測試項目…(多個)

  - 範例 :
 
        $ python you.py https://ctf.picowork.com/#!/home qatest2@yopmail.com qatest Chrome 51.0 http://bsuser26076:aQs2qkDbfKLxhgGf9U6q@hub.browserstack.com:80/wd/hub cloudbook(self) invite4contactsintocowork(self) publicchat(self) privatechat(self) filesincowork(self) minifycowork(self) filesindesk(self) invitenewcontacts(self) changepw(self)



# BrowserStack
一、測試結果
  - https://www.browserstack.com/automate/builds/454323d9cd9930b9087e5ee982dd8a24516799d6/sessions/0654bfa4ad3c707ae50219d069014a93c3e19719#automate_button

二、browserstack python 教學
  - https://www.browserstack.com/automate/python