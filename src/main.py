from src.utils.logger import logger


class Main:
    def run(self) -> None:
        logger.decorate_log("Run!")


if __name__ == '__main__':
    Main().run()
