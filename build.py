import PyInstaller.__main__
import subprocess

# Build the app
PyInstaller.__main__.run([
    'browser.py',
    '--onefile',
    '--windowed',
    '--name=Spaceship',
    '--icon=icon.icns'
])

# Create DMG
result = subprocess.run([
    'hdiutil', 'create',
    '-volname', 'Spaceship',
    '-srcfolder', 'dist/Spaceship.app',
    '-ov',
    '-format', 'UDBZ',
    'Spaceship.dmg'
], capture_output=True, text=True)

if result.returncode == 0:
    print("✅ Spaceship.dmg created successfully!")
else:
    print("❌ DMG creation failed:")
    print(result.stderr)

# print("✅ Spaceship.dmg created!")