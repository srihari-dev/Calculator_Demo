"""
Command Line Interface for Calculator
Example: python src/cli.py add 5 3
"""
import sys
import click

from calculator import add, subtract, multiply, divide, power, square_root

@click.command()
@click.argument('operation')
@click.argument('num1', type=float)
@click.argument('num2', type=float, required=False)
def calculate(operation, num1, num2=None):
	"""Simple calculator CLI"""

	try:
		if operation == 'add':
			if num2 is None:
				raise ValueError("add requires two operands")
			result = add(num1, num2)
		elif operation == 'subtract':
			if num2 is None:
				raise ValueError("subtract requires two operands")
			result = subtract(num1, num2)
		elif operation == 'multiply':
			if num2 is None:
				raise ValueError("multiply requires two operands")
			result = multiply(num1, num2)
		elif operation == 'divide':
			if num2 is None:
				raise ValueError("divide requires two operands")
			result = divide(num1, num2)
		elif operation == 'power':
			if num2 is None:
				raise ValueError("power requires two operands")
			result = power(num1, num2)
		elif operation in ('sqrt', 'square_root'):
			result = square_root(num1)
		else:
			click.echo(f"Unknown operation: {operation}")
			sys.exit(1)

		# Format result nicely
		if float(result).is_integer():
			click.echo(int(result))
		else:
			click.echo(f"{result:.2f()}".replace("()", "") if isinstance(result, float) else str(result))

	except ValueError as e:
		click.echo(f"Error: {e}")
		sys.exit(1)
	except Exception as e:
		click.echo(f"Unexpected error: {e}")
		sys.exit(1)

if __name__ == '__main__':
	calculate()