#!/usr/bin/env sh

# Try to zip up the required draught files into a package, then make it executable.

# Check if build exists, if not create it
mkdir -p build

echo 'Copying draught.py...'
cp draught.py __main__.py

echo 'Making draught.zip...'
zip -r ./draught.zip __main__.py manager.py resources/* README.md LICENSE

echo 'Making executable...'
echo '#!/usr/bin/env python' | cat - draught.zip > ./build/draught
chmod +x ./build/draught

echo 'Cleaning up...'
rm draught.zip __main__.py
