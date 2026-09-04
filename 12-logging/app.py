
import logging

# Create a basic setting
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

# Create logger
logger = logging.getLogger("ArithmeticApp")


def add(a, b):
    result = a + b
    logger.debug(f"Addition of {a} and {b} is {result}")
    return result


def subtract(a, b):
    result = a - b
    logger.debug(f"Subtraction of {a} and {b} is {result}")
    return result


def multiply(a, b):
    result = a * b
    logger.debug(f"Multiplication of {a} and {b} is {result}")
    return result


def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Division of {a} and {b} is {result}")
        return result

    except ZeroDivisionError:
        logger.error("Division by zero is not possible")
        return None


# Function calls
add(12, 23)
subtract(345, 23)
multiply(23, 5)
divide(12, 4)

