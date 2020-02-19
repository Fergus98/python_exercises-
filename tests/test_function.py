import pytest
from applications import function

def test_grades():
	assert function.gradeCalc(24, 21) == 0.6
