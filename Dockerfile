FROM python:3.6.3
LABEL maintainer="SallyZhang"
WORKDIR /root
RUN git clone https://github.com/SallyHang/Recommend
WORKDIR /root/Recommend

WORKDIR /root/Recommend/Recommend
CMD [ "python", "myrec.py" ]
