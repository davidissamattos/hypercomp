FROM davidissamattos/hypercomp_base

RUN mkdir hypercomp
WORKDIR hypercomp
COPY . .

ENTRYPOINT ["python3", "main.py"]