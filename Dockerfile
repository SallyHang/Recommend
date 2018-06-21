FROM python:3.6.3
LABEL maintainer="SallyZhang"
WORKDIR /root
RUN git clone https://github.com/SallyHang/Recommend
#根据requirements内容安装代码需要的包
WORKDIR /root/Recommend
RUN pip install -r requirements.txt
WORKDIR /root/Recommend/Recommend
CMD [ "python", "myrec.py" ]
