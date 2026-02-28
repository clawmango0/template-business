#!/bin/bash
# Convenience wrapper for all conversions
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_PYTHON="$SCRIPT_DIR/venv/bin/python"

# Use venv python if available
PYTHON="$VENV_PYTHON"
[ ! -f "$PYTHON" ] && PYTHON="python3"

case "$1" in
    pdf)
        shift
        for f in "$@"; do
            $PYTHON "$SCRIPT_DIR/make_fillable.py" "$f"
        done
        ;;
    docx|html)
        for f in "$@"; do
            pandoc "$f" -o "${f%.*}.$1" --standalone
        done
        ;;
    all)
        shift
        for f in "$@"; do
            $PYTHON "$SCRIPT_DIR/make_fillable.py" "$f"
            pandoc "$f" -o "${f%.*}.docx" --standalone 2>/dev/null
            pandoc "$f" -o "${f%.*}.html" --standalone 2>/dev/null
        done
        ;;
    *)
        echo "Usage: $0 <pdf|docx|html|all> <file.md>..."
        echo ""
        echo "Examples:"
        echo "  $0 pdf pressure-washing/01-service-agreement.md"
        echo "  $0 all templates/*.md"
        ;;
esac
