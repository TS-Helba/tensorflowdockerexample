#localhost:7070/tflow:train
FROM localhost:7070/tflow:deps
CMD ["mkdir","/app/buildfiles"]
COPY buildfiles/* /app/buildfiles/
EXPOSE 3306
ENTRYPOINT ["python3", "/app/buildfiles/tftrain.py"]
