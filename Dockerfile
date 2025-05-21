FROM python:3 AS builder
WORKDIR /polymath
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN sh build.sh

FROM python:3-alpine AS runner
WORKDIR /polymath
COPY --from=builder /polymath .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
VOLUME /polymath/polymath/storage
ENV PYTHONUNBUFFERED="1"
CMD ["python", "-u", "run"]
