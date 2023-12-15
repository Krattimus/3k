from deep_translator import GoogleTranslator
import sys
from tintin import TinTin

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

to_translate = str(sys.argv[1])
translated = GoogleTranslator(source='auto', target='ja').translate(to_translate)
TinTin.echo(translated)