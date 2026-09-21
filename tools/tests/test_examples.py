"""Run the offline example scripts and the snippets in docs/appendix/tools.md end to end.

Both run in a subprocess, exactly as a learner would run them. Network examples/snippets (marked
``# needs network``) are skipped so the suite stays offline.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys

import pytest
from conftest import REPO_ROOT, TOOLS_DIR

OFFLINE_EXAMPLES = [
    ("kaveri_ratio_dashboard.py", "115"),
    ("kaveri_dcf_and_reverse_dcf.py", "₹320"),
    ("forensic_scores_kaveri.py", "m_score"),
    ("build_kaveri_model.py", "value per share ₹320"),
]
TOOLS_MD = REPO_ROOT / "docs" / "appendix" / "tools.md"


def _run(args: list[str], cwd) -> subprocess.CompletedProcess:
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    return subprocess.run([sys.executable, *args], cwd=cwd, capture_output=True, timeout=300, env=env,
                          encoding="utf-8", errors="replace")


@pytest.mark.parametrize("script,expected", OFFLINE_EXAMPLES)
def test_offline_example_runs(script, expected, tmp_path):
    proc = _run([str(TOOLS_DIR / "examples" / script)], cwd=tmp_path)  # from an unrelated directory
    assert proc.returncode == 0, proc.stderr
    assert expected in proc.stdout


def test_network_example_is_importable_and_documents_vpn():
    text = (TOOLS_DIR / "examples" / "fetch_indian_company.py").read_text(encoding="utf-8")
    assert "VPN" in text and "io.TextIOWrapper" in text
    compile(text, "fetch_indian_company.py", "exec")


def test_every_printing_script_wraps_stdout():
    for path in (TOOLS_DIR / "examples").glob("*.py"):
        assert "sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding=\"utf-8\")" in path.read_text(
            encoding="utf-8"), path.name


@pytest.mark.skipif(not TOOLS_MD.exists(), reason="docs/appendix/tools.md not present")
def test_tools_md_snippets_run(tmp_path):
    text = TOOLS_MD.read_text(encoding="utf-8")
    blocks = re.findall(r"```python\n(.*?)```", text, flags=re.S)
    offline = [b for b in blocks if not b.lstrip().startswith("# needs network")]
    assert len(offline) >= 4
    script = tmp_path / "tools_md_snippets.py"
    script.write_text("\n".join(offline), encoding="utf-8")
    proc = _run([str(script)], cwd=REPO_ROOT)  # snippets say "run from the repository root"
    assert proc.returncode == 0, proc.stderr
    out = proc.stdout
    for expected in ("WACC 12.19%", "₹320/share", "14.1%", "1.30x", "Piotroski F 4/9", "₹320 per share",
                     "[69.4, 75.7, 94.8]", "154.9%"):
        assert expected in out, expected
