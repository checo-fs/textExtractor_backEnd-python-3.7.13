# FROM python:3.8.16-buster
FROM paddlepaddle/paddle:2.4.2
RUN apt-get update && apt-get -y install \
    poppler-utils python3-opencv

# RUN wget https://paddleocr.bj.bcebos.com/whl/layoutparser-0.0.0-py3-none-any.whl



# RUN pip install -U layoutparser-0.0.0-py3-none-any.whl

# RUN pip install opencv-python

# RUN python -m pip install paddlepaddle==2.4.2 -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip install "paddleocr>=2.6.0.3"

# RUN pip3 install paddleclas>=2.4.3

RUN pip install pdf2image
RUN wget https://paddleocr.bj.bcebos.com/whl/layoutparser-0.0.0-py3-none-any.whl
RUN pip install -U layoutparser-0.0.0-py3-none-any.whl

# WORKDIR ../
# COPY ./src ./
# CMD ["python", "ocr.py"]

