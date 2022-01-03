pip -q install pytest pytest-sugar

# move to tdd directory
from pathlib import Path
if Path.cwd().name != 'tdd':
    %mkdir tdd
    %cd tdd
%pwd

!python -m pytest test_math.py 

