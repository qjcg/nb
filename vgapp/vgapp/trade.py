def sell():
    return "SOLD!"


def buy():
    return "BOUGHT!"


if __name__ == '__main__':
    print("Executing demo trades")
    for _ in range(5):
        print(sell())
        print(buy())
