import unittest
import subprocess
from termgraph import termgraph as tg

def run_process(args):
    command = 'python3 termgraph/termgraph.py ' + ' '.join(args)
    process = subprocess.run(command,
                             shell=True,
                             timeout=10,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, check=True)
    return process

class TermgraphCLITest(unittest.TestCase):
    def test_help_arg_returns_0(self):
        process = run_process(['-h'])
        self.assertEqual(process.returncode, 0)

    def test_help_arg_returns_help_message(self):
        process = run_process(['-h'])
        output = process.stdout.split(b'\n')
        self.assertEqual(output, 
                         [b'usage: termgraph.py [-h] [--title TITLE] [--width WIDTH] [--format FORMAT]',
                          b'                    [--suffix SUFFIX] [--no-labels]',
                          b'                    [--color [{red,blue,green,magenta,yellow,black,cyan} [{red,blue,green,magenta,yellow,black,cyan} ...]]]',
                          b'                    [--vertical] [--stacked] [--different-scale] [--calendar]',
                          b'                    [--start-dt START_DT] [--custom-tick CUSTOM_TICK]',
                          b'                    [--delim DELIM] [--verbose] [--version]',
                          b'                    [filename]',
                          b'',
                          b'draw basic graphs on terminal',
                          b'',
                          b'positional arguments:',
                          b'  filename              data file name (comma or space separated). Defaults to',
                          b'                        stdin.',
                          b'',
                          b'optional arguments:',
                          b'  -h, --help            show this help message and exit',
                          b'  --title TITLE         Title of graph',
                          b'  --width WIDTH         width of graph in characters default:50',
                          b'  --format FORMAT       format specifier to use.',
                          b'  --suffix SUFFIX       string to add as a suffix to all data points.',
                          b'  --no-labels           Do not print the label column',
                          b'  --color [{red,blue,green,magenta,yellow,black,cyan} [{red,blue,green,magenta,yellow,black,cyan} ...]]',
                          b'                        Graph bar color( s )',
                          b'  --vertical            Vertical graph',
                          b'  --stacked             Stacked bar graph',
                          b'  --different-scale     Categories have different scales.',
                          b'  --calendar            Calendar Heatmap chart',
                          b'  --start-dt START_DT   Start date for Calendar chart',
                          b'  --custom-tick CUSTOM_TICK',
                          b'                        Custom tick mark, emoji approved',
                          b'  --delim DELIM         Custom delimiter, default , or space',
                          b'  --verbose             Verbose output, helpful for debugging',
                          b'  --version             Display version and exit',
                          b''])

    def test_no_args_and_no_stdin_returns_2(self):
        with self.assertRaises(subprocess.CalledProcessError) as cm:
            process = run_process([])

        self.assertEqual(cm.exception.returncode, 2)
