from sites.google import Google
from loguru import logger


def main():
    logger.info("Start the crawler.")
    Google().run()
    logger.info("Successfully terminated crawler.")


if __name__ == "__main__":
    main()
