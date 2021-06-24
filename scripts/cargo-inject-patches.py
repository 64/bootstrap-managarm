#!/usr/bin/env python3

import argparse, os, subprocess, pathlib, sys, re

patched_libs = {
	'libc': '0.2.97',
	'num_cpus': '1.13.0',
	'users': '0.11.0',
	'socket2': '0.4.0',
	'nix': '0.21.0',
	'getrandom': '0.2.3',
	'filetime': '0.2.14',
	'mio': '0.7.13',
}

parser = argparse.ArgumentParser(description='Inject patched Rust libraries into Cargo lockfiles')
parser.add_argument('manifest', type=pathlib.Path, help='path to Cargo.toml')
manifest = parser.parse_args().manifest

# First, delete the existing lockfile to work around https://github.com/rust-lang/cargo/issues/9470
lockfile = os.path.join(os.path.dirname(manifest), 'Cargo.lock')
if os.path.exists(lockfile):
    print('cargo-inject-patches: workaround cargo bug by removing existing lockfile...')
    os.remove(lockfile)

for lib, version in patched_libs.items():
	cmd = [
		'cargo',
		'update',
		'--manifest-path', manifest,
		'--package', lib,
		'--precise', version
	]

	output = subprocess.run(cmd, capture_output=True)
	expected = [
		f'Updating {lib} v{version} \\(\\S+\\) -> v{version}',
		f'Adding {lib} v{version} \\(\\S+\\)'
	]

	if any(re.search(rg, str(output.stderr)) is not None for rg in expected):
		print(f'cargo-inject-patches: Injected {lib} v{version}')
	elif 'did not match any packages' in str(output.stderr):
		print(f'cargo-inject-patches: Didn\'t inject {lib} v{version} (crate not used in dependency graph)')
	else:
		print(f'cargo-inject-patches: Injecting {lib} v{version} failed (didn\'t find expected strings):')
		sys.stdout.buffer.write(output.stderr)
		exit(1)
