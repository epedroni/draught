#!/usr/bin/env sh

# Try to zip up the required draught files into a package, then make it executable.
# The list of files to zip up should be externalised, I'll do that eventually.

echo 'Making draught.zip...'
zip -r ./draught.zip __main__.py manager.py resources/* README.md LICENSE

echo 'Making executable...'
echo '#!/usr/bin/env python' | cat - draught.zip > draught
chmod +x draught

echo 'Cleaning up...'
rm draught.zip
