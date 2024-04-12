FROM golang:1.21-alpine AS build

WORKDIR /golang_app

COPY go.mod go.sum ./

RUN go mod download

COPY . .

RUN go build -o build/fizzbuzz

FROM gcr.io/distroless/static-debian11

WORKDIR /golang_app

COPY --from=build /golang_app/templates templates

COPY --from=build /golang_app/build/fizzbuzz fizzbuzz

EXPOSE 8080

CMD ["./fizzbuzz", "serve"]