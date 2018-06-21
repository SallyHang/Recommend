FROM yingsf/python3.6.5
LABEL maintainer="SallyZhang"
WORKDIR /root
RUN git clone https://github.com/SallyHang/Recommend
WORKDIR /root/Recommend/Recommend
CMD [ "python", "myrec.py" ]
