from utils.utils import reverse_string


def main(var1=None, var2=None):
    print("Hello from my-python-app!")
    if var1 is not None:
        print(f"var1: {var1}")
    if var2 is not None:
        print(f"var2: {var2}")
    print(f"the reversed string is: {reverse_string('Hello, World!')}")


if __name__ == "__main__":
    main(var1="value1", var2="value2")
