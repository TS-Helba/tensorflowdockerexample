#helba/tensorflowdockerexample:train
FROM helba/tensorflowdockerexample:deps
CMD ["mkdir","/app/buildfiles"]
COPY buildfiles/* /app/buildfiles/
EXPOSE 3306
ENTRYPOINT ["python3", "/app/buildfiles/tftrain.py"]
