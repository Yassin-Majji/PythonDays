import traceback

try:
    int("x")
except Exception as e:
    traceback.print_tb(e.__traceback__)