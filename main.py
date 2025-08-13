from config import CONFIG
from optimizer import Optimizer


def main():
    optimizer = Optimizer(CONFIG)
    optimizer.optimize()


if __name__ == "__main__":
    main()
