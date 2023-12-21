# You should normally never do wildcard imports
# Here it is useful to allow the configuration to be maintained elsewhere
from starterkit_ci.sphinx_config import *  # NOQA

project = 'Starterkit Lessons'
copyright = '2015-2020, Starterkit'
author = 'Starterkit'

exclude_patterns += [
    'README.md',
]

html_context = {
    'display_github': True,
    'github_user': 'lhcb',
    'github_repo': 'menglin-xu.github.io',
    'github_version': 'master',
    'conf_py_path': '/',
}

html_static_path += [
    f'_static',
]

# Links to be ignored by the CI check
#linkcheck_ignore += [
#    r'https://groups\.cern\.ch/group/lhcb-distributed-analysis/default\.aspx',  # 403 error, requires a login
#    r'https://lhcb-doxygen\.web\.cern\.ch/.*',  # 403 error, requires a login
#]

#starterkit_ci_redirects['first-analysis-steps/index.html'] = 'https://lhcb.github.io/starterkit-lessons/first-analysis-steps/README.html'
#starterkit_ci_redirects['second-analysis-steps/index.html'] = 'https://lhcb.github.io/starterkit-lessons/second-analysis-steps/README.html'


def starterkit_ci_setup(app):
    app.add_css_file('starterkit.css')

setup.extra_setup_funcs += [starterkit_ci_setup]
