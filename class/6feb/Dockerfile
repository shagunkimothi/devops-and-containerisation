FROM ubuntu:22.04 AS build
RUN apt-get update && apt-get install -y gcc
COPY hello.c .
RUN gcc -static -o hello hello.c

# Problem: Includes entire Ubuntu + gcc in final image
CMD ["./hello"]
 

# Stage 2: Runtime (FROM scratch = minimal)
FROM scratch
COPY --from=builder /hello /hello
CMD ["/hello"]
