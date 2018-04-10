#localhost:7070/tflow:dbiris
FROM localhost:7070/tflow:deps
CMD ["mkdir","/app/buildfiles"]
COPY buildfiles/* /app/buildfiles/
EXPOSE 3306
ENTRYPOINT ["python3", "/app/buildfiles/tfdbloader.py"]
