import sys, os
import sphinx_rtd_theme


from datetime import datetime
sys.path.insert(0, os.path.abspath("../"))
# lexers['php'] = PhpLexer(startinline=True)

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_autopackagesummary'
              ]
# autosummary_generate = False
# autosummary = []
source_suffix = '.rst'
master_doc = 'index'
pygments_style = 'sphinx'

project = 'QCircuit'
copyright = ''
author = 'Ilia Besedin'

version = '1'
release = '13072020'

exclude_patterns = ['_build']
add_function_parentheses = False
autosummary_generate = True

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['_static']
templates_path = ['_templates']

html_theme_options = {
    'collapse_navigation': True,
    'display_version': True,
}

# html_context = {
#     'copyright_url': 'https://www.acme.com',
#     'current_year': datetime.utcnow().year
# }
# from sphinx.ext.autosummary import Autosummary
# from sphinx.ext.autosummary import get_documenter
# from docutils.parsers.rst import directives
# from sphinx.util.inspect import safe_getattr
#
# autodoc_default_options = {'members': True, 'inherited-members': True}
# autodoc_mock_imports = ['qutip', 'pytest', 'ipywidgets', 'IPython', 'tqdm']
#
#
# class AutoAutoSummary(Autosummary):
#
#     option_spec = {
#         'methods': directives.unchanged,
#         'attributes': directives.unchanged
#     }
#
#     required_arguments = 1
#
#     @staticmethod
#     def get_members(obj, typ, include_public=None):
#         if not include_public:
#             include_public = []
#         items = []
#         for name in dir(obj):
#             try:
#                 documenter = get_documenter(safe_getattr(obj, name), obj)
#             except AttributeError:
#                 continue
#             if documenter.objtype == typ:
#                 items.append(name)
#         public = [x for x in items if x in include_public or not x.startswith('_')]
#         return public, items
#
#     def run(self):
#         clazz = str(self.arguments[0])
#         try:
#             (module_name, class_name) = clazz.rsplit('.', 1)
#             m = __import__(module_name, globals(), locals(), [class_name])
#             c = getattr(m, class_name)
#             if 'methods' in self.options:
#                 _, methods = self.get_members(c, 'method', ['__init__'])
#
#                 self.content = ["~%s.%s" % (clazz, method) for method in methods if not method.startswith('_')]
#             if 'attributes' in self.options:
#                 _, attribs = self.get_members(c, 'attribute')
#                 self.content = ["~%s.%s" % (clazz, attrib) for attrib in attribs if not attrib.startswith('_')]
#         finally:
#             return super(AutoAutoSummary, self).run()

def setup(app):
    app.add_css_file("css/style.css")
    # app.add_directive('autoautosummary', AutoAutoSummary)