# MQTT Publishing Client in Docker

A simple MQTT client written in Python. Ships with batteries included inside a Docker container.

Perfect for test environments.

## Acknowledgements

- [Eclipse Mosquitto](https://mosquitto.org/) for writing such a clean MQTT broker!
- [readme.so](https.//readme.so) for making it easy to write good-looking READMEs!
- Again: [Eclipse](https://www.eclipse.org/paho/index.php?page=clients/python/index.php) for publishing this stable and OSS MQTT library!

## Authors

- [@torbendury](https://www.github.com/torbendury)
  - [TorbenTechBlog](https://torbentechblog.com)

## Usage/Examples

Running the client is both possible easily, bare-metal or inside a docker container.

### Running bare-metal

```bash
  $ ./main.py \
      --client-name "test123" \
      --broker-endpoint 127.0.0.1 \
      --port 1883 \
      --topic "test/topic" \
      --message "Hello World!"
```

### Running on Docker

```bash
  $ docker run --rm -ti --name mqtt-publisher torbendury/mqtt-publisher \
      --client-name "test123" \
      --broker-endpoint 127.0.0.1 \
      --port 1883 \
      --topic "test/topic" \
      --message "Hello World!"
```

## Contributing

Contributions are always welcome! Always feel free to open issues or PRs.

## License

MIT
