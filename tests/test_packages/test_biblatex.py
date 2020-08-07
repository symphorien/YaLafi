

import pytest
from yalafi import parameters, parser, utils

preamble = '\\usepackage{biblatex}\n'

def get_plain(latex):
    parms = parameters.Parameters()
    p = parser.Parser(parms)
    plain, nums = utils.get_txt_pos(p.parse(preamble + latex))
    return plain


data_test_macros_latex = [

    (r'A\cite*{x}B', 'A[0]B'),
    (r'A\cite[p. 15]{x}B', 'A[0, p. 15]B'),
    (r'A\cite[][p. 15]{x}B', 'A[0, p. 15]B'),
    (r'A\cite*[p. 15]{x}B', 'A[0, p. 15]B'),
    (r'A\cite[]{x}B', 'A[0]B'),
    (r'A\cite[][]{x}B', 'A[0]B'),
    (r'A\cite[ ]{x}B', 'A[0,  ]B'),
    (r'A\cite[ ][ ]{x}B', 'A[  0,  ]B'),
    (r'A\cite[See][]{x}B', 'A[See 0]B'),
    (r'A\cite[See][p. 15]{x}B', 'A[See 0, p. 15]B'),
    (r'A\Cite{x}B', 'A[0]B'),
    (r'A\footcite{x} B', 'A B\n\n\n[0].\n'),
    (r'A\footcitetext{x} B', 'A B\n\n\n[0].\n'),
    (r'A\parencite{x}B', 'A[0]B'),
    (r'A\Parencite{x}B', 'A[0]B'),

]

@pytest.mark.parametrize('latex,plain_expected', data_test_macros_latex)
def test_macros_latex(latex, plain_expected):
    plain = get_plain(latex)
    assert plain == plain_expected

