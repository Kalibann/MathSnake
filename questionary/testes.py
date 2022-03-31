from subprocess import PIPE, run
import sys

result = run([sys.executable, "-c", "print(2 + 2 ** 4)"], stdout=PIPE, universal_newlines=True)
print(result.stdout)

