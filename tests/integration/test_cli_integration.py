"""
Integration Tests - CLI + Calculator Working Together
"""
import subprocess
import sys

class TestCLIIntegration:
	"""Test CLI application integrating with
	calculator module"""

	def run_cli(self, *args):
		"""Helper method to run CLI and capture
		output"""
		cmd = [sys.executable, 'src/cli.py'] + list(args)
		result = subprocess.run(cmd, capture_output=True, text=True, cwd='.')
		return result

	def test_cli_add_integration(self):
		"""Test CLI can perform addition"""
		result = self.run_cli('add', '5', '3')
		assert result.returncode == 0
		assert result.stdout.strip() == '8'

	def test_cli_subtract_integration(self):
		"""Test CLI can perform subtraction"""
		result = self.run_cli('subtract', '5', '3')
		assert result.returncode == 0
		assert result.stdout.strip() == '2'

	def test_cli_subtract_missing_operand_error(self):
		"""Test CLI handles missing operand for
		subtraction gracefully"""
		# call subtract with only one operand; CLI
		# should exit with non-zero and print an error
		result = self.run_cli('subtract', '5')
		# accept any non-zero exit code (CLI may use different non-zero codes)
		assert result.returncode != 0
		# CLI may print errors to stdout or stderr; check both
		expected = 'Error: subtract requires two operands'
		combined = (result.stdout or '') + '\n' + (result.stderr or '')
		assert expected in combined.strip()