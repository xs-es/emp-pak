from pathlib import Path

# Create package structure
base = Path("/mnt/data/qhrf_core_package")
dirs = [
    base / "qhrf" / "resonance",
    base / "qhrf" / "circuits",
    base / "qhrf" / "neural",
    base / "qhrf" / "crypto",
    base / "examples"
]

for d in dirs:
    d.mkdir(parents=True, exist_ok=True)

# __init__.py placeholders
for d in dirs:
    (d / "__init__.py").write_text("")

# setup.py
(base / "setup.py").write_text("""\
from setuptools import setup, find_packages

setup(
    name="qhrf",
    version="0.1.0",
    description="Quantum Harmonic Resonance Framework SDK",
    author="Zachary L. Musselwhite",
    packages=find_packages(),
    install_requires=["qiskit", "numpy"],
    python_requires=">=3.10",
)
""")

# LICENSE
(base / "LICENSE").write_text("""\
Apache License 2.0

Copyright 2025 Zachary L. Musselwhite

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy at

    http://www.apache.org/licenses/LICENSE-2.0

You may sublicense this framework for commercial use, redistribution, and productization under explicit commercial license agreements available from the author.
Contact: Xses.Science@gmail.com for enterprise licensing.
""")

# README.md
(base / "README.md").write_text("""\
# QHRF Core SDK

**Quantum Harmonic Resonance Framework**: Coherence boosters, fractal entanglement, and QPU optimizers.

## Modules

- `qhrf.resonance`: Infinite Coherence, Fractal Phase Locking
- `qhrf.circuits`: Circuit optimizers, state recycling
- `qhrf.neural`: Quantum-AI hybrid QHRF layers
- `qhrf.crypto`: QRNG, secure entanglement channel

## Installation

```bash
pip install .
